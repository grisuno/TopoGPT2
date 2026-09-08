# Symbols

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `BPETokenizer` | class | `app.py:1082` | `class BPETokenizer` |
| `CheckpointManager` | class | `app.py:1220` | `class CheckpointManager` |
| `CorpusDownloader` | class | `app.py:1107` | `class CorpusDownloader` |
| `MechanisticMetrics` | class | `app.py:1746` | `class MechanisticMetrics` |
| `MultiHeadAttention` | class | `app.py:847` | `class MultiHeadAttention(Module)` |
| `Phase0_KernelOptimizer` | class | `app.py:1983` | `class Phase0_KernelOptimizer` |
| `Phase1_BatchProspector` | class | `app.py:2058` | `class Phase1_BatchProspector` |
| `Phase2_SeedMiner` | class | `app.py:2141` | `class Phase2_SeedMiner` |
| `Phase4_AnnealingRefiner` | class | `app.py:2223` | `class Phase4_AnnealingRefiner` |
| `QuaternionLinear` | class | `app.py:216` | `class QuaternionLinear(Module)` |
| `QuaternionOps` | class | `app.py:177` | `class QuaternionOps` |
| `QuaternionSpectralLayer` | class | `app.py:261` | `class QuaternionSpectralLayer(Module)` |
| `QuaternionTorusBrain` | class | `app.py:431` | `class QuaternionTorusBrain(Module)` |
| `RMSNorm` | class | `app.py:696` | `class RMSNorm(Module)` |
| `RotaryEmbedding` | class | `app.py:648` | `class RotaryEmbedding(Module)` |
| `SpectralAutoencoder` | class | `app.py:348` | `class SpectralAutoencoder(Module)` |
| `SwiGLU` | class | `app.py:713` | `class SwiGLU(Module)` |
| `TokenizedDataset` | class | `app.py:1170` | `class TokenizedDataset(Dataset)` |
| `TopoGPT2` | class | `app.py:976` | `class TopoGPT2(Module)` |
| `TopoGPT2Config` | class | `app.py:55` | `class TopoGPT2Config` |
| `TopoGPT2Layer` | class | `app.py:929` | `class TopoGPT2Layer(Module)` |
| `TopoGPT2Trainer` | class | `app.py:1453` | `class TopoGPT2Trainer` |
| `TopoMoEBrain` | class | `app.py:742` | `class TopoMoEBrain(Module)` |
| `TopoPhasePipeline` | class | `app.py:2384` | `class TopoPhasePipeline` |
| `__getitem__` | method | `app.py:1209` | `def __getitem__(self, idx)` |
| `__init__` | method | `app.py:228` | `def __init__(self, in_features, out_features, bias)` |
| `__init__` | method | `app.py:281` | `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)` |
| `__init__` | method | `app.py:361` | `def __init__(self, config)` |
| `__init__` | method | `app.py:449` | `def __init__(self, d_model, config)` |
| `__init__` | method | `app.py:655` | `def __init__(self, d_head, max_seq_len, base)` |
| `__init__` | method | `app.py:699` | `def __init__(self, d_model, eps)` |
| `__init__` | method | `app.py:720` | `def __init__(self, d_model, expansion, dropout)` |
| `__init__` | method | `app.py:757` | `def __init__(self, d_model, config)` |
| `__init__` | method | `app.py:857` | `def __init__(self, d_model, n_heads, config)` |
| `__init__` | method | `app.py:938` | `def __init__(self, d_model, n_heads, config)` |
| `__init__` | method | `app.py:987` | `def __init__(self, config)` |
| `__init__` | method | `app.py:1085` | `def __init__(self, encoding)` |
| `__init__` | method | `app.py:1119` | `def __init__(self, corpus, data_dir, logger)` |
| `__init__` | method | `app.py:1179` | `def __init__(self, text, tokenizer, seq_len, max_tokens, cache_dir, split_tag)` |
| `__init__` | method | `app.py:1245` | `def __init__(self, config, logger)` |
| `__init__` | method | `app.py:1465` | `def __init__(self, model, config, tokenizer)` |
| `__init__` | method | `app.py:1766` | `def __init__(self, config)` |
| `__init__` | method | `app.py:2001` | `def __init__(self, config, logger)` |
| `__init__` | method | `app.py:2074` | `def __init__(self, config, logger)` |
| `__init__` | method | `app.py:2157` | `def __init__(self, config, logger)` |
| `__init__` | method | `app.py:2243` | `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)` |
| `__init__` | method | `app.py:2404` | `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)` |
| `__len__` | method | `app.py:1206` | `def __len__(self)` |
| `__post_init__` | method | `app.py:124` | `def __post_init__(self)` |
| `_build_cache` | method | `app.py:661` | `def _build_cache(self, seq_len)` |
| `_build_torus_graph` | method | `app.py:489` | `def _build_torus_graph(self)` |
| `_contract` | method | `app.py:303` | `def _contract(self, W, X)` |
| `_cosine_lr` | method | `app.py:1536` | `def _cosine_lr(self, step_in_session, total_steps_session)` |
| `_current_state` | method | `app.py:1525` | `def _current_state(self)` |
| `_download_hf` | method | `app.py:1150` | `def _download_hf(self, dataset_name, split, text_column, name)` |
| `_filter1d` | method | `app.py:393` | `def _filter1d(self, x, kr, ki)` |
| `_forward_impl` | method | `app.py:947` | `def _forward_impl(self, x, past_kv)` |
| `_init_weights` | method | `app.py:1006` | `def _init_weights(self)` |
| `_kernel` | method | `app.py:300` | `def _kernel(self, c)` |
| `_load_model` | method | `app.py:1297` | `def _load_model(self, model, directory)` |
| `_load_optimizer` | method | `app.py:1331` | `def _load_optimizer(self, optimizer, directory, device)` |
| `_load_state` | method | `app.py:1345` | `def _load_state(self, directory)` |
| `_make_dataloaders` | method | `app.py:2414` | `def _make_dataloaders(self, batch_size)` |
| `_measure_ratio` | method | `app.py:2005` | `def _measure_ratio(self, ratio, sample_batch)` |
| `_message_passing` | method | `app.py:550` | `def _message_passing(self, node_feat)` |
| `_rotate_half` | method | `app.py:668` | `def _rotate_half(self, x)` |
| `_route` | method | `app.py:778` | `def _route(self, x)` |
| `_sample_text` | method | `app.py:1684` | `def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)` |
| `_save_model` | method | `app.py:1284` | `def _save_model(self, model, directory)` |
| `_save_optimizer` | method | `app.py:1328` | `def _save_optimizer(self, optimizer, directory)` |
| `_save_state` | method | `app.py:1340` | `def _save_state(self, state, directory)` |
| `_set_lr` | method | `app.py:1544` | `def _set_lr(self, lr)` |
| `_torus_soft_assign` | method | `app.py:523` | `def _torus_soft_assign(self, phi1, phi2)` |
| `ckpt_fn` | method | `app.py:964` | `def ckpt_fn(x_in)` |
| `classify_phase` | method | `app.py:1921` | `def classify_phase(self, delta, kappa, berry)` |
| `compute_all` | method | `app.py:1940` | `def compute_all(self, model, lr, dataloader, compute_kappa)` |
| `compute_alpha` | method | `app.py:1781` | `def compute_alpha(self, delta)` |
| `compute_berry_phase` | method | `app.py:1878` | `def compute_berry_phase(self, model)` |
| `compute_delta` | method | `app.py:1774` | `def compute_delta(self, model)` |
| `compute_kappa` | method | `app.py:1820` | `def compute_kappa(self, model, dataloader, n_batches)` |
| `compute_lc` | method | `app.py:1891` | `def compute_lc(self, model)` |
| `compute_sp` | method | `app.py:1905` | `def compute_sp(self, model)` |
| `compute_t_eff` | method | `app.py:1812` | `def compute_t_eff(self, lr)` |
| `conjugate` | method | `app.py:201` | `def conjugate(q)` |
| `count_params` | method | `app.py:1036` | `def count_params(self)` |
| `decode` | method | `app.py:404` | `def decode(self, z)` |
| `decode` | method | `app.py:1096` | `def decode(self, tokens)` |
| `encode` | method | `app.py:399` | `def encode(self, x)` |
| `encode` | method | `app.py:1093` | `def encode(self, text)` |
| `eot_token` | method | `app.py:1099` | `def eot_token(self)` |
| `evaluate` | method | `app.py:1716` | `def evaluate(self, dataloader)` |
| `format_log` | method | `app.py:1965` | `def format_log(self, m)` |
| `forward` | method | `app.py:244` | `def forward(self, x)` |
| `forward` | method | `app.py:307` | `def forward(self, x)` |
| `forward` | method | `app.py:409` | `def forward(self, x)` |
| `forward` | method | `app.py:587` | `def forward(self, x)` |
| `forward` | method | `app.py:672` | `def forward(self, q, k, seq_len, offset)` |
| `forward` | method | `app.py:704` | `def forward(self, x)` |
| `forward` | method | `app.py:734` | `def forward(self, x)` |
| `forward` | method | `app.py:820` | `def forward(self, x)` |
| `forward` | method | `app.py:875` | `def forward(self, x, is_causal, past_kv)` |
| `forward` | method | `app.py:956` | `def forward(self, x, past_kv)` |
| `forward` | method | `app.py:1013` | `def forward(self, token_ids, past_kvs)` |
| `generate` | method | `app.py:1042` | `def generate(self, token_ids, max_new_tokens, temperature, top_k)` |
| `get_text` | method | `app.py:1125` | `def get_text(self, split)` |
| `hamilton_product` | method | `app.py:185` | `def hamilton_product(q1, q2)` |
| `has_checkpoint` | method | `app.py:1443` | `def has_checkpoint(self)` |
| `load_best` | method | `app.py:1431` | `def load_best(self, model)` |
| `load_latest` | method | `app.py:1404` | `def load_latest(self, model, optimizer)` |
| `main` | method | `app.py:2506` | `def main()` |
| `mine` | method | `app.py:2161` | `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)` |
| `normalize` | method | `app.py:197` | `def normalize(q, eps)` |
| `optimize` | method | `app.py:2034` | `def optimize(self, dataloader)` |
| `patch_config_for_resume` | method | `app.py:1255` | `def patch_config_for_resume(self, cfg)` |
| `process_torus_grid` | method | `app.py:416` | `def process_torus_grid(self, grid)` |
| `prospect` | method | `app.py:2078` | `def prospect(self, candidates, train_dataset, prospect_steps)` |
| `refine` | method | `app.py:2252` | `def refine(self, train_dl, val_dl, refine_epochs)` |
| `resume` | method | `app.py:1500` | `def resume(self)` |
| `rotate_vector` | method | `app.py:206` | `def rotate_vector(v, q)` |
| `run` | method | `app.py:2426` | `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)` |
| `save` | method | `app.py:1359` | `def save(self, model, optimizer, state, is_best)` |
| `set_seed` | method | `app.py:165` | `def set_seed(seed, device)` |
| `setup_logger` | method | `app.py:155` | `def setup_logger(name, level)` |
| `should_save` | method | `app.py:1356` | `def should_save(self)` |
| `train` | method | `app.py:1548` | `def train(self, train_dl, val_dl)` |
| `update_grad_buffer` | method | `app.py:1786` | `def update_grad_buffer(self, model)` |
| `CheckpointInspector` | class | `inference.py:45` | `class CheckpointInspector` |
| `GenerationEngine` | class | `inference.py:115` | `class GenerationEngine` |
| `InferenceConfig` | class | `inference.py:28` | `class InferenceConfig` |
| `InferenceRunner` | class | `inference.py:140` | `class InferenceRunner` |
| `ModelLoader` | class | `inference.py:90` | `class ModelLoader` |
| `__init__` | method | `inference.py:47` | `def __init__(self, logger)` |
| `__init__` | method | `inference.py:92` | `def __init__(self, checkpoint_name, logger)` |
| `__init__` | method | `inference.py:117` | `def __init__(self, config, logger)` |
| `__init__` | method | `inference.py:142` | `def __init__(self, config)` |
| `_load_source_module` | function | `inference.py:19` | `def _load_source_module(path)` |
| `_print_result` | method | `inference.py:170` | `def _print_result(self, prompt, output)` |
| `_resolve_preset` | method | `inference.py:81` | `def _resolve_preset(self, scale)` |
| `_setup_logger` | method | `inference.py:146` | `def _setup_logger(self)` |
| `generate` | method | `inference.py:121` | `def generate(self, model, tokenizer, prompt_text)` |
| `inspect_kq_head_count` | method | `inference.py:50` | `def inspect_kq_head_count(self, checkpoint_path, d_model, n_heads)` |
| `load_model` | method | `inference.py:96` | `def load_model(self, config, source_module)` |
| `parse_arguments` | method | `inference.py:178` | `def parse_arguments()` |
| `patch_config` | method | `inference.py:62` | `def patch_config(self, config, source_module)` |
| `run` | method | `inference.py:155` | `def run(self)` |
| `sample_logits` | method | `inference.py:132` | `def sample_logits(self, logits)` |
| `BPETokenizer` | class | `inference2.py:170` | `class BPETokenizer` |
| `CheckpointArchProber` | class | `inference2.py:735` | `class CheckpointArchProber` |
| `CheckpointLoader` | class | `inference2.py:890` | `class CheckpointLoader` |
| `GenerationEngine` | class | `inference2.py:1003` | `class GenerationEngine` |
| `InferenceConfig` | class | `inference2.py:97` | `class InferenceConfig` |
| `InferencePipeline` | class | `inference2.py:1116` | `class InferencePipeline` |
| `ModelConfig` | class | `inference2.py:700` | `class ModelConfig` |
| `MultiHeadAttention` | class | `inference2.py:589` | `class MultiHeadAttention(Module)` |
| `QuaternionLinear` | class | `inference2.py:219` | `class QuaternionLinear(Module)` |
| `QuaternionOps` | class | `inference2.py:196` | `class QuaternionOps` |
| `QuaternionSpectralLayer` | class | `inference2.py:252` | `class QuaternionSpectralLayer(Module)` |
| `QuaternionTorusBrain` | class | `inference2.py:358` | `class QuaternionTorusBrain(Module)` |
| `RMSNorm` | class | `inference2.py:577` | `class RMSNorm(Module)` |
| `ResultPrinter` | class | `inference2.py:1082` | `class ResultPrinter` |
| `RotaryEmbedding` | class | `inference2.py:537` | `class RotaryEmbedding(Module)` |
| `Sampler` | class | `inference2.py:943` | `class Sampler` |
| `SpectralAutoencoder` | class | `inference2.py:306` | `class SpectralAutoencoder(Module)` |
| `SwiGLU` | class | `inference2.py:462` | `class SwiGLU(Module)` |
| `TopoGPT2` | class | `inference2.py:660` | `class TopoGPT2(Module)` |
| `TopoGPT2Layer` | class | `inference2.py:638` | `class TopoGPT2Layer(Module)` |
| `TopoMoEBrain` | class | `inference2.py:481` | `class TopoMoEBrain(Module)` |
| `__call__` | method | `inference2.py:953` | `def __call__(self, logits, generated_ids)` |
| `__init__` | method | `inference2.py:175` | `def __init__(self)` |
| `__init__` | method | `inference2.py:227` | `def __init__(self, in_features, out_features, bias)` |
| `__init__` | method | `inference2.py:259` | `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)` |
| `__init__` | method | `inference2.py:312` | `def __init__(self, cfg)` |
| `__init__` | method | `inference2.py:370` | `def __init__(self, d_model, cfg)` |
| `__init__` | method | `inference2.py:465` | `def __init__(self, d_model, expansion, dropout)` |
| `__init__` | method | `inference2.py:488` | `def __init__(self, d_model, cfg)` |
| `__init__` | method | `inference2.py:542` | `def __init__(self, d_head, max_seq_len)` |
| `__init__` | method | `inference2.py:580` | `def __init__(self, d_model, eps)` |
| `__init__` | method | `inference2.py:594` | `def __init__(self, d_model, n_heads, cfg)` |
| `__init__` | method | `inference2.py:641` | `def __init__(self, d_model, n_heads, cfg)` |
| `__init__` | method | `inference2.py:666` | `def __init__(self, cfg)` |
| `__init__` | method | `inference2.py:768` | `def __init__(self, logger)` |
| `__init__` | method | `inference2.py:896` | `def __init__(self, logger)` |
| `__init__` | method | `inference2.py:950` | `def __init__(self, cfg)` |
| `__init__` | method | `inference2.py:1013` | `def __init__(self, model, tokenizer, cfg, logger)` |
| `__init__` | method | `inference2.py:1127` | `def __init__(self, cfg, logger)` |
| `_build_cache` | method | `inference2.py:550` | `def _build_cache(self, seq_len)` |
| `_build_model` | method | `inference2.py:1131` | `def _build_model(self)` |
| `_build_torus_graph` | method | `inference2.py:395` | `def _build_torus_graph(self)` |
| `_contract` | method | `inference2.py:279` | `def _contract(self, W, X)` |
| `_fallback_d_head` | method | `inference2.py:871` | `def _fallback_d_head(d_model, q_out, k_out)` |
| `_filter1d` | method | `inference2.py:334` | `def _filter1d(self, x, kr, ki)` |
| `_kernel` | method | `inference2.py:276` | `def _kernel(self, c)` |
| `_load_shapes` | method | `inference2.py:771` | `def _load_shapes(self, path)` |
| `_maybe_stream` | method | `inference2.py:1071` | `def _maybe_stream(self, token_id)` |
| `_message_passing` | method | `inference2.py:423` | `def _message_passing(self, node_feat)` |
| `_rotate_half` | method | `inference2.py:557` | `def _rotate_half(x)` |
| `_route` | method | `inference2.py:503` | `def _route(self, x)` |
| `_run_benchmark` | method | `inference2.py:1199` | `def _run_benchmark(self, engine, printer)` |
| `_run_interactive` | method | `inference2.py:1176` | `def _run_interactive(self, engine, printer)` |
| `_run_single` | method | `inference2.py:1164` | `def _run_single(self, engine, printer)` |
| `_torus_soft_assign` | method | `inference2.py:411` | `def _torus_soft_assign(self, phi1, phi2)` |
| `build_arg_parser` | method | `inference2.py:1217` | `def build_arg_parser()` |
| `build_logger` | function | `inference2.py:79` | `def build_logger(name, level)` |
| `conjugate` | method | `inference2.py:215` | `def conjugate(q)` |
| `d_quat` | method | `inference2.py:723` | `def d_quat(self)` |
| `decode` | method | `inference2.py:185` | `def decode(self, token_ids)` |
| `decode` | method | `inference2.py:344` | `def decode(self, z)` |
| `decode_single` | method | `inference2.py:188` | `def decode_single(self, token_id)` |
| `encode` | method | `inference2.py:182` | `def encode(self, text)` |
| `encode` | method | `inference2.py:341` | `def encode(self, x)` |
| `forward` | method | `inference2.py:241` | `def forward(self, x)` |
| `forward` | method | `inference2.py:282` | `def forward(self, x)` |
| `forward` | method | `inference2.py:347` | `def forward(self, x)` |
| `forward` | method | `inference2.py:437` | `def forward(self, x)` |
| `forward` | method | `inference2.py:475` | `def forward(self, x)` |
| `forward` | method | `inference2.py:528` | `def forward(self, x)` |
| `forward` | method | `inference2.py:561` | `def forward(self, q, k, seq_len, offset)` |
| `forward` | method | `inference2.py:585` | `def forward(self, x)` |
| `forward` | method | `inference2.py:609` | `def forward(self, x, is_causal, past_kv)` |
| `forward` | method | `inference2.py:649` | `def forward(self, x, past_kv)` |
| `forward` | method | `inference2.py:678` | `def forward(self, token_ids, past_kvs)` |
| `generate` | method | `inference2.py:1027` | `def generate(self, prompt)` |
| `gqa_groups` | method | `inference2.py:727` | `def gqa_groups(self)` |
| `hamilton_product` | method | `inference2.py:200` | `def hamilton_product(q1, q2)` |
| `load` | method | `inference2.py:899` | `def load(self, path, model, device)` |
| `main` | method | `inference2.py:1288` | `def main()` |
| `normalize` | method | `inference2.py:211` | `def normalize(q, eps)` |
| `print_benchmark` | method | `inference2.py:1100` | `def print_benchmark(self, runs, tps_list)` |
| `print_single` | method | `inference2.py:1087` | `def print_single(self, prompt, full_text, tps, show_timing)` |
| `probe` | method | `inference2.py:786` | `def probe(self, path)` |
| `process_torus_grid` | method | `inference2.py:351` | `def process_torus_grid(self, grid)` |
| `run` | method | `inference2.py:1149` | `def run(self)` |
| `validate` | method | `inference2.py:148` | `def validate(self)` |
| `BFloat16Quantizer` | class | `quantize.py:774` | `class BFloat16Quantizer(IQuantizer)` |
| `BPETokenizer` | class | `quantize.py:651` | `class BPETokenizer` |
| `BitNetQuantizer` | class | `quantize.py:692` | `class BitNetQuantizer(IQuantizer)` |
| `CheckpointInspector` | class | `quantize.py:105` | `class CheckpointInspector` |
| `Float16Quantizer` | class | `quantize.py:760` | `class Float16Quantizer(IQuantizer)` |
| `Float32Quantizer` | class | `quantize.py:788` | `class Float32Quantizer(IQuantizer)` |
| `Float64Quantizer` | class | `quantize.py:802` | `class Float64Quantizer(IQuantizer)` |
| `INT4Quantizer` | class | `quantize.py:721` | `class INT4Quantizer(IQuantizer)` |
| `INT8Quantizer` | class | `quantize.py:746` | `class INT8Quantizer(IQuantizer)` |
| `IQuantizer` | class | `quantize.py:678` | `class IQuantizer(ABC)` |
| `InferenceConfig` | class | `quantize.py:34` | `class InferenceConfig` |
| `InferenceEngine` | class | `quantize.py:883` | `class InferenceEngine` |
| `ModelLoader` | class | `quantize.py:834` | `class ModelLoader` |
| `MultiHeadAttention` | class | `quantize.py:522` | `class MultiHeadAttention(Module)` |
| `QuantizationFormat` | class | `quantize.py:668` | `class QuantizationFormat(Enum)` |
| `QuantizationInferencePipeline` | class | `quantize.py:907` | `class QuantizationInferencePipeline` |
| `QuantizerFactory` | class | `quantize.py:816` | `class QuantizerFactory` |
| `QuaternionLinear` | class | `quantize.py:195` | `class QuaternionLinear(Module)` |
| `QuaternionOps` | class | `quantize.py:162` | `class QuaternionOps` |
| `QuaternionSpectralLayer` | class | `quantize.py:220` | `class QuaternionSpectralLayer(Module)` |
| `QuaternionTorusBrain` | class | `quantize.py:312` | `class QuaternionTorusBrain(Module)` |
| `RMSNorm` | class | `quantize.py:440` | `class RMSNorm(Module)` |
| `RotaryEmbedding` | class | `quantize.py:408` | `class RotaryEmbedding(Module)` |
| `SpectralAutoencoder` | class | `quantize.py:262` | `class SpectralAutoencoder(Module)` |
| `SwiGLU` | class | `quantize.py:451` | `class SwiGLU(Module)` |
| `TopoGPT2` | class | `quantize.py:590` | `class TopoGPT2(Module)` |
| `TopoGPT2Layer` | class | `quantize.py:568` | `class TopoGPT2Layer(Module)` |
| `TopoMoEBrain` | class | `quantize.py:468` | `class TopoMoEBrain(Module)` |
| `__init__` | method | `quantize.py:196` | `def __init__(self, in_features, out_features, bias)` |
| `__init__` | method | `quantize.py:221` | `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)` |
| `__init__` | method | `quantize.py:263` | `def __init__(self, config)` |
| `__init__` | method | `quantize.py:313` | `def __init__(self, d_model, config)` |
| `__init__` | method | `quantize.py:409` | `def __init__(self, d_head, max_seq_len, base)` |
| `__init__` | method | `quantize.py:441` | `def __init__(self, d_model, eps)` |
| `__init__` | method | `quantize.py:452` | `def __init__(self, d_model, expansion, dropout)` |
| `__init__` | method | `quantize.py:469` | `def __init__(self, d_model, config)` |
| `__init__` | method | `quantize.py:523` | `def __init__(self, d_model, n_heads, config)` |
| `__init__` | method | `quantize.py:569` | `def __init__(self, d_model, n_heads, config)` |
| `__init__` | method | `quantize.py:591` | `def __init__(self, config)` |
| `__init__` | method | `quantize.py:652` | `def __init__(self, encoding)` |
| `__init__` | method | `quantize.py:693` | `def __init__(self, config)` |
| `__init__` | method | `quantize.py:722` | `def __init__(self, config)` |
| `__init__` | method | `quantize.py:747` | `def __init__(self, config)` |
| `__init__` | method | `quantize.py:761` | `def __init__(self, config)` |
| `__init__` | method | `quantize.py:775` | `def __init__(self, config)` |
| `__init__` | method | `quantize.py:789` | `def __init__(self, config)` |
| `__init__` | method | `quantize.py:803` | `def __init__(self, config)` |
| `__init__` | method | `quantize.py:835` | `def __init__(self, config, logger)` |
| `__init__` | method | `quantize.py:884` | `def __init__(self, config, model, tokenizer)` |
| `__init__` | method | `quantize.py:908` | `def __init__(self, config)` |
| `_build_cache` | method | `quantize.py:415` | `def _build_cache(self, seq_len)` |
| `_build_torus_graph` | method | `quantize.py:338` | `def _build_torus_graph(self)` |
| `_contract` | method | `quantize.py:236` | `def _contract(self, W, X)` |
| `_filter1d` | method | `quantize.py:286` | `def _filter1d(self, x, kr, ki)` |
| `_forward_impl` | method | `quantize.py:579` | `def _forward_impl(self, x, past_kv)` |
| `_init_weights` | method | `quantize.py:606` | `def _init_weights(self)` |
| `_kernel` | method | `quantize.py:233` | `def _kernel(self, c)` |
| `_message_passing` | method | `quantize.py:365` | `def _message_passing(self, node_feat)` |
| `_rotate_half` | method | `quantize.py:422` | `def _rotate_half(self, x)` |
| `_route` | method | `quantize.py:486` | `def _route(self, x)` |
| `_torus_soft_assign` | method | `quantize.py:354` | `def _torus_soft_assign(self, phi1, phi2)` |
| `conjugate` | method | `quantize.py:180` | `def conjugate(q)` |
| `create_quantizer` | method | `quantize.py:818` | `def create_quantizer(fmt, config)` |
| `decode` | method | `quantize.py:295` | `def decode(self, z)` |
| `decode` | method | `quantize.py:661` | `def decode(self, tokens)` |
| `encode` | method | `quantize.py:291` | `def encode(self, x)` |
| `encode` | method | `quantize.py:658` | `def encode(self, text)` |
| `eot_token` | method | `quantize.py:664` | `def eot_token(self)` |
| `execute` | method | `quantize.py:919` | `def execute(self)` |
| `forward` | method | `quantize.py:209` | `def forward(self, x)` |
| `forward` | method | `quantize.py:239` | `def forward(self, x)` |
| `forward` | method | `quantize.py:299` | `def forward(self, x)` |
| `forward` | method | `quantize.py:380` | `def forward(self, x)` |
| `forward` | method | `quantize.py:426` | `def forward(self, q, k, seq_len, offset)` |
| `forward` | method | `quantize.py:446` | `def forward(self, x)` |
| `forward` | method | `quantize.py:464` | `def forward(self, x)` |
| `forward` | method | `quantize.py:509` | `def forward(self, x)` |
| `forward` | method | `quantize.py:539` | `def forward(self, x, is_causal, past_kv)` |
| `forward` | method | `quantize.py:586` | `def forward(self, x, past_kv)` |
| `forward` | method | `quantize.py:613` | `def forward(self, token_ids, past_kvs)` |
| `generate` | method | `quantize.py:627` | `def generate(self, token_ids, max_new_tokens, temperature, top_k, eos_token_id)` |
| `get_bits_per_weight` | method | `quantize.py:688` | `def get_bits_per_weight(self)` |
| `get_bits_per_weight` | method | `quantize.py:717` | `def get_bits_per_weight(self)` |
| `get_bits_per_weight` | method | `quantize.py:742` | `def get_bits_per_weight(self)` |
| `get_bits_per_weight` | method | `quantize.py:756` | `def get_bits_per_weight(self)` |
| `get_bits_per_weight` | method | `quantize.py:770` | `def get_bits_per_weight(self)` |
| `get_bits_per_weight` | method | `quantize.py:784` | `def get_bits_per_weight(self)` |
| `get_bits_per_weight` | method | `quantize.py:798` | `def get_bits_per_weight(self)` |
| `get_bits_per_weight` | method | `quantize.py:812` | `def get_bits_per_weight(self)` |
| `get_format_name` | method | `quantize.py:684` | `def get_format_name(self)` |
| `get_format_name` | method | `quantize.py:714` | `def get_format_name(self)` |
| `get_format_name` | method | `quantize.py:739` | `def get_format_name(self)` |
| `get_format_name` | method | `quantize.py:753` | `def get_format_name(self)` |
| `get_format_name` | method | `quantize.py:767` | `def get_format_name(self)` |
| `get_format_name` | method | `quantize.py:781` | `def get_format_name(self)` |
| `get_format_name` | method | `quantize.py:795` | `def get_format_name(self)` |
| `get_format_name` | method | `quantize.py:809` | `def get_format_name(self)` |
| `hamilton_product` | method | `quantize.py:165` | `def hamilton_product(q1, q2)` |
| `inspect_and_patch` | method | `quantize.py:108` | `def inspect_and_patch(path, config)` |
| `load_checkpoint` | method | `quantize.py:839` | `def load_checkpoint(self)` |
| `main` | method | `quantize.py:965` | `def main()` |
| `normalize` | method | `quantize.py:176` | `def normalize(q, eps)` |
| `parse_arguments` | method | `quantize.py:939` | `def parse_arguments()` |
| `process_torus_grid` | method | `quantize.py:305` | `def process_torus_grid(self, grid)` |
| `quantize` | method | `quantize.py:680` | `def quantize(self, model)` |
| `quantize` | method | `quantize.py:696` | `def quantize(self, model)` |
| `quantize` | method | `quantize.py:725` | `def quantize(self, model)` |
| `quantize` | method | `quantize.py:750` | `def quantize(self, model)` |
| `quantize` | method | `quantize.py:764` | `def quantize(self, model)` |
| `quantize` | method | `quantize.py:778` | `def quantize(self, model)` |
| `quantize` | method | `quantize.py:792` | `def quantize(self, model)` |
| `quantize` | method | `quantize.py:806` | `def quantize(self, model)` |
| `resolve_gqa` | method | `quantize.py:86` | `def resolve_gqa(self)` |
| `rotate_vector` | method | `quantize.py:185` | `def rotate_vector(v, q)` |
| `run_inference` | method | `quantize.py:891` | `def run_inference(self, prompt)` |
| `ChatAgent` | class | `reinforce.py:519` | `class ChatAgent` |
| `CheckpointPatcher` | class | `reinforce.py:84` | `class CheckpointPatcher` |
| `ExperienceBuffer` | class | `reinforce.py:189` | `class ExperienceBuffer` |
| `MechanisticRewardCalculator` | class | `reinforce.py:120` | `class MechanisticRewardCalculator` |
| `PPOTrainer` | class | `reinforce.py:262` | `class PPOTrainer` |
| `RLConfig` | class | `reinforce.py:27` | `class RLConfig` |
| `RewardModel` | class | `reinforce.py:152` | `class RewardModel(Module)` |
| `RewardSignalType` | class | `reinforce.py:72` | `class RewardSignalType(Enum)` |
| `ValueHead` | class | `reinforce.py:240` | `class ValueHead(Module)` |
| `__init__` | method | `reinforce.py:86` | `def __init__(self, logger)` |
| `__init__` | method | `reinforce.py:122` | `def __init__(self, config, logger)` |
| `__init__` | method | `reinforce.py:154` | `def __init__(self, config, vocab_size, d_model)` |
| `__init__` | method | `reinforce.py:191` | `def __init__(self, config, capacity)` |
| `__init__` | method | `reinforce.py:242` | `def __init__(self, d_model, hidden_dim)` |
| `__init__` | method | `reinforce.py:264` | `def __init__(self, policy_model, config, reward_model, ref_model, logger)` |
| `__init__` | method | `reinforce.py:521` | `def __init__(self, policy_model, config, tokenizer, logger)` |
| `_collate` | method | `reinforce.py:226` | `def _collate(self, batch)` |
| `_extract_mechanistic_metrics` | method | `reinforce.py:367` | `def _extract_mechanistic_metrics(self, tokens)` |
| `_format_conversation` | method | `reinforce.py:553` | `def _format_conversation(self)` |
| `_init_weights` | method | `reinforce.py:173` | `def _init_weights(self)` |
| `_init_weights` | method | `reinforce.py:251` | `def _init_weights(self)` |
| `_resolve_preset` | method | `reinforce.py:111` | `def _resolve_preset(self, scale)` |
| `_save_checkpoint` | method | `reinforce.py:482` | `def _save_checkpoint(self)` |
| `add` | method | `reinforce.py:198` | `def add(self, experience)` |
| `align_config` | method | `reinforce.py:89` | `def align_config(self, model_path, config, source_module)` |
| `attach_trainer` | method | `reinforce.py:530` | `def attach_trainer(self, trainer)` |
| `clear` | method | `reinforce.py:237` | `def clear(self)` |
| `collect_experience` | method | `reinforce.py:336` | `def collect_experience(self, prompts, num_samples)` |
| `compute_advantages` | method | `reinforce.py:201` | `def compute_advantages(self, values, rewards, masks)` |
| `compute_delta_reward` | method | `reinforce.py:137` | `def compute_delta_reward(self, delta_value)` |
| `compute_kl_divergence` | method | `reinforce.py:306` | `def compute_kl_divergence(self, policy_logits, ref_logits)` |
| `compute_lc_reward` | method | `reinforce.py:129` | `def compute_lc_reward(self, lc_value)` |
| `compute_mechanistic_reward` | method | `reinforce.py:142` | `def compute_mechanistic_reward(self, metrics)` |
| `compute_reward` | method | `reinforce.py:317` | `def compute_reward(self, responses, prompts, metrics)` |
| `compute_sp_reward` | method | `reinforce.py:133` | `def compute_sp_reward(self, sp_value)` |
| `create_rl_agent_from_checkpoint` | method | `reinforce.py:606` | `def create_rl_agent_from_checkpoint(model_path, config, tokenizer, logger)` |
| `forward` | method | `reinforce.py:180` | `def forward(self, input_ids, attention_mask)` |
| `forward` | method | `reinforce.py:258` | `def forward(self, hidden_states)` |
| `generate_with_policy` | method | `reinforce.py:294` | `def generate_with_policy(self, prompt_ids, max_new_tokens)` |
| `load_checkpoint` | method | `reinforce.py:498` | `def load_checkpoint(self, path)` |
| `ppo_update` | method | `reinforce.py:398` | `def ppo_update(self, batch)` |
| `reset_conversation` | method | `reinforce.py:594` | `def reset_conversation(self)` |
| `respond` | method | `reinforce.py:533` | `def respond(self, user_message, max_new_tokens)` |
| `sample_minibatches` | method | `reinforce.py:215` | `def sample_minibatches(self, batch_size)` |
| `setup_logger` | method | `reinforce.py:597` | `def setup_logger(name, level)` |
| `train_on_feedback` | method | `reinforce.py:562` | `def train_on_feedback(self, user_message, response, reward_score)` |
| `train_step` | method | `reinforce.py:460` | `def train_step(self, prompts)` |
| `BPETokenizer` | class | `topogpt2_1.py:1082` | `class BPETokenizer` |
| `CheckpointManager` | class | `topogpt2_1.py:1220` | `class CheckpointManager` |
| `CorpusDownloader` | class | `topogpt2_1.py:1107` | `class CorpusDownloader` |
| `MechanisticMetrics` | class | `topogpt2_1.py:1746` | `class MechanisticMetrics` |
| `MultiHeadAttention` | class | `topogpt2_1.py:847` | `class MultiHeadAttention(Module)` |
| `Phase0_KernelOptimizer` | class | `topogpt2_1.py:1983` | `class Phase0_KernelOptimizer` |
| `Phase1_BatchProspector` | class | `topogpt2_1.py:2058` | `class Phase1_BatchProspector` |
| `Phase2_SeedMiner` | class | `topogpt2_1.py:2141` | `class Phase2_SeedMiner` |
| `Phase4_AnnealingRefiner` | class | `topogpt2_1.py:2223` | `class Phase4_AnnealingRefiner` |
| `QuaternionLinear` | class | `topogpt2_1.py:216` | `class QuaternionLinear(Module)` |
| `QuaternionOps` | class | `topogpt2_1.py:177` | `class QuaternionOps` |
| `QuaternionSpectralLayer` | class | `topogpt2_1.py:261` | `class QuaternionSpectralLayer(Module)` |
| `QuaternionTorusBrain` | class | `topogpt2_1.py:431` | `class QuaternionTorusBrain(Module)` |
| `RMSNorm` | class | `topogpt2_1.py:696` | `class RMSNorm(Module)` |
| `RotaryEmbedding` | class | `topogpt2_1.py:648` | `class RotaryEmbedding(Module)` |
| `SpectralAutoencoder` | class | `topogpt2_1.py:348` | `class SpectralAutoencoder(Module)` |
| `SwiGLU` | class | `topogpt2_1.py:713` | `class SwiGLU(Module)` |
| `TokenizedDataset` | class | `topogpt2_1.py:1170` | `class TokenizedDataset(Dataset)` |
| `TopoGPT2` | class | `topogpt2_1.py:976` | `class TopoGPT2(Module)` |
| `TopoGPT2Config` | class | `topogpt2_1.py:55` | `class TopoGPT2Config` |
| `TopoGPT2Layer` | class | `topogpt2_1.py:929` | `class TopoGPT2Layer(Module)` |
| `TopoGPT2Trainer` | class | `topogpt2_1.py:1453` | `class TopoGPT2Trainer` |
| `TopoMoEBrain` | class | `topogpt2_1.py:742` | `class TopoMoEBrain(Module)` |
| `TopoPhasePipeline` | class | `topogpt2_1.py:2384` | `class TopoPhasePipeline` |
| `__getitem__` | method | `topogpt2_1.py:1209` | `def __getitem__(self, idx)` |
| `__init__` | method | `topogpt2_1.py:228` | `def __init__(self, in_features, out_features, bias)` |
| `__init__` | method | `topogpt2_1.py:281` | `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)` |
| `__init__` | method | `topogpt2_1.py:361` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_1.py:449` | `def __init__(self, d_model, config)` |
| `__init__` | method | `topogpt2_1.py:655` | `def __init__(self, d_head, max_seq_len, base)` |
| `__init__` | method | `topogpt2_1.py:699` | `def __init__(self, d_model, eps)` |
| `__init__` | method | `topogpt2_1.py:720` | `def __init__(self, d_model, expansion, dropout)` |
| `__init__` | method | `topogpt2_1.py:757` | `def __init__(self, d_model, config)` |
| `__init__` | method | `topogpt2_1.py:857` | `def __init__(self, d_model, n_heads, config)` |
| `__init__` | method | `topogpt2_1.py:938` | `def __init__(self, d_model, n_heads, config)` |
| `__init__` | method | `topogpt2_1.py:987` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_1.py:1085` | `def __init__(self, encoding)` |
| `__init__` | method | `topogpt2_1.py:1119` | `def __init__(self, corpus, data_dir, logger)` |
| `__init__` | method | `topogpt2_1.py:1179` | `def __init__(self, text, tokenizer, seq_len, max_tokens, cache_dir, split_tag)` |
| `__init__` | method | `topogpt2_1.py:1245` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt2_1.py:1465` | `def __init__(self, model, config, tokenizer)` |
| `__init__` | method | `topogpt2_1.py:1766` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_1.py:2001` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt2_1.py:2074` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt2_1.py:2157` | `def __init__(self, config, logger)` |
| `__init__` | method | `topogpt2_1.py:2243` | `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)` |
| `__init__` | method | `topogpt2_1.py:2404` | `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)` |
| `__len__` | method | `topogpt2_1.py:1206` | `def __len__(self)` |
| `__post_init__` | method | `topogpt2_1.py:124` | `def __post_init__(self)` |
| `_build_cache` | method | `topogpt2_1.py:661` | `def _build_cache(self, seq_len)` |
| `_build_torus_graph` | method | `topogpt2_1.py:489` | `def _build_torus_graph(self)` |
| `_contract` | method | `topogpt2_1.py:303` | `def _contract(self, W, X)` |
| `_cosine_lr` | method | `topogpt2_1.py:1536` | `def _cosine_lr(self, step_in_session, total_steps_session)` |
| `_current_state` | method | `topogpt2_1.py:1525` | `def _current_state(self)` |
| `_download_hf` | method | `topogpt2_1.py:1150` | `def _download_hf(self, dataset_name, split, text_column, name)` |
| `_filter1d` | method | `topogpt2_1.py:393` | `def _filter1d(self, x, kr, ki)` |
| `_forward_impl` | method | `topogpt2_1.py:947` | `def _forward_impl(self, x, past_kv)` |
| `_init_weights` | method | `topogpt2_1.py:1006` | `def _init_weights(self)` |
| `_kernel` | method | `topogpt2_1.py:300` | `def _kernel(self, c)` |
| `_load_model` | method | `topogpt2_1.py:1297` | `def _load_model(self, model, directory)` |
| `_load_optimizer` | method | `topogpt2_1.py:1331` | `def _load_optimizer(self, optimizer, directory, device)` |
| `_load_state` | method | `topogpt2_1.py:1345` | `def _load_state(self, directory)` |
| `_make_dataloaders` | method | `topogpt2_1.py:2414` | `def _make_dataloaders(self, batch_size)` |
| `_measure_ratio` | method | `topogpt2_1.py:2005` | `def _measure_ratio(self, ratio, sample_batch)` |
| `_message_passing` | method | `topogpt2_1.py:550` | `def _message_passing(self, node_feat)` |
| `_rotate_half` | method | `topogpt2_1.py:668` | `def _rotate_half(self, x)` |
| `_route` | method | `topogpt2_1.py:778` | `def _route(self, x)` |
| `_sample_text` | method | `topogpt2_1.py:1684` | `def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)` |
| `_save_model` | method | `topogpt2_1.py:1284` | `def _save_model(self, model, directory)` |
| `_save_optimizer` | method | `topogpt2_1.py:1328` | `def _save_optimizer(self, optimizer, directory)` |
| `_save_state` | method | `topogpt2_1.py:1340` | `def _save_state(self, state, directory)` |
| `_set_lr` | method | `topogpt2_1.py:1544` | `def _set_lr(self, lr)` |
| `_torus_soft_assign` | method | `topogpt2_1.py:523` | `def _torus_soft_assign(self, phi1, phi2)` |
| `ckpt_fn` | method | `topogpt2_1.py:964` | `def ckpt_fn(x_in)` |
| `classify_phase` | method | `topogpt2_1.py:1921` | `def classify_phase(self, delta, kappa, berry)` |
| `compute_all` | method | `topogpt2_1.py:1940` | `def compute_all(self, model, lr, dataloader, compute_kappa)` |
| `compute_alpha` | method | `topogpt2_1.py:1781` | `def compute_alpha(self, delta)` |
| `compute_berry_phase` | method | `topogpt2_1.py:1878` | `def compute_berry_phase(self, model)` |
| `compute_delta` | method | `topogpt2_1.py:1774` | `def compute_delta(self, model)` |
| `compute_kappa` | method | `topogpt2_1.py:1820` | `def compute_kappa(self, model, dataloader, n_batches)` |
| `compute_lc` | method | `topogpt2_1.py:1891` | `def compute_lc(self, model)` |
| `compute_sp` | method | `topogpt2_1.py:1905` | `def compute_sp(self, model)` |
| `compute_t_eff` | method | `topogpt2_1.py:1812` | `def compute_t_eff(self, lr)` |
| `conjugate` | method | `topogpt2_1.py:201` | `def conjugate(q)` |
| `count_params` | method | `topogpt2_1.py:1036` | `def count_params(self)` |
| `decode` | method | `topogpt2_1.py:404` | `def decode(self, z)` |
| `decode` | method | `topogpt2_1.py:1096` | `def decode(self, tokens)` |
| `encode` | method | `topogpt2_1.py:399` | `def encode(self, x)` |
| `encode` | method | `topogpt2_1.py:1093` | `def encode(self, text)` |
| `eot_token` | method | `topogpt2_1.py:1099` | `def eot_token(self)` |
| `evaluate` | method | `topogpt2_1.py:1716` | `def evaluate(self, dataloader)` |
| `format_log` | method | `topogpt2_1.py:1965` | `def format_log(self, m)` |
| `forward` | method | `topogpt2_1.py:244` | `def forward(self, x)` |
| `forward` | method | `topogpt2_1.py:307` | `def forward(self, x)` |
| `forward` | method | `topogpt2_1.py:409` | `def forward(self, x)` |
| `forward` | method | `topogpt2_1.py:587` | `def forward(self, x)` |
| `forward` | method | `topogpt2_1.py:672` | `def forward(self, q, k, seq_len, offset)` |
| `forward` | method | `topogpt2_1.py:704` | `def forward(self, x)` |
| `forward` | method | `topogpt2_1.py:734` | `def forward(self, x)` |
| `forward` | method | `topogpt2_1.py:820` | `def forward(self, x)` |
| `forward` | method | `topogpt2_1.py:875` | `def forward(self, x, is_causal, past_kv)` |
| `forward` | method | `topogpt2_1.py:956` | `def forward(self, x, past_kv)` |
| `forward` | method | `topogpt2_1.py:1013` | `def forward(self, token_ids, past_kvs)` |
| `generate` | method | `topogpt2_1.py:1042` | `def generate(self, token_ids, max_new_tokens, temperature, top_k)` |
| `get_text` | method | `topogpt2_1.py:1125` | `def get_text(self, split)` |
| `hamilton_product` | method | `topogpt2_1.py:185` | `def hamilton_product(q1, q2)` |
| `has_checkpoint` | method | `topogpt2_1.py:1443` | `def has_checkpoint(self)` |
| `load_best` | method | `topogpt2_1.py:1431` | `def load_best(self, model)` |
| `load_latest` | method | `topogpt2_1.py:1404` | `def load_latest(self, model, optimizer)` |
| `main` | method | `topogpt2_1.py:2506` | `def main()` |
| `mine` | method | `topogpt2_1.py:2161` | `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)` |
| `normalize` | method | `topogpt2_1.py:197` | `def normalize(q, eps)` |
| `optimize` | method | `topogpt2_1.py:2034` | `def optimize(self, dataloader)` |
| `patch_config_for_resume` | method | `topogpt2_1.py:1255` | `def patch_config_for_resume(self, cfg)` |
| `process_torus_grid` | method | `topogpt2_1.py:416` | `def process_torus_grid(self, grid)` |
| `prospect` | method | `topogpt2_1.py:2078` | `def prospect(self, candidates, train_dataset, prospect_steps)` |
| `refine` | method | `topogpt2_1.py:2252` | `def refine(self, train_dl, val_dl, refine_epochs)` |
| `resume` | method | `topogpt2_1.py:1500` | `def resume(self)` |
| `rotate_vector` | method | `topogpt2_1.py:206` | `def rotate_vector(v, q)` |
| `run` | method | `topogpt2_1.py:2426` | `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)` |
| `save` | method | `topogpt2_1.py:1359` | `def save(self, model, optimizer, state, is_best)` |
| `set_seed` | method | `topogpt2_1.py:165` | `def set_seed(seed, device)` |
| `setup_logger` | method | `topogpt2_1.py:155` | `def setup_logger(name, level)` |
| `should_save` | method | `topogpt2_1.py:1356` | `def should_save(self)` |
| `train` | method | `topogpt2_1.py:1548` | `def train(self, train_dl, val_dl)` |
| `update_grad_buffer` | method | `topogpt2_1.py:1786` | `def update_grad_buffer(self, model)` |
| `ActivationCapture` | class | `topogpt2_embeddings_navigator.py:522` | `class ActivationCapture` |
| `BaseEmbeddingView` | class | `topogpt2_embeddings_navigator.py:1255` | `class BaseEmbeddingView(ABC)` |
| `BerryPhaseView` | class | `topogpt2_embeddings_navigator.py:1666` | `class BerryPhaseView(BaseEmbeddingView)` |
| `CheckpointBundle` | class | `topogpt2_embeddings_navigator.py:263` | `class CheckpointBundle` |
| `CloudView` | class | `topogpt2_embeddings_navigator.py:1352` | `class CloudView(BaseEmbeddingView)` |
| `CrossLayerView` | class | `topogpt2_embeddings_navigator.py:1933` | `class CrossLayerView(BaseEmbeddingView)` |
| `FigureStyler` | class | `topogpt2_embeddings_navigator.py:1195` | `class FigureStyler` |
| `LipschitzView` | class | `topogpt2_embeddings_navigator.py:1758` | `class LipschitzView(BaseEmbeddingView)` |
| `MetricSuite` | class | `topogpt2_embeddings_navigator.py:600` | `class MetricSuite` |
| `MetricsConfig` | class | `topogpt2_embeddings_navigator.py:132` | `class MetricsConfig` |
| `MetricsView` | class | `topogpt2_embeddings_navigator.py:1475` | `class MetricsView(BaseEmbeddingView)` |
| `ModelLoader` | class | `topogpt2_embeddings_navigator.py:312` | `class ModelLoader` |
| `ModuleImporter` | class | `topogpt2_embeddings_navigator.py:2217` | `class ModuleImporter` |
| `NavigatorApp` | class | `topogpt2_embeddings_navigator.py:2255` | `class NavigatorApp` |
| `NavigatorConfig` | class | `topogpt2_embeddings_navigator.py:156` | `class NavigatorConfig` |
| `NeighborhoodView` | class | `topogpt2_embeddings_navigator.py:1834` | `class NeighborhoodView(BaseEmbeddingView)` |
| `OverviewView` | class | `topogpt2_embeddings_navigator.py:1274` | `class OverviewView(BaseEmbeddingView)` |
| `PersistenceView` | class | `topogpt2_embeddings_navigator.py:1569` | `class PersistenceView(BaseEmbeddingView)` |
| `PlotTheme` | class | `topogpt2_embeddings_navigator.py:103` | `class PlotTheme` |
| `ProjectionConfig` | class | `topogpt2_embeddings_navigator.py:146` | `class ProjectionConfig` |
| `Projector` | class | `topogpt2_embeddings_navigator.py:1068` | `class Projector` |
| `QuaternionView` | class | `topogpt2_embeddings_navigator.py:1994` | `class QuaternionView(BaseEmbeddingView)` |
| `RawView` | class | `topogpt2_embeddings_navigator.py:2108` | `class RawView(BaseEmbeddingView)` |
| `RenderContext` | class | `topogpt2_embeddings_navigator.py:1243` | `class RenderContext` |
| `SamplingLimits` | class | `topogpt2_embeddings_navigator.py:118` | `class SamplingLimits` |
| `SidebarController` | class | `topogpt2_embeddings_navigator.py:2161` | `class SidebarController` |
| `StyleInjector` | class | `topogpt2_embeddings_navigator.py:189` | `class StyleInjector` |
| `ThemeTokens` | class | `topogpt2_embeddings_navigator.py:86` | `class ThemeTokens` |
| `ViewRegistry` | class | `topogpt2_embeddings_navigator.py:2145` | `class ViewRegistry` |
| `__init__` | method | `topogpt2_embeddings_navigator.py:192` | `def __init__(self, theme)` |
| `__init__` | method | `topogpt2_embeddings_navigator.py:266` | `def __init__(self, model, config, tokenizer, source_name)` |
| `__init__` | method | `topogpt2_embeddings_navigator.py:315` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_embeddings_navigator.py:525` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_embeddings_navigator.py:603` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_embeddings_navigator.py:1071` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_embeddings_navigator.py:1198` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_embeddings_navigator.py:1261` | `def __init__(self, ctx)` |
| `__init__` | method | `topogpt2_embeddings_navigator.py:2148` | `def __init__(self, context)` |
| `__init__` | method | `topogpt2_embeddings_navigator.py:2164` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_embeddings_navigator.py:2258` | `def __init__(self, config)` |
| `_berry_phases` | method | `topogpt2_embeddings_navigator.py:905` | `def _berry_phases(self, points)` |
| `_build_config` | method | `topogpt2_embeddings_navigator.py:391` | `def _build_config(self, topogpt2_module, embedded_cfg, state_dict)` |
| `_build_registry` | method | `topogpt2_embeddings_navigator.py:2380` | `def _build_registry(self, ctx)` |
| `_choose` | method | `topogpt2_embeddings_navigator.py:1378` | `def _choose(self, acts, selection)` |
| `_compute_all_metrics` | method | `topogpt2_embeddings_navigator.py:2351` | `def _compute_all_metrics(self, activations, knn)` |
| `_cosine_diag` | method | `topogpt2_embeddings_navigator.py:1962` | `def _cosine_diag(self, A, B)` |
| `_decode_pieces` | method | `topogpt2_embeddings_navigator.py:589` | `def _decode_pieces(tokenizer, ids)` |
| `_extract_payload` | method | `topogpt2_embeddings_navigator.py:374` | `def _extract_payload(self, obj)` |
| `_get_metrics` | method | `topogpt2_embeddings_navigator.py:1490` | `def _get_metrics(self, stage)` |
| `_gromov_delta` | method | `topogpt2_embeddings_navigator.py:759` | `def _gromov_delta(self, dist_geo)` |
| `_h0_from_mst` | method | `topogpt2_embeddings_navigator.py:810` | `def _h0_from_mst(self, edges, n)` |
| `_h1_from_edges` | method | `topogpt2_embeddings_navigator.py:845` | `def _h1_from_edges(self, edges, n)` |
| `_infer_config` | method | `topogpt2_embeddings_navigator.py:405` | `def _infer_config(self, topogpt2_module, state_dict)` |
| `_infer_d_model` | method | `topogpt2_embeddings_navigator.py:433` | `def _infer_d_model(state_dict)` |
| `_infer_max_seq_len` | method | `topogpt2_embeddings_navigator.py:467` | `def _infer_max_seq_len(state_dict)` |
| `_infer_n_heads` | method | `topogpt2_embeddings_navigator.py:450` | `def _infer_n_heads(state_dict, d_model)` |
| `_infer_n_kv_heads` | method | `topogpt2_embeddings_navigator.py:475` | `def _infer_n_kv_heads(state_dict, d_head, n_heads)` |
| `_infer_num_layers` | method | `topogpt2_embeddings_navigator.py:439` | `def _infer_num_layers(state_dict)` |
| `_infer_torus_grid` | method | `topogpt2_embeddings_navigator.py:505` | `def _infer_torus_grid(state_dict)` |
| `_isomap` | method | `topogpt2_embeddings_navigator.py:1123` | `def _isomap(self, points, n_components)` |
| `_kappa` | method | `topogpt2_embeddings_navigator.py:718` | `def _kappa(self, dist_eucl, dist_geo)` |
| `_lipschitz` | method | `topogpt2_embeddings_navigator.py:947` | `def _lipschitz(self, points)` |
| `_materialize` | method | `topogpt2_embeddings_navigator.py:366` | `def _materialize(self, source)` |
| `_pairwise` | method | `topogpt2_embeddings_navigator.py:675` | `def _pairwise(self, points)` |
| `_pca` | method | `topogpt2_embeddings_navigator.py:1105` | `def _pca(self, points, n_components)` |
| `_persistence` | method | `topogpt2_embeddings_navigator.py:783` | `def _persistence(self, points, dist_eucl)` |
| `_planar_winding` | method | `topogpt2_embeddings_navigator.py:936` | `def _planar_winding(self, xs, ys)` |
| `_points` | method | `topogpt2_embeddings_navigator.py:2021` | `def _points(self, stage)` |
| `_points` | method | `topogpt2_embeddings_navigator.py:2136` | `def _points(self, stage)` |
| `_random` | method | `topogpt2_embeddings_navigator.py:1171` | `def _random(self, points, n_components)` |
| `_read_state_dict` | method | `topogpt2_embeddings_navigator.py:344` | `def _read_state_dict(self, source)` |
| `_render_barcode` | method | `topogpt2_embeddings_navigator.py:1633` | `def _render_barcode(self, m)` |
| `_render_berry` | method | `topogpt2_embeddings_navigator.py:1688` | `def _render_berry(self, m, stage)` |
| `_render_card` | method | `topogpt2_embeddings_navigator.py:1496` | `def _render_card(self, m)` |
| `_render_coherence` | method | `topogpt2_embeddings_navigator.py:1911` | `def _render_coherence(self, points)` |
| `_render_component_norms` | method | `topogpt2_embeddings_navigator.py:2029` | `def _render_component_norms(self, comps)` |
| `_render_diagram` | method | `topogpt2_embeddings_navigator.py:1591` | `def _render_diagram(self, m)` |
| `_render_dynamics` | method | `topogpt2_embeddings_navigator.py:1807` | `def _render_dynamics(self, m)` |
| `_render_footer` | method | `topogpt2_embeddings_navigator.py:2408` | `def _render_footer(self)` |
| `_render_graph` | method | `topogpt2_embeddings_navigator.py:1864` | `def _render_graph(self, points, m)` |
| `_render_header` | method | `topogpt2_embeddings_navigator.py:2307` | `def _render_header(self)` |
| `_render_heatmap` | method | `topogpt2_embeddings_navigator.py:1968` | `def _render_heatmap(self, title, z, xlabels, tokens, diverging)` |
| `_render_kappa` | method | `topogpt2_embeddings_navigator.py:1521` | `def _render_kappa(self, m)` |
| `_render_landing` | method | `topogpt2_embeddings_navigator.py:2324` | `def _render_landing(self)` |
| `_render_layer_evolution` | method | `topogpt2_embeddings_navigator.py:1310` | `def _render_layer_evolution(self)` |
| `_render_lc` | method | `topogpt2_embeddings_navigator.py:1780` | `def _render_lc(self, m)` |
| `_render_meta` | method | `topogpt2_embeddings_navigator.py:2367` | `def _render_meta(self, bundle, activations, knn)` |
| `_render_path_metrics` | method | `topogpt2_embeddings_navigator.py:1544` | `def _render_path_metrics(self, m)` |
| `_render_quaternion_norms` | method | `topogpt2_embeddings_navigator.py:2054` | `def _render_quaternion_norms(self, comps)` |
| `_render_residual_streams` | method | `topogpt2_embeddings_navigator.py:1442` | `def _render_residual_streams(self, acts, method)` |
| `_render_sphere` | method | `topogpt2_embeddings_navigator.py:2070` | `def _render_sphere(self, comps)` |
| `_render_tabs` | method | `topogpt2_embeddings_navigator.py:2394` | `def _render_tabs(self, registry)` |
| `_render_tokens` | method | `topogpt2_embeddings_navigator.py:1284` | `def _render_tokens(self)` |
| `_render_trajectory` | method | `topogpt2_embeddings_navigator.py:1386` | `def _render_trajectory(self, emb, tokens, ids, norms, stage, method, info)` |
| `_render_winding` | method | `topogpt2_embeddings_navigator.py:1720` | `def _render_winding(self, m, stage)` |
| `_safe_pca3` | method | `topogpt2_embeddings_navigator.py:1017` | `def _safe_pca3(self, points)` |
| `_sanitize` | method | `topogpt2_embeddings_navigator.py:642` | `def _sanitize(self, points)` |
| `_shortest_paths` | method | `topogpt2_embeddings_navigator.py:678` | `def _shortest_paths(self, points, knn)` |
| `_sp_metrics` | method | `topogpt2_embeddings_navigator.py:698` | `def _sp_metrics(self, dist_eucl, dist_geo)` |
| `_spectral_properties` | method | `topogpt2_embeddings_navigator.py:1030` | `def _spectral_properties(self, points)` |
| `_sphere` | method | `topogpt2_embeddings_navigator.py:1181` | `def _sphere(self, points, n_components)` |
| `_stage_metrics` | method | `topogpt2_embeddings_navigator.py:1583` | `def _stage_metrics(self, stage)` |
| `_stage_metrics` | method | `topogpt2_embeddings_navigator.py:1680` | `def _stage_metrics(self, stage)` |
| `_stage_metrics` | method | `topogpt2_embeddings_navigator.py:1772` | `def _stage_metrics(self, stage)` |
| `_stage_metrics` | method | `topogpt2_embeddings_navigator.py:1849` | `def _stage_metrics(self, stage)` |
| `_stage_points` | method | `topogpt2_embeddings_navigator.py:1857` | `def _stage_points(self, stage)` |
| `_trajectory_geometry` | method | `topogpt2_embeddings_navigator.py:954` | `def _trajectory_geometry(self, points)` |
| `_trivial` | method | `topogpt2_embeddings_navigator.py:645` | `def _trivial(self, base)` |
| `_try_load_bundle` | method | `topogpt2_embeddings_navigator.py:2335` | `def _try_load_bundle(self, selections)` |
| `_umap` | method | `topogpt2_embeddings_navigator.py:1144` | `def _umap(self, points, n_components)` |
| `_validate_load` | method | `topogpt2_embeddings_navigator.py:514` | `def _validate_load(missing, unexpected)` |
| `_winding_numbers` | method | `topogpt2_embeddings_navigator.py:920` | `def _winding_numbers(self, points)` |
| `build` | method | `topogpt2_embeddings_navigator.py:2156` | `def build(self)` |
| `compute` | method | `topogpt2_embeddings_navigator.py:606` | `def compute(self, points, knn)` |
| `config` | method | `topogpt2_embeddings_navigator.py:284` | `def config(self)` |
| `ctx` | method | `topogpt2_embeddings_navigator.py:1265` | `def ctx(self)` |
| `device` | method | `topogpt2_embeddings_navigator.py:299` | `def device(self)` |
| `embedding_dim` | method | `topogpt2_embeddings_navigator.py:307` | `def embedding_dim(self)` |
| `find` | method | `topogpt2_embeddings_navigator.py:818` | `def find(x)` |
| `find` | method | `topogpt2_embeddings_navigator.py:864` | `def find(x)` |
| `hook` | method | `topogpt2_embeddings_navigator.py:561` | `def hook(_module, _inputs, output)` |
| `inject` | method | `topogpt2_embeddings_navigator.py:195` | `def inject(self)` |
| `load` | method | `topogpt2_embeddings_navigator.py:318` | `def load(self, source, topogpt2_module)` |
| `load` | method | `topogpt2_embeddings_navigator.py:2220` | `def load(self, path)` |
| `main` | method | `topogpt2_embeddings_navigator.py:2418` | `def main()` |
| `model` | method | `topogpt2_embeddings_navigator.py:279` | `def model(self)` |
| `num_layers` | method | `topogpt2_embeddings_navigator.py:303` | `def num_layers(self)` |
| `project` | method | `topogpt2_embeddings_navigator.py:1074` | `def project(self, points, method, n_components)` |
| `register` | method | `topogpt2_embeddings_navigator.py:2152` | `def register(self, factory)` |
| `render` | method | `topogpt2_embeddings_navigator.py:1270` | `def render(self)` |
| `render` | method | `topogpt2_embeddings_navigator.py:1280` | `def render(self)` |
| `render` | method | `topogpt2_embeddings_navigator.py:1358` | `def render(self)` |
| `render` | method | `topogpt2_embeddings_navigator.py:1481` | `def render(self)` |
| `render` | method | `topogpt2_embeddings_navigator.py:1575` | `def render(self)` |
| `render` | method | `topogpt2_embeddings_navigator.py:1672` | `def render(self)` |
| `render` | method | `topogpt2_embeddings_navigator.py:1764` | `def render(self)` |
| `render` | method | `topogpt2_embeddings_navigator.py:1840` | `def render(self)` |
| `render` | method | `topogpt2_embeddings_navigator.py:1939` | `def render(self)` |
| `render` | method | `topogpt2_embeddings_navigator.py:2000` | `def render(self)` |
| `render` | method | `topogpt2_embeddings_navigator.py:2114` | `def render(self)` |
| `render` | method | `topogpt2_embeddings_navigator.py:2167` | `def render(self)` |
| `run` | method | `topogpt2_embeddings_navigator.py:528` | `def run(self, bundle, text)` |
| `run` | method | `topogpt2_embeddings_navigator.py:2269` | `def run(self)` |
| `source_name` | method | `topogpt2_embeddings_navigator.py:294` | `def source_name(self)` |
| `style_2d` | method | `topogpt2_embeddings_navigator.py:1223` | `def style_2d(self, fig, title, height)` |
| `style_3d` | method | `topogpt2_embeddings_navigator.py:1201` | `def style_3d(self, fig, title, height)` |
| `tokenizer` | method | `topogpt2_embeddings_navigator.py:289` | `def tokenizer(self)` |
| `union` | method | `topogpt2_embeddings_navigator.py:824` | `def union(x, y)` |
| `union` | method | `topogpt2_embeddings_navigator.py:870` | `def union(x, y)` |
| `AttentionVisualizer` | class | `topogpt2_explorer.py:1773` | `class AttentionVisualizer(BaseVisualizer)` |
| `BaseVisualizer` | class | `topogpt2_explorer.py:904` | `class BaseVisualizer(ABC)` |
| `CheckpointLoader` | class | `topogpt2_explorer.py:337` | `class CheckpointLoader` |
| `ExplorerApp` | class | `topogpt2_explorer.py:2359` | `class ExplorerApp` |
| `ExplorerConfig` | class | `topogpt2_explorer.py:129` | `class ExplorerConfig` |
| `FigureStyler` | class | `topogpt2_explorer.py:836` | `class FigureStyler` |
| `GenerationLimits` | class | `topogpt2_explorer.py:120` | `class GenerationLimits` |
| `GlobalGeometryVisualizer` | class | `topogpt2_explorer.py:2151` | `class GlobalGeometryVisualizer(BaseVisualizer)` |
| `LayerEvolutionVisualizer` | class | `topogpt2_explorer.py:2061` | `class LayerEvolutionVisualizer(BaseVisualizer)` |
| `MetricCalculator` | class | `topogpt2_explorer.py:635` | `class MetricCalculator` |
| `MetricsConfig` | class | `topogpt2_explorer.py:108` | `class MetricsConfig` |
| `MoEVisualizer` | class | `topogpt2_explorer.py:1916` | `class MoEVisualizer(BaseVisualizer)` |
| `OverviewVisualizer` | class | `topogpt2_explorer.py:931` | `class OverviewVisualizer(BaseVisualizer)` |
| `PlotTheme` | class | `topogpt2_explorer.py:76` | `class PlotTheme` |
| `QuaternionDecompositionVisualizer` | class | `topogpt2_explorer.py:1227` | `class QuaternionDecompositionVisualizer(BaseVisualizer)` |
| `RenderContext` | class | `topogpt2_explorer.py:894` | `class RenderContext` |
| `SamplingLimits` | class | `topogpt2_explorer.py:91` | `class SamplingLimits` |
| `SidebarController` | class | `topogpt2_explorer.py:2316` | `class SidebarController` |
| `SpectralKernelVisualizer` | class | `topogpt2_explorer.py:1385` | `class SpectralKernelVisualizer(BaseVisualizer)` |
| `StyleInjector` | class | `topogpt2_explorer.py:168` | `class StyleInjector` |
| `TensorClassifier` | class | `topogpt2_explorer.py:244` | `class TensorClassifier` |
| `TensorExplorerVisualizer` | class | `topogpt2_explorer.py:999` | `class TensorExplorerVisualizer(BaseVisualizer)` |
| `TensorInventory` | class | `topogpt2_explorer.py:429` | `class TensorInventory` |
| `TensorProjector` | class | `topogpt2_explorer.py:515` | `class TensorProjector` |
| `ThemeTokens` | class | `topogpt2_explorer.py:59` | `class ThemeTokens` |
| `TorusTopologyVisualizer` | class | `topogpt2_explorer.py:1538` | `class TorusTopologyVisualizer(BaseVisualizer)` |
| `VisualizationContext` | class | `topogpt2_explorer.py:883` | `class VisualizationContext(Protocol)` |
| `VisualizerRegistry` | class | `topogpt2_explorer.py:2291` | `class VisualizerRegistry` |
| `__init__` | method | `topogpt2_explorer.py:171` | `def __init__(self, theme)` |
| `__init__` | method | `topogpt2_explorer.py:345` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_explorer.py:432` | `def __init__(self, tensors, classifier)` |
| `__init__` | method | `topogpt2_explorer.py:526` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_explorer.py:643` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_explorer.py:839` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_explorer.py:914` | `def __init__(self, context)` |
| `__init__` | method | `topogpt2_explorer.py:2294` | `def __init__(self, context)` |
| `__init__` | method | `topogpt2_explorer.py:2319` | `def __init__(self, config)` |
| `__init__` | method | `topogpt2_explorer.py:2362` | `def __init__(self, config)` |
| `_add_edges` | method | `topogpt2_explorer.py:1631` | `def _add_edges(self, fig, positions, radial_bins, angular_bins, edges)` |
| `_add_nodes` | method | `topogpt2_explorer.py:1697` | `def _add_nodes(self, fig, positions, node_colors, n_nodes)` |
| `_build_css` | method | `topogpt2_explorer.py:174` | `def _build_css(self)` |
| `_build_palette` | method | `topogpt2_explorer.py:2279` | `def _build_palette(n)` |
| `_build_registry` | method | `topogpt2_explorer.py:2452` | `def _build_registry(self, context)` |
| `_build_segments` | method | `topogpt2_explorer.py:1678` | `def _build_segments(positions, radial_bins, angular_bins)` |
| `_classify_role` | method | `topogpt2_explorer.py:286` | `def _classify_role(self, name)` |
| `_configure_page` | method | `topogpt2_explorer.py:2394` | `def _configure_page(self)` |
| `_edge_label` | method | `topogpt2_explorer.py:1669` | `def _edge_label(edge_type)` |
| `_effective_rank_from_svd` | method | `topogpt2_explorer.py:690` | `def _effective_rank_from_svd(self, svd_values, shape)` |
| `_extract_layer` | method | `topogpt2_explorer.py:328` | `def _extract_layer(self, name)` |
| `_extract_quaternion_component` | method | `topogpt2_explorer.py:332` | `def _extract_quaternion_component(self, name)` |
| `_extract_state_dict` | method | `topogpt2_explorer.py:399` | `def _extract_state_dict(self, obj)` |
| `_group_quaternion_bundles` | method | `topogpt2_explorer.py:1249` | `def _group_quaternion_bundles(self)` |
| `_infer_grid` | method | `topogpt2_explorer.py:1568` | `def _infer_grid(self, n_nodes)` |
| `_infer_head_count` | method | `topogpt2_explorer.py:1813` | `def _infer_head_count(self, matrix, proj)` |
| `_load_safetensors` | method | `topogpt2_explorer.py:382` | `def _load_safetensors(self, buffer)` |
| `_load_torch` | method | `topogpt2_explorer.py:389` | `def _load_torch(self, buffer)` |
| `_looks_like_state_dict` | method | `topogpt2_explorer.py:413` | `def _looks_like_state_dict(obj)` |
| `_materialize` | method | `topogpt2_explorer.py:373` | `def _materialize(self, source)` |
| `_pair_kr_ki` | method | `topogpt2_explorer.py:1413` | `def _pair_kr_ki(self)` |
| `_participation_from_svd` | method | `topogpt2_explorer.py:707` | `def _participation_from_svd(self, svd_values, shape)` |
| `_pca_3d` | method | `topogpt2_explorer.py:606` | `def _pca_3d(self, matrix)` |
| `_quaternion_bundle_key` | method | `topogpt2_explorer.py:1263` | `def _quaternion_bundle_key(name, component)` |
| `_random_3d` | method | `topogpt2_explorer.py:617` | `def _random_3d(self, matrix)` |
| `_render_3d_torus` | method | `topogpt2_explorer.py:1591` | `def _render_3d_torus(self, nodes, edges, radial_bins, angular_bins)` |
| `_render_complex_scatter` | method | `topogpt2_explorer.py:1470` | `def _render_complex_scatter(self, complex_kernel, key)` |
| `_render_component_heatmaps` | method | `topogpt2_explorer.py:1290` | `def _render_component_heatmaps(self, components)` |
| `_render_component_spectra` | method | `topogpt2_explorer.py:1315` | `def _render_component_spectra(self, components)` |
| `_render_component_stats` | method | `topogpt2_explorer.py:1278` | `def _render_component_stats(self, components)` |
| `_render_distribution` | method | `topogpt2_explorer.py:1125` | `def _render_distribution(self, matrix, name)` |
| `_render_edge_quaternions` | method | `topogpt2_explorer.py:1747` | `def _render_edge_quaternions(self, edges)` |
| `_render_expert_similarity` | method | `topogpt2_explorer.py:2015` | `def _render_expert_similarity(self, layer)` |
| `_render_feature_correlation` | method | `topogpt2_explorer.py:2246` | `def _render_feature_correlation(self, X_std, example)` |
| `_render_footer` | method | `topogpt2_explorer.py:2483` | `def _render_footer(self)` |
| `_render_head_similarity` | method | `topogpt2_explorer.py:1881` | `def _render_head_similarity(self, matrix, proj, layer)` |
| `_render_header` | method | `topogpt2_explorer.py:2401` | `def _render_header(self)` |
| `_render_headline` | method | `topogpt2_explorer.py:950` | `def _render_headline(self, total_params, num_tensors, num_layers)` |
| `_render_headline_metrics` | method | `topogpt2_explorer.py:1578` | `def _render_headline_metrics(self, nodes, edges, radial_bins, angular_bins)` |
| `_render_heatmap` | method | `topogpt2_explorer.py:1103` | `def _render_heatmap(self, matrix, name)` |
| `_render_inventory_table` | method | `topogpt2_explorer.py:984` | `def _render_inventory_table(self, rows)` |
| `_render_landing` | method | `topogpt2_explorer.py:2416` | `def _render_landing(self)` |
| `_render_magnitude_phase` | method | `topogpt2_explorer.py:1439` | `def _render_magnitude_phase(self, magnitude, phase, key)` |
| `_render_meta` | method | `topogpt2_explorer.py:1042` | `def _render_meta(self, meta)` |
| `_render_metric_grid` | method | `topogpt2_explorer.py:1050` | `def _render_metric_grid(self, metrics)` |
| `_render_metric_grid` | method | `topogpt2_explorer.py:2113` | `def _render_metric_grid(self, role, layers, series)` |
| `_render_node_correlation` | method | `topogpt2_explorer.py:1725` | `def _render_node_correlation(self, nodes)` |
| `_render_per_head_norms` | method | `topogpt2_explorer.py:1822` | `def _render_per_head_norms(self, matrix, proj)` |
| `_render_per_head_spectrum` | method | `topogpt2_explorer.py:1849` | `def _render_per_head_spectrum(self, matrix, proj, layer)` |
| `_render_point_cloud` | method | `topogpt2_explorer.py:1069` | `def _render_point_cloud(self, matrix, name, method)` |
| `_render_radial_profile` | method | `topogpt2_explorer.py:1504` | `def _render_radial_profile(self, magnitude, key)` |
| `_render_role_breakdown` | method | `topogpt2_explorer.py:957` | `def _render_role_breakdown(self, role_counts, role_params)` |
| `_render_router_norms` | method | `topogpt2_explorer.py:1949` | `def _render_router_norms(self, router, layer)` |
| `_render_routing_probe` | method | `topogpt2_explorer.py:1972` | `def _render_routing_probe(self, router, layer)` |
| `_render_scatter` | method | `topogpt2_explorer.py:2204` | `def _render_scatter(self, emb, labels, roles, sizes, pca)` |
| `_render_singular_spectrum` | method | `topogpt2_explorer.py:1180` | `def _render_singular_spectrum(self, matrix, name)` |
| `_render_spectrum` | method | `topogpt2_explorer.py:1149` | `def _render_spectrum(self, matrix, name)` |
| `_render_summary_metrics` | method | `topogpt2_explorer.py:1908` | `def _render_summary_metrics(self, metrics)` |
| `_render_tabs` | method | `topogpt2_explorer.py:2465` | `def _render_tabs(self, registry)` |
| `_render_unit_norm_distribution` | method | `topogpt2_explorer.py:1346` | `def _render_unit_norm_distribution(self, components)` |
| `_reshape_to_2d` | method | `topogpt2_explorer.py:1428` | `def _reshape_to_2d(self, magnitude, phase)` |
| `_resolve_checkpoint` | method | `topogpt2_explorer.py:2437` | `def _resolve_checkpoint(self, selections)` |
| `_softmax` | method | `topogpt2_explorer.py:2055` | `def _softmax(logits)` |
| `_subsample_for_pca` | method | `topogpt2_explorer.py:830` | `def _subsample_for_pca(self, matrix)` |
| `_subsample_for_svd` | method | `topogpt2_explorer.py:824` | `def _subsample_for_svd(self, matrix)` |
| `_svd_safe` | method | `topogpt2_explorer.py:681` | `def _svd_safe(self, matrix)` |
| `_to_cpu_float32` | method | `topogpt2_explorer.py:420` | `def _to_cpu_float32(tensor)` |
| `_torus_positions` | method | `topogpt2_explorer.py:1605` | `def _torus_positions(self, nodes, radial_bins, angular_bins)` |
| `applicable` | method | `topogpt2_explorer.py:2311` | `def applicable(self)` |
| `build` | method | `topogpt2_explorer.py:2307` | `def build(self)` |
| `classify` | method | `topogpt2_explorer.py:258` | `def classify(self, name, shape)` |
| `coherence` | method | `topogpt2_explorer.py:781` | `def coherence(self, matrix)` |
| `compute_all` | method | `topogpt2_explorer.py:649` | `def compute_all(self, matrix)` |
| `ctx` | method | `topogpt2_explorer.py:918` | `def ctx(self)` |
| `dominant_frequency` | method | `topogpt2_explorer.py:814` | `def dominant_frequency(self, matrix)` |
| `effective_rank` | method | `topogpt2_explorer.py:748` | `def effective_rank(self, matrix)` |
| `entropy` | method | `topogpt2_explorer.py:727` | `def entropy(self, matrix)` |
| `filter` | method | `topogpt2_explorer.py:464` | `def filter(self, role, layer, component, spectral_only)` |
| `fractal_dimension` | method | `topogpt2_explorer.py:762` | `def fractal_dimension(self, matrix)` |
| `inject` | method | `topogpt2_explorer.py:239` | `def inject(self)` |
| `is_applicable` | method | `topogpt2_explorer.py:922` | `def is_applicable(self)` |
| `is_applicable` | method | `topogpt2_explorer.py:1233` | `def is_applicable(self)` |
| `is_applicable` | method | `topogpt2_explorer.py:1391` | `def is_applicable(self)` |
| `is_applicable` | method | `topogpt2_explorer.py:1544` | `def is_applicable(self)` |
| `is_applicable` | method | `topogpt2_explorer.py:1779` | `def is_applicable(self)` |
| `is_applicable` | method | `topogpt2_explorer.py:1922` | `def is_applicable(self)` |
| `is_applicable` | method | `topogpt2_explorer.py:2067` | `def is_applicable(self)` |
| `layers` | method | `topogpt2_explorer.py:455` | `def layers(self)` |
| `load` | method | `topogpt2_explorer.py:348` | `def load(self, source)` |
| `main` | method | `topogpt2_explorer.py:2493` | `def main()` |
| `meta` | method | `topogpt2_explorer.py:451` | `def meta(self, name)` |
| `names` | method | `topogpt2_explorer.py:443` | `def names(self)` |
| `participation_ratio` | method | `topogpt2_explorer.py:753` | `def participation_ratio(self, matrix)` |
| `project_3d` | method | `topogpt2_explorer.py:575` | `def project_3d(self, matrix, method)` |
| `register` | method | `topogpt2_explorer.py:2298` | `def register(self, factory)` |
| `render` | method | `topogpt2_explorer.py:927` | `def render(self)` |
| `render` | method | `topogpt2_explorer.py:937` | `def render(self)` |
| `render` | method | `topogpt2_explorer.py:1005` | `def render(self)` |
| `render` | method | `topogpt2_explorer.py:1237` | `def render(self)` |
| `render` | method | `topogpt2_explorer.py:1397` | `def render(self)` |
| `render` | method | `topogpt2_explorer.py:1547` | `def render(self)` |
| `render` | method | `topogpt2_explorer.py:1785` | `def render(self)` |
| `render` | method | `topogpt2_explorer.py:1927` | `def render(self)` |
| `render` | method | `topogpt2_explorer.py:2070` | `def render(self)` |
| `render` | method | `topogpt2_explorer.py:2157` | `def render(self)` |
| `render` | method | `topogpt2_explorer.py:2322` | `def render(self)` |
| `roles` | method | `topogpt2_explorer.py:460` | `def roles(self)` |
| `run` | method | `topogpt2_explorer.py:2372` | `def run(self)` |
| `sparsity` | method | `topogpt2_explorer.py:720` | `def sparsity(self, matrix, threshold)` |
| `spectral_flatness` | method | `topogpt2_explorer.py:796` | `def spectral_flatness(self, matrix)` |
| `style_2d` | method | `topogpt2_explorer.py:864` | `def style_2d(self, fig, title, height)` |
| `style_3d` | method | `topogpt2_explorer.py:842` | `def style_3d(self, fig, title)` |
| `subsample` | method | `topogpt2_explorer.py:553` | `def subsample(self, matrix, max_rows, max_cols, seed)` |
| `summary_rows` | method | `topogpt2_explorer.py:489` | `def summary_rows(self)` |
| `tensor` | method | `topogpt2_explorer.py:447` | `def tensor(self, name)` |
| `to_matrix` | method | `topogpt2_explorer.py:531` | `def to_matrix(self, tensor)` |
| `total_parameters` | method | `topogpt2_explorer.py:485` | `def total_parameters(self)` |
| `CheckpointReader` | class | `topogpt2_grid_scaler.py:205` | `class CheckpointReader` |
| `CheckpointSaver` | class | `topogpt2_grid_scaler.py:751` | `class CheckpointSaver` |
| `ConfigReconstructor` | class | `topogpt2_grid_scaler.py:242` | `class ConfigReconstructor` |
| `InterpolationConfig` | class | `topogpt2_grid_scaler.py:97` | `class InterpolationConfig` |
| `ModelAssembler` | class | `topogpt2_grid_scaler.py:723` | `class ModelAssembler` |
| `ModuleImporter` | class | `topogpt2_grid_scaler.py:181` | `class ModuleImporter` |
| `OutputConfig` | class | `topogpt2_grid_scaler.py:131` | `class OutputConfig` |
| `ProgressiveConfig` | class | `topogpt2_grid_scaler.py:121` | `class ProgressiveConfig` |
| `ScalingValidator` | class | `topogpt2_grid_scaler.py:635` | `class ScalingValidator` |
| `SpectralInterpolator` | class | `topogpt2_grid_scaler.py:380` | `class SpectralInterpolator` |
| `StateScaler` | class | `topogpt2_grid_scaler.py:483` | `class StateScaler` |
| `TensorRole` | class | `topogpt2_grid_scaler.py:328` | `class TensorRole` |
| `TopoGPT2DModelScaler` | class | `topogpt2_grid_scaler.py:860` | `class TopoGPT2DModelScaler` |
| `TopoScalerConfig` | class | `topogpt2_grid_scaler.py:141` | `class TopoScalerConfig` |
| `ValidationConfig` | class | `topogpt2_grid_scaler.py:108` | `class ValidationConfig` |
| `__init__` | method | `topogpt2_grid_scaler.py:388` | `def __init__(self, cfg)` |
| `__init__` | method | `topogpt2_grid_scaler.py:499` | `def __init__(self, interp, role_clf, logger)` |
| `__init__` | method | `topogpt2_grid_scaler.py:638` | `def __init__(self, cfg)` |
| `__init__` | method | `topogpt2_grid_scaler.py:872` | `def __init__(self, cfg)` |
| `__post_init__` | method | `topogpt2_grid_scaler.py:159` | `def __post_init__(self)` |
| `_bilinear_fallback` | method | `topogpt2_grid_scaler.py:626` | `def _bilinear_fallback(self, src, tgt_shape)` |
| `_build_target_config` | method | `topogpt2_grid_scaler.py:1001` | `def _build_target_config(self, mod, src_cfg, tgt_d)` |
| `_cfg_dict` | method | `topogpt2_grid_scaler.py:770` | `def _cfg_dict(c)` |
| `_dispatch` | method | `topogpt2_grid_scaler.py:567` | `def _dispatch(self, src, tgt_shape, role, key)` |
| `_extract` | method | `topogpt2_grid_scaler.py:225` | `def _extract(self, obj)` |
| `_infer` | method | `topogpt2_grid_scaler.py:259` | `def _infer(self, mod, sd)` |
| `_infer_d_head` | method | `topogpt2_grid_scaler.py:291` | `def _infer_d_head(sd)` |
| `_infer_max_seq` | method | `topogpt2_grid_scaler.py:308` | `def _infer_max_seq(sd)` |
| `_infer_n_heads` | method | `topogpt2_grid_scaler.py:1018` | `def _infer_n_heads(tgt_d, src_n_heads)` |
| `_infer_n_kv` | method | `topogpt2_grid_scaler.py:298` | `def _infer_n_kv(sd, d_head, n_heads)` |
| `_infer_n_kv_heads` | method | `topogpt2_grid_scaler.py:1033` | `def _infer_n_kv_heads(tgt_d, tgt_n_heads, src_n_heads, src_n_kv)` |
| `_infer_torus` | method | `topogpt2_grid_scaler.py:315` | `def _infer_torus(sd)` |
| `_phase_coherence` | method | `topogpt2_grid_scaler.py:708` | `def _phase_coherence(self, sd)` |
| `_print_summary` | method | `topogpt2_grid_scaler.py:1047` | `def _print_summary(self, results, src_cfg)` |
| `_resize_spectrum_2d` | method | `topogpt2_grid_scaler.py:452` | `def _resize_spectrum_2d(self, W_f, tgt_rows, tgt_cols)` |
| `_scale_spectral_2d_to` | method | `topogpt2_grid_scaler.py:598` | `def _scale_spectral_2d_to(self, t, tgt_shape, key)` |
| `_setup_logger` | method | `topogpt2_grid_scaler.py:169` | `def _setup_logger(name, level)` |
| `_spectral_concentration` | method | `topogpt2_grid_scaler.py:690` | `def _spectral_concentration(self, sd)` |
| `_write_report` | method | `topogpt2_grid_scaler.py:815` | `def _write_report(self, path, src_cfg, tgt_cfg, before, after, ckpt)` |
| `assemble` | method | `topogpt2_grid_scaler.py:726` | `def assemble(self, mod, tgt_cfg, scaled_state, logger)` |
| `build_parser` | method | `topogpt2_grid_scaler.py:1070` | `def build_parser()` |
| `check_degradation` | method | `topogpt2_grid_scaler.py:656` | `def check_degradation(self, before, after, logger)` |
| `classify` | method | `topogpt2_grid_scaler.py:340` | `def classify(self, key, shape)` |
| `compute` | method | `topogpt2_grid_scaler.py:641` | `def compute(self, state, d_model)` |
| `config_from_args` | method | `topogpt2_grid_scaler.py:1097` | `def config_from_args(args)` |
| `interpolate_1d` | method | `topogpt2_grid_scaler.py:421` | `def interpolate_1d(self, v, tgt_len)` |
| `interpolate_2d` | method | `topogpt2_grid_scaler.py:391` | `def interpolate_2d(self, W, tgt_rows, tgt_cols)` |
| `load` | method | `topogpt2_grid_scaler.py:184` | `def load(self, path)` |
| `main` | method | `topogpt2_grid_scaler.py:1119` | `def main()` |
| `read` | method | `topogpt2_grid_scaler.py:208` | `def read(self, path, device)` |
| `reconstruct` | method | `topogpt2_grid_scaler.py:245` | `def reconstruct(self, mod, state_dict, embedded)` |
| `run` | method | `topogpt2_grid_scaler.py:888` | `def run(self)` |
| `save` | method | `topogpt2_grid_scaler.py:754` | `def save(self, model, tgt_cfg, src_cfg, metrics_before, metrics_after, out_cfg, step_tag, logger)` |
| `scale` | method | `topogpt2_grid_scaler.py:509` | `def scale(self, src_state, src_cfg, tgt_cfg, mod)` |
| `CheckpointDiscovery` | class | `topogpt2_multi_inference.py:122` | `class CheckpointDiscovery` |
| `CheckpointLoader` | class | `topogpt2_multi_inference.py:164` | `class CheckpointLoader` |
| `ConfigReconstructor` | class | `topogpt2_multi_inference.py:219` | `class ConfigReconstructor` |
| `GenerationEngine` | class | `topogpt2_multi_inference.py:327` | `class GenerationEngine` |
| `JsonExporter` | class | `topogpt2_multi_inference.py:677` | `class JsonExporter` |
| `ModelResult` | class | `topogpt2_multi_inference.py:433` | `class ModelResult` |
| `ModuleImporter` | class | `topogpt2_multi_inference.py:95` | `class ModuleImporter` |
| `MultiInferenceRunner` | class | `topogpt2_multi_inference.py:450` | `class MultiInferenceRunner` |
| `ResultRenderer` | class | `topogpt2_multi_inference.py:584` | `class ResultRenderer` |
| `RunConfig` | class | `topogpt2_multi_inference.py:72` | `class RunConfig` |
| `SamplingConfig` | class | `topogpt2_multi_inference.py:60` | `class SamplingConfig` |
| `TokenizerFactory` | class | `topogpt2_multi_inference.py:315` | `class TokenizerFactory` |
| `__init__` | method | `topogpt2_multi_inference.py:330` | `def __init__(self, cfg, device)` |
| `__init__` | method | `topogpt2_multi_inference.py:453` | `def __init__(self, cfg)` |
| `_apply_repetition_penalty` | method | `topogpt2_multi_inference.py:412` | `def _apply_repetition_penalty(logits, generated, penalty)` |
| `_apply_top_p` | method | `topogpt2_multi_inference.py:424` | `def _apply_top_p(logits, p)` |
| `_fast_generate` | method | `topogpt2_multi_inference.py:361` | `def _fast_generate(self, model, input_ids)` |
| `_fmt_params` | method | `topogpt2_multi_inference.py:666` | `def _fmt_params(n)` |
| `_infer` | method | `topogpt2_multi_inference.py:243` | `def _infer(self, mod, sd)` |
| `_infer_d_head` | method | `topogpt2_multi_inference.py:278` | `def _infer_d_head(sd)` |
| `_infer_max_seq` | method | `topogpt2_multi_inference.py:295` | `def _infer_max_seq(sd)` |
| `_infer_n_kv` | method | `topogpt2_multi_inference.py:285` | `def _infer_n_kv(sd, d_head, n_heads)` |
| `_infer_torus` | method | `topogpt2_multi_inference.py:302` | `def _infer_torus(sd)` |
| `_load_safetensors` | method | `topogpt2_multi_inference.py:183` | `def _load_safetensors(self, path, device)` |
| `_load_torch` | method | `topogpt2_multi_inference.py:191` | `def _load_torch(self, path, device)` |
| `_make_label` | method | `topogpt2_multi_inference.py:570` | `def _make_label(path)` |
| `_manual_generate` | method | `topogpt2_multi_inference.py:372` | `def _manual_generate(self, model, input_ids)` |
| `_print_comparison_table` | method | `topogpt2_multi_inference.py:628` | `def _print_comparison_table(self, results)` |
| `_print_model_output` | method | `topogpt2_multi_inference.py:605` | `def _print_model_output(self, r)` |
| `_print_prompt_header` | method | `topogpt2_multi_inference.py:597` | `def _print_prompt_header(self, prompt)` |
| `_run_one` | method | `topogpt2_multi_inference.py:499` | `def _run_one(self, ckpt_path, mod, tokenizer, engine)` |
| `_setup_logger` | method | `topogpt2_multi_inference.py:85` | `def _setup_logger(name, level)` |
| `build_parser` | method | `topogpt2_multi_inference.py:707` | `def build_parser()` |
| `config_from_args` | method | `topogpt2_multi_inference.py:780` | `def config_from_args(args)` |
| `export` | method | `topogpt2_multi_inference.py:680` | `def export(self, results, path, prompt)` |
| `generate` | method | `topogpt2_multi_inference.py:334` | `def generate(self, model, tokenizer, prompt)` |
| `get` | method | `topogpt2_multi_inference.py:320` | `def get(self, mod)` |
| `load` | method | `topogpt2_multi_inference.py:100` | `def load(self, path)` |
| `load` | method | `topogpt2_multi_inference.py:167` | `def load(self, path, device)` |
| `main` | method | `topogpt2_multi_inference.py:800` | `def main()` |
| `reconstruct` | method | `topogpt2_multi_inference.py:222` | `def reconstruct(self, mod, state_dict, embedded)` |
| `render` | method | `topogpt2_multi_inference.py:590` | `def render(self, results, prompt)` |
| `resolve` | method | `topogpt2_multi_inference.py:127` | `def resolve(self, sources)` |
| `run` | method | `topogpt2_multi_inference.py:462` | `def run(self)` |
| `CheckpointArch` | class | `zeroshot.py:1216` | `class CheckpointArch` |
| `CheckpointArchProber` | class | `zeroshot.py:1239` | `class CheckpointArchProber` |
| `CheckpointIO` | class | `zeroshot.py:1120` | `class CheckpointIO` |
| `ExpansionConfig` | class | `zeroshot.py:87` | `class ExpansionConfig` |
| `ExpansionValidator` | class | `zeroshot.py:1463` | `class ExpansionValidator` |
| `MultiHeadAttention` | class | `zeroshot.py:665` | `class MultiHeadAttention(Module)` |
| `NodeEmbedInterpolator` | class | `zeroshot.py:876` | `class NodeEmbedInterpolator` |
| `QuaternionLinear` | class | `zeroshot.py:287` | `class QuaternionLinear(Module)` |
| `QuaternionOps` | class | `zeroshot.py:254` | `class QuaternionOps` |
| `QuaternionSpectralLayer` | class | `zeroshot.py:321` | `class QuaternionSpectralLayer(Module)` |
| `QuaternionTorusBrain` | class | `zeroshot.py:427` | `class QuaternionTorusBrain(Module)` |
| `RMSNorm` | class | `zeroshot.py:652` | `class RMSNorm(Module)` |
| `RotaryEmbedding` | class | `zeroshot.py:613` | `class RotaryEmbedding(Module)` |
| `SpectralAutoencoder` | class | `zeroshot.py:373` | `class SpectralAutoencoder(Module)` |
| `SpectralKernelInterpolator` | class | `zeroshot.py:828` | `class SpectralKernelInterpolator` |
| `SwiGLU` | class | `zeroshot.py:534` | `class SwiGLU(Module)` |
| `TopoGPT2` | class | `zeroshot.py:749` | `class TopoGPT2(Module)` |
| `TopoGPT2Config` | class | `zeroshot.py:169` | `class TopoGPT2Config` |
| `TopoGPT2Expander` | class | `zeroshot.py:1052` | `class TopoGPT2Expander` |
| `TopoGPT2Layer` | class | `zeroshot.py:719` | `class TopoGPT2Layer(Module)` |
| `TopoMoEBrain` | class | `zeroshot.py:556` | `class TopoMoEBrain(Module)` |
| `TopoMoEBrainExpander` | class | `zeroshot.py:1009` | `class TopoMoEBrainExpander` |
| `TorusBrainExpander` | class | `zeroshot.py:917` | `class TorusBrainExpander` |
| `ZeroShotExpansionPipeline` | class | `zeroshot.py:1550` | `class ZeroShotExpansionPipeline` |
| `__init__` | method | `zeroshot.py:296` | `def __init__(self, in_features, out_features, bias)` |
| `__init__` | method | `zeroshot.py:329` | `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)` |
| `__init__` | method | `zeroshot.py:382` | `def __init__(self, config)` |
| `__init__` | method | `zeroshot.py:443` | `def __init__(self, d_model, config)` |
| `__init__` | method | `zeroshot.py:540` | `def __init__(self, d_model, expansion, dropout)` |
| `__init__` | method | `zeroshot.py:565` | `def __init__(self, d_model, config)` |
| `__init__` | method | `zeroshot.py:618` | `def __init__(self, d_head, max_seq_len)` |
| `__init__` | method | `zeroshot.py:655` | `def __init__(self, d_model, eps)` |
| `__init__` | method | `zeroshot.py:671` | `def __init__(self, d_model, n_heads, config)` |
| `__init__` | method | `zeroshot.py:725` | `def __init__(self, d_model, n_heads, config)` |
| `__init__` | method | `zeroshot.py:757` | `def __init__(self, config)` |
| `__init__` | method | `zeroshot.py:837` | `def __init__(self, mode)` |
| `__init__` | method | `zeroshot.py:886` | `def __init__(self, mode)` |
| `__init__` | method | `zeroshot.py:936` | `def __init__(self, spec_interp_mode, node_interp_mode, logger)` |
| `__init__` | method | `zeroshot.py:1018` | `def __init__(self, spec_interp_mode, node_interp_mode, logger)` |
| `__init__` | method | `zeroshot.py:1072` | `def __init__(self, spec_interp_mode, node_interp_mode, logger)` |
| `__init__` | method | `zeroshot.py:1126` | `def __init__(self, logger)` |
| `__init__` | method | `zeroshot.py:1286` | `def __init__(self, logger)` |
| `__init__` | method | `zeroshot.py:1474` | `def __init__(self, logger)` |
| `__init__` | method | `zeroshot.py:1565` | `def __init__(self, exp_cfg, logger)` |
| `__post_init__` | method | `zeroshot.py:222` | `def __post_init__(self)` |
| `_build_cache` | method | `zeroshot.py:626` | `def _build_cache(self, seq_len)` |
| `_build_metadata_for_save` | method | `zeroshot.py:1609` | `def _build_metadata_for_save(self, src_meta, arch, tgt_radial, tgt_angular)` |
| `_build_torus_graph` | method | `zeroshot.py:468` | `def _build_torus_graph(self)` |
| `_config_from_arch` | method | `zeroshot.py:1570` | `def _config_from_arch(self, arch, torus_radial, torus_angular)` |
| `_contract` | method | `zeroshot.py:347` | `def _contract(self, W, X)` |
| `_filter1d` | method | `zeroshot.py:404` | `def _filter1d(self, x, kr, ki)` |
| `_forward_impl` | method | `zeroshot.py:734` | `def _forward_impl(self, x, past_kv)` |
| `_infer_d_head_fallback` | method | `zeroshot.py:1433` | `def _infer_d_head_fallback(d_model, q_out, k_out)` |
| `_init_weights` | method | `zeroshot.py:771` | `def _init_weights(self)` |
| `_interp2d` | method | `zeroshot.py:840` | `def _interp2d(self, tensor, tgt_h, tgt_w)` |
| `_kernel` | method | `zeroshot.py:344` | `def _kernel(self, c)` |
| `_load_metadata` | method | `zeroshot.py:1304` | `def _load_metadata(self, path)` |
| `_load_shapes` | method | `zeroshot.py:1289` | `def _load_shapes(self, path)` |
| `_message_passing` | method | `zeroshot.py:495` | `def _message_passing(self, node_feat)` |
| `_rotate_half` | method | `zeroshot.py:633` | `def _rotate_half(x)` |
| `_route` | method | `zeroshot.py:581` | `def _route(self, x)` |
| `_torus_soft_assign` | method | `zeroshot.py:484` | `def _torus_soft_assign(self, phi1, phi2)` |
| `build_arg_parser` | method | `zeroshot.py:1709` | `def build_arg_parser()` |
| `build_logger` | function | `zeroshot.py:69` | `def build_logger(name, level)` |
| `conjugate` | method | `zeroshot.py:273` | `def conjugate(q)` |
| `decode` | method | `zeroshot.py:412` | `def decode(self, z)` |
| `encode` | method | `zeroshot.py:409` | `def encode(self, x)` |
| `expand` | method | `zeroshot.py:946` | `def expand(self, src, tgt)` |
| `expand` | method | `zeroshot.py:1031` | `def expand(self, src, tgt)` |
| `expand` | method | `zeroshot.py:1085` | `def expand(self, src, tgt)` |
| `forward` | method | `zeroshot.py:310` | `def forward(self, x)` |
| `forward` | method | `zeroshot.py:350` | `def forward(self, x)` |
| `forward` | method | `zeroshot.py:415` | `def forward(self, x)` |
| `forward` | method | `zeroshot.py:509` | `def forward(self, x)` |
| `forward` | method | `zeroshot.py:552` | `def forward(self, x)` |
| `forward` | method | `zeroshot.py:604` | `def forward(self, x)` |
| `forward` | method | `zeroshot.py:637` | `def forward(self, q, k, seq_len, offset)` |
| `forward` | method | `zeroshot.py:660` | `def forward(self, x)` |
| `forward` | method | `zeroshot.py:686` | `def forward(self, x, is_causal, past_kv)` |
| `forward` | method | `zeroshot.py:743` | `def forward(self, x, past_kv)` |
| `forward` | method | `zeroshot.py:778` | `def forward(self, token_ids, past_kvs)` |
| `generate` | method | `zeroshot.py:795` | `def generate(self, token_ids, max_new_tokens, temperature, top_k)` |
| `hamilton_product` | method | `zeroshot.py:258` | `def hamilton_product(q1, q2)` |
| `load` | method | `zeroshot.py:1133` | `def load(self, path, model, device)` |
| `main` | method | `zeroshot.py:1774` | `def main()` |
| `normalize` | method | `zeroshot.py:269` | `def normalize(q, eps)` |
| `probe` | method | `zeroshot.py:1315` | `def probe(self, path, fallback_radial, fallback_angular)` |
| `process_torus_grid` | method | `zeroshot.py:420` | `def process_torus_grid(self, grid)` |
| `rotate_vector` | method | `zeroshot.py:278` | `def rotate_vector(v, q)` |
| `run` | method | `zeroshot.py:1631` | `def run(self)` |
| `save` | method | `zeroshot.py:1177` | `def save(self, path, model, metadata)` |
| `src_nodes` | method | `zeroshot.py:154` | `def src_nodes(self)` |
| `tgt_nodes` | method | `zeroshot.py:158` | `def tgt_nodes(self)` |
| `transfer` | method | `zeroshot.py:856` | `def transfer(self, src_layer, tgt_layer)` |
| `transfer` | method | `zeroshot.py:889` | `def transfer(self, src_embed, src_radial, src_angular, tgt_embed, tgt_radial, tgt_angular)` |
| `validate` | method | `zeroshot.py:1477` | `def validate(self, model, prompt)` |
| `validate_geometry` | method | `zeroshot.py:140` | `def validate_geometry(self)` |
