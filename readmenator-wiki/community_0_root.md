# root

*Community 0 | 12 files | cohesion 1.00*

## Definition

This community groups 12 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `ActivationCapture`, `AttentionVisualizer`, `BFloat16Quantizer`, `BPETokenizer`, `BaseEmbeddingView`, `BaseVisualizer`, `BerryPhaseView`, `BitNetQuantizer`. Core file: `topogpt2_explorer.py` (155 symbols). Documented purpose: TopoGPT2: Quaternion-Enhanced Topological Transformer Language Model  Author: Gris Iscomeback Email: grisiscomeback@gmail.com License: GPL v3  Mejoras sobre top.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 126 | yes |
| `inference.py` | py | utility | 20 | yes |
| `inference2.py` | py | utility | 87 | yes |
| `install.sh` | sh | utility | 0 | no |
| `quantize.py` | py | utility | 115 | yes |
| `reinforce.py` | py | utility | 47 | yes |
| `topogpt2_1.py` | py | utility | 126 | yes |
| `topogpt2_embeddings_navigator.py` | py | utility | 149 | yes |
| `topogpt2_explorer.py` | py | utility | 155 | yes |
| `topogpt2_grid_scaler.py` | py | utility | 54 | yes |
| `topogpt2_multi_inference.py` | py | utility | 44 | yes |
| `zeroshot.py` | py | utility | 97 | yes |

## Key Symbols

- `TopoGPT2Config` (class, `app.py:55`) `class TopoGPT2Config` - Configuración completa para TopoGPT2.
- `__post_init__` (method, `app.py:124`) `def __post_init__(self)`
- `setup_logger` (method, `app.py:155`) `def setup_logger(name, level)`
- `set_seed` (method, `app.py:165`) `def set_seed(seed, device)`
- `QuaternionOps` (class, `app.py:177`) `class QuaternionOps` - Operaciones de cuaterniones puras en PyTorch.
- `hamilton_product` (method, `app.py:185`) `def hamilton_product(q1, q2)` - Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].
- `normalize` (method, `app.py:197`) `def normalize(q, eps)`
- `conjugate` (method, `app.py:201`) `def conjugate(q)`
- `rotate_vector` (method, `app.py:206`) `def rotate_vector(v, q)` - Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]
- `QuaternionLinear` (class, `app.py:216`) `class QuaternionLinear(Module)` - Capa lineal con pesos cuaterniones.
- `__init__` (method, `app.py:228`) `def __init__(self, in_features, out_features, bias)`
- `forward` (method, `app.py:244`) `def forward(self, x)` - x: [..., in_features] → [..., out_features]
- `QuaternionSpectralLayer` (class, `app.py:261`) `class QuaternionSpectralLayer(Module)` - Convolución espectral 2D con cuaterniones y producto de Hamilton completo.
- `__init__` (method, `app.py:281`) `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- `_kernel` (method, `app.py:300`) `def _kernel(self, c)`
- `_contract` (method, `app.py:303`) `def _contract(self, W, X)` - Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]
- `forward` (method, `app.py:307`) `def forward(self, x)` - x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)
- `SpectralAutoencoder` (class, `app.py:348`) `class SpectralAutoencoder(Module)` - Autoencoder espectral con cuaterniones.
- `__init__` (method, `app.py:361`) `def __init__(self, config)`
- `_filter1d` (method, `app.py:393`) `def _filter1d(self, x, kr, ki)` - Filtro espectral 1D: x[..., D] → filtrado[..., D]
- `encode` (method, `app.py:399`) `def encode(self, x)` - x: [..., D_MODEL] → latent: [..., D_LAT]
- `decode` (method, `app.py:404`) `def decode(self, z)` - z: [..., D_LAT] → recon: [..., D_MODEL]
- `forward` (method, `app.py:409`) `def forward(self, x)` - Devuelve (latent, recon_loss)
- `process_torus_grid` (method, `app.py:416`) `def process_torus_grid(self, grid)` - Procesa el grid del toro con QuaternionSpectralLayer.
- `QuaternionTorusBrain` (class, `app.py:431`) `class QuaternionTorusBrain(Module)` - Reemplaza el MLP en cada capa del transformer.
- `__init__` (method, `app.py:449`) `def __init__(self, d_model, config)`
- `_build_torus_graph` (method, `app.py:489`) `def _build_torus_graph(self)` - Construye las aristas del grafo toro 2×4.
- `_torus_soft_assign` (method, `app.py:523`) `def _torus_soft_assign(self, phi1, phi2)` - Asignación blanda de tokens a los 8 nodos del toro via distancia circular.
- `_message_passing` (method, `app.py:550`) `def _message_passing(self, node_feat)` - Message-passing VECTORIZADO con rotaciones cuaterniones.
- `forward` (method, `app.py:587`) `def forward(self, x)` - x: [B, S, D_MODEL]

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `install.sh`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `app.py`
- `inference.py`
- `inference2.py`
- `install.sh`
- `quantize.py`
- `reinforce.py`
- `topogpt2_1.py`
- `topogpt2_embeddings_navigator.py`
- `topogpt2_explorer.py`
- `topogpt2_grid_scaler.py`
- `topogpt2_multi_inference.py`
- `zeroshot.py`
