#!/usr/bin/env python3
"""
topogpt2_expand.py

Zero-shot torus resolution expansion for TopoGPT2.

Transfers all weights from a trained TopoGPT2 checkpoint into a new model
whose torus topology (TORUS_RADIAL_BINS x TORUS_ANGULAR_BINS) has been scaled
up, without any fine-tuning.  The fixed message-passing graph is rebuilt at
the new resolution; the spectral kernels are interpolated in frequency space;
the node embeddings are bilinearly interpolated over the torus manifold; and
all other weights are copied verbatim.

Usage
-----
    python topogpt2_expand.py \\
        --src   checkpoints_topogpt2/latest/model.safetensors \\
        --dst   checkpoints_topogpt2/expanded/model.safetensors \\
        --radial   4 \\
        --angular  8 \\
        --scale small \\
        --validate \\
        --prompt "Once upon a time"

Author  : Gris Iscomeback
License : GPL v3
"""

from __future__ import annotations

import argparse
import json
import logging
import math
import os
import sys
import warnings
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F

warnings.filterwarnings("ignore")

# ---------------------------------------------------------------------------
# Optional heavy imports – fail gracefully so the expander can be imported
# as a library even when tiktoken / safetensors are absent.
# ---------------------------------------------------------------------------
try:
    from safetensors.torch import save_file as st_save, load_file as st_load
    _SAFETENSORS_AVAILABLE = True
except ImportError:
    _SAFETENSORS_AVAILABLE = False

try:
    import tiktoken as _tiktoken
    _TIKTOKEN_AVAILABLE = True
except ImportError:
    _TIKTOKEN_AVAILABLE = False


# ===========================================================================
# LOGGING
# ===========================================================================

def build_logger(name: str, level: str = "INFO") -> logging.Logger:
    """Return a stderr logger with timestamp formatting."""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(
            logging.Formatter("%(asctime)s  %(name)s  %(levelname)s  %(message)s")
        )
        logger.addHandler(handler)
    return logger


# ===========================================================================
# CONFIGURATION
# ===========================================================================

@dataclass
class ExpansionConfig:
    """
    All tuneable knobs for the zero-shot expansion procedure.

    Attributes
    ----------
    src_path : str
        Path to the source safetensors checkpoint.
    dst_path : str
        Path where the expanded checkpoint will be written.
    src_radial : int
        Source TORUS_RADIAL_BINS (read from the checkpoint metadata when
        available; otherwise taken from the model scale preset).
    src_angular : int
        Source TORUS_ANGULAR_BINS.
    tgt_radial : int
        Target TORUS_RADIAL_BINS after expansion.
    tgt_angular : int
        Target TORUS_ANGULAR_BINS after expansion.
    scale : str
        Model scale preset: micro | small | medium | gpt2.
    device : str
        Torch device for weight manipulation.
    validate : bool
        Run a forward-pass sanity check on the expanded model.
    validate_prompt : str
        Prompt text for the sanity check (requires tiktoken).
    log_level : str
        Python logging level name.
    spectral_interp_mode : str
        How to interpolate spectral kernels: 'bilinear' or 'nearest'.
    node_embed_interp_mode : str
        How to interpolate node embeddings: 'bilinear' or 'nearest'.
    """

    src_path: str = "checkpoints_topogpt2/latest/model.safetensors"
    dst_path: str = "checkpoints_topogpt2/expanded/model.safetensors"

    src_radial: int = 2
    src_angular: int = 4
    tgt_radial: int = 4
    tgt_angular: int = 8

    scale: str = "small"
    device: str = "cpu"

    validate: bool = False
    validate_prompt: str = "Once upon a time"
    log_level: str = "INFO"

    spectral_interp_mode: str = "bilinear"
    node_embed_interp_mode: str = "bilinear"

    def validate_geometry(self) -> None:
        """Raise ValueError for impossible torus configurations."""
        if self.tgt_radial < self.src_radial:
            raise ValueError(
                f"tgt_radial ({self.tgt_radial}) must be >= src_radial ({self.src_radial})"
            )
        if self.tgt_angular < self.src_angular:
            raise ValueError(
                f"tgt_angular ({self.tgt_angular}) must be >= src_angular ({self.src_angular})"
            )
        if self.tgt_radial < 1 or self.tgt_angular < 1:
            raise ValueError("Torus bins must be positive integers.")

    @property
    def src_nodes(self) -> int:
        return self.src_radial * self.src_angular

    @property
    def tgt_nodes(self) -> int:
        return self.tgt_radial * self.tgt_angular


# ---------------------------------------------------------------------------
# TopoGPT2Config – minimal reproduction needed for model construction.
# The full training config is intentionally NOT imported to keep this script
# self-contained and free of corpus / checkpoint-manager dependencies.
# ---------------------------------------------------------------------------

@dataclass
class TopoGPT2Config:
    """
    Minimal reproduction of the model-architecture fields from the original
    TopoGPT2Config.  Only the fields required to instantiate the neural
    network are present here.
    """

    DEVICE: str = "cpu"
    RANDOM_SEED: int = 42
    USE_AMP: bool = False

    SCALE: str = "small"

    VOCAB_SIZE: int = 50257
    MAX_SEQ_LEN: int = 512

    D_MODEL: int = 256
    N_HEADS: int = 8
    N_KV_HEADS: int = 0
    N_LAYERS: int = 6
    DROPOUT: float = 0.0

    MOE_ENABLED: bool = True
    N_EXPERTS: int = 4
    MOE_TOP_K: int = 2
    MOE_AUX_LOSS_WEIGHT: float = 0.01

    TORUS_GRID_SIZE: int = 8
    TORUS_RADIAL_BINS: int = 2
    TORUS_ANGULAR_BINS: int = 4

    SPECTRAL_LATENT_RATIO: float = 0.5
    SPECTRAL_KERNEL_INIT_SCALE: float = 0.02
    NUM_SPECTRAL_LAYERS: int = 2
    AE_RECON_WEIGHT: float = 0.01

    GRADIENT_CHECKPOINTING: bool = False
    T_INIT: float = 1.0

    # Derived fields – computed in __post_init__
    D_QUAT: int = field(init=False, default=0)
    D_HEAD: int = field(init=False, default=0)
    SPECTRAL_LATENT_DIM: int = field(init=False, default=0)
    N_TORUS_NODES: int = field(init=False, default=0)
    GQA_GROUPS: int = field(init=False, default=0)

    _SCALE_PRESETS: Dict = field(init=False, repr=False, default_factory=lambda: {
        "micro":  dict(D_MODEL=64,  N_HEADS=4,  N_LAYERS=2,  MAX_SEQ_LEN=128),
        "small":  dict(D_MODEL=256, N_HEADS=8,  N_LAYERS=6,  MAX_SEQ_LEN=256),
        "medium": dict(D_MODEL=512, N_HEADS=8,  N_LAYERS=12, MAX_SEQ_LEN=512),
        "gpt2":   dict(D_MODEL=768, N_HEADS=12, N_LAYERS=12, MAX_SEQ_LEN=1024),
    })

    def __post_init__(self) -> None:
        if self.SCALE in self._SCALE_PRESETS:
            for key, val in self._SCALE_PRESETS[self.SCALE].items():
                setattr(self, key, val)

        if self.D_MODEL % 4 != 0:
            raise ValueError("D_MODEL must be divisible by 4 (quaternion algebra).")
        if self.D_MODEL % self.N_HEADS != 0:
            raise ValueError("D_MODEL must be divisible by N_HEADS.")

        self.D_QUAT = self.D_MODEL // 4
        self.D_HEAD = self.D_MODEL // self.N_HEADS
        self.SPECTRAL_LATENT_DIM = max(16, int(self.D_MODEL * self.SPECTRAL_LATENT_RATIO))
        self.N_TORUS_NODES = self.TORUS_RADIAL_BINS * self.TORUS_ANGULAR_BINS

        if self.N_KV_HEADS == 0:
            kv = max(1, self.N_HEADS // 4)
            while self.N_HEADS % kv != 0:
                kv -= 1
            self.N_KV_HEADS = kv
        elif self.N_KV_HEADS == -1:
            self.N_KV_HEADS = self.N_HEADS

        if self.N_HEADS % self.N_KV_HEADS != 0:
            raise ValueError("N_HEADS must be divisible by N_KV_HEADS.")
        self.GQA_GROUPS = self.N_HEADS // self.N_KV_HEADS


# ===========================================================================
# ARCHITECTURE (verbatim from topogpt2.py – self-contained copy)
# ===========================================================================

class QuaternionOps:
    """Static quaternion algebra operations in PyTorch."""

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
        sign = q.new_tensor([1.0, -1.0, -1.0, -1.0])
        return q * sign

    @staticmethod
    def rotate_vector(v: torch.Tensor, q: torch.Tensor) -> torch.Tensor:
        zero = torch.zeros(*v.shape[:-1], 1, device=v.device, dtype=v.dtype)
        v_q = torch.cat([zero, v], dim=-1)
        q_c = QuaternionOps.conjugate(q)
        rotated = QuaternionOps.hamilton_product(
            QuaternionOps.hamilton_product(q, v_q), q_c)
        return rotated[..., 1:]


class QuaternionLinear(nn.Module):
    """
    Quaternion-valued linear layer.

    Performs the Hamilton product W ⊗ x in the quaternion algebra,
    using four real weight matrices (one per quaternion component).
    Both in_features and out_features must be divisible by 4.
    """

    def __init__(self, in_features: int, out_features: int, bias: bool = True):
        super().__init__()
        if in_features % 4 != 0 or out_features % 4 != 0:
            raise ValueError("in_features and out_features must be multiples of 4.")
        self.in_q = in_features // 4
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
    2D spectral convolution with quaternion Hamilton product in frequency domain.

    Kernel tensors are registered for each quaternion component (w, x, y, z),
    each with separate real and imaginary parts for the complex frequency domain.
    """

    def __init__(self, in_q: int, out_q: int, grid_h: int, grid_w: int,
                 init_scale: float = 0.02):
        super().__init__()
        self.in_q = in_q
        self.out_q = out_q
        self.grid_h = grid_h
        self.grid_w = grid_w
        freq_h = grid_h
        freq_w = grid_w // 2 + 1
        for c in ("w", "x", "y", "z"):
            self.register_parameter(
                f"kr_{c}", nn.Parameter(torch.randn(in_q, out_q, freq_h, freq_w) * init_scale))
            self.register_parameter(
                f"ki_{c}", nn.Parameter(torch.randn(in_q, out_q, freq_h, freq_w) * init_scale))

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
        Ww, Wx, Wy, Wz = self._kernel("w"), self._kernel("x"), self._kernel("y"), self._kernel("z")
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
    Spectral autoencoder operating in both 1D (feature axis) and 2D (torus grid).

    Encodes via FFT filtering and quaternion projection to a latent space;
    decodes back for reconstruction regularisation.  Also exposes a method
    for processing the torus grid through stacked QuaternionSpectralLayers.
    """

    def __init__(self, config: TopoGPT2Config):
        super().__init__()
        d = config.D_MODEL
        d_lat = config.SPECTRAL_LATENT_DIM
        d_q = config.D_QUAT
        r = config.TORUS_RADIAL_BINS
        a = config.TORUS_ANGULAR_BINS
        init_s = config.SPECTRAL_KERNEL_INIT_SCALE
        n_freq = d // 2 + 1
        self.enc_kr = nn.Parameter(torch.randn(n_freq) * init_s)
        self.enc_ki = nn.Parameter(torch.randn(n_freq) * init_s)
        self.dec_kr = nn.Parameter(torch.randn(n_freq) * init_s)
        self.dec_ki = nn.Parameter(torch.randn(n_freq) * init_s)
        self.enc_proj = QuaternionLinear(d, d_lat)
        self.dec_proj = QuaternionLinear(d_lat, d)
        self.torus_spectral = nn.ModuleList([
            QuaternionSpectralLayer(d_q, d_q, r, a, init_scale=init_s)
            for _ in range(config.NUM_SPECTRAL_LAYERS)
        ])
        self.act = nn.GELU()
        self.d_model = d

    def _filter1d(self, x: torch.Tensor, kr: torch.Tensor, ki: torch.Tensor) -> torch.Tensor:
        X = torch.fft.rfft(x, dim=-1)
        K = torch.complex(kr, ki)
        return torch.fft.irfft(X * K, n=self.d_model, dim=-1)

    def encode(self, x: torch.Tensor) -> torch.Tensor:
        return self.enc_proj(self.act(self._filter1d(x, self.enc_kr, self.enc_ki)))

    def decode(self, z: torch.Tensor) -> torch.Tensor:
        return self._filter1d(self.dec_proj(z), self.dec_kr, self.dec_ki)

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        z = self.encode(x)
        recon = self.decode(z)
        return z, F.mse_loss(recon, x.detach())

    def process_torus_grid(self, grid: torch.Tensor) -> torch.Tensor:
        h = grid
        for layer in self.torus_spectral:
            h = self.act(layer(h))
        return h


class QuaternionTorusBrain(nn.Module):
    """
    Replaces the MLP in each transformer layer.

    Vectorised pipeline:
        1. Flatten [B, S, D] -> [BS, D]
        2. SpectralAutoencoder (1D filter + quaternion projection)
        3. Project to torus angles (phi1, phi2)
        4. Soft-assign each token to N_NODES via circular distances
        5. Build node grid [BS, N_NODES, D]
        6. QuaternionSpectralLayer 2D on the torus grid
        7. Quaternion message-passing on the torus graph
        8. Readout: weighted sum over nodes -> [BS, D]
        9. Reshape to [B, S, D]
    """

    def __init__(self, d_model: int, config: TopoGPT2Config):
        super().__init__()
        self.d_model = d_model
        self.d_lat = config.SPECTRAL_LATENT_DIM
        self.d_q = d_model // 4
        self.n_radial = config.TORUS_RADIAL_BINS
        self.n_angular = config.TORUS_ANGULAR_BINS
        self.n_nodes = config.N_TORUS_NODES
        self.config = config
        self.spectral_ae = SpectralAutoencoder(config)
        self.torus_proj = nn.Sequential(
            QuaternionLinear(d_model, d_model),
            nn.GELU(),
            nn.Linear(d_model, 4),
        )
        self.node_embed = nn.Parameter(torch.randn(self.n_nodes, d_model) * 0.02)
        self.edge_quat = nn.Parameter(torch.randn(4, 4) * 0.1)
        self.node_net = QuaternionLinear(d_model, d_model)
        self.readout = nn.Sequential(
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
        self.register_buffer("edges_i", torch.tensor(edges_i, dtype=torch.long))
        self.register_buffer("edges_j", torch.tensor(edges_j, dtype=torch.long))
        self.register_buffer("edge_type", torch.tensor(edge_type, dtype=torch.long))

    def _torus_soft_assign(self, phi1: torch.Tensor, phi2: torch.Tensor) -> torch.Tensor:
        soft_temperature = 0.3
        BS = phi1.shape[0]
        device = phi1.device
        ang_pos = torch.linspace(-math.pi, math.pi, self.n_angular + 1, device=device)[:-1]
        rad_pos = torch.linspace(-math.pi, math.pi, self.n_radial + 1, device=device)[:-1]
        d_ang = torch.sin((phi1.unsqueeze(1) - ang_pos.unsqueeze(0)) / 2).pow(2)
        d_rad = torch.sin((phi2.unsqueeze(1) - rad_pos.unsqueeze(0)) / 2).pow(2)
        d_torus = d_rad.unsqueeze(2) + d_ang.unsqueeze(1)
        return torch.softmax(-d_torus.view(BS, -1) / soft_temperature, dim=-1)

    def _message_passing(self, node_feat: torch.Tensor) -> torch.Tensor:
        BS = node_feat.shape[0]
        n_edges = self.edges_i.shape[0]
        d_q = self.d_q
        eq = QuaternionOps.normalize(self.edge_quat)
        src_feat = node_feat[:, self.edges_j, :]
        edge_q = eq[self.edge_type].unsqueeze(0).unsqueeze(2).expand(BS, -1, d_q, -1)
        src_q = src_feat.view(BS, n_edges, d_q, 4)
        msg_rot = QuaternionOps.hamilton_product(edge_q, src_q).view(BS, n_edges, self.d_model)
        agg = torch.zeros_like(node_feat)
        dst_idx = self.edges_i.view(1, n_edges, 1).expand(BS, -1, self.d_model)
        agg.scatter_add_(1, dst_idx, msg_rot)
        return self.node_net(node_feat + agg)

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        B, S, D = x.shape
        x_flat = x.reshape(B * S, D)
        z, recon_loss = self.spectral_ae(x_flat)
        coords = self.torus_proj(x_flat)
        phi1 = math.pi * torch.tanh(coords[:, 0])
        phi2 = math.pi * torch.tanh(coords[:, 1])
        attn_w = self._torus_soft_assign(phi1, phi2)
        nodes = (
            attn_w.unsqueeze(-1) * self.node_embed.unsqueeze(0)
            + attn_w.unsqueeze(-1) * x_flat.unsqueeze(1)
        )
        d_q = self.d_q
        grid = nodes.view(B * S, self.n_radial, self.n_angular, D)
        grid = grid.permute(0, 3, 1, 2)
        grid_q = grid.view(B * S, 4, d_q, self.n_radial, self.n_angular)
        grid_q = grid_q.reshape(B * S, 4 * d_q, self.n_radial, self.n_angular)
        grid_spec = self.spectral_ae.process_torus_grid(grid_q)
        grid_back = grid_spec.view(B * S, 4, d_q, self.n_radial, self.n_angular)
        grid_back = grid_back.permute(0, 3, 4, 1, 2).reshape(B * S, self.n_nodes, D)
        nodes_mp = self._message_passing(grid_back)
        out_flat = self.readout((attn_w.unsqueeze(-1) * nodes_mp).sum(dim=1))
        return out_flat.reshape(B, S, D), recon_loss


class SwiGLU(nn.Module):
    """
    SwiGLU feed-forward block (LLaMA-style).
    inner dimension = round(d_model * expansion) up to multiple of 4.
    """

    def __init__(self, d_model: int, expansion: float = 8.0 / 3.0,
                 dropout: float = 0.0):
        super().__init__()
        inner = max(4, int(d_model * expansion))
        inner = (inner + 3) // 4 * 4
        self.gate_proj = nn.Linear(d_model, inner, bias=False)
        self.up_proj   = nn.Linear(d_model, inner, bias=False)
        self.down_proj = nn.Linear(inner, d_model, bias=False)
        self.drop = nn.Dropout(dropout) if dropout > 0.0 else nn.Identity()
        for w in (self.gate_proj, self.up_proj, self.down_proj):
            nn.init.normal_(w.weight, std=0.02)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.drop(self.down_proj(F.silu(self.gate_proj(x)) * self.up_proj(x)))


class TopoMoEBrain(nn.Module):
    """
    Mixture-of-Experts wrapper around QuaternionTorusBrain.

    One always-active shared expert (QuaternionTorusBrain) plus N_EXPERTS
    sparse SwiGLU experts selected by a linear router (top-K per token).
    When MOE_ENABLED is False this reduces to a plain QuaternionTorusBrain.
    """

    def __init__(self, d_model: int, config: TopoGPT2Config):
        super().__init__()
        self.d_model = d_model
        self.moe_enabled = config.MOE_ENABLED
        self.n_experts = config.N_EXPERTS
        self.top_k = config.MOE_TOP_K
        self.aux_weight = config.MOE_AUX_LOSS_WEIGHT
        self.shared_expert = QuaternionTorusBrain(d_model, config)
        if self.moe_enabled:
            self.experts = nn.ModuleList([
                SwiGLU(d_model, expansion=4.0 / 3.0, dropout=config.DROPOUT)
                for _ in range(self.n_experts)
            ])
            self.router = nn.Linear(d_model, self.n_experts, bias=False)
            nn.init.normal_(self.router.weight, std=0.02)

    def _route(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        N, D = x.shape
        router_probs = F.softmax(self.router(x), dim=-1)
        top_k_probs, top_k_idx = torch.topk(router_probs, self.top_k, dim=-1)
        top_k_probs = top_k_probs / top_k_probs.sum(dim=-1, keepdim=True).clamp(min=1e-9)
        flat_idx = top_k_idx.reshape(-1)
        flat_weights = top_k_probs.reshape(-1)
        token_indices = (
            torch.arange(N, device=x.device, dtype=torch.long)
            .unsqueeze(1).expand(-1, self.top_k).reshape(-1)
        )
        expert_out = torch.zeros_like(x)
        for e in range(self.n_experts):
            mask = flat_idx == e
            src = token_indices[mask]
            w = flat_weights[mask].unsqueeze(-1).to(x.dtype)
            contrib = w * self.experts[e](x[src])
            expert_out.scatter_add_(0, src.unsqueeze(1).expand_as(contrib), contrib)
        token_frac = router_probs.mean(dim=0)
        dispatch_frac = F.one_hot(top_k_idx, self.n_experts).float().mean(dim=(0, 1))
        aux_loss = self.n_experts * (token_frac * dispatch_frac).sum()
        return expert_out, aux_loss

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        B, S, D = x.shape
        shared_out, recon_loss = self.shared_expert(x)
        if not self.moe_enabled:
            return shared_out, recon_loss
        expert_out, aux_loss = self._route(x.reshape(B * S, D))
        return shared_out + expert_out.reshape(B, S, D), recon_loss + self.aux_weight * aux_loss


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
        t = torch.arange(seq_len, device=self.inv_freq.device).float()
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
        return q * cq + self._rotate_half(q) * sq_, k * ck + self._rotate_half(k) * sk_


class RMSNorm(nn.Module):
    """Root Mean Square Layer Normalization (no bias)."""

    def __init__(self, d_model: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(d_model))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        rms = x.pow(2).mean(-1, keepdim=True).add(self.eps).sqrt()
        return x / rms * self.weight


class MultiHeadAttention(nn.Module):
    """
    Multi-head attention with Flash Attention, RoPE, and Grouped Query Attention.
    Supports an optional KV cache for autoregressive generation.
    """

    def __init__(self, d_model: int, n_heads: int, config: TopoGPT2Config):
        super().__init__()
        self.d_model = d_model
        self.n_heads = n_heads
        self.n_kv = config.N_KV_HEADS
        self.n_groups = config.GQA_GROUPS
        self.d_head = d_model // n_heads
        self.q_proj = nn.Linear(d_model, n_heads * self.d_head, bias=False)
        self.k_proj = nn.Linear(d_model, self.n_kv * self.d_head, bias=False)
        self.v_proj = nn.Linear(d_model, self.n_kv * self.d_head, bias=False)
        self.o_proj = nn.Linear(d_model, d_model, bias=False)
        self.rope = RotaryEmbedding(self.d_head, max_seq_len=config.MAX_SEQ_LEN)
        self.temperature = nn.Parameter(torch.tensor(config.T_INIT))
        self.dropout_p = config.DROPOUT if config.DROPOUT > 0 else 0.0

    def forward(
        self, x: torch.Tensor, is_causal: bool = True,
        past_kv: Optional[Tuple[torch.Tensor, torch.Tensor]] = None
    ) -> Tuple[torch.Tensor, Tuple[torch.Tensor, torch.Tensor]]:
        B, S, D = x.shape
        Q = self.q_proj(x).view(B, S, self.n_heads, self.d_head).transpose(1, 2)
        K = self.k_proj(x).view(B, S, self.n_kv, self.d_head).transpose(1, 2)
        V = self.v_proj(x).view(B, S, self.n_kv, self.d_head).transpose(1, 2)
        offset = past_kv[0].shape[2] if past_kv is not None else 0
        Q, K = self.rope(Q, K, seq_len=S, offset=offset)
        if past_kv is not None:
            K = torch.cat([past_kv[0], K], dim=2)
            V = torch.cat([past_kv[1], V], dim=2)
        kv_cache = (K, V)
        if self.n_groups > 1:
            K_full = K.unsqueeze(2).expand(-1, -1, self.n_groups, -1, -1).reshape(
                B, self.n_heads, K.shape[2], self.d_head)
            V_exp = V.unsqueeze(2).expand(-1, -1, self.n_groups, -1, -1).reshape(
                B, self.n_heads, V.shape[2], self.d_head)
        else:
            K_full, V_exp = K, V
        scale = (self.d_head ** -0.5) / self.temperature.abs().clamp(min=1e-6)
        out = F.scaled_dot_product_attention(
            Q, K_full, V_exp,
            attn_mask=None,
            dropout_p=self.dropout_p if self.training else 0.0,
            is_causal=(is_causal and past_kv is None),
            scale=scale.item(),
        )
        out = out.transpose(1, 2).contiguous().view(B, S, D)
        return self.o_proj(out), kv_cache


class TopoGPT2Layer(nn.Module):
    """
    Single transformer layer: pre-norm attention + pre-norm TopoMoEBrain.
    Gradient checkpointing is disabled during inference/expansion.
    """

    def __init__(self, d_model: int, n_heads: int, config: TopoGPT2Config):
        super().__init__()
        self.norm1 = RMSNorm(d_model)
        self.norm2 = RMSNorm(d_model)
        self.attn = MultiHeadAttention(d_model, n_heads, config)
        self.topo_brain = TopoMoEBrain(d_model, config)
        self.dropout = nn.Dropout(config.DROPOUT)
        self.use_ckpt = config.GRADIENT_CHECKPOINTING

    def _forward_impl(
        self, x: torch.Tensor, past_kv: Optional[Tuple] = None
    ) -> Tuple[torch.Tensor, torch.Tensor, Optional[Tuple]]:
        attn_out, kv_cache = self.attn(self.norm1(x), past_kv=past_kv)
        x = x + self.dropout(attn_out)
        brain_out, aux_loss = self.topo_brain(self.norm2(x))
        x = x + self.dropout(brain_out)
        return x, aux_loss, kv_cache

    def forward(
        self, x: torch.Tensor, past_kv: Optional[Tuple] = None
    ) -> Tuple[torch.Tensor, torch.Tensor, Optional[Tuple]]:
        return self._forward_impl(x, past_kv=past_kv)


class TopoGPT2(nn.Module):
    """
    TopoGPT2: causal language model with quaternion torus topology.

    Embedding -> N_LAYERS x (Attention + QuaternionTorusBrain) -> RMSNorm -> LM head.
    The embedding and LM head share weights (weight tying).
    """

    def __init__(self, config: TopoGPT2Config):
        super().__init__()
        self.config = config
        self.token_embed = nn.Embedding(config.VOCAB_SIZE, config.D_MODEL)
        nn.init.normal_(self.token_embed.weight, std=0.02)
        self.layers = nn.ModuleList([
            TopoGPT2Layer(config.D_MODEL, config.N_HEADS, config)
            for _ in range(config.N_LAYERS)
        ])
        self.final_norm = RMSNorm(config.D_MODEL)
        self.lm_head = nn.Linear(config.D_MODEL, config.VOCAB_SIZE, bias=False)
        self.lm_head.weight = self.token_embed.weight
        self._init_weights()

    def _init_weights(self) -> None:
        for module in self.modules():
            if isinstance(module, nn.Linear) and module is not self.lm_head:
                nn.init.normal_(module.weight, std=0.02)
                if module.bias is not None:
                    nn.init.zeros_(module.bias)

    def forward(
        self, token_ids: torch.Tensor,
        past_kvs: Optional[List[Optional[Tuple]]] = None
    ) -> Tuple[torch.Tensor, torch.Tensor, List]:
        x = self.token_embed(token_ids)
        total_aux = torch.tensor(0.0, device=x.device)
        new_kvs: List = []
        for i, layer in enumerate(self.layers):
            pkv = past_kvs[i] if past_kvs is not None else None
            x, al, kvc = layer(x, past_kv=pkv)
            total_aux = total_aux + al
            new_kvs.append(kvc)
        x = self.final_norm(x)
        logits = self.lm_head(x)
        return logits, total_aux / len(self.layers), new_kvs

    @torch.no_grad()
    def generate(
        self, token_ids: torch.Tensor, max_new_tokens: int = 200,
        temperature: float = 0.8, top_k: int = 50
    ) -> torch.Tensor:
        """Top-k autoregressive generation with KV cache."""
        self.eval()
        eos_token_id = 50256
        cfg = self.config
        ctx = token_ids[:, -cfg.MAX_SEQ_LEN:]
        logits, _, past_kvs = self(ctx)
        logits = logits[:, -1, :] / max(temperature, 1e-8)
        if top_k > 0:
            v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
            logits[logits < v[:, -1:]] = float("-inf")
        next_tok = torch.multinomial(F.softmax(logits, dim=-1), 1)
        token_ids = torch.cat([token_ids, next_tok], dim=1)
        for _ in range(max_new_tokens - 1):
            logits, _, past_kvs = self(next_tok, past_kvs=past_kvs)
            logits = logits[:, -1, :] / max(temperature, 1e-8)
            if top_k > 0:
                v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                logits[logits < v[:, -1:]] = float("-inf")
            next_tok = torch.multinomial(F.softmax(logits, dim=-1), 1)
            token_ids = torch.cat([token_ids, next_tok], dim=1)
            if (next_tok == eos_token_id).all():
                break
        return token_ids


# ===========================================================================
# WEIGHT INTERPOLATION UTILITIES
# ===========================================================================

class SpectralKernelInterpolator:
    """
    Interpolates QuaternionSpectralLayer kernels to a new (grid_h, grid_w).

    The kernels live in frequency space with shape [in_q, out_q, freq_h, freq_w]
    where freq_w = grid_w // 2 + 1.  We treat (freq_h, freq_w) as a 2D spatial
    grid and apply torch.nn.functional.interpolate.
    """

    def __init__(self, mode: str = "bilinear"):
        self.mode = mode

    def _interp2d(
        self, tensor: torch.Tensor,
        tgt_h: int, tgt_w: int
    ) -> torch.Tensor:
        """
        Interpolate a 4D real tensor [in_q, out_q, h, w] to [in_q, out_q, tgt_h, tgt_w].
        """
        in_q, out_q, h, w = tensor.shape
        flat = tensor.reshape(1, in_q * out_q, h, w)
        interp = F.interpolate(
            flat, size=(tgt_h, tgt_w),
            mode=self.mode,
            align_corners=False if self.mode == "bilinear" else None,
        )
        return interp.reshape(in_q, out_q, tgt_h, tgt_w)

    def transfer(
        self,
        src_layer: QuaternionSpectralLayer,
        tgt_layer: QuaternionSpectralLayer,
    ) -> None:
        """
        Copy and interpolate all kernel parameters from src_layer to tgt_layer.
        """
        tgt_freq_h = tgt_layer.grid_h
        tgt_freq_w = tgt_layer.grid_w // 2 + 1

        with torch.no_grad():
            for c in ("w", "x", "y", "z"):
                for part in ("r", "i"):
                    attr = f"k{part}_{c}"
                    src_t = getattr(src_layer, attr).data
                    new_t = self._interp2d(src_t, tgt_freq_h, tgt_freq_w)
                    getattr(tgt_layer, attr).data.copy_(new_t)


class NodeEmbedInterpolator:
    """
    Interpolates the torus node embedding table to a new (n_radial, n_angular).

    node_embed has shape [n_nodes, d_model] = [n_radial * n_angular, d_model].
    We reshape to a 2D spatial grid [n_radial, n_angular, d_model], transpose
    to [d_model, n_radial, n_angular], interpolate per feature dimension, then
    reshape back.
    """

    def __init__(self, mode: str = "bilinear"):
        self.mode = mode

    def transfer(
        self,
        src_embed: nn.Parameter,
        src_radial: int, src_angular: int,
        tgt_embed: nn.Parameter,
        tgt_radial: int, tgt_angular: int,
    ) -> None:
        """
        Interpolate src_embed [src_R*src_A, D] into tgt_embed [tgt_R*tgt_A, D].
        """
        d_model = src_embed.shape[1]
        src_grid = src_embed.data.reshape(1, d_model, src_radial, src_angular)
        tgt_grid = F.interpolate(
            src_grid.float(),
            size=(tgt_radial, tgt_angular),
            mode=self.mode,
            align_corners=False if self.mode == "bilinear" else None,
        )
        with torch.no_grad():
            tgt_embed.data.copy_(
                tgt_grid.reshape(d_model, tgt_radial * tgt_angular).T
            )


# ===========================================================================
# TORUS BRAIN EXPANDER (single QuaternionTorusBrain layer)
# ===========================================================================

class TorusBrainExpander:
    """
    Transfers weights from a source QuaternionTorusBrain to a target one with
    a different torus resolution.

    Transfer strategy per sub-module
    ---------------------------------
    spectral_ae.enc_kr/ki, dec_kr/ki  : copy verbatim (1D feature-axis filters,
                                         independent of torus resolution)
    spectral_ae.enc_proj, dec_proj     : copy verbatim (QuaternionLinear, no torus)
    spectral_ae.torus_spectral[i]      : interpolate each QuaternionSpectralLayer
                                         kernel to new (tgt_radial, tgt_angular)
    torus_proj                         : copy verbatim (projects to angles, not nodes)
    node_embed                         : bilinear interpolation over the torus grid
    edge_quat                          : copy verbatim (4 edge types, always 4)
    node_net                           : copy verbatim (QuaternionLinear, pointwise)
    readout                            : copy verbatim (pointwise MLP)
    """

    def __init__(
        self,
        spec_interp_mode: str = "bilinear",
        node_interp_mode: str = "bilinear",
        logger: Optional[logging.Logger] = None,
    ):
        self._spec_interp = SpectralKernelInterpolator(mode=spec_interp_mode)
        self._node_interp = NodeEmbedInterpolator(mode=node_interp_mode)
        self._log = logger or build_logger("TorusBrainExpander")

    def expand(
        self,
        src: QuaternionTorusBrain,
        tgt: QuaternionTorusBrain,
    ) -> None:
        """Mutates tgt in-place to carry the expanded weights of src."""
        self._log.info(
            "Expanding QuaternionTorusBrain: "
            f"({src.n_radial}R x {src.n_angular}A) -> "
            f"({tgt.n_radial}R x {tgt.n_angular}A)"
        )

        with torch.no_grad():
            # 1D spectral filters (feature axis – resolution-independent)
            tgt.spectral_ae.enc_kr.data.copy_(src.spectral_ae.enc_kr.data)
            tgt.spectral_ae.enc_ki.data.copy_(src.spectral_ae.enc_ki.data)
            tgt.spectral_ae.dec_kr.data.copy_(src.spectral_ae.dec_kr.data)
            tgt.spectral_ae.dec_ki.data.copy_(src.spectral_ae.dec_ki.data)

            # QuaternionLinear projections (resolution-independent)
            tgt.spectral_ae.enc_proj.load_state_dict(
                src.spectral_ae.enc_proj.state_dict())
            tgt.spectral_ae.dec_proj.load_state_dict(
                src.spectral_ae.dec_proj.state_dict())

        # 2D torus spectral kernels – interpolate to new torus grid
        n_spec = len(src.spectral_ae.torus_spectral)
        for i in range(n_spec):
            self._spec_interp.transfer(
                src.spectral_ae.torus_spectral[i],
                tgt.spectral_ae.torus_spectral[i],
            )
            self._log.debug(f"Spectral layer {i} kernels interpolated.")

        # Torus projection (maps features -> angles, resolution-independent)
        with torch.no_grad():
            tgt.torus_proj.load_state_dict(src.torus_proj.state_dict())

        # Node embeddings – interpolate over the torus manifold
        self._node_interp.transfer(
            src.node_embed,
            src.n_radial, src.n_angular,
            tgt.node_embed,
            tgt.n_radial, tgt.n_angular,
        )
        self._log.debug("Node embeddings interpolated.")

        # Edge quaternions (4 fixed edge types, no dependency on resolution)
        with torch.no_grad():
            tgt.edge_quat.data.copy_(src.edge_quat.data)

        # Node net and readout (pointwise, resolution-independent)
        with torch.no_grad():
            tgt.node_net.load_state_dict(src.node_net.state_dict())
            tgt.readout.load_state_dict(src.readout.state_dict())

        self._log.info("QuaternionTorusBrain expansion complete.")


# ===========================================================================
# MoE BRAIN EXPANDER
# ===========================================================================

class TopoMoEBrainExpander:
    """
    Transfers weights from a source TopoMoEBrain to a target one.

    The shared QuaternionTorusBrain is expanded via TorusBrainExpander.
    All SwiGLU expert weights and the router are copied verbatim (they do not
    depend on torus resolution – they process flat token embeddings).
    """

    def __init__(
        self,
        spec_interp_mode: str = "bilinear",
        node_interp_mode: str = "bilinear",
        logger: Optional[logging.Logger] = None,
    ):
        self._brain_expander = TorusBrainExpander(
            spec_interp_mode=spec_interp_mode,
            node_interp_mode=node_interp_mode,
            logger=logger,
        )
        self._log = logger or build_logger("TopoMoEBrainExpander")

    def expand(self, src: TopoMoEBrain, tgt: TopoMoEBrain) -> None:
        """Mutates tgt in-place."""
        self._brain_expander.expand(src.shared_expert, tgt.shared_expert)
        if src.moe_enabled and tgt.moe_enabled:
            if len(src.experts) != len(tgt.experts):
                raise ValueError(
                    f"Expert count mismatch: src has {len(src.experts)}, "
                    f"tgt has {len(tgt.experts)}.  Change N_EXPERTS in the config."
                )
            with torch.no_grad():
                for i, (se, te) in enumerate(zip(src.experts, tgt.experts)):
                    te.load_state_dict(se.state_dict())
                    self._log.debug(f"SwiGLU expert {i} copied.")
                tgt.router.load_state_dict(src.router.state_dict())
                self._log.debug("Router copied.")


# ===========================================================================
# FULL MODEL EXPANDER
# ===========================================================================

class TopoGPT2Expander:
    """
    Zero-shot torus expansion of a complete TopoGPT2 model.

    All weights that are resolution-independent are copied verbatim.
    The torus-dependent weights inside each TopoMoEBrain are interpolated
    by TopoMoEBrainExpander.

    Resolution-independent weights (copied verbatim)
    -------------------------------------------------
    token_embed, lm_head (weight-tied)
    final_norm
    per-layer: norm1, norm2, attn (all projections + temperature + rope)
    per-layer: topo_brain -> experts, router

    Resolution-dependent weights (interpolated)
    -------------------------------------------
    per-layer: topo_brain -> shared_expert (QuaternionTorusBrain)
    """

    def __init__(
        self,
        spec_interp_mode: str = "bilinear",
        node_interp_mode: str = "bilinear",
        logger: Optional[logging.Logger] = None,
    ):
        self._moe_expander = TopoMoEBrainExpander(
            spec_interp_mode=spec_interp_mode,
            node_interp_mode=node_interp_mode,
            logger=logger,
        )
        self._log = logger or build_logger("TopoGPT2Expander")

    def expand(self, src: TopoGPT2, tgt: TopoGPT2) -> TopoGPT2:
        """
        Expand src into tgt.  Returns tgt with all weights transferred.
        tgt must have already been instantiated with the target config.
        """
        if len(src.layers) != len(tgt.layers):
            raise ValueError(
                f"Layer count mismatch: src={len(src.layers)}, tgt={len(tgt.layers)}."
            )

        self._log.info("Transferring resolution-independent weights ...")
        with torch.no_grad():
            # Embeddings (lm_head is weight-tied, so only embed needs copy)
            tgt.token_embed.weight.data.copy_(src.token_embed.weight.data)
            tgt.final_norm.weight.data.copy_(src.final_norm.weight.data)

        for layer_idx, (src_layer, tgt_layer) in enumerate(
            zip(src.layers, tgt.layers)
        ):
            self._log.info(f"Processing layer {layer_idx} ...")
            with torch.no_grad():
                tgt_layer.norm1.load_state_dict(src_layer.norm1.state_dict())
                tgt_layer.norm2.load_state_dict(src_layer.norm2.state_dict())
                tgt_layer.attn.load_state_dict(src_layer.attn.state_dict())

            self._moe_expander.expand(src_layer.topo_brain, tgt_layer.topo_brain)

        self._log.info("Full model expansion complete.")
        return tgt


# ===========================================================================
# CHECKPOINT I/O
# ===========================================================================

class CheckpointIO:
    """
    Loads and saves TopoGPT2 weights using safetensors.
    Falls back to torch.save / torch.load when safetensors is unavailable.
    """

    def __init__(self, logger: Optional[logging.Logger] = None):
        self._log = logger or build_logger("CheckpointIO")
        if not _SAFETENSORS_AVAILABLE:
            self._log.warning(
                "safetensors not installed.  Falling back to torch pickle format."
            )

    def load(self, path: str, model: TopoGPT2, device: str) -> Dict:
        """
        Load weights into model from path.  Returns the metadata dict.
        Supports: .safetensors, .pt, .pth (state_dict or wrapped dict).

        Weight tying: checkpoints saved by this script omit lm_head.weight
        (it is redundant with token_embed.weight).  After loading, the tie is
        restored by pointing lm_head.weight at token_embed.weight.
        """
        path_obj = Path(path)
        if not path_obj.exists():
            raise FileNotFoundError(f"Checkpoint not found: {path}")

        self._log.info(f"Loading checkpoint from {path}")

        if path_obj.suffix == ".safetensors" and _SAFETENSORS_AVAILABLE:
            state = st_load(path, device=device)
            # lm_head.weight may be absent (weight-tied and omitted on save)
            missing, unexpected = model.load_state_dict(state, strict=False)
            metadata: Dict = {}
        else:
            raw = torch.load(path, map_location=device, weights_only=False)
            if isinstance(raw, dict) and "model_state_dict" in raw:
                state = raw["model_state_dict"]
                metadata = {k: v for k, v in raw.items() if k != "model_state_dict"}
            else:
                state = raw
                metadata = {}
            missing, unexpected = model.load_state_dict(state, strict=False)

        # Re-apply weight tying regardless of save format
        model.lm_head.weight = model.token_embed.weight

        # lm_head.weight missing is expected and not an error
        missing = [k for k in missing if k != "lm_head.weight"]

        if missing:
            self._log.warning(f"Missing keys ({len(missing)}): {missing[:5]} ...")
        if unexpected:
            self._log.warning(f"Unexpected keys ({len(unexpected)}): {unexpected[:5]} ...")

        self._log.info("Checkpoint loaded successfully.")
        return metadata

    def save(self, path: str, model: TopoGPT2, metadata: Optional[Dict] = None) -> None:
        """
        Save model weights to path.

        Weight tying: token_embed.weight and lm_head.weight share the same
        storage tensor.  safetensors rejects aliased tensors with a RuntimeError.
        We exclude lm_head.weight from the state dict before saving (it is
        redundant) and record the tie in metadata so load() can restore it.
        """
        path_obj = Path(path)
        path_obj.parent.mkdir(parents=True, exist_ok=True)

        self._log.info(f"Saving expanded checkpoint to {path}")

        if path_obj.suffix == ".safetensors" and _SAFETENSORS_AVAILABLE:
            state = model.state_dict()
            # Drop the tied alias; load() will re-tie from token_embed.weight
            state = {k: v for k, v in state.items() if k != "lm_head.weight"}
            str_metadata = {k: str(v) for k, v in (metadata or {}).items()}
            str_metadata["weight_tied_lm_head"] = "1"
            st_save(state, str(path), metadata=str_metadata)
        else:
            state = model.state_dict()
            # For pickle format, clone the lm_head tensor to break the alias
            # so torch.save does not store two references to the same data.
            state["lm_head.weight"] = state["lm_head.weight"].clone()
            payload = {"model_state_dict": state}
            if metadata:
                payload.update(metadata)
            torch.save(payload, path)

        self._log.info("Checkpoint saved.")


# ===========================================================================
# CHECKPOINT ARCHITECTURE PROBER
# ===========================================================================

@dataclass
class CheckpointArch:
    """
    Architecture hyperparameters inferred directly from checkpoint tensor shapes.

    All fields that affect tensor dimensions are recovered so that the source
    model can be instantiated to exactly match the saved weights, regardless of
    what the CLI scale preset would compute.
    """

    d_model: int
    n_heads: int
    n_kv_heads: int
    n_layers: int
    vocab_size: int
    torus_radial: int
    torus_angular: int
    spectral_latent_dim: int
    n_experts: int
    moe_enabled: bool
    num_spectral_layers: int
    n_freq_1d: int


class CheckpointArchProber:
    """
    Infers all architecture hyperparameters from the raw tensor shapes stored
    in a checkpoint, without relying on any saved metadata or scale presets.

    Probing strategy (all derivable from tensor names and shapes)
    -------------------------------------------------------------
    d_model         : token_embed.weight  shape [vocab, D] -> D
    vocab_size      : token_embed.weight  shape [V, D]     -> V
    n_heads         : layers.0.attn.q_proj.weight [n_heads*d_head, D]
                      with d_head = D // n_heads; since q always uses n_heads,
                      shape is [D, D] when n_heads = n_kv_heads.
                      We read n_heads from q_proj: out = n_heads * d_head = D
                      (always), so d_head = D // n_heads.  We look at the
                      actual out dim of q_proj.
    n_kv_heads      : layers.0.attn.k_proj.weight [n_kv*d_head, D]
                      -> n_kv = out_dim // d_head
    n_layers        : count of "layers.N.attn.q_proj.weight" keys
    torus_radial    : layers.0.topo_brain.shared_expert.spectral_ae
                      .torus_spectral.0.kr_w  shape [in_q, out_q, freq_h, freq_w]
                      grid_h = freq_h  (no //2+1 on h),  we store it directly
    torus_angular   : freq_w = grid_w // 2 + 1  -> grid_w = (freq_w - 1) * 2
    spectral_latent : layers.0.topo_brain.shared_expert.spectral_ae
                      .enc_proj.Ww.weight  shape [out_q, in_q]
                      latent_dim = out_q * 4
    n_experts       : count of "layers.0.topo_brain.experts.N.gate_proj.weight"
                      keys; 0 means moe_enabled=False
    num_spec_layers : count of torus_spectral keys for layer 0
    n_freq_1d       : layers.0.topo_brain.shared_expert.spectral_ae.enc_kr
                      shape [n_freq]  where n_freq = d_model // 2 + 1
    """

    _Q_PROJ_KEY = "layers.0.attn.q_proj.weight"
    _K_PROJ_KEY = "layers.0.attn.k_proj.weight"
    _EMBED_KEY  = "token_embed.weight"
    _ROPE_KEY   = "layers.0.attn.rope.inv_freq"
    _TORUS_SPEC_KEY = (
        "layers.0.topo_brain.shared_expert.spectral_ae.torus_spectral.0.kr_w"
    )
    _ENC_PROJ_KEY = (
        "layers.0.topo_brain.shared_expert.spectral_ae.enc_proj.Ww.weight"
    )
    _ENC_KR_KEY = (
        "layers.0.topo_brain.shared_expert.spectral_ae.enc_kr"
    )
    _EXPERT_GATE_PATTERN = "layers.0.topo_brain.experts."

    def __init__(self, logger: Optional[logging.Logger] = None):
        self._log = logger or build_logger("CheckpointArchProber")

    def _load_shapes(self, path: str) -> Dict[str, Tuple[int, ...]]:
        """Return {key: shape} for every tensor in the checkpoint."""
        path_obj = Path(path)
        if path_obj.suffix == ".safetensors" and _SAFETENSORS_AVAILABLE:
            from safetensors import safe_open
            shapes: Dict[str, Tuple[int, ...]] = {}
            with safe_open(path, framework="pt", device="cpu") as f:
                for key in f.keys():
                    shapes[key] = tuple(f.get_tensor(key).shape)
            return shapes
        else:
            raw = torch.load(path, map_location="cpu", weights_only=False)
            state = raw["model_state_dict"] if "model_state_dict" in raw else raw
            return {k: tuple(v.shape) for k, v in state.items()}

    def _load_metadata(self, path: str) -> Dict[str, str]:
        """Return safetensors string metadata dict (empty when unavailable)."""
        if not _SAFETENSORS_AVAILABLE or not path.endswith(".safetensors"):
            return {}
        try:
            from safetensors import safe_open
            with safe_open(path, framework="pt", device="cpu") as f:
                return f.metadata() or {}
        except Exception:
            return {}

    def probe(
        self,
        path: str,
        fallback_radial: int,
        fallback_angular: int,
    ) -> CheckpointArch:
        """
        Infer CheckpointArch from the checkpoint at path.

        Parameters
        ----------
        path            : checkpoint file path
        fallback_radial : used only when torus_spectral key is absent
        fallback_angular: used only when torus_spectral key is absent
        """
        shapes = self._load_shapes(path)
        meta   = self._load_metadata(path)

        # d_model, vocab_size
        embed_shape = shapes[self._EMBED_KEY]
        vocab_size  = embed_shape[0]
        d_model     = embed_shape[1]

        # d_head from RoPE inv_freq: inv_freq shape is [d_head // 2]
        if self._ROPE_KEY in shapes:
            d_head = shapes[self._ROPE_KEY][0] * 2
        else:
            # Fallback: try to infer from k_proj and q_proj
            q_out = shapes[self._Q_PROJ_KEY][0]
            k_out = shapes[self._K_PROJ_KEY][0]
            d_head = self._infer_d_head_fallback(d_model, q_out, k_out)
            self._log.warning(
                f"rope.inv_freq key absent; d_head inferred as {d_head} via fallback."
            )

        q_out = shapes[self._Q_PROJ_KEY][0]
        k_out = shapes[self._K_PROJ_KEY][0]
        n_heads    = q_out // d_head
        n_kv_heads = k_out // d_head

        self._log.info(
            f"Probed attention: d_model={d_model}, n_heads={n_heads}, "
            f"n_kv_heads={n_kv_heads}, d_head={d_head}"
        )

        # n_layers
        n_layers = sum(
            1 for k in shapes if k.startswith("layers.") and k.endswith(".attn.q_proj.weight")
        )

        # torus geometry from torus_spectral kernel
        if self._TORUS_SPEC_KEY in shapes:
            ks = shapes[self._TORUS_SPEC_KEY]  # [in_q, out_q, freq_h, freq_w]
            freq_h = ks[2]
            freq_w = ks[3]
            torus_radial  = freq_h
            torus_angular = (freq_w - 1) * 2
            self._log.info(
                f"Probed torus geometry from spectral kernel: "
                f"R={torus_radial}, A={torus_angular}"
            )
        else:
            torus_radial  = int(meta.get("TORUS_RADIAL_BINS",  fallback_radial))
            torus_angular = int(meta.get("TORUS_ANGULAR_BINS", fallback_angular))
            self._log.warning(
                f"torus_spectral key absent; using fallback/metadata: "
                f"R={torus_radial}, A={torus_angular}"
            )

        # spectral_latent_dim from enc_proj
        enc_proj_shape = shapes.get(self._ENC_PROJ_KEY)
        if enc_proj_shape is not None:
            spectral_latent_dim = enc_proj_shape[0] * 4
        else:
            spectral_latent_dim = max(16, d_model // 2)
            self._log.warning(
                f"enc_proj key absent; spectral_latent_dim defaulted to {spectral_latent_dim}"
            )

        # n_experts and moe_enabled
        expert_keys = [
            k for k in shapes
            if k.startswith(self._EXPERT_GATE_PATTERN) and k.endswith("gate_proj.weight")
        ]
        n_experts   = len(expert_keys)
        moe_enabled = n_experts > 0

        # num_spectral_layers
        spec_layer_keys = [
            k for k in shapes
            if "topo_brain.shared_expert.spectral_ae.torus_spectral." in k
            and k.startswith("layers.0.")
            and k.endswith(".kr_w")
        ]
        num_spectral_layers = len(spec_layer_keys)

        # n_freq_1d
        enc_kr_shape = shapes.get(self._ENC_KR_KEY)
        n_freq_1d = enc_kr_shape[0] if enc_kr_shape is not None else d_model // 2 + 1

        arch = CheckpointArch(
            d_model=d_model,
            n_heads=n_heads,
            n_kv_heads=n_kv_heads,
            n_layers=n_layers,
            vocab_size=vocab_size,
            torus_radial=torus_radial,
            torus_angular=torus_angular,
            spectral_latent_dim=spectral_latent_dim,
            n_experts=n_experts,
            moe_enabled=moe_enabled,
            num_spectral_layers=num_spectral_layers,
            n_freq_1d=n_freq_1d,
        )
        self._log.info(f"Probed architecture: {arch}")
        return arch

    @staticmethod
    def _infer_d_head_fallback(d_model: int, q_out: int, k_out: int) -> int:
        """
        Fallback d_head inference when rope.inv_freq is absent.

        d_head must divide both q_out and d_model, and n_heads % n_kv_heads == 0.
        Returns the largest valid candidate (most heads, smallest d_head is wrong
        intuition; we pick the value that makes n_kv_heads a proper divisor of n_heads
        and n_heads a standard power-of-2 count).
        """
        candidates = []
        for d in range(1, d_model + 1):
            if d_model % d == 0 and q_out % d == 0 and k_out % d == 0:
                n_h  = q_out // d
                n_kv = k_out // d
                if n_h > 0 and n_kv > 0 and n_h % n_kv == 0:
                    candidates.append(d)
        if not candidates:
            raise RuntimeError(
                f"Cannot infer d_head from d_model={d_model}, "
                f"q_out={q_out}, k_out={k_out}."
            )
        # Prefer standard head dims (power of 2, >= 16)
        standard = [d for d in candidates if d >= 16 and (d & (d - 1)) == 0]
        return max(standard) if standard else max(candidates)


# ===========================================================================
# VALIDATOR
# ===========================================================================

class ExpansionValidator:
    """
    Runs a forward-pass sanity check on the expanded model.

    Checks:
    - The model produces finite logits for a random token sequence.
    - The model produces finite logits for the given text prompt (if tiktoken
      is available).
    - The model can generate a short sequence without crashing.
    """

    def __init__(self, logger: Optional[logging.Logger] = None):
        self._log = logger or build_logger("ExpansionValidator")

    def validate(self, model: TopoGPT2, prompt: str = "Once upon a time") -> bool:
        """
        Return True if all checks pass, False otherwise.
        Does not raise; errors are logged as warnings.
        """
        cfg = model.config
        device = cfg.DEVICE
        model.eval()
        ok = True

        # Check 1: random token sequence
        self._log.info("Validation: random token forward pass ...")
        try:
            with torch.no_grad():
                dummy = torch.randint(0, cfg.VOCAB_SIZE, (1, min(8, cfg.MAX_SEQ_LEN)),
                                      device=device)
                logits, aux, _ = model(dummy)
                if not torch.isfinite(logits).all():
                    self._log.warning("Validation FAILED: non-finite logits on random input.")
                    ok = False
                else:
                    self._log.info(
                        f"Validation OK: logits shape={tuple(logits.shape)}, "
                        f"aux_loss={aux.item():.6f}"
                    )
        except Exception as exc:
            self._log.warning(f"Validation FAILED (random pass): {exc}")
            ok = False

        # Check 2: prompt-based forward pass
        if _TIKTOKEN_AVAILABLE:
            self._log.info("Validation: prompt-based forward pass ...")
            try:
                import tiktoken
                enc = tiktoken.get_encoding("gpt2")
                tokens = enc.encode(prompt, allowed_special={"<|endoftext|>"})
                tokens = tokens[:cfg.MAX_SEQ_LEN]
                ids = torch.tensor([tokens], dtype=torch.long, device=device)
                with torch.no_grad():
                    logits, _, _ = model(ids)
                if not torch.isfinite(logits).all():
                    self._log.warning("Validation FAILED: non-finite logits on prompt.")
                    ok = False
                else:
                    self._log.info("Validation OK: prompt forward pass.")
            except Exception as exc:
                self._log.warning(f"Validation FAILED (prompt pass): {exc}")
                ok = False
        else:
            self._log.info("tiktoken not available; skipping prompt validation.")

        # Check 3: short generation
        self._log.info("Validation: short autoregressive generation ...")
        try:
            with torch.no_grad():
                seed_ids = torch.randint(0, cfg.VOCAB_SIZE, (1, 4), device=device)
                gen = model.generate(seed_ids, max_new_tokens=8, temperature=1.0, top_k=50)
                if gen.shape[1] < seed_ids.shape[1]:
                    self._log.warning("Validation FAILED: generate returned fewer tokens.")
                    ok = False
                else:
                    self._log.info(f"Validation OK: generated {gen.shape[1]} tokens.")
        except Exception as exc:
            self._log.warning(f"Validation FAILED (generation): {exc}")
            ok = False

        return ok


# ===========================================================================
# ORCHESTRATOR
# ===========================================================================

class ZeroShotExpansionPipeline:
    """
    Orchestrates the full zero-shot expansion workflow:

    1. Read source torus geometry from checkpoint metadata (or config defaults).
    2. Build source and target TopoGPT2 configs.
    3. Instantiate source and target models.
    4. Load source weights into the source model.
    5. Expand weights via TopoGPT2Expander.
    6. Optionally validate the expanded model.
    7. Save the expanded model.

    No training is performed at any stage.
    """

    def __init__(self, exp_cfg: ExpansionConfig, logger: Optional[logging.Logger] = None):
        self._exp_cfg = exp_cfg
        self._log = logger or build_logger("ZeroShotExpansionPipeline")
        exp_cfg.validate_geometry()

    def _config_from_arch(
        self,
        arch: CheckpointArch,
        torus_radial: int,
        torus_angular: int,
    ) -> TopoGPT2Config:
        """
        Build a TopoGPT2Config whose tensor dimensions exactly match arch.

        The scale preset is applied first (to get sane defaults for fields not
        covered by arch), then every field that affects tensor shapes is
        overwritten with the probed value.  This guarantees that the
        instantiated model accepts the checkpoint weights without size mismatches.
        """
        cfg = TopoGPT2Config(
            SCALE=self._exp_cfg.scale,
            DEVICE=self._exp_cfg.device,
            GRADIENT_CHECKPOINTING=False,
            DROPOUT=0.0,
            TORUS_RADIAL_BINS=torus_radial,
            TORUS_ANGULAR_BINS=torus_angular,
        )
        # Overwrite every arch-derived field unconditionally
        cfg.D_MODEL            = arch.d_model
        cfg.N_HEADS            = arch.n_heads
        cfg.N_KV_HEADS         = arch.n_kv_heads
        cfg.N_LAYERS           = arch.n_layers
        cfg.VOCAB_SIZE         = arch.vocab_size
        cfg.N_EXPERTS          = arch.n_experts
        cfg.MOE_ENABLED        = arch.moe_enabled
        cfg.NUM_SPECTRAL_LAYERS = arch.num_spectral_layers
        # Derived fields that __post_init__ computes must be recomputed after override
        cfg.D_QUAT             = arch.d_model // 4
        cfg.D_HEAD             = arch.d_model // arch.n_heads
        cfg.SPECTRAL_LATENT_DIM = arch.spectral_latent_dim
        cfg.N_TORUS_NODES      = torus_radial * torus_angular
        cfg.GQA_GROUPS         = arch.n_heads // arch.n_kv_heads
        return cfg

    def _build_metadata_for_save(
        self, src_meta: Dict, arch: CheckpointArch,
        tgt_radial: int, tgt_angular: int
    ) -> Dict:
        meta = dict(src_meta)
        meta["TORUS_RADIAL_BINS"]    = tgt_radial
        meta["TORUS_ANGULAR_BINS"]   = tgt_angular
        meta["expanded_from_radial"] = arch.torus_radial
        meta["expanded_from_angular"]= arch.torus_angular
        meta["D_MODEL"]              = arch.d_model
        meta["N_HEADS"]              = arch.n_heads
        meta["N_KV_HEADS"]           = arch.n_kv_heads
        meta["N_LAYERS"]             = arch.n_layers
        meta["VOCAB_SIZE"]           = arch.vocab_size
        meta["N_EXPERTS"]            = arch.n_experts
        meta["MOE_ENABLED"]          = int(arch.moe_enabled)
        meta["NUM_SPECTRAL_LAYERS"]  = arch.num_spectral_layers
        meta["expansion_timestamp"]  = str(
            __import__("datetime").datetime.utcnow().isoformat()
        )
        return meta

    def run(self) -> TopoGPT2:
        """Execute the full expansion pipeline.  Returns the expanded model."""
        exp_cfg = self._exp_cfg
        io      = CheckpointIO(logger=self._log)
        prober  = CheckpointArchProber(logger=self._log)

        # Step 1: probe source checkpoint architecture from tensor shapes
        arch = prober.probe(
            exp_cfg.src_path,
            fallback_radial=exp_cfg.src_radial,
            fallback_angular=exp_cfg.src_angular,
        )
        self._log.info(
            f"Source geometry: R={arch.torus_radial}, A={arch.torus_angular} "
            f"({arch.torus_radial * arch.torus_angular} nodes)"
        )
        self._log.info(
            f"Target geometry: R={exp_cfg.tgt_radial}, A={exp_cfg.tgt_angular} "
            f"({exp_cfg.tgt_nodes} nodes)"
        )

        # Step 2: build configs that exactly reproduce the checkpoint shapes
        src_model_cfg = self._config_from_arch(
            arch, arch.torus_radial, arch.torus_angular
        )
        tgt_model_cfg = self._config_from_arch(
            arch, exp_cfg.tgt_radial, exp_cfg.tgt_angular
        )

        # Step 3: instantiate models
        self._log.info("Instantiating source model ...")
        src_model = TopoGPT2(src_model_cfg).to(exp_cfg.device)

        self._log.info("Instantiating target model ...")
        tgt_model = TopoGPT2(tgt_model_cfg).to(exp_cfg.device)

        src_params = sum(p.numel() for p in src_model.parameters())
        tgt_params = sum(p.numel() for p in tgt_model.parameters())
        self._log.info(
            f"Parameter counts: src={src_params:,}  tgt={tgt_params:,}"
        )

        # Step 4: load source weights (exact match now guaranteed)
        src_meta = io.load(exp_cfg.src_path, src_model, exp_cfg.device)

        # Step 5: expand weights
        expander = TopoGPT2Expander(
            spec_interp_mode=exp_cfg.spectral_interp_mode,
            node_interp_mode=exp_cfg.node_embed_interp_mode,
            logger=self._log,
        )
        tgt_model = expander.expand(src_model, tgt_model)

        # Step 6: validate
        if exp_cfg.validate:
            validator = ExpansionValidator(logger=self._log)
            passed = validator.validate(tgt_model, prompt=exp_cfg.validate_prompt)
            if not passed:
                self._log.warning(
                    "One or more validation checks failed.  "
                    "The checkpoint will still be saved."
                )
            else:
                self._log.info("All validation checks passed.")

        # Step 7: save
        save_meta = self._build_metadata_for_save(
            src_meta, arch, exp_cfg.tgt_radial, exp_cfg.tgt_angular
        )
        io.save(exp_cfg.dst_path, tgt_model, metadata=save_meta)

        return tgt_model


# ===========================================================================
# CLI ENTRY POINT
# ===========================================================================

def build_arg_parser() -> argparse.ArgumentParser:
    """Construct and return the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Zero-shot torus expansion for TopoGPT2.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--src", required=True,
        help="Path to the source safetensors (or .pt/.pth) checkpoint.",
    )
    parser.add_argument(
        "--dst", required=True,
        help="Destination path for the expanded checkpoint.",
    )
    parser.add_argument(
        "--radial", type=int, required=True,
        help="Target TORUS_RADIAL_BINS.",
    )
    parser.add_argument(
        "--angular", type=int, required=True,
        help="Target TORUS_ANGULAR_BINS.",
    )
    parser.add_argument(
        "--src-radial", type=int, default=2,
        help="Source TORUS_RADIAL_BINS (overridden by checkpoint metadata if present).",
    )
    parser.add_argument(
        "--src-angular", type=int, default=4,
        help="Source TORUS_ANGULAR_BINS (overridden by checkpoint metadata if present).",
    )
    parser.add_argument(
        "--scale", default="small",
        choices=["micro", "small", "medium", "gpt2"],
        help="Model scale preset.",
    )
    parser.add_argument(
        "--device", default="cpu",
        help="Torch device for weight manipulation.",
    )
    parser.add_argument(
        "--validate", action="store_true",
        help="Run forward-pass sanity checks on the expanded model.",
    )
    parser.add_argument(
        "--prompt", default="Once upon a time",
        help="Prompt text for the validation forward pass.",
    )
    parser.add_argument(
        "--spectral-interp", default="bilinear",
        choices=["bilinear", "nearest"],
        help="Interpolation mode for spectral kernels.",
    )
    parser.add_argument(
        "--node-interp", default="bilinear",
        choices=["bilinear", "nearest"],
        help="Interpolation mode for node embeddings.",
    )
    parser.add_argument(
        "--log-level", default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging verbosity.",
    )
    return parser


def main() -> None:
    """CLI entry point."""
    parser = build_arg_parser()
    args = parser.parse_args()

    logger = build_logger("topogpt2_expand", level=args.log_level)

    exp_cfg = ExpansionConfig(
        src_path=args.src,
        dst_path=args.dst,
        src_radial=args.src_radial,
        src_angular=args.src_angular,
        tgt_radial=args.radial,
        tgt_angular=args.angular,
        scale=args.scale,
        device=args.device,
        validate=args.validate,
        validate_prompt=args.prompt,
        log_level=args.log_level,
        spectral_interp_mode=args.spectral_interp,
        node_embed_interp_mode=args.node_interp,
    )

    pipeline = ZeroShotExpansionPipeline(exp_cfg, logger=logger)
    pipeline.run()

    logger.info("Done.")


if __name__ == "__main__":
    main()