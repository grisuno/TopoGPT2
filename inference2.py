#!/usr/bin/env python3
"""
topogpt2_infer.py

Inference engine for TopoGPT2 and its zero-shot expanded variants.

Probes the checkpoint tensor shapes directly to reconstruct every
architecture hyperparameter, so no source file, no scale flag, and no
manual config patching are required.  Works with both the original
checkpoint (2R x 4A torus) and the expanded one (any R x A).

Sampling modes
--------------
- Greedy   : temperature = 0, top_k = 0, top_p = 1.0
- Top-k    : temperature > 0, top_k > 0
- Top-p    : temperature > 0, top_p < 1.0
- Combined : top_k + top_p applied sequentially

Execution modes
---------------
- Single prompt  (default)
- Interactive REPL (--interactive)
- Benchmark      (--benchmark N)

Usage
-----
    python topogpt2_infer.py \\
        --ckpt checkpoints_topogpt2/expanded/model.safetensors \\
        --prompt "Once upon a time" \\
        --max-new 200 \\
        --temp 0.8 \\
        --top-k 50 \\
        --top-p 0.95

    python topogpt2_infer.py \\
        --ckpt checkpoints_topogpt2/expanded/model.safetensors \\
        --interactive

Author  : Gris Iscomeback
License : GPL v3
"""

from __future__ import annotations

import argparse
import logging
import math
import os
import sys
import time
import warnings
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F

warnings.filterwarnings("ignore")

try:
    from safetensors.torch import load_file as st_load
    _SAFETENSORS = True
except ImportError:
    _SAFETENSORS = False

try:
    import tiktoken as _tiktoken
    _TIKTOKEN = True
except ImportError:
    _TIKTOKEN = False


# ===========================================================================
# LOGGING
# ===========================================================================

def build_logger(name: str, level: str = "INFO") -> logging.Logger:
    """Stderr logger with timestamp formatting."""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    if not logger.handlers:
        h = logging.StreamHandler(sys.stderr)
        h.setFormatter(logging.Formatter(
            "%(asctime)s  %(name)s  %(levelname)s  %(message)s"
        ))
        logger.addHandler(h)
    return logger


# ===========================================================================
# CONFIGURATION
# ===========================================================================

@dataclass
class InferenceConfig:
    """
    All tuneable knobs for the inference pipeline.

    Attributes
    ----------
    checkpoint_path : str
        Path to a .safetensors or .pt/.pth checkpoint file.
    device : str
        Torch device string.
    max_new_tokens : int
        Maximum tokens to generate beyond the prompt.
    temperature : float
        Softmax temperature.  0 activates greedy decoding.
    top_k : int
        Top-k filtering.  0 disables it.
    top_p : float
        Nucleus (top-p) filtering.  1.0 disables it.
    repetition_penalty : float
        Multiplicative penalty for tokens already in context.  1.0 disables.
    seed : int
        RNG seed for reproducibility.
    log_level : str
        Python logging level name.
    stream : bool
        Print tokens as they are generated instead of all at once.
    show_timing : bool
        Print tokens-per-second after generation.
    prompt : str
        Default prompt for single-shot mode.
    interactive : bool
        Enter a REPL loop instead of generating a single response.
    benchmark_runs : int
        If > 0, run this many generation passes and report throughput.
    """

    checkpoint_path: str = "checkpoints_topogpt2/expanded/model.safetensors"
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    max_new_tokens: int = 200
    temperature: float = 0.8
    top_k: int = 50
    top_p: float = 0.95
    repetition_penalty: float = 1.1
    seed: int = 42
    log_level: str = "INFO"
    stream: bool = False
    show_timing: bool = True
    prompt: str = "Once upon a time"
    interactive: bool = False
    benchmark_runs: int = 0

    def validate(self) -> None:
        """Raise ValueError for impossible parameter combinations."""
        if not Path(self.checkpoint_path).exists():
            raise FileNotFoundError(
                f"Checkpoint not found: {self.checkpoint_path}"
            )
        if self.temperature < 0.0:
            raise ValueError("temperature must be >= 0.")
        if self.top_k < 0:
            raise ValueError("top_k must be >= 0.")
        if not (0.0 < self.top_p <= 1.0):
            raise ValueError("top_p must be in (0, 1].")
        if self.repetition_penalty < 1.0:
            raise ValueError("repetition_penalty must be >= 1.0.")
        if self.max_new_tokens < 1:
            raise ValueError("max_new_tokens must be >= 1.")


# ===========================================================================
# TOKENIZER
# ===========================================================================

class BPETokenizer:
    """Thin wrapper around tiktoken with GPT-2 encoding."""

    _EOT_TOKEN: int = 50256

    def __init__(self):
        if not _TIKTOKEN:
            raise ImportError("tiktoken is required: pip install tiktoken")
        self._enc = _tiktoken.get_encoding("gpt2")
        self.vocab_size: int = self._enc.n_vocab
        self.eot_token: int = self._EOT_TOKEN

    def encode(self, text: str) -> List[int]:
        return self._enc.encode(text, allowed_special={"<|endoftext|>"})

    def decode(self, token_ids: List[int]) -> str:
        return self._enc.decode(token_ids)

    def decode_single(self, token_id: int) -> str:
        return self._enc.decode([token_id])


# ===========================================================================
# ARCHITECTURE (self-contained copy, identical to topogpt2_expand.py)
# ===========================================================================

class QuaternionOps:
    """Static quaternion algebra operations."""

    @staticmethod
    def hamilton_product(q1: torch.Tensor, q2: torch.Tensor) -> torch.Tensor:
        w1, x1, y1, z1 = q1[..., 0], q1[..., 1], q1[..., 2], q1[..., 3]
        w2, x2, y2, z2 = q2[..., 0], q2[..., 1], q2[..., 2], q2[..., 3]
        return torch.stack([
            w1*w2 - x1*x2 - y1*y2 - z1*z2,
            w1*x2 + x1*w2 + y1*z2 - z1*y2,
            w1*y2 - x1*z2 + y1*w2 + z1*x2,
            w1*z2 + x1*y2 - y1*x2 + z1*w2,
        ], dim=-1)

    @staticmethod
    def normalize(q: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
        return q / (q.norm(dim=-1, keepdim=True) + eps)

    @staticmethod
    def conjugate(q: torch.Tensor) -> torch.Tensor:
        return q * q.new_tensor([1.0, -1.0, -1.0, -1.0])


class QuaternionLinear(nn.Module):
    """
    Linear layer in the quaternion algebra.

    Implements the Hamilton product W ⊗ x using four real weight matrices.
    Both in_features and out_features must be divisible by 4.
    """

    def __init__(self, in_features: int, out_features: int, bias: bool = True):
        super().__init__()
        if in_features % 4 != 0 or out_features % 4 != 0:
            raise ValueError("Features must be multiples of 4.")
        self.in_q  = in_features  // 4
        self.out_q = out_features // 4
        self.Ww = nn.Linear(self.in_q, self.out_q, bias=False)
        self.Wx = nn.Linear(self.in_q, self.out_q, bias=False)
        self.Wy = nn.Linear(self.in_q, self.out_q, bias=False)
        self.Wz = nn.Linear(self.in_q, self.out_q, bias=False)
        self.bias = nn.Parameter(torch.zeros(out_features)) if bias else None
        for w in (self.Ww, self.Wx, self.Wy, self.Wz):
            nn.init.normal_(w.weight, std=0.02)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        d = self.in_q
        xw, xx, xy, xz = x[..., :d], x[..., d:2*d], x[..., 2*d:3*d], x[..., 3*d:]
        ow = self.Ww(xw) - self.Wx(xx) - self.Wy(xy) - self.Wz(xz)
        ox = self.Ww(xx) + self.Wx(xw) + self.Wy(xz) - self.Wz(xy)
        oy = self.Ww(xy) - self.Wx(xz) + self.Wy(xw) + self.Wz(xx)
        oz = self.Ww(xz) + self.Wx(xy) - self.Wy(xx) + self.Wz(xw)
        out = torch.cat([ow, ox, oy, oz], dim=-1)
        return out + self.bias if self.bias is not None else out


class QuaternionSpectralLayer(nn.Module):
    """
    2-D spectral convolution using the quaternion Hamilton product in the
    frequency domain.  Each quaternion component (w, x, y, z) has an
    independent complex kernel (real + imaginary parts).
    """

    def __init__(self, in_q: int, out_q: int, grid_h: int, grid_w: int,
                 init_scale: float = 0.02):
        super().__init__()
        self.in_q   = in_q
        self.out_q  = out_q
        self.grid_h = grid_h
        self.grid_w = grid_w
        freq_h = grid_h
        freq_w = grid_w // 2 + 1
        for c in ("w", "x", "y", "z"):
            self.register_parameter(
                f"kr_{c}",
                nn.Parameter(torch.randn(in_q, out_q, freq_h, freq_w) * init_scale))
            self.register_parameter(
                f"ki_{c}",
                nn.Parameter(torch.randn(in_q, out_q, freq_h, freq_w) * init_scale))

    def _kernel(self, c: str) -> torch.Tensor:
        return torch.complex(getattr(self, f"kr_{c}"), getattr(self, f"ki_{c}"))

    def _contract(self, W: torch.Tensor, X: torch.Tensor) -> torch.Tensor:
        return torch.einsum("iohw,bihw->bohw", W, X)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        q = self.in_q
        xw, xx, xy, xz = x[:, :q], x[:, q:2*q], x[:, 2*q:3*q], x[:, 3*q:]
        Xw = torch.fft.rfft2(xw, s=(self.grid_h, self.grid_w))
        Xx = torch.fft.rfft2(xx, s=(self.grid_h, self.grid_w))
        Xy = torch.fft.rfft2(xy, s=(self.grid_h, self.grid_w))
        Xz = torch.fft.rfft2(xz, s=(self.grid_h, self.grid_w))
        Ww = self._kernel("w"); Wx = self._kernel("x")
        Wy = self._kernel("y"); Wz = self._kernel("z")
        C: Dict[Tuple[str, str], torch.Tensor] = {}
        for wc, W in (("w", Ww), ("x", Wx), ("y", Wy), ("z", Wz)):
            for xc, X in (("w", Xw), ("x", Xx), ("y", Xy), ("z", Xz)):
                C[(wc, xc)] = self._contract(W, X)
        Pw = C[("w","w")] - C[("x","x")] - C[("y","y")] - C[("z","z")]
        Px = C[("w","x")] + C[("x","w")] + C[("y","z")] - C[("z","y")]
        Py = C[("w","y")] - C[("x","z")] + C[("y","w")] + C[("z","x")]
        Pz = C[("w","z")] + C[("x","y")] - C[("y","x")] + C[("z","w")]
        ow = torch.fft.irfft2(Pw, s=(self.grid_h, self.grid_w))
        ox = torch.fft.irfft2(Px, s=(self.grid_h, self.grid_w))
        oy = torch.fft.irfft2(Py, s=(self.grid_h, self.grid_w))
        oz = torch.fft.irfft2(Pz, s=(self.grid_h, self.grid_w))
        return torch.cat([ow, ox, oy, oz], dim=1)


class SpectralAutoencoder(nn.Module):
    """
    Spectral autoencoder: 1-D FFT filtering + quaternion projection for
    encoding/decoding, plus stacked QuaternionSpectralLayers for the torus grid.
    """

    def __init__(self, cfg: "ModelConfig"):
        super().__init__()
        d     = cfg.d_model
        d_lat = cfg.spectral_latent_dim
        d_q   = cfg.d_quat
        r     = cfg.torus_radial
        a     = cfg.torus_angular
        s     = cfg.spectral_kernel_init_scale
        n_f   = d // 2 + 1
        self.enc_kr = nn.Parameter(torch.randn(n_f) * s)
        self.enc_ki = nn.Parameter(torch.randn(n_f) * s)
        self.dec_kr = nn.Parameter(torch.randn(n_f) * s)
        self.dec_ki = nn.Parameter(torch.randn(n_f) * s)
        self.enc_proj = QuaternionLinear(d, d_lat)
        self.dec_proj = QuaternionLinear(d_lat, d)
        self.torus_spectral = nn.ModuleList([
            QuaternionSpectralLayer(d_q, d_q, r, a, init_scale=s)
            for _ in range(cfg.num_spectral_layers)
        ])
        self.act     = nn.GELU()
        self.d_model = d

    def _filter1d(self, x: torch.Tensor,
                  kr: torch.Tensor, ki: torch.Tensor) -> torch.Tensor:
        return torch.fft.irfft(
            torch.fft.rfft(x, dim=-1) * torch.complex(kr, ki),
            n=self.d_model, dim=-1
        )

    def encode(self, x: torch.Tensor) -> torch.Tensor:
        return self.enc_proj(self.act(self._filter1d(x, self.enc_kr, self.enc_ki)))

    def decode(self, z: torch.Tensor) -> torch.Tensor:
        return self._filter1d(self.dec_proj(z), self.dec_kr, self.dec_ki)

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        z = self.encode(x)
        return z, F.mse_loss(self.decode(z), x.detach())

    def process_torus_grid(self, grid: torch.Tensor) -> torch.Tensor:
        h = grid
        for layer in self.torus_spectral:
            h = self.act(layer(h))
        return h


class QuaternionTorusBrain(nn.Module):
    """
    Replaces the MLP in each transformer layer.

    Fully vectorised pipeline:
        [B, S, D] -> spectral AE -> torus projection -> soft node assignment
        -> 2-D spectral layer on grid -> quaternion message-passing -> readout
        -> [B, S, D]
    """

    _SOFT_TEMPERATURE: float = 0.3

    def __init__(self, d_model: int, cfg: "ModelConfig"):
        super().__init__()
        self.d_model   = d_model
        self.d_q       = d_model // 4
        self.n_radial  = cfg.torus_radial
        self.n_angular = cfg.torus_angular
        self.n_nodes   = cfg.torus_radial * cfg.torus_angular
        self.spectral_ae = SpectralAutoencoder(cfg)
        self.torus_proj  = nn.Sequential(
            QuaternionLinear(d_model, d_model),
            nn.GELU(),
            nn.Linear(d_model, 4),
        )
        self.node_embed = nn.Parameter(
            torch.randn(self.n_nodes, d_model) * 0.02
        )
        self.edge_quat = nn.Parameter(torch.randn(4, 4) * 0.1)
        self.node_net  = QuaternionLinear(d_model, d_model)
        self.readout   = nn.Sequential(
            nn.Linear(d_model, d_model * 2),
            nn.GELU(),
            nn.Linear(d_model * 2, d_model),
        )
        self._build_torus_graph()

    def _build_torus_graph(self) -> None:
        edges_i, edges_j, edge_type = [], [], []
        R, A = self.n_radial, self.n_angular
        for r in range(R):
            for a in range(A):
                n = r * A + a
                edges_i.append(n); edges_j.append(r * A + (a - 1) % A); edge_type.append(0)
                edges_i.append(n); edges_j.append(r * A + (a + 1) % A); edge_type.append(1)
                if r > 0:
                    edges_i.append(n); edges_j.append((r - 1) * A + a); edge_type.append(2)
                if r < R - 1:
                    edges_i.append(n); edges_j.append((r + 1) * A + a); edge_type.append(3)
        self.register_buffer("edges_i",    torch.tensor(edges_i,   dtype=torch.long))
        self.register_buffer("edges_j",    torch.tensor(edges_j,   dtype=torch.long))
        self.register_buffer("edge_type",  torch.tensor(edge_type, dtype=torch.long))

    def _torus_soft_assign(
        self, phi1: torch.Tensor, phi2: torch.Tensor
    ) -> torch.Tensor:
        BS     = phi1.shape[0]
        device = phi1.device
        ang_pos = torch.linspace(-math.pi, math.pi, self.n_angular + 1, device=device)[:-1]
        rad_pos = torch.linspace(-math.pi, math.pi, self.n_radial  + 1, device=device)[:-1]
        d_ang  = torch.sin((phi1.unsqueeze(1) - ang_pos.unsqueeze(0)) / 2).pow(2)
        d_rad  = torch.sin((phi2.unsqueeze(1) - rad_pos.unsqueeze(0)) / 2).pow(2)
        d_torus = d_rad.unsqueeze(2) + d_ang.unsqueeze(1)
        return torch.softmax(-d_torus.view(BS, -1) / self._SOFT_TEMPERATURE, dim=-1)

    def _message_passing(self, node_feat: torch.Tensor) -> torch.Tensor:
        BS     = node_feat.shape[0]
        n_edges = self.edges_i.shape[0]
        d_q    = self.d_q
        eq     = QuaternionOps.normalize(self.edge_quat)
        src    = node_feat[:, self.edges_j, :]
        eq_exp = eq[self.edge_type].unsqueeze(0).unsqueeze(2).expand(BS, -1, d_q, -1)
        src_q  = src.view(BS, n_edges, d_q, 4)
        msg    = QuaternionOps.hamilton_product(eq_exp, src_q).view(BS, n_edges, self.d_model)
        agg    = torch.zeros_like(node_feat)
        idx    = self.edges_i.view(1, n_edges, 1).expand(BS, -1, self.d_model)
        agg.scatter_add_(1, idx, msg)
        return self.node_net(node_feat + agg)

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        B, S, D = x.shape
        xf = x.reshape(B * S, D)
        z, recon_loss = self.spectral_ae(xf)
        coords = self.torus_proj(xf)
        phi1   = math.pi * torch.tanh(coords[:, 0])
        phi2   = math.pi * torch.tanh(coords[:, 1])
        attn_w = self._torus_soft_assign(phi1, phi2)
        nodes  = (
            attn_w.unsqueeze(-1) * self.node_embed.unsqueeze(0)
            + attn_w.unsqueeze(-1) * xf.unsqueeze(1)
        )
        d_q    = self.d_q
        grid   = nodes.view(B * S, self.n_radial, self.n_angular, D)
        grid   = grid.permute(0, 3, 1, 2)
        grid_q = grid.view(B * S, 4, d_q, self.n_radial, self.n_angular)
        grid_q = grid_q.reshape(B * S, 4 * d_q, self.n_radial, self.n_angular)
        gs     = self.spectral_ae.process_torus_grid(grid_q)
        gb     = gs.view(B * S, 4, d_q, self.n_radial, self.n_angular)
        gb     = gb.permute(0, 3, 4, 1, 2).reshape(B * S, self.n_nodes, D)
        nmp    = self._message_passing(gb)
        out    = self.readout((attn_w.unsqueeze(-1) * nmp).sum(dim=1))
        return out.reshape(B, S, D), recon_loss


class SwiGLU(nn.Module):
    """SwiGLU feed-forward block (LLaMA-style)."""

    def __init__(self, d_model: int, expansion: float = 8.0 / 3.0,
                 dropout: float = 0.0):
        super().__init__()
        inner = max(4, int(d_model * expansion))
        inner = (inner + 3) // 4 * 4
        self.gate_proj = nn.Linear(d_model, inner, bias=False)
        self.up_proj   = nn.Linear(d_model, inner, bias=False)
        self.down_proj = nn.Linear(inner,   d_model, bias=False)
        self.drop = nn.Dropout(dropout) if dropout > 0.0 else nn.Identity()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.drop(
            self.down_proj(F.silu(self.gate_proj(x)) * self.up_proj(x))
        )


class TopoMoEBrain(nn.Module):
    """
    Mixture-of-Experts wrapper: one always-active QuaternionTorusBrain plus
    N sparse SwiGLU experts selected by a linear router (top-K per token).
    When moe_enabled is False this reduces to a plain QuaternionTorusBrain.
    """

    def __init__(self, d_model: int, cfg: "ModelConfig"):
        super().__init__()
        self.d_model     = d_model
        self.moe_enabled = cfg.moe_enabled
        self.n_experts   = cfg.n_experts
        self.top_k       = cfg.moe_top_k
        self.aux_weight  = cfg.moe_aux_loss_weight
        self.shared_expert = QuaternionTorusBrain(d_model, cfg)
        if self.moe_enabled:
            self.experts = nn.ModuleList([
                SwiGLU(d_model, expansion=4.0 / 3.0)
                for _ in range(self.n_experts)
            ])
            self.router = nn.Linear(d_model, self.n_experts, bias=False)

    def _route(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        N = x.shape[0]
        probs = F.softmax(self.router(x), dim=-1)
        top_k_probs, top_k_idx = torch.topk(probs, self.top_k, dim=-1)
        top_k_probs = top_k_probs / top_k_probs.sum(dim=-1, keepdim=True).clamp(min=1e-9)
        flat_idx     = top_k_idx.reshape(-1)
        flat_weights = top_k_probs.reshape(-1)
        tok_idx      = (
            torch.arange(N, device=x.device, dtype=torch.long)
            .unsqueeze(1).expand(-1, self.top_k).reshape(-1)
        )
        expert_out = torch.zeros_like(x)
        for e in range(self.n_experts):
            mask = flat_idx == e
            src  = tok_idx[mask]
            w    = flat_weights[mask].unsqueeze(-1).to(x.dtype)
            expert_out.scatter_add_(
                0, src.unsqueeze(1).expand(-1, x.shape[1]),
                w * self.experts[e](x[src])
            )
        tf  = probs.mean(dim=0)
        df  = F.one_hot(top_k_idx, self.n_experts).float().mean(dim=(0, 1))
        aux = self.n_experts * (tf * df).sum()
        return expert_out, aux

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        B, S, D = x.shape
        shared, recon = self.shared_expert(x)
        if not self.moe_enabled:
            return shared, recon
        expert_out, aux = self._route(x.reshape(B * S, D))
        return shared + expert_out.reshape(B, S, D), recon + self.aux_weight * aux


class RotaryEmbedding(nn.Module):
    """Rotary Position Embeddings (RoPE) – Su et al., 2021."""

    _BASE: int = 10000

    def __init__(self, d_head: int, max_seq_len: int = 2048):
        super().__init__()
        inv_freq = 1.0 / (
            self._BASE ** (torch.arange(0, d_head, 2).float() / d_head)
        )
        self.register_buffer("inv_freq", inv_freq)
        self._build_cache(max_seq_len)

    def _build_cache(self, seq_len: int) -> None:
        t   = torch.arange(seq_len, device=self.inv_freq.device).float()
        emb = torch.cat([torch.outer(t, self.inv_freq)] * 2, dim=-1)
        self.register_buffer("cos_cache", emb.cos())
        self.register_buffer("sin_cache", emb.sin())

    @staticmethod
    def _rotate_half(x: torch.Tensor) -> torch.Tensor:
        h = x.shape[-1] // 2
        return torch.cat([-x[..., h:], x[..., :h]], dim=-1)

    def forward(
        self, q: torch.Tensor, k: torch.Tensor,
        seq_len: int, offset: int = 0
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        needed = offset + max(q.shape[2], k.shape[2])
        if needed > self.cos_cache.shape[0]:
            self._build_cache(needed * 2)
        sq, sk = q.shape[2], k.shape[2]
        cq = self.cos_cache[offset:offset + sq].unsqueeze(0).unsqueeze(0)
        sq_ = self.sin_cache[offset:offset + sq].unsqueeze(0).unsqueeze(0)
        ck = self.cos_cache[offset:offset + sk].unsqueeze(0).unsqueeze(0)
        sk_ = self.sin_cache[offset:offset + sk].unsqueeze(0).unsqueeze(0)
        return (q * cq + self._rotate_half(q) * sq_,
                k * ck + self._rotate_half(k) * sk_)


class RMSNorm(nn.Module):
    """Root Mean Square Layer Normalization (no bias)."""

    def __init__(self, d_model: int, eps: float = 1e-6):
        super().__init__()
        self.eps    = eps
        self.weight = nn.Parameter(torch.ones(d_model))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x / x.pow(2).mean(-1, keepdim=True).add(self.eps).sqrt() * self.weight


class MultiHeadAttention(nn.Module):
    """
    GQA-capable multi-head attention with Flash Attention, RoPE, and KV cache.
    """

    def __init__(self, d_model: int, n_heads: int, cfg: "ModelConfig"):
        super().__init__()
        self.d_model  = d_model
        self.n_heads  = n_heads
        self.n_kv     = cfg.n_kv_heads
        self.n_groups = cfg.gqa_groups
        self.d_head   = d_model // n_heads
        self.q_proj   = nn.Linear(d_model, n_heads      * self.d_head, bias=False)
        self.k_proj   = nn.Linear(d_model, self.n_kv    * self.d_head, bias=False)
        self.v_proj   = nn.Linear(d_model, self.n_kv    * self.d_head, bias=False)
        self.o_proj   = nn.Linear(d_model, d_model,                    bias=False)
        self.rope      = RotaryEmbedding(self.d_head, max_seq_len=cfg.max_seq_len)
        self.temperature = nn.Parameter(torch.tensor(1.0))
        self.dropout_p   = 0.0

    def forward(
        self, x: torch.Tensor, is_causal: bool = True,
        past_kv: Optional[Tuple[torch.Tensor, torch.Tensor]] = None
    ) -> Tuple[torch.Tensor, Tuple[torch.Tensor, torch.Tensor]]:
        B, S, D = x.shape
        Q = self.q_proj(x).view(B, S, self.n_heads, self.d_head).transpose(1, 2)
        K = self.k_proj(x).view(B, S, self.n_kv,    self.d_head).transpose(1, 2)
        V = self.v_proj(x).view(B, S, self.n_kv,    self.d_head).transpose(1, 2)
        offset = past_kv[0].shape[2] if past_kv is not None else 0
        Q, K   = self.rope(Q, K, seq_len=S, offset=offset)
        if past_kv is not None:
            K = torch.cat([past_kv[0], K], dim=2)
            V = torch.cat([past_kv[1], V], dim=2)
        kv_cache = (K, V)
        if self.n_groups > 1:
            K = K.unsqueeze(2).expand(-1, -1, self.n_groups, -1, -1).reshape(
                B, self.n_heads, K.shape[2], self.d_head)
            V = V.unsqueeze(2).expand(-1, -1, self.n_groups, -1, -1).reshape(
                B, self.n_heads, V.shape[2], self.d_head)
        scale = (self.d_head ** -0.5) / self.temperature.abs().clamp(min=1e-6)
        out   = F.scaled_dot_product_attention(
            Q, K, V, attn_mask=None,
            dropout_p=0.0,
            is_causal=(is_causal and past_kv is None),
            scale=scale.item(),
        )
        return self.o_proj(out.transpose(1, 2).contiguous().view(B, S, D)), kv_cache


class TopoGPT2Layer(nn.Module):
    """Pre-norm transformer layer: attention + TopoMoEBrain."""

    def __init__(self, d_model: int, n_heads: int, cfg: "ModelConfig"):
        super().__init__()
        self.norm1      = RMSNorm(d_model)
        self.norm2      = RMSNorm(d_model)
        self.attn       = MultiHeadAttention(d_model, n_heads, cfg)
        self.topo_brain = TopoMoEBrain(d_model, cfg)
        self.dropout    = nn.Dropout(0.0)

    def forward(
        self, x: torch.Tensor,
        past_kv: Optional[Tuple] = None
    ) -> Tuple[torch.Tensor, torch.Tensor, Optional[Tuple]]:
        attn_out, kv_cache = self.attn(self.norm1(x), past_kv=past_kv)
        x = x + self.dropout(attn_out)
        brain_out, aux    = self.topo_brain(self.norm2(x))
        x = x + self.dropout(brain_out)
        return x, aux, kv_cache


class TopoGPT2(nn.Module):
    """
    TopoGPT2: causal language model with quaternion torus topology.
    Embedding -> N layers (Attention + QuaternionTorusBrain) -> RMSNorm -> LM head.
    """

    def __init__(self, cfg: "ModelConfig"):
        super().__init__()
        self.cfg         = cfg
        self.token_embed = nn.Embedding(cfg.vocab_size, cfg.d_model)
        self.layers      = nn.ModuleList([
            TopoGPT2Layer(cfg.d_model, cfg.n_heads, cfg)
            for _ in range(cfg.n_layers)
        ])
        self.final_norm  = RMSNorm(cfg.d_model)
        self.lm_head     = nn.Linear(cfg.d_model, cfg.vocab_size, bias=False)
        self.lm_head.weight = self.token_embed.weight

    def forward(
        self, token_ids: torch.Tensor,
        past_kvs: Optional[List[Optional[Tuple]]] = None
    ) -> Tuple[torch.Tensor, torch.Tensor, List]:
        x         = self.token_embed(token_ids)
        total_aux = token_ids.new_zeros(1, dtype=torch.float)
        new_kvs: List = []
        for i, layer in enumerate(self.layers):
            pkv = past_kvs[i] if past_kvs is not None else None
            x, al, kvc = layer(x, past_kv=pkv)
            total_aux   = total_aux + al
            new_kvs.append(kvc)
        x      = self.final_norm(x)
        logits = self.lm_head(x)
        return logits, total_aux / len(self.layers), new_kvs


# ===========================================================================
# INTERNAL MODEL CONFIG (decoupled from InferenceConfig)
# ===========================================================================

@dataclass
class ModelConfig:
    """
    All architectural hyperparameters required to instantiate TopoGPT2.
    Populated entirely from the probed checkpoint shapes.
    """

    d_model:                 int
    n_heads:                 int
    n_kv_heads:              int
    n_layers:                int
    vocab_size:              int
    torus_radial:            int
    torus_angular:           int
    spectral_latent_dim:     int
    n_experts:               int
    moe_enabled:             bool
    num_spectral_layers:     int
    max_seq_len:             int = 512
    moe_top_k:               int = 2
    moe_aux_loss_weight:     float = 0.01
    spectral_kernel_init_scale: float = 0.02

    @property
    def d_quat(self) -> int:
        return self.d_model // 4

    @property
    def gqa_groups(self) -> int:
        return self.n_heads // self.n_kv_heads


# ===========================================================================
# CHECKPOINT ARCHITECTURE PROBER
# ===========================================================================

class CheckpointArchProber:
    """
    Infers all ModelConfig fields directly from checkpoint tensor shapes,
    without relying on any saved metadata, scale preset, or source file.

    Key derivations
    ---------------
    d_model        : token_embed.weight shape [V, D] -> D
    vocab_size     : token_embed.weight shape [V, D] -> V
    d_head         : rope.inv_freq shape [d_head // 2] -> d_head
    n_heads        : q_proj.weight shape [n_heads * d_head, D] -> n_heads
    n_kv_heads     : k_proj.weight shape [n_kv * d_head, D] -> n_kv
    n_layers       : count of q_proj keys
    torus_radial   : torus_spectral.0.kr_w shape [..., freq_h, ...] -> freq_h
    torus_angular  : torus_spectral.0.kr_w shape [..., freq_w] -> (freq_w-1)*2
    spectral_latent: enc_proj.Ww.weight shape [out_q, in_q] -> out_q * 4
    n_experts      : count of experts.N.gate_proj.weight keys in layer 0
    num_spec_layers: count of torus_spectral.N.kr_w keys in layer 0
    """

    _EMBED_KEY     = "token_embed.weight"
    _Q_PROJ_KEY    = "layers.0.attn.q_proj.weight"
    _K_PROJ_KEY    = "layers.0.attn.k_proj.weight"
    _ROPE_KEY      = "layers.0.attn.rope.inv_freq"
    _ROPE_COS_KEY  = "layers.0.attn.rope.cos_cache"
    _TORUS_SPEC_KEY = (
        "layers.0.topo_brain.shared_expert.spectral_ae.torus_spectral.0.kr_w"
    )
    _ENC_PROJ_KEY  = (
        "layers.0.topo_brain.shared_expert.spectral_ae.enc_proj.Ww.weight"
    )
    _EXPERT_GATE_PATTERN = "layers.0.topo_brain.experts."

    def __init__(self, logger: Optional[logging.Logger] = None):
        self._log = logger or build_logger("CheckpointArchProber")

    def _load_shapes(
        self, path: str
    ) -> Dict[str, Tuple[int, ...]]:
        path_obj = Path(path)
        if path_obj.suffix == ".safetensors" and _SAFETENSORS:
            from safetensors import safe_open
            shapes: Dict[str, Tuple[int, ...]] = {}
            with safe_open(path, framework="pt", device="cpu") as f:
                for key in f.keys():
                    shapes[key] = tuple(f.get_tensor(key).shape)
            return shapes
        raw = torch.load(path, map_location="cpu", weights_only=False)
        sd  = raw.get("model_state_dict", raw)
        return {k: tuple(v.shape) for k, v in sd.items()}

    def probe(self, path: str) -> ModelConfig:
        """Return a ModelConfig whose dimensions exactly match the checkpoint."""
        shapes = self._load_shapes(path)

        embed_shape = shapes[self._EMBED_KEY]
        vocab_size  = embed_shape[0]
        d_model     = embed_shape[1]

        if self._ROPE_KEY in shapes:
            d_head = shapes[self._ROPE_KEY][0] * 2
        else:
            d_head = self._fallback_d_head(
                d_model,
                shapes[self._Q_PROJ_KEY][0],
                shapes[self._K_PROJ_KEY][0],
            )
            self._log.warning("rope.inv_freq absent; d_head inferred as %d.", d_head)

        # max_seq_len from RoPE cosine cache (shape [seq_len, d_head])
        if self._ROPE_COS_KEY in shapes:
            max_seq_len = shapes[self._ROPE_COS_KEY][0]
        else:
            max_seq_len = 512
            self._log.warning("rope.cos_cache absent; max_seq_len defaulted to %d.", max_seq_len)

        q_out      = shapes[self._Q_PROJ_KEY][0]
        k_out      = shapes[self._K_PROJ_KEY][0]
        n_heads    = q_out // d_head
        n_kv_heads = k_out // d_head

        n_layers = sum(
            1 for k in shapes
            if k.startswith("layers.") and k.endswith(".attn.q_proj.weight")
        )

        if self._TORUS_SPEC_KEY in shapes:
            ks            = shapes[self._TORUS_SPEC_KEY]
            torus_radial  = ks[2]
            torus_angular = (ks[3] - 1) * 2
        else:
            raise RuntimeError(
                f"Cannot determine torus geometry: key '{self._TORUS_SPEC_KEY}' "
                "not found in checkpoint."
            )

        enc_proj = shapes.get(self._ENC_PROJ_KEY)
        spectral_latent = enc_proj[0] * 4 if enc_proj else max(16, d_model // 2)

        expert_keys = [
            k for k in shapes
            if k.startswith(self._EXPERT_GATE_PATTERN) and k.endswith("gate_proj.weight")
        ]
        n_experts   = len(expert_keys)
        moe_enabled = n_experts > 0

        num_spec_layers = sum(
            1 for k in shapes
            if "topo_brain.shared_expert.spectral_ae.torus_spectral." in k
            and k.startswith("layers.0.")
            and k.endswith(".kr_w")
        )

        cfg = ModelConfig(
            d_model=d_model,
            n_heads=n_heads,
            n_kv_heads=n_kv_heads,
            n_layers=n_layers,
            vocab_size=vocab_size,
            torus_radial=torus_radial,
            torus_angular=torus_angular,
            spectral_latent_dim=spectral_latent,
            n_experts=n_experts,
            moe_enabled=moe_enabled,
            num_spectral_layers=num_spec_layers,
            max_seq_len=max_seq_len,
        )
        self._log.info(
            "Probed: d=%d  heads=%d  kv_heads=%d  layers=%d  "
            "torus=%dR×%dA  experts=%d  latent=%d",
            d_model, n_heads, n_kv_heads, n_layers,
            torus_radial, torus_angular, n_experts, spectral_latent,
        )
        return cfg

    @staticmethod
    def _fallback_d_head(d_model: int, q_out: int, k_out: int) -> int:
        candidates = [
            d for d in range(1, d_model + 1)
            if d_model % d == 0 and q_out % d == 0 and k_out % d == 0
            and (q_out // d) % (k_out // d) == 0
        ]
        if not candidates:
            raise RuntimeError(
                f"Cannot infer d_head: d_model={d_model}, "
                f"q_out={q_out}, k_out={k_out}."
            )
        standard = [d for d in candidates if d >= 16 and (d & (d - 1)) == 0]
        return max(standard) if standard else max(candidates)


# ===========================================================================
# CHECKPOINT LOADER
# ===========================================================================

class CheckpointLoader:
    """
    Loads a safetensors or pickle checkpoint into a TopoGPT2 instance.
    Restores weight tying after loading.
    """

    def __init__(self, logger: Optional[logging.Logger] = None):
        self._log = logger or build_logger("CheckpointLoader")

    def load(self, path: str, model: TopoGPT2, device: str) -> None:
        """Load weights into model in-place."""
        path_obj = Path(path)
        if not path_obj.exists():
            raise FileNotFoundError(f"Checkpoint not found: {path}")

        self._log.info("Loading weights from %s", path)

        if path_obj.suffix == ".safetensors" and _SAFETENSORS:
            state = st_load(path, device=device)
        else:
            raw   = torch.load(path, map_location=device, weights_only=False)
            state = raw.get("model_state_dict", raw)

        # RoPE cos/sin caches are purely derived buffers that are recomputed
        # on the first forward pass.  Removing them before load_state_dict
        # avoids size-mismatch errors when the checkpoint's max_seq_len
        # differs from what we probed (e.g. expanded vs original models).
        rope_cache_keys = {
            k for k in state
            if k.endswith(".cos_cache") or k.endswith(".sin_cache")
        }
        for k in rope_cache_keys:
            del state[k]

        missing, unexpected = model.load_state_dict(state, strict=False)

        # Re-apply weight tying; lm_head.weight is intentionally absent
        model.lm_head.weight = model.token_embed.weight

        silent_missing = {"lm_head.weight"} | rope_cache_keys
        real_missing   = [k for k in missing if k not in silent_missing]
        if real_missing:
            self._log.warning("Missing keys (%d): %s ...", len(real_missing), real_missing[:5])
        if unexpected:
            self._log.warning("Unexpected keys (%d): %s ...", len(unexpected), unexpected[:5])

        self._log.info("Checkpoint loaded.")


# ===========================================================================
# SAMPLER
# ===========================================================================

class Sampler:
    """
    Stateless token sampling with temperature, top-k, top-p, and
    repetition penalty.  All operations are performed on the logit tensor
    returned by the model before softmax.
    """

    def __init__(self, cfg: InferenceConfig):
        self._cfg = cfg

    def __call__(
        self,
        logits: torch.Tensor,
        generated_ids: Optional[List[int]] = None,
    ) -> int:
        """
        Sample one token from logits.

        Parameters
        ----------
        logits       : [vocab_size] raw logits for the next token position.
        generated_ids: token IDs already generated (for repetition penalty).

        Returns
        -------
        Sampled token id.
        """
        logits = logits.clone().float()

        if self._cfg.repetition_penalty != 1.0 and generated_ids:
            unique_ids = torch.tensor(
                list(set(generated_ids)), dtype=torch.long, device=logits.device
            )
            logits[unique_ids] /= self._cfg.repetition_penalty

        if self._cfg.temperature == 0.0:
            return int(logits.argmax().item())

        logits = logits / self._cfg.temperature

        if self._cfg.top_k > 0:
            k = min(self._cfg.top_k, logits.size(-1))
            threshold = torch.topk(logits, k).values[..., -1]
            logits[logits < threshold] = float("-inf")

        if self._cfg.top_p < 1.0:
            sorted_logits, sorted_idx = torch.sort(logits, descending=True)
            cum_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)
            remove_mask = cum_probs - F.softmax(sorted_logits, dim=-1) > self._cfg.top_p
            sorted_logits[remove_mask] = float("-inf")
            logits = torch.zeros_like(logits).scatter_(0, sorted_idx, sorted_logits)

        probs = F.softmax(logits, dim=-1)
        return int(torch.multinomial(probs, num_samples=1).item())


# ===========================================================================
# GENERATION ENGINE
# ===========================================================================

class GenerationEngine:
    """
    Autoregressive generation with KV cache and optional token streaming.

    First forward pass processes the full prompt and seeds the KV cache.
    Subsequent passes process a single token each, giving O(n) complexity.
    """

    _EOS_TOKEN_ID: int = 50256

    def __init__(
        self,
        model: TopoGPT2,
        tokenizer: BPETokenizer,
        cfg: InferenceConfig,
        logger: Optional[logging.Logger] = None,
    ):
        self._model     = model
        self._tokenizer = tokenizer
        self._cfg       = cfg
        self._sampler   = Sampler(cfg)
        self._log       = logger or build_logger("GenerationEngine")

    @torch.inference_mode()
    def generate(self, prompt: str) -> Tuple[str, float]:
        """
        Generate text from prompt.

        Returns
        -------
        (generated_text, tokens_per_second)
        generated_text includes the prompt prefix.
        """
        device   = self._cfg.device
        max_seq  = self._model.cfg.max_seq_len
        prompt_ids = self._tokenizer.encode(prompt)
        if not prompt_ids:
            raise ValueError("Prompt encodes to zero tokens.")

        ctx_ids    = prompt_ids[-max_seq:]
        input_t    = torch.tensor([ctx_ids], dtype=torch.long, device=device)
        generated  = list(ctx_ids)

        t0 = time.perf_counter()

        logits, _, past_kvs = self._model(input_t)
        next_id = self._sampler(logits[0, -1, :], generated)
        generated.append(next_id)
        self._maybe_stream(next_id)

        for _ in range(self._cfg.max_new_tokens - 1):
            if next_id == self._EOS_TOKEN_ID:
                break
            next_t = torch.tensor([[next_id]], dtype=torch.long, device=device)
            logits, _, past_kvs = self._model(next_t, past_kvs=past_kvs)
            next_id = self._sampler(logits[0, -1, :], generated)
            generated.append(next_id)
            self._maybe_stream(next_id)

        elapsed     = time.perf_counter() - t0
        new_tokens  = len(generated) - len(ctx_ids)
        tps         = new_tokens / elapsed if elapsed > 0 else 0.0

        if self._cfg.stream:
            print(flush=True)

        return self._tokenizer.decode(generated), tps

    def _maybe_stream(self, token_id: int) -> None:
        if not self._cfg.stream:
            return
        piece = self._tokenizer.decode_single(token_id)
        print(piece, end="", flush=True)


# ===========================================================================
# RESULT PRINTER
# ===========================================================================

class ResultPrinter:
    """Formats and writes generation results to stdout."""

    _WIDTH: int = 72

    def print_single(
        self, prompt: str, full_text: str, tps: float, show_timing: bool
    ) -> None:
        continuation = full_text[len(prompt):]
        print("\n" + "=" * self._WIDTH)
        print("PROMPT:")
        print(prompt)
        print("\nGENERATED:")
        print(continuation)
        if show_timing:
            print(f"\n[{tps:.1f} tok/s]")
        print("=" * self._WIDTH)

    def print_benchmark(
        self, runs: int, tps_list: List[float]
    ) -> None:
        avg = sum(tps_list) / len(tps_list)
        mn  = min(tps_list)
        mx  = max(tps_list)
        print("\n" + "=" * self._WIDTH)
        print(f"BENCHMARK  ({runs} runs)")
        print(f"  avg: {avg:.2f} tok/s   min: {mn:.2f}   max: {mx:.2f}")
        print("=" * self._WIDTH)


# ===========================================================================
# INFERENCE PIPELINE
# ===========================================================================

class InferencePipeline:
    """
    Orchestrates the full inference workflow.

    1. Validate config.
    2. Probe checkpoint architecture.
    3. Instantiate model.
    4. Load weights.
    5. Run generation in the requested mode.
    """

    def __init__(self, cfg: InferenceConfig, logger: Optional[logging.Logger] = None):
        self._cfg = cfg
        self._log = logger or build_logger("InferencePipeline", level=cfg.log_level)

    def _build_model(self) -> Tuple[TopoGPT2, BPETokenizer]:
        prober = CheckpointArchProber(logger=self._log)
        arch   = prober.probe(self._cfg.checkpoint_path)

        model  = TopoGPT2(arch).to(self._cfg.device)
        model.eval()

        loader = CheckpointLoader(logger=self._log)
        loader.load(self._cfg.checkpoint_path, model, self._cfg.device)

        tokenizer = BPETokenizer()
        self._log.info(
            "Model ready: %.2fM parameters  vocab=%d",
            sum(p.numel() for p in model.parameters()) / 1e6,
            arch.vocab_size,
        )
        return model, tokenizer

    def run(self) -> None:
        self._cfg.validate()
        torch.manual_seed(self._cfg.seed)

        model, tokenizer = self._build_model()
        engine  = GenerationEngine(model, tokenizer, self._cfg, logger=self._log)
        printer = ResultPrinter()

        if self._cfg.benchmark_runs > 0:
            self._run_benchmark(engine, printer)
        elif self._cfg.interactive:
            self._run_interactive(engine, printer)
        else:
            self._run_single(engine, printer)

    def _run_single(
        self, engine: GenerationEngine, printer: ResultPrinter
    ) -> None:
        self._log.info("Generating for prompt: %r", self._cfg.prompt)
        text, tps = engine.generate(self._cfg.prompt)
        if not self._cfg.stream:
            printer.print_single(
                self._cfg.prompt, text, tps, self._cfg.show_timing
            )
        elif self._cfg.show_timing:
            print(f"\n[{tps:.1f} tok/s]")

    def _run_interactive(
        self, engine: GenerationEngine, printer: ResultPrinter
    ) -> None:
        print("TopoGPT2 interactive mode.  Type 'quit' or Ctrl-D to exit.\n")
        while True:
            try:
                prompt = input(">>> ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if not prompt:
                continue
            if prompt.lower() in {"quit", "exit", "q"}:
                break
            try:
                text, tps = engine.generate(prompt)
                if not self._cfg.stream:
                    printer.print_single(prompt, text, tps, self._cfg.show_timing)
                elif self._cfg.show_timing:
                    print(f"\n[{tps:.1f} tok/s]")
            except Exception as exc:
                print(f"[error] {exc}")

    def _run_benchmark(
        self, engine: GenerationEngine, printer: ResultPrinter
    ) -> None:
        runs    = self._cfg.benchmark_runs
        prompt  = self._cfg.prompt
        tps_list: List[float] = []
        self._log.info("Benchmark: %d runs, prompt=%r", runs, prompt)
        for i in range(runs):
            _, tps = engine.generate(prompt)
            tps_list.append(tps)
            self._log.info("Run %d/%d: %.2f tok/s", i + 1, runs, tps)
        printer.print_benchmark(runs, tps_list)


# ===========================================================================
# CLI
# ===========================================================================

def build_arg_parser() -> argparse.ArgumentParser:
    """Construct and return the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="TopoGPT2 Inference Engine (auto-probes checkpoint architecture)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--ckpt", required=True,
        metavar="PATH",
        help="Path to .safetensors or .pt checkpoint.",
    )
    parser.add_argument(
        "--prompt", default="Once upon a time",
        help="Prompt text for single-shot generation.",
    )
    parser.add_argument(
        "--max-new", type=int, default=200,
        metavar="N",
        help="Maximum new tokens to generate.",
    )
    parser.add_argument(
        "--temp", type=float, default=0.8,
        metavar="T",
        help="Sampling temperature.  0 = greedy.",
    )
    parser.add_argument(
        "--top-k", type=int, default=50,
        metavar="K",
        help="Top-k filtering.  0 disables.",
    )
    parser.add_argument(
        "--top-p", type=float, default=0.95,
        metavar="P",
        help="Nucleus (top-p) filtering.  1.0 disables.",
    )
    parser.add_argument(
        "--rep-penalty", type=float, default=1.1,
        metavar="R",
        help="Repetition penalty.  1.0 disables.",
    )
    parser.add_argument(
        "--seed", type=int, default=42,
    )
    parser.add_argument(
        "--device", default="cuda" if torch.cuda.is_available() else "cpu",
    )
    parser.add_argument(
        "--stream", action="store_true",
        help="Print tokens as they are generated.",
    )
    parser.add_argument(
        "--no-timing", action="store_true",
        help="Suppress tokens-per-second display.",
    )
    parser.add_argument(
        "--interactive", action="store_true",
        help="Enter an interactive REPL instead of single-shot generation.",
    )
    parser.add_argument(
        "--benchmark", type=int, default=0,
        metavar="N",
        help="Run N benchmark passes and report throughput.",
    )
    parser.add_argument(
        "--log", default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging verbosity.",
    )
    return parser


def main() -> None:
    """CLI entry point."""
    parser = build_arg_parser()
    args   = parser.parse_args()

    cfg = InferenceConfig(
        checkpoint_path=args.ckpt,
        device=args.device,
        max_new_tokens=args.max_new,
        temperature=args.temp,
        top_k=args.top_k,
        top_p=args.top_p,
        repetition_penalty=args.rep_penalty,
        seed=args.seed,
        log_level=args.log,
        stream=args.stream,
        show_timing=not args.no_timing,
        prompt=args.prompt,
        interactive=args.interactive,
        benchmark_runs=args.benchmark,
    )

    pipeline = InferencePipeline(cfg)
    pipeline.run()


if __name__ == "__main__":
    main()