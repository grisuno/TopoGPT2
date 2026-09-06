# API

## app.py

### setup_logger `def setup_logger(name, level)`
- Defined: `app.py:155`

### set_seed `def set_seed(seed, device)`
- Defined: `app.py:165`

### main `def main()`
- Defined: `app.py:2506`

### __post_init__ `def __post_init__(self)`
- Defined: `app.py:124`

### hamilton_product `def hamilton_product(q1, q2)`
- Defined: `app.py:185`
- Doc: Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].

### normalize `def normalize(q, eps)`
- Defined: `app.py:197`

### conjugate `def conjugate(q)`
- Defined: `app.py:201`

### rotate_vector `def rotate_vector(v, q)`
- Defined: `app.py:206`
- Doc: Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]

### __init__ `def __init__(self, in_features, out_features, bias)`
- Defined: `app.py:228`

### forward `def forward(self, x)`
- Defined: `app.py:244`
- Doc: x: [..., in_features] → [..., out_features]

### __init__ `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- Defined: `app.py:281`

### _kernel `def _kernel(self, c)`
- Defined: `app.py:300`

### _contract `def _contract(self, W, X)`
- Defined: `app.py:303`
- Doc: Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]

### forward `def forward(self, x)`
- Defined: `app.py:307`
- Doc: x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)

### __init__ `def __init__(self, config)`
- Defined: `app.py:361`

### _filter1d `def _filter1d(self, x, kr, ki)`
- Defined: `app.py:393`
- Doc: Filtro espectral 1D: x[..., D] → filtrado[..., D]

### encode `def encode(self, x)`
- Defined: `app.py:399`
- Doc: x: [..., D_MODEL] → latent: [..., D_LAT]

### decode `def decode(self, z)`
- Defined: `app.py:404`
- Doc: z: [..., D_LAT] → recon: [..., D_MODEL]

### forward `def forward(self, x)`
- Defined: `app.py:409`
- Doc: Devuelve (latent, recon_loss)

### process_torus_grid `def process_torus_grid(self, grid)`
- Defined: `app.py:416`
- Doc: Procesa el grid del toro con QuaternionSpectralLayer.

### __init__ `def __init__(self, d_model, config)`
- Defined: `app.py:449`

### _build_torus_graph `def _build_torus_graph(self)`
- Defined: `app.py:489`
- Doc: Construye las aristas del grafo toro 2×4.

### _torus_soft_assign `def _torus_soft_assign(self, phi1, phi2)`
- Defined: `app.py:523`
- Doc: Asignación blanda de tokens a los 8 nodos del toro via distancia circular.

### _message_passing `def _message_passing(self, node_feat)`
- Defined: `app.py:550`
- Doc: Message-passing VECTORIZADO con rotaciones cuaterniones.

### forward `def forward(self, x)`
- Defined: `app.py:587`
- Doc: x: [B, S, D_MODEL]

### __init__ `def __init__(self, d_head, max_seq_len, base)`
- Defined: `app.py:655`

### _build_cache `def _build_cache(self, seq_len)`
- Defined: `app.py:661`

### _rotate_half `def _rotate_half(self, x)`
- Defined: `app.py:668`

### forward `def forward(self, q, k, seq_len, offset)`
- Defined: `app.py:672`
- Doc: q, k: [B, n_heads, S_q/S_k, d_head]

### __init__ `def __init__(self, d_model, eps)`
- Defined: `app.py:699`

### forward `def forward(self, x)`
- Defined: `app.py:704`

### __init__ `def __init__(self, d_model, expansion, dropout)`
- Defined: `app.py:720`

### forward `def forward(self, x)`
- Defined: `app.py:734`

### __init__ `def __init__(self, d_model, config)`
- Defined: `app.py:757`

### _route `def _route(self, x)`
- Defined: `app.py:778`
- Doc: x: [N, D] donde N = B*S (tokens aplanados)

### forward `def forward(self, x)`
- Defined: `app.py:820`
- Doc: x: [B, S, D]

### __init__ `def __init__(self, d_model, n_heads, config)`
- Defined: `app.py:857`

### forward `def forward(self, x, is_causal, past_kv)`
- Defined: `app.py:875`
- Doc: Args:

### __init__ `def __init__(self, d_model, n_heads, config)`
- Defined: `app.py:938`

### _forward_impl `def _forward_impl(self, x, past_kv)`
- Defined: `app.py:947`

### forward `def forward(self, x, past_kv)`
- Defined: `app.py:956`
- Doc: Retorna (x_out, aux_loss, kv_cache).

### __init__ `def __init__(self, config)`
- Defined: `app.py:987`

### _init_weights `def _init_weights(self)`
- Defined: `app.py:1006`

### forward `def forward(self, token_ids, past_kvs)`
- Defined: `app.py:1013`
- Doc: token_ids: [B, S]  (enteros)

### count_params `def count_params(self)`
- Defined: `app.py:1036`

### generate `def generate(self, token_ids, max_new_tokens, temperature, top_k)`
- Defined: `app.py:1042`
- Doc: Generacion autoregresiva con KV cache y muestreo top-k.

### __init__ `def __init__(self, encoding)`
- Defined: `app.py:1085`

### encode `def encode(self, text)`
- Defined: `app.py:1093`

### decode `def decode(self, tokens)`
- Defined: `app.py:1096`

### eot_token `def eot_token(self)`
- Defined: `app.py:1099`

### __init__ `def __init__(self, corpus, data_dir, logger)`
- Defined: `app.py:1119`

### get_text `def get_text(self, split)`
- Defined: `app.py:1125`
- Doc: Devuelve el texto del corpus. Descarga si es necesario.

### _download_hf `def _download_hf(self, dataset_name, split, text_column, name)`
- Defined: `app.py:1150`

### __init__ `def __init__(self, text, tokenizer, seq_len, max_tokens, cache_dir, split_tag)`
- Defined: `app.py:1179`

### __len__ `def __len__(self)`
- Defined: `app.py:1206`

### __getitem__ `def __getitem__(self, idx)`
- Defined: `app.py:1209`

### __init__ `def __init__(self, config, logger)`
- Defined: `app.py:1245`

### patch_config_for_resume `def patch_config_for_resume(self, cfg)`
- Defined: `app.py:1255`
- Doc: Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS

### _save_model `def _save_model(self, model, directory)`
- Defined: `app.py:1284`

### _load_model `def _load_model(self, model, directory)`
- Defined: `app.py:1297`

### _save_optimizer `def _save_optimizer(self, optimizer, directory)`
- Defined: `app.py:1328`

### _load_optimizer `def _load_optimizer(self, optimizer, directory, device)`
- Defined: `app.py:1331`

### _save_state `def _save_state(self, state, directory)`
- Defined: `app.py:1340`

### _load_state `def _load_state(self, directory)`
- Defined: `app.py:1345`

### should_save `def should_save(self)`
- Defined: `app.py:1356`

### save `def save(self, model, optimizer, state, is_best)`
- Defined: `app.py:1359`
- Doc: Guarda checkpoint completo.

### load_latest `def load_latest(self, model, optimizer)`
- Defined: `app.py:1404`
- Doc: Carga el ultimo checkpoint guardado.

### load_best `def load_best(self, model)`
- Defined: `app.py:1431`
- Doc: Carga el mejor modelo guardado (solo pesos, sin optimizador).

### has_checkpoint `def has_checkpoint(self)`
- Defined: `app.py:1443`

### __init__ `def __init__(self, model, config, tokenizer)`
- Defined: `app.py:1465`

### resume `def resume(self)`
- Defined: `app.py:1500`
- Doc: Carga el ultimo checkpoint disponible.

### _current_state `def _current_state(self)`
- Defined: `app.py:1525`
- Doc: Construye el dict de estado para persistir en state.json.

### _cosine_lr `def _cosine_lr(self, step_in_session, total_steps_session)`
- Defined: `app.py:1536`
- Doc: Cosine decay con warmup. El schedule es relativo a la sesion actual.

### _set_lr `def _set_lr(self, lr)`
- Defined: `app.py:1544`

### train `def train(self, train_dl, val_dl)`
- Defined: `app.py:1548`
- Doc: Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.

### _sample_text `def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)`
- Defined: `app.py:1684`
- Doc: Genera una muestra de texto al final de cada epoch para monitorear

### evaluate `def evaluate(self, dataloader)`
- Defined: `app.py:1716`

### __init__ `def __init__(self, config)`
- Defined: `app.py:1766`

### compute_delta `def compute_delta(self, model)`
- Defined: `app.py:1774`

### compute_alpha `def compute_alpha(self, delta)`
- Defined: `app.py:1781`

### update_grad_buffer `def update_grad_buffer(self, model)`
- Defined: `app.py:1786`
- Doc: Captura gradientes de forma segura, ignorando tensores corruptos.

### compute_t_eff `def compute_t_eff(self, lr)`
- Defined: `app.py:1812`
- Doc: T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva.

### compute_kappa `def compute_kappa(self, model, dataloader, n_batches)`
- Defined: `app.py:1820`
- Doc: κ = λ_max / λ_min de la covarianza del gradiente.

### compute_berry_phase `def compute_berry_phase(self, model)`
- Defined: `app.py:1878`
- Doc: Fase de Berry de los kernels espectrales imaginarios.

### compute_lc `def compute_lc(self, model)`
- Defined: `app.py:1891`
- Doc: Complejidad local: 1 - similitud coseno promedio entre filas de pesos.

### compute_sp `def compute_sp(self, model)`
- Defined: `app.py:1905`
- Doc: Superposicion: correlacion inter-fila promedio (entrelazamiento de features).

### classify_phase `def classify_phase(self, delta, kappa, berry)`
- Defined: `app.py:1921`
- Doc: Clasificacion de fase segun Book.md:

### compute_all `def compute_all(self, model, lr, dataloader, compute_kappa)`
- Defined: `app.py:1940`
- Doc: Calcula todas las metricas.

### format_log `def format_log(self, m)`
- Defined: `app.py:1965`

### __init__ `def __init__(self, config, logger)`
- Defined: `app.py:2001`

### _measure_ratio `def _measure_ratio(self, ratio, sample_batch)`
- Defined: `app.py:2005`
- Doc: Mide la coherencia espectral para un ratio dado.

### optimize `def optimize(self, dataloader)`
- Defined: `app.py:2034`
- Doc: Retorna el mejor ratio de inicializacion de kernels espectrales.

### __init__ `def __init__(self, config, logger)`
- Defined: `app.py:2074`

### prospect `def prospect(self, candidates, train_dataset, prospect_steps)`
- Defined: `app.py:2078`
- Doc: Retorna el mejor batch size segun delta y T_eff.

### __init__ `def __init__(self, config, logger)`
- Defined: `app.py:2157`

### mine `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)`
- Defined: `app.py:2161`
- Doc: Retorna la semilla con la mejor trayectoria de delta.

### __init__ `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)`
- Defined: `app.py:2243`

### refine `def refine(self, train_dl, val_dl, refine_epochs)`
- Defined: `app.py:2252`
- Doc: Ejecuta refine_epochs epocas de recocido simulado.

### __init__ `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)`
- Defined: `app.py:2404`

### _make_dataloaders `def _make_dataloaders(self, batch_size)`
- Defined: `app.py:2414`

### run `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)`
- Defined: `app.py:2426`
- Doc: Ejecuta el pipeline completo.

### ckpt_fn `def ckpt_fn(x_in)`
- Defined: `app.py:964`

## inference.py

### _load_source_module `def _load_source_module(path)`
- Defined: `inference.py:19`

### parse_arguments `def parse_arguments()`
- Defined: `inference.py:178`

### __init__ `def __init__(self, logger)`
- Defined: `inference.py:47`

### inspect_kq_head_count `def inspect_kq_head_count(self, checkpoint_path, d_model, n_heads)`
- Defined: `inference.py:50`

### patch_config `def patch_config(self, config, source_module)`
- Defined: `inference.py:62`

### _resolve_preset `def _resolve_preset(self, scale)`
- Defined: `inference.py:81`

### __init__ `def __init__(self, checkpoint_name, logger)`
- Defined: `inference.py:92`

### load_model `def load_model(self, config, source_module)`
- Defined: `inference.py:96`

### __init__ `def __init__(self, config, logger)`
- Defined: `inference.py:117`

### generate `def generate(self, model, tokenizer, prompt_text)`
- Defined: `inference.py:121`

### sample_logits `def sample_logits(self, logits)`
- Defined: `inference.py:132`

### __init__ `def __init__(self, config)`
- Defined: `inference.py:142`

### _setup_logger `def _setup_logger(self)`
- Defined: `inference.py:146`

### run `def run(self)`
- Defined: `inference.py:155`

### _print_result `def _print_result(self, prompt, output)`
- Defined: `inference.py:170`

## inference2.py

### build_logger `def build_logger(name, level)`
- Defined: `inference2.py:79`
- Doc: Stderr logger with timestamp formatting.

### build_arg_parser `def build_arg_parser()`
- Defined: `inference2.py:1217`
- Doc: Construct and return the CLI argument parser.

### main `def main()`
- Defined: `inference2.py:1288`
- Doc: CLI entry point.

### validate `def validate(self)`
- Defined: `inference2.py:148`
- Doc: Raise ValueError for impossible parameter combinations.

### __init__ `def __init__(self)`
- Defined: `inference2.py:175`

### encode `def encode(self, text)`
- Defined: `inference2.py:182`

### decode `def decode(self, token_ids)`
- Defined: `inference2.py:185`

### decode_single `def decode_single(self, token_id)`
- Defined: `inference2.py:188`

### hamilton_product `def hamilton_product(q1, q2)`
- Defined: `inference2.py:200`

### normalize `def normalize(q, eps)`
- Defined: `inference2.py:211`

### conjugate `def conjugate(q)`
- Defined: `inference2.py:215`

### __init__ `def __init__(self, in_features, out_features, bias)`
- Defined: `inference2.py:227`

### forward `def forward(self, x)`
- Defined: `inference2.py:241`

### __init__ `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- Defined: `inference2.py:259`

### _kernel `def _kernel(self, c)`
- Defined: `inference2.py:276`

### _contract `def _contract(self, W, X)`
- Defined: `inference2.py:279`

### forward `def forward(self, x)`
- Defined: `inference2.py:282`

### __init__ `def __init__(self, cfg)`
- Defined: `inference2.py:312`

### _filter1d `def _filter1d(self, x, kr, ki)`
- Defined: `inference2.py:334`

### encode `def encode(self, x)`
- Defined: `inference2.py:341`

### decode `def decode(self, z)`
- Defined: `inference2.py:344`

### forward `def forward(self, x)`
- Defined: `inference2.py:347`

### process_torus_grid `def process_torus_grid(self, grid)`
- Defined: `inference2.py:351`

### __init__ `def __init__(self, d_model, cfg)`
- Defined: `inference2.py:370`

### _build_torus_graph `def _build_torus_graph(self)`
- Defined: `inference2.py:395`

### _torus_soft_assign `def _torus_soft_assign(self, phi1, phi2)`
- Defined: `inference2.py:411`

### _message_passing `def _message_passing(self, node_feat)`
- Defined: `inference2.py:423`

### forward `def forward(self, x)`
- Defined: `inference2.py:437`

### __init__ `def __init__(self, d_model, expansion, dropout)`
- Defined: `inference2.py:465`

### forward `def forward(self, x)`
- Defined: `inference2.py:475`

### __init__ `def __init__(self, d_model, cfg)`
- Defined: `inference2.py:488`

### _route `def _route(self, x)`
- Defined: `inference2.py:503`

### forward `def forward(self, x)`
- Defined: `inference2.py:528`

### __init__ `def __init__(self, d_head, max_seq_len)`
- Defined: `inference2.py:542`

### _build_cache `def _build_cache(self, seq_len)`
- Defined: `inference2.py:550`

### _rotate_half `def _rotate_half(x)`
- Defined: `inference2.py:557`

### forward `def forward(self, q, k, seq_len, offset)`
- Defined: `inference2.py:561`

### __init__ `def __init__(self, d_model, eps)`
- Defined: `inference2.py:580`

### forward `def forward(self, x)`
- Defined: `inference2.py:585`

### __init__ `def __init__(self, d_model, n_heads, cfg)`
- Defined: `inference2.py:594`

### forward `def forward(self, x, is_causal, past_kv)`
- Defined: `inference2.py:609`

### __init__ `def __init__(self, d_model, n_heads, cfg)`
- Defined: `inference2.py:641`

### forward `def forward(self, x, past_kv)`
- Defined: `inference2.py:649`

### __init__ `def __init__(self, cfg)`
- Defined: `inference2.py:666`

### forward `def forward(self, token_ids, past_kvs)`
- Defined: `inference2.py:678`

### d_quat `def d_quat(self)`
- Defined: `inference2.py:723`

### gqa_groups `def gqa_groups(self)`
- Defined: `inference2.py:727`

### __init__ `def __init__(self, logger)`
- Defined: `inference2.py:768`

### _load_shapes `def _load_shapes(self, path)`
- Defined: `inference2.py:771`

### probe `def probe(self, path)`
- Defined: `inference2.py:786`
- Doc: Return a ModelConfig whose dimensions exactly match the checkpoint.

### _fallback_d_head `def _fallback_d_head(d_model, q_out, k_out)`
- Defined: `inference2.py:871`

### __init__ `def __init__(self, logger)`
- Defined: `inference2.py:896`

### load `def load(self, path, model, device)`
- Defined: `inference2.py:899`
- Doc: Load weights into model in-place.

### __init__ `def __init__(self, cfg)`
- Defined: `inference2.py:950`

### __call__ `def __call__(self, logits, generated_ids)`
- Defined: `inference2.py:953`
- Doc: Sample one token from logits.

### __init__ `def __init__(self, model, tokenizer, cfg, logger)`
- Defined: `inference2.py:1013`

### generate `def generate(self, prompt)`
- Defined: `inference2.py:1027`
- Doc: Generate text from prompt.

### _maybe_stream `def _maybe_stream(self, token_id)`
- Defined: `inference2.py:1071`

### print_single `def print_single(self, prompt, full_text, tps, show_timing)`
- Defined: `inference2.py:1087`

### print_benchmark `def print_benchmark(self, runs, tps_list)`
- Defined: `inference2.py:1100`

### __init__ `def __init__(self, cfg, logger)`
- Defined: `inference2.py:1127`

### _build_model `def _build_model(self)`
- Defined: `inference2.py:1131`

### run `def run(self)`
- Defined: `inference2.py:1149`

### _run_single `def _run_single(self, engine, printer)`
- Defined: `inference2.py:1164`

### _run_interactive `def _run_interactive(self, engine, printer)`
- Defined: `inference2.py:1176`

### _run_benchmark `def _run_benchmark(self, engine, printer)`
- Defined: `inference2.py:1199`

## quantize.py

### parse_arguments `def parse_arguments()`
- Defined: `quantize.py:939`

### main `def main()`
- Defined: `quantize.py:965`

### resolve_gqa `def resolve_gqa(self)`
- Defined: `quantize.py:86`

### inspect_and_patch `def inspect_and_patch(path, config)`
- Defined: `quantize.py:108`

### hamilton_product `def hamilton_product(q1, q2)`
- Defined: `quantize.py:165`

### normalize `def normalize(q, eps)`
- Defined: `quantize.py:176`

### conjugate `def conjugate(q)`
- Defined: `quantize.py:180`

### rotate_vector `def rotate_vector(v, q)`
- Defined: `quantize.py:185`

### __init__ `def __init__(self, in_features, out_features, bias)`
- Defined: `quantize.py:196`

### forward `def forward(self, x)`
- Defined: `quantize.py:209`

### __init__ `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- Defined: `quantize.py:221`

### _kernel `def _kernel(self, c)`
- Defined: `quantize.py:233`

### _contract `def _contract(self, W, X)`
- Defined: `quantize.py:236`

### forward `def forward(self, x)`
- Defined: `quantize.py:239`

### __init__ `def __init__(self, config)`
- Defined: `quantize.py:263`

### _filter1d `def _filter1d(self, x, kr, ki)`
- Defined: `quantize.py:286`

### encode `def encode(self, x)`
- Defined: `quantize.py:291`

### decode `def decode(self, z)`
- Defined: `quantize.py:295`

### forward `def forward(self, x)`
- Defined: `quantize.py:299`

### process_torus_grid `def process_torus_grid(self, grid)`
- Defined: `quantize.py:305`

### __init__ `def __init__(self, d_model, config)`
- Defined: `quantize.py:313`

### _build_torus_graph `def _build_torus_graph(self)`
- Defined: `quantize.py:338`

### _torus_soft_assign `def _torus_soft_assign(self, phi1, phi2)`
- Defined: `quantize.py:354`

### _message_passing `def _message_passing(self, node_feat)`
- Defined: `quantize.py:365`

### forward `def forward(self, x)`
- Defined: `quantize.py:380`

### __init__ `def __init__(self, d_head, max_seq_len, base)`
- Defined: `quantize.py:409`

### _build_cache `def _build_cache(self, seq_len)`
- Defined: `quantize.py:415`

### _rotate_half `def _rotate_half(self, x)`
- Defined: `quantize.py:422`

### forward `def forward(self, q, k, seq_len, offset)`
- Defined: `quantize.py:426`

### __init__ `def __init__(self, d_model, eps)`
- Defined: `quantize.py:441`

### forward `def forward(self, x)`
- Defined: `quantize.py:446`

### __init__ `def __init__(self, d_model, expansion, dropout)`
- Defined: `quantize.py:452`

### forward `def forward(self, x)`
- Defined: `quantize.py:464`

### __init__ `def __init__(self, d_model, config)`
- Defined: `quantize.py:469`

### _route `def _route(self, x)`
- Defined: `quantize.py:486`

### forward `def forward(self, x)`
- Defined: `quantize.py:509`

### __init__ `def __init__(self, d_model, n_heads, config)`
- Defined: `quantize.py:523`

### forward `def forward(self, x, is_causal, past_kv)`
- Defined: `quantize.py:539`

### __init__ `def __init__(self, d_model, n_heads, config)`
- Defined: `quantize.py:569`

### _forward_impl `def _forward_impl(self, x, past_kv)`
- Defined: `quantize.py:579`

### forward `def forward(self, x, past_kv)`
- Defined: `quantize.py:586`

### __init__ `def __init__(self, config)`
- Defined: `quantize.py:591`

### _init_weights `def _init_weights(self)`
- Defined: `quantize.py:606`

### forward `def forward(self, token_ids, past_kvs)`
- Defined: `quantize.py:613`

### generate `def generate(self, token_ids, max_new_tokens, temperature, top_k, eos_token_id)`
- Defined: `quantize.py:627`

### __init__ `def __init__(self, encoding)`
- Defined: `quantize.py:652`

### encode `def encode(self, text)`
- Defined: `quantize.py:658`

### decode `def decode(self, tokens)`
- Defined: `quantize.py:661`

### eot_token `def eot_token(self)`
- Defined: `quantize.py:664`

### quantize `def quantize(self, model)`
- Defined: `quantize.py:680`

### get_format_name `def get_format_name(self)`
- Defined: `quantize.py:684`

### get_bits_per_weight `def get_bits_per_weight(self)`
- Defined: `quantize.py:688`

### __init__ `def __init__(self, config)`
- Defined: `quantize.py:693`

### quantize `def quantize(self, model)`
- Defined: `quantize.py:696`

### get_format_name `def get_format_name(self)`
- Defined: `quantize.py:714`

### get_bits_per_weight `def get_bits_per_weight(self)`
- Defined: `quantize.py:717`

### __init__ `def __init__(self, config)`
- Defined: `quantize.py:722`

### quantize `def quantize(self, model)`
- Defined: `quantize.py:725`

### get_format_name `def get_format_name(self)`
- Defined: `quantize.py:739`

### get_bits_per_weight `def get_bits_per_weight(self)`
- Defined: `quantize.py:742`

### __init__ `def __init__(self, config)`
- Defined: `quantize.py:747`

### quantize `def quantize(self, model)`
- Defined: `quantize.py:750`

### get_format_name `def get_format_name(self)`
- Defined: `quantize.py:753`

### get_bits_per_weight `def get_bits_per_weight(self)`
- Defined: `quantize.py:756`

### __init__ `def __init__(self, config)`
- Defined: `quantize.py:761`

### quantize `def quantize(self, model)`
- Defined: `quantize.py:764`

### get_format_name `def get_format_name(self)`
- Defined: `quantize.py:767`

### get_bits_per_weight `def get_bits_per_weight(self)`
- Defined: `quantize.py:770`

### __init__ `def __init__(self, config)`
- Defined: `quantize.py:775`

### quantize `def quantize(self, model)`
- Defined: `quantize.py:778`

### get_format_name `def get_format_name(self)`
- Defined: `quantize.py:781`

### get_bits_per_weight `def get_bits_per_weight(self)`
- Defined: `quantize.py:784`

### __init__ `def __init__(self, config)`
- Defined: `quantize.py:789`

### quantize `def quantize(self, model)`
- Defined: `quantize.py:792`

### get_format_name `def get_format_name(self)`
- Defined: `quantize.py:795`

### get_bits_per_weight `def get_bits_per_weight(self)`
- Defined: `quantize.py:798`

### __init__ `def __init__(self, config)`
- Defined: `quantize.py:803`

### quantize `def quantize(self, model)`
- Defined: `quantize.py:806`

### get_format_name `def get_format_name(self)`
- Defined: `quantize.py:809`

### get_bits_per_weight `def get_bits_per_weight(self)`
- Defined: `quantize.py:812`

### create_quantizer `def create_quantizer(fmt, config)`
- Defined: `quantize.py:818`

### __init__ `def __init__(self, config, logger)`
- Defined: `quantize.py:835`

### load_checkpoint `def load_checkpoint(self)`
- Defined: `quantize.py:839`

### __init__ `def __init__(self, config, model, tokenizer)`
- Defined: `quantize.py:884`

### run_inference `def run_inference(self, prompt)`
- Defined: `quantize.py:891`

### __init__ `def __init__(self, config)`
- Defined: `quantize.py:908`

### execute `def execute(self)`
- Defined: `quantize.py:919`

## reinforce.py

### setup_logger `def setup_logger(name, level)`
- Defined: `reinforce.py:597`

### create_rl_agent_from_checkpoint `def create_rl_agent_from_checkpoint(model_path, config, tokenizer, logger)`
- Defined: `reinforce.py:606`

### __init__ `def __init__(self, logger)`
- Defined: `reinforce.py:86`

### align_config `def align_config(self, model_path, config, source_module)`
- Defined: `reinforce.py:89`

### _resolve_preset `def _resolve_preset(self, scale)`
- Defined: `reinforce.py:111`

### __init__ `def __init__(self, config, logger)`
- Defined: `reinforce.py:122`

### compute_lc_reward `def compute_lc_reward(self, lc_value)`
- Defined: `reinforce.py:129`

### compute_sp_reward `def compute_sp_reward(self, sp_value)`
- Defined: `reinforce.py:133`

### compute_delta_reward `def compute_delta_reward(self, delta_value)`
- Defined: `reinforce.py:137`

### compute_mechanistic_reward `def compute_mechanistic_reward(self, metrics)`
- Defined: `reinforce.py:142`

### __init__ `def __init__(self, config, vocab_size, d_model)`
- Defined: `reinforce.py:154`

### _init_weights `def _init_weights(self)`
- Defined: `reinforce.py:173`

### forward `def forward(self, input_ids, attention_mask)`
- Defined: `reinforce.py:180`

### __init__ `def __init__(self, config, capacity)`
- Defined: `reinforce.py:191`

### add `def add(self, experience)`
- Defined: `reinforce.py:198`

### compute_advantages `def compute_advantages(self, values, rewards, masks)`
- Defined: `reinforce.py:201`

### sample_minibatches `def sample_minibatches(self, batch_size)`
- Defined: `reinforce.py:215`

### _collate `def _collate(self, batch)`
- Defined: `reinforce.py:226`

### clear `def clear(self)`
- Defined: `reinforce.py:237`

### __init__ `def __init__(self, d_model, hidden_dim)`
- Defined: `reinforce.py:242`

### _init_weights `def _init_weights(self)`
- Defined: `reinforce.py:251`

### forward `def forward(self, hidden_states)`
- Defined: `reinforce.py:258`

### __init__ `def __init__(self, policy_model, config, reward_model, ref_model, logger)`
- Defined: `reinforce.py:264`

### generate_with_policy `def generate_with_policy(self, prompt_ids, max_new_tokens)`
- Defined: `reinforce.py:294`

### compute_kl_divergence `def compute_kl_divergence(self, policy_logits, ref_logits)`
- Defined: `reinforce.py:306`

### compute_reward `def compute_reward(self, responses, prompts, metrics)`
- Defined: `reinforce.py:317`

### collect_experience `def collect_experience(self, prompts, num_samples)`
- Defined: `reinforce.py:336`

### _extract_mechanistic_metrics `def _extract_mechanistic_metrics(self, tokens)`
- Defined: `reinforce.py:367`

### ppo_update `def ppo_update(self, batch)`
- Defined: `reinforce.py:398`

### train_step `def train_step(self, prompts)`
- Defined: `reinforce.py:460`

### _save_checkpoint `def _save_checkpoint(self)`
- Defined: `reinforce.py:482`

### load_checkpoint `def load_checkpoint(self, path)`
- Defined: `reinforce.py:498`

### __init__ `def __init__(self, policy_model, config, tokenizer, logger)`
- Defined: `reinforce.py:521`

### attach_trainer `def attach_trainer(self, trainer)`
- Defined: `reinforce.py:530`

### respond `def respond(self, user_message, max_new_tokens)`
- Defined: `reinforce.py:533`

### _format_conversation `def _format_conversation(self)`
- Defined: `reinforce.py:553`

### train_on_feedback `def train_on_feedback(self, user_message, response, reward_score)`
- Defined: `reinforce.py:562`

### reset_conversation `def reset_conversation(self)`
- Defined: `reinforce.py:594`

## topogpt2_1.py

### setup_logger `def setup_logger(name, level)`
- Defined: `topogpt2_1.py:155`

### set_seed `def set_seed(seed, device)`
- Defined: `topogpt2_1.py:165`

### main `def main()`
- Defined: `topogpt2_1.py:2506`

### __post_init__ `def __post_init__(self)`
- Defined: `topogpt2_1.py:124`

### hamilton_product `def hamilton_product(q1, q2)`
- Defined: `topogpt2_1.py:185`
- Doc: Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].

### normalize `def normalize(q, eps)`
- Defined: `topogpt2_1.py:197`

### conjugate `def conjugate(q)`
- Defined: `topogpt2_1.py:201`

### rotate_vector `def rotate_vector(v, q)`
- Defined: `topogpt2_1.py:206`
- Doc: Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]

### __init__ `def __init__(self, in_features, out_features, bias)`
- Defined: `topogpt2_1.py:228`

### forward `def forward(self, x)`
- Defined: `topogpt2_1.py:244`
- Doc: x: [..., in_features] → [..., out_features]

### __init__ `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- Defined: `topogpt2_1.py:281`

### _kernel `def _kernel(self, c)`
- Defined: `topogpt2_1.py:300`

### _contract `def _contract(self, W, X)`
- Defined: `topogpt2_1.py:303`
- Doc: Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]

### forward `def forward(self, x)`
- Defined: `topogpt2_1.py:307`
- Doc: x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_1.py:361`

### _filter1d `def _filter1d(self, x, kr, ki)`
- Defined: `topogpt2_1.py:393`
- Doc: Filtro espectral 1D: x[..., D] → filtrado[..., D]

### encode `def encode(self, x)`
- Defined: `topogpt2_1.py:399`
- Doc: x: [..., D_MODEL] → latent: [..., D_LAT]

### decode `def decode(self, z)`
- Defined: `topogpt2_1.py:404`
- Doc: z: [..., D_LAT] → recon: [..., D_MODEL]

### forward `def forward(self, x)`
- Defined: `topogpt2_1.py:409`
- Doc: Devuelve (latent, recon_loss)

### process_torus_grid `def process_torus_grid(self, grid)`
- Defined: `topogpt2_1.py:416`
- Doc: Procesa el grid del toro con QuaternionSpectralLayer.

### __init__ `def __init__(self, d_model, config)`
- Defined: `topogpt2_1.py:449`

### _build_torus_graph `def _build_torus_graph(self)`
- Defined: `topogpt2_1.py:489`
- Doc: Construye las aristas del grafo toro 2×4.

### _torus_soft_assign `def _torus_soft_assign(self, phi1, phi2)`
- Defined: `topogpt2_1.py:523`
- Doc: Asignación blanda de tokens a los 8 nodos del toro via distancia circular.

### _message_passing `def _message_passing(self, node_feat)`
- Defined: `topogpt2_1.py:550`
- Doc: Message-passing VECTORIZADO con rotaciones cuaterniones.

### forward `def forward(self, x)`
- Defined: `topogpt2_1.py:587`
- Doc: x: [B, S, D_MODEL]

### __init__ `def __init__(self, d_head, max_seq_len, base)`
- Defined: `topogpt2_1.py:655`

### _build_cache `def _build_cache(self, seq_len)`
- Defined: `topogpt2_1.py:661`

### _rotate_half `def _rotate_half(self, x)`
- Defined: `topogpt2_1.py:668`

### forward `def forward(self, q, k, seq_len, offset)`
- Defined: `topogpt2_1.py:672`
- Doc: q, k: [B, n_heads, S_q/S_k, d_head]

### __init__ `def __init__(self, d_model, eps)`
- Defined: `topogpt2_1.py:699`

### forward `def forward(self, x)`
- Defined: `topogpt2_1.py:704`

### __init__ `def __init__(self, d_model, expansion, dropout)`
- Defined: `topogpt2_1.py:720`

### forward `def forward(self, x)`
- Defined: `topogpt2_1.py:734`

### __init__ `def __init__(self, d_model, config)`
- Defined: `topogpt2_1.py:757`

### _route `def _route(self, x)`
- Defined: `topogpt2_1.py:778`
- Doc: x: [N, D] donde N = B*S (tokens aplanados)

### forward `def forward(self, x)`
- Defined: `topogpt2_1.py:820`
- Doc: x: [B, S, D]

### __init__ `def __init__(self, d_model, n_heads, config)`
- Defined: `topogpt2_1.py:857`

### forward `def forward(self, x, is_causal, past_kv)`
- Defined: `topogpt2_1.py:875`
- Doc: Args:

### __init__ `def __init__(self, d_model, n_heads, config)`
- Defined: `topogpt2_1.py:938`

### _forward_impl `def _forward_impl(self, x, past_kv)`
- Defined: `topogpt2_1.py:947`

### forward `def forward(self, x, past_kv)`
- Defined: `topogpt2_1.py:956`
- Doc: Retorna (x_out, aux_loss, kv_cache).

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_1.py:987`

### _init_weights `def _init_weights(self)`
- Defined: `topogpt2_1.py:1006`

### forward `def forward(self, token_ids, past_kvs)`
- Defined: `topogpt2_1.py:1013`
- Doc: token_ids: [B, S]  (enteros)

### count_params `def count_params(self)`
- Defined: `topogpt2_1.py:1036`

### generate `def generate(self, token_ids, max_new_tokens, temperature, top_k)`
- Defined: `topogpt2_1.py:1042`
- Doc: Generacion autoregresiva con KV cache y muestreo top-k.

### __init__ `def __init__(self, encoding)`
- Defined: `topogpt2_1.py:1085`

### encode `def encode(self, text)`
- Defined: `topogpt2_1.py:1093`

### decode `def decode(self, tokens)`
- Defined: `topogpt2_1.py:1096`

### eot_token `def eot_token(self)`
- Defined: `topogpt2_1.py:1099`

### __init__ `def __init__(self, corpus, data_dir, logger)`
- Defined: `topogpt2_1.py:1119`

### get_text `def get_text(self, split)`
- Defined: `topogpt2_1.py:1125`
- Doc: Devuelve el texto del corpus. Descarga si es necesario.

### _download_hf `def _download_hf(self, dataset_name, split, text_column, name)`
- Defined: `topogpt2_1.py:1150`

### __init__ `def __init__(self, text, tokenizer, seq_len, max_tokens, cache_dir, split_tag)`
- Defined: `topogpt2_1.py:1179`

### __len__ `def __len__(self)`
- Defined: `topogpt2_1.py:1206`

### __getitem__ `def __getitem__(self, idx)`
- Defined: `topogpt2_1.py:1209`

### __init__ `def __init__(self, config, logger)`
- Defined: `topogpt2_1.py:1245`

### patch_config_for_resume `def patch_config_for_resume(self, cfg)`
- Defined: `topogpt2_1.py:1255`
- Doc: Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS

### _save_model `def _save_model(self, model, directory)`
- Defined: `topogpt2_1.py:1284`

### _load_model `def _load_model(self, model, directory)`
- Defined: `topogpt2_1.py:1297`

### _save_optimizer `def _save_optimizer(self, optimizer, directory)`
- Defined: `topogpt2_1.py:1328`

### _load_optimizer `def _load_optimizer(self, optimizer, directory, device)`
- Defined: `topogpt2_1.py:1331`

### _save_state `def _save_state(self, state, directory)`
- Defined: `topogpt2_1.py:1340`

### _load_state `def _load_state(self, directory)`
- Defined: `topogpt2_1.py:1345`

### should_save `def should_save(self)`
- Defined: `topogpt2_1.py:1356`

### save `def save(self, model, optimizer, state, is_best)`
- Defined: `topogpt2_1.py:1359`
- Doc: Guarda checkpoint completo.

### load_latest `def load_latest(self, model, optimizer)`
- Defined: `topogpt2_1.py:1404`
- Doc: Carga el ultimo checkpoint guardado.

### load_best `def load_best(self, model)`
- Defined: `topogpt2_1.py:1431`
- Doc: Carga el mejor modelo guardado (solo pesos, sin optimizador).

### has_checkpoint `def has_checkpoint(self)`
- Defined: `topogpt2_1.py:1443`

### __init__ `def __init__(self, model, config, tokenizer)`
- Defined: `topogpt2_1.py:1465`

### resume `def resume(self)`
- Defined: `topogpt2_1.py:1500`
- Doc: Carga el ultimo checkpoint disponible.

### _current_state `def _current_state(self)`
- Defined: `topogpt2_1.py:1525`
- Doc: Construye el dict de estado para persistir en state.json.

### _cosine_lr `def _cosine_lr(self, step_in_session, total_steps_session)`
- Defined: `topogpt2_1.py:1536`
- Doc: Cosine decay con warmup. El schedule es relativo a la sesion actual.

### _set_lr `def _set_lr(self, lr)`
- Defined: `topogpt2_1.py:1544`

### train `def train(self, train_dl, val_dl)`
- Defined: `topogpt2_1.py:1548`
- Doc: Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.

### _sample_text `def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)`
- Defined: `topogpt2_1.py:1684`
- Doc: Genera una muestra de texto al final de cada epoch para monitorear

### evaluate `def evaluate(self, dataloader)`
- Defined: `topogpt2_1.py:1716`

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_1.py:1766`

### compute_delta `def compute_delta(self, model)`
- Defined: `topogpt2_1.py:1774`

### compute_alpha `def compute_alpha(self, delta)`
- Defined: `topogpt2_1.py:1781`

### update_grad_buffer `def update_grad_buffer(self, model)`
- Defined: `topogpt2_1.py:1786`
- Doc: Captura gradientes de forma segura, ignorando tensores corruptos.

### compute_t_eff `def compute_t_eff(self, lr)`
- Defined: `topogpt2_1.py:1812`
- Doc: T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva.

### compute_kappa `def compute_kappa(self, model, dataloader, n_batches)`
- Defined: `topogpt2_1.py:1820`
- Doc: κ = λ_max / λ_min de la covarianza del gradiente.

### compute_berry_phase `def compute_berry_phase(self, model)`
- Defined: `topogpt2_1.py:1878`
- Doc: Fase de Berry de los kernels espectrales imaginarios.

### compute_lc `def compute_lc(self, model)`
- Defined: `topogpt2_1.py:1891`
- Doc: Complejidad local: 1 - similitud coseno promedio entre filas de pesos.

### compute_sp `def compute_sp(self, model)`
- Defined: `topogpt2_1.py:1905`
- Doc: Superposicion: correlacion inter-fila promedio (entrelazamiento de features).

### classify_phase `def classify_phase(self, delta, kappa, berry)`
- Defined: `topogpt2_1.py:1921`
- Doc: Clasificacion de fase segun Book.md:

### compute_all `def compute_all(self, model, lr, dataloader, compute_kappa)`
- Defined: `topogpt2_1.py:1940`
- Doc: Calcula todas las metricas.

### format_log `def format_log(self, m)`
- Defined: `topogpt2_1.py:1965`

### __init__ `def __init__(self, config, logger)`
- Defined: `topogpt2_1.py:2001`

### _measure_ratio `def _measure_ratio(self, ratio, sample_batch)`
- Defined: `topogpt2_1.py:2005`
- Doc: Mide la coherencia espectral para un ratio dado.

### optimize `def optimize(self, dataloader)`
- Defined: `topogpt2_1.py:2034`
- Doc: Retorna el mejor ratio de inicializacion de kernels espectrales.

### __init__ `def __init__(self, config, logger)`
- Defined: `topogpt2_1.py:2074`

### prospect `def prospect(self, candidates, train_dataset, prospect_steps)`
- Defined: `topogpt2_1.py:2078`
- Doc: Retorna el mejor batch size segun delta y T_eff.

### __init__ `def __init__(self, config, logger)`
- Defined: `topogpt2_1.py:2157`

### mine `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)`
- Defined: `topogpt2_1.py:2161`
- Doc: Retorna la semilla con la mejor trayectoria de delta.

### __init__ `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)`
- Defined: `topogpt2_1.py:2243`

### refine `def refine(self, train_dl, val_dl, refine_epochs)`
- Defined: `topogpt2_1.py:2252`
- Doc: Ejecuta refine_epochs epocas de recocido simulado.

### __init__ `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)`
- Defined: `topogpt2_1.py:2404`

### _make_dataloaders `def _make_dataloaders(self, batch_size)`
- Defined: `topogpt2_1.py:2414`

### run `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)`
- Defined: `topogpt2_1.py:2426`
- Doc: Ejecuta el pipeline completo.

### ckpt_fn `def ckpt_fn(x_in)`
- Defined: `topogpt2_1.py:964`

## topogpt2_embeddings_navigator.py

### main `def main()`
- Defined: `topogpt2_embeddings_navigator.py:2418`
- Doc: Streamlit script entry point.

### __init__ `def __init__(self, theme)`
- Defined: `topogpt2_embeddings_navigator.py:192`

### inject `def inject(self)`
- Defined: `topogpt2_embeddings_navigator.py:195`
- Doc: Render the CSS block in the current Streamlit page.

### __init__ `def __init__(self, model, config, tokenizer, source_name)`
- Defined: `topogpt2_embeddings_navigator.py:266`

### model `def model(self)`
- Defined: `topogpt2_embeddings_navigator.py:279`
- Doc: Return the underlying nn.Module in eval mode.

### config `def config(self)`
- Defined: `topogpt2_embeddings_navigator.py:284`
- Doc: Return the model config object.

### tokenizer `def tokenizer(self)`
- Defined: `topogpt2_embeddings_navigator.py:289`
- Doc: Return the BPE tokenizer.

### source_name `def source_name(self)`
- Defined: `topogpt2_embeddings_navigator.py:294`
- Doc: Return the original file name of the checkpoint.

### device `def device(self)`
- Defined: `topogpt2_embeddings_navigator.py:299`
- Doc: Return the device the model is currently placed on.

### num_layers `def num_layers(self)`
- Defined: `topogpt2_embeddings_navigator.py:303`
- Doc: Return the number of transformer layers in the model.

### embedding_dim `def embedding_dim(self)`
- Defined: `topogpt2_embeddings_navigator.py:307`
- Doc: Return the model hidden size.

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_embeddings_navigator.py:315`

### load `def load(self, source, topogpt2_module)`
- Defined: `topogpt2_embeddings_navigator.py:318`
- Doc: Load a checkpoint and instantiate the corresponding model.

### _read_state_dict `def _read_state_dict(self, source)`
- Defined: `topogpt2_embeddings_navigator.py:344`

### _materialize `def _materialize(self, source)`
- Defined: `topogpt2_embeddings_navigator.py:366`

### _extract_payload `def _extract_payload(self, obj)`
- Defined: `topogpt2_embeddings_navigator.py:374`

### _build_config `def _build_config(self, topogpt2_module, embedded_cfg, state_dict)`
- Defined: `topogpt2_embeddings_navigator.py:391`

### _infer_config `def _infer_config(self, topogpt2_module, state_dict)`
- Defined: `topogpt2_embeddings_navigator.py:405`

### _infer_d_model `def _infer_d_model(state_dict)`
- Defined: `topogpt2_embeddings_navigator.py:433`

### _infer_num_layers `def _infer_num_layers(state_dict)`
- Defined: `topogpt2_embeddings_navigator.py:439`

### _infer_n_heads `def _infer_n_heads(state_dict, d_model)`
- Defined: `topogpt2_embeddings_navigator.py:450`

### _infer_max_seq_len `def _infer_max_seq_len(state_dict)`
- Defined: `topogpt2_embeddings_navigator.py:467`

### _infer_n_kv_heads `def _infer_n_kv_heads(state_dict, d_head, n_heads)`
- Defined: `topogpt2_embeddings_navigator.py:475`
- Doc: Infer the number of key/value heads for GQA.

### _infer_torus_grid `def _infer_torus_grid(state_dict)`
- Defined: `topogpt2_embeddings_navigator.py:505`

### _validate_load `def _validate_load(missing, unexpected)`
- Defined: `topogpt2_embeddings_navigator.py:514`

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_embeddings_navigator.py:525`

### run `def run(self, bundle, text)`
- Defined: `topogpt2_embeddings_navigator.py:528`
- Doc: Run a single forward pass and return activations and tokens.

### _decode_pieces `def _decode_pieces(tokenizer, ids)`
- Defined: `topogpt2_embeddings_navigator.py:589`

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_embeddings_navigator.py:603`

### compute `def compute(self, points, knn)`
- Defined: `topogpt2_embeddings_navigator.py:606`
- Doc: Compute every metric on a point cloud ``[N, D]``.

### _sanitize `def _sanitize(self, points)`
- Defined: `topogpt2_embeddings_navigator.py:642`

### _trivial `def _trivial(self, base)`
- Defined: `topogpt2_embeddings_navigator.py:645`

### _pairwise `def _pairwise(self, points)`
- Defined: `topogpt2_embeddings_navigator.py:675`

### _shortest_paths `def _shortest_paths(self, points, knn)`
- Defined: `topogpt2_embeddings_navigator.py:678`

### _sp_metrics `def _sp_metrics(self, dist_eucl, dist_geo)`
- Defined: `topogpt2_embeddings_navigator.py:698`

### _kappa `def _kappa(self, dist_eucl, dist_geo)`
- Defined: `topogpt2_embeddings_navigator.py:718`
- Doc: Local curvature proxy from the chord-vs-arc ratio.

### _gromov_delta `def _gromov_delta(self, dist_geo)`
- Defined: `topogpt2_embeddings_navigator.py:759`

### _persistence `def _persistence(self, points, dist_eucl)`
- Defined: `topogpt2_embeddings_navigator.py:783`

### _h0_from_mst `def _h0_from_mst(self, edges, n)`
- Defined: `topogpt2_embeddings_navigator.py:810`

### _h1_from_edges `def _h1_from_edges(self, edges, n)`
- Defined: `topogpt2_embeddings_navigator.py:845`
- Doc: Estimate H1 persistence bars from a distance-sorted edge list.

### _berry_phases `def _berry_phases(self, points)`
- Defined: `topogpt2_embeddings_navigator.py:905`

### _winding_numbers `def _winding_numbers(self, points)`
- Defined: `topogpt2_embeddings_navigator.py:920`

### _planar_winding `def _planar_winding(self, xs, ys)`
- Defined: `topogpt2_embeddings_navigator.py:936`

### _lipschitz `def _lipschitz(self, points)`
- Defined: `topogpt2_embeddings_navigator.py:947`

### _trajectory_geometry `def _trajectory_geometry(self, points)`
- Defined: `topogpt2_embeddings_navigator.py:954`
- Doc: Frenet-Serret differential geometry of the token trajectory.

### _safe_pca3 `def _safe_pca3(self, points)`
- Defined: `topogpt2_embeddings_navigator.py:1017`

### _spectral_properties `def _spectral_properties(self, points)`
- Defined: `topogpt2_embeddings_navigator.py:1030`

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_embeddings_navigator.py:1071`

### project `def project(self, points, method, n_components)`
- Defined: `topogpt2_embeddings_navigator.py:1074`
- Doc: Project ``[N, D]`` points to ``n_components`` dims.

### _pca `def _pca(self, points, n_components)`
- Defined: `topogpt2_embeddings_navigator.py:1105`

### _isomap `def _isomap(self, points, n_components)`
- Defined: `topogpt2_embeddings_navigator.py:1123`

### _umap `def _umap(self, points, n_components)`
- Defined: `topogpt2_embeddings_navigator.py:1144`

### _random `def _random(self, points, n_components)`
- Defined: `topogpt2_embeddings_navigator.py:1171`

### _sphere `def _sphere(self, points, n_components)`
- Defined: `topogpt2_embeddings_navigator.py:1181`

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_embeddings_navigator.py:1198`

### style_3d `def style_3d(self, fig, title, height)`
- Defined: `topogpt2_embeddings_navigator.py:1201`
- Doc: Apply 3D styling.

### style_2d `def style_2d(self, fig, title, height)`
- Defined: `topogpt2_embeddings_navigator.py:1223`
- Doc: Apply 2D styling.

### __init__ `def __init__(self, ctx)`
- Defined: `topogpt2_embeddings_navigator.py:1261`

### ctx `def ctx(self)`
- Defined: `topogpt2_embeddings_navigator.py:1265`
- Doc: Return the shared render context.

### render `def render(self)`
- Defined: `topogpt2_embeddings_navigator.py:1270`
- Doc: Render the view into the current Streamlit container.

### render `def render(self)`
- Defined: `topogpt2_embeddings_navigator.py:1280`

### _render_tokens `def _render_tokens(self)`
- Defined: `topogpt2_embeddings_navigator.py:1284`

### _render_layer_evolution `def _render_layer_evolution(self)`
- Defined: `topogpt2_embeddings_navigator.py:1310`

### render `def render(self)`
- Defined: `topogpt2_embeddings_navigator.py:1358`

### _choose `def _choose(self, acts, selection)`
- Defined: `topogpt2_embeddings_navigator.py:1378`

### _render_trajectory `def _render_trajectory(self, emb, tokens, ids, norms, stage, method, info)`
- Defined: `topogpt2_embeddings_navigator.py:1386`

### _render_residual_streams `def _render_residual_streams(self, acts, method)`
- Defined: `topogpt2_embeddings_navigator.py:1442`

### render `def render(self)`
- Defined: `topogpt2_embeddings_navigator.py:1481`

### _get_metrics `def _get_metrics(self, stage)`
- Defined: `topogpt2_embeddings_navigator.py:1490`

### _render_card `def _render_card(self, m)`
- Defined: `topogpt2_embeddings_navigator.py:1496`

### _render_kappa `def _render_kappa(self, m)`
- Defined: `topogpt2_embeddings_navigator.py:1521`

### _render_path_metrics `def _render_path_metrics(self, m)`
- Defined: `topogpt2_embeddings_navigator.py:1544`

### render `def render(self)`
- Defined: `topogpt2_embeddings_navigator.py:1575`

### _stage_metrics `def _stage_metrics(self, stage)`
- Defined: `topogpt2_embeddings_navigator.py:1583`

### _render_diagram `def _render_diagram(self, m)`
- Defined: `topogpt2_embeddings_navigator.py:1591`

### _render_barcode `def _render_barcode(self, m)`
- Defined: `topogpt2_embeddings_navigator.py:1633`

### render `def render(self)`
- Defined: `topogpt2_embeddings_navigator.py:1672`

### _stage_metrics `def _stage_metrics(self, stage)`
- Defined: `topogpt2_embeddings_navigator.py:1680`

### _render_berry `def _render_berry(self, m, stage)`
- Defined: `topogpt2_embeddings_navigator.py:1688`

### _render_winding `def _render_winding(self, m, stage)`
- Defined: `topogpt2_embeddings_navigator.py:1720`

### render `def render(self)`
- Defined: `topogpt2_embeddings_navigator.py:1764`

### _stage_metrics `def _stage_metrics(self, stage)`
- Defined: `topogpt2_embeddings_navigator.py:1772`

### _render_lc `def _render_lc(self, m)`
- Defined: `topogpt2_embeddings_navigator.py:1780`

### _render_dynamics `def _render_dynamics(self, m)`
- Defined: `topogpt2_embeddings_navigator.py:1807`

### render `def render(self)`
- Defined: `topogpt2_embeddings_navigator.py:1840`

### _stage_metrics `def _stage_metrics(self, stage)`
- Defined: `topogpt2_embeddings_navigator.py:1849`

### _stage_points `def _stage_points(self, stage)`
- Defined: `topogpt2_embeddings_navigator.py:1857`

### _render_graph `def _render_graph(self, points, m)`
- Defined: `topogpt2_embeddings_navigator.py:1864`

### _render_coherence `def _render_coherence(self, points)`
- Defined: `topogpt2_embeddings_navigator.py:1911`

### render `def render(self)`
- Defined: `topogpt2_embeddings_navigator.py:1939`

### _cosine_diag `def _cosine_diag(self, A, B)`
- Defined: `topogpt2_embeddings_navigator.py:1962`

### _render_heatmap `def _render_heatmap(self, title, z, xlabels, tokens, diverging)`
- Defined: `topogpt2_embeddings_navigator.py:1968`

### render `def render(self)`
- Defined: `topogpt2_embeddings_navigator.py:2000`

### _points `def _points(self, stage)`
- Defined: `topogpt2_embeddings_navigator.py:2021`

### _render_component_norms `def _render_component_norms(self, comps)`
- Defined: `topogpt2_embeddings_navigator.py:2029`

### _render_quaternion_norms `def _render_quaternion_norms(self, comps)`
- Defined: `topogpt2_embeddings_navigator.py:2054`

### _render_sphere `def _render_sphere(self, comps)`
- Defined: `topogpt2_embeddings_navigator.py:2070`

### render `def render(self)`
- Defined: `topogpt2_embeddings_navigator.py:2114`

### _points `def _points(self, stage)`
- Defined: `topogpt2_embeddings_navigator.py:2136`

### __init__ `def __init__(self, context)`
- Defined: `topogpt2_embeddings_navigator.py:2148`

### register `def register(self, factory)`
- Defined: `topogpt2_embeddings_navigator.py:2152`
- Doc: Register a view factory.

### build `def build(self)`
- Defined: `topogpt2_embeddings_navigator.py:2156`
- Doc: Instantiate every registered view.

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_embeddings_navigator.py:2164`

### render `def render(self)`
- Defined: `topogpt2_embeddings_navigator.py:2167`
- Doc: Render the sidebar and return user selections.

### load `def load(self, path)`
- Defined: `topogpt2_embeddings_navigator.py:2220`
- Doc: Dynamically import the TopoGPT2 module.

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_embeddings_navigator.py:2258`

### run `def run(self)`
- Defined: `topogpt2_embeddings_navigator.py:2269`
- Doc: Entry point for ``streamlit run``.

### _render_header `def _render_header(self)`
- Defined: `topogpt2_embeddings_navigator.py:2307`

### _render_landing `def _render_landing(self)`
- Defined: `topogpt2_embeddings_navigator.py:2324`

### _try_load_bundle `def _try_load_bundle(self, selections)`
- Defined: `topogpt2_embeddings_navigator.py:2335`

### _compute_all_metrics `def _compute_all_metrics(self, activations, knn)`
- Defined: `topogpt2_embeddings_navigator.py:2351`

### _render_meta `def _render_meta(self, bundle, activations, knn)`
- Defined: `topogpt2_embeddings_navigator.py:2367`

### _build_registry `def _build_registry(self, ctx)`
- Defined: `topogpt2_embeddings_navigator.py:2380`

### _render_tabs `def _render_tabs(self, registry)`
- Defined: `topogpt2_embeddings_navigator.py:2394`

### _render_footer `def _render_footer(self)`
- Defined: `topogpt2_embeddings_navigator.py:2408`

### hook `def hook(_module, _inputs, output)`
- Defined: `topogpt2_embeddings_navigator.py:561`

### find `def find(x)`
- Defined: `topogpt2_embeddings_navigator.py:818`

### union `def union(x, y)`
- Defined: `topogpt2_embeddings_navigator.py:824`

### find `def find(x)`
- Defined: `topogpt2_embeddings_navigator.py:864`

### union `def union(x, y)`
- Defined: `topogpt2_embeddings_navigator.py:870`

## topogpt2_explorer.py

### main `def main()`
- Defined: `topogpt2_explorer.py:2493`
- Doc: Streamlit script entry point.

### __init__ `def __init__(self, theme)`
- Defined: `topogpt2_explorer.py:171`

### _build_css `def _build_css(self)`
- Defined: `topogpt2_explorer.py:174`

### inject `def inject(self)`
- Defined: `topogpt2_explorer.py:239`
- Doc: Render the CSS block inside the current Streamlit page.

### classify `def classify(self, name, shape)`
- Defined: `topogpt2_explorer.py:258`
- Doc: Return structured metadata for a checkpoint tensor.

### _classify_role `def _classify_role(self, name)`
- Defined: `topogpt2_explorer.py:286`

### _extract_layer `def _extract_layer(self, name)`
- Defined: `topogpt2_explorer.py:328`

### _extract_quaternion_component `def _extract_quaternion_component(self, name)`
- Defined: `topogpt2_explorer.py:332`

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_explorer.py:345`

### load `def load(self, source)`
- Defined: `topogpt2_explorer.py:348`
- Doc: Load a checkpoint from a file path or an uploaded file-like.

### _materialize `def _materialize(self, source)`
- Defined: `topogpt2_explorer.py:373`

### _load_safetensors `def _load_safetensors(self, buffer)`
- Defined: `topogpt2_explorer.py:382`

### _load_torch `def _load_torch(self, buffer)`
- Defined: `topogpt2_explorer.py:389`

### _extract_state_dict `def _extract_state_dict(self, obj)`
- Defined: `topogpt2_explorer.py:399`

### _looks_like_state_dict `def _looks_like_state_dict(obj)`
- Defined: `topogpt2_explorer.py:413`

### _to_cpu_float32 `def _to_cpu_float32(tensor)`
- Defined: `topogpt2_explorer.py:420`

### __init__ `def __init__(self, tensors, classifier)`
- Defined: `topogpt2_explorer.py:432`

### names `def names(self)`
- Defined: `topogpt2_explorer.py:443`
- Doc: Return all tensor names sorted alphabetically.

### tensor `def tensor(self, name)`
- Defined: `topogpt2_explorer.py:447`
- Doc: Retrieve a tensor by name.

### meta `def meta(self, name)`
- Defined: `topogpt2_explorer.py:451`
- Doc: Retrieve structured metadata for a tensor.

### layers `def layers(self)`
- Defined: `topogpt2_explorer.py:455`
- Doc: Return all unique layer indices present in the checkpoint.

### roles `def roles(self)`
- Defined: `topogpt2_explorer.py:460`
- Doc: Return the distinct roles present in the checkpoint.

### filter `def filter(self, role, layer, component, spectral_only)`
- Defined: `topogpt2_explorer.py:464`
- Doc: Return tensor names matching the supplied filters.

### total_parameters `def total_parameters(self)`
- Defined: `topogpt2_explorer.py:485`
- Doc: Total parameter count across the checkpoint.

### summary_rows `def summary_rows(self)`
- Defined: `topogpt2_explorer.py:489`
- Doc: Return a list of per-tensor rows suitable for a Streamlit table.

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_explorer.py:526`

### to_matrix `def to_matrix(self, tensor)`
- Defined: `topogpt2_explorer.py:531`
- Doc: Convert a tensor to a 2D ``float64`` matrix.

### subsample `def subsample(self, matrix, max_rows, max_cols, seed)`
- Defined: `topogpt2_explorer.py:553`
- Doc: Return a row/column subsample bounded by the configured caps.

### project_3d `def project_3d(self, matrix, method)`
- Defined: `topogpt2_explorer.py:575`
- Doc: Project a matrix to 3D using PCA or Gaussian random projection.

### _pca_3d `def _pca_3d(self, matrix)`
- Defined: `topogpt2_explorer.py:606`

### _random_3d `def _random_3d(self, matrix)`
- Defined: `topogpt2_explorer.py:617`

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_explorer.py:643`

### compute_all `def compute_all(self, matrix)`
- Defined: `topogpt2_explorer.py:649`
- Doc: Compute the full metrics dictionary in one pass.

### _svd_safe `def _svd_safe(self, matrix)`
- Defined: `topogpt2_explorer.py:681`
- Doc: Compute singular values once, reused by rank and participation ratio.

### _effective_rank_from_svd `def _effective_rank_from_svd(self, svd_values, shape)`
- Defined: `topogpt2_explorer.py:690`

### _participation_from_svd `def _participation_from_svd(self, svd_values, shape)`
- Defined: `topogpt2_explorer.py:707`

### sparsity `def sparsity(self, matrix, threshold)`
- Defined: `topogpt2_explorer.py:720`
- Doc: Fraction of entries whose absolute value is below ``threshold``.

### entropy `def entropy(self, matrix)`
- Defined: `topogpt2_explorer.py:727`
- Doc: Shannon entropy (nats) of the discrete value histogram.

### effective_rank `def effective_rank(self, matrix)`
- Defined: `topogpt2_explorer.py:748`
- Doc: Effective rank via the exponential of the entropy of singular values.

### participation_ratio `def participation_ratio(self, matrix)`
- Defined: `topogpt2_explorer.py:753`
- Doc: Participation ratio of the singular value spectrum.

### fractal_dimension `def fractal_dimension(self, matrix)`
- Defined: `topogpt2_explorer.py:762`
- Doc: Approximate the effective embedding dimension via PCA.

### coherence `def coherence(self, matrix)`
- Defined: `topogpt2_explorer.py:781`
- Doc: Maximum and mean absolute cosine similarity between rows.

### spectral_flatness `def spectral_flatness(self, matrix)`
- Defined: `topogpt2_explorer.py:796`
- Doc: Spectral flatness (Wiener entropy) in dB averaged over rows.

### dominant_frequency `def dominant_frequency(self, matrix)`
- Defined: `topogpt2_explorer.py:814`
- Doc: Index of the dominant non-zero frequency bin of row 0.

### _subsample_for_svd `def _subsample_for_svd(self, matrix)`
- Defined: `topogpt2_explorer.py:824`

### _subsample_for_pca `def _subsample_for_pca(self, matrix)`
- Defined: `topogpt2_explorer.py:830`

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_explorer.py:839`

### style_3d `def style_3d(self, fig, title)`
- Defined: `topogpt2_explorer.py:842`
- Doc: Apply the standard 3D scene styling.

### style_2d `def style_2d(self, fig, title, height)`
- Defined: `topogpt2_explorer.py:864`
- Doc: Apply the standard 2D figure styling.

### __init__ `def __init__(self, context)`
- Defined: `topogpt2_explorer.py:914`

### ctx `def ctx(self)`
- Defined: `topogpt2_explorer.py:918`
- Doc: Return the render context bound to this visualizer.

### is_applicable `def is_applicable(self)`
- Defined: `topogpt2_explorer.py:922`
- Doc: Return ``True`` if there is data in the inventory to render.

### render `def render(self)`
- Defined: `topogpt2_explorer.py:927`
- Doc: Render the visualizer into the current Streamlit container.

### render `def render(self)`
- Defined: `topogpt2_explorer.py:937`

### _render_headline `def _render_headline(self, total_params, num_tensors, num_layers)`
- Defined: `topogpt2_explorer.py:950`

### _render_role_breakdown `def _render_role_breakdown(self, role_counts, role_params)`
- Defined: `topogpt2_explorer.py:957`

### _render_inventory_table `def _render_inventory_table(self, rows)`
- Defined: `topogpt2_explorer.py:984`

### render `def render(self)`
- Defined: `topogpt2_explorer.py:1005`

### _render_meta `def _render_meta(self, meta)`
- Defined: `topogpt2_explorer.py:1042`

### _render_metric_grid `def _render_metric_grid(self, metrics)`
- Defined: `topogpt2_explorer.py:1050`

### _render_point_cloud `def _render_point_cloud(self, matrix, name, method)`
- Defined: `topogpt2_explorer.py:1069`

### _render_heatmap `def _render_heatmap(self, matrix, name)`
- Defined: `topogpt2_explorer.py:1103`

### _render_distribution `def _render_distribution(self, matrix, name)`
- Defined: `topogpt2_explorer.py:1125`

### _render_spectrum `def _render_spectrum(self, matrix, name)`
- Defined: `topogpt2_explorer.py:1149`

### _render_singular_spectrum `def _render_singular_spectrum(self, matrix, name)`
- Defined: `topogpt2_explorer.py:1180`

### is_applicable `def is_applicable(self)`
- Defined: `topogpt2_explorer.py:1233`

### render `def render(self)`
- Defined: `topogpt2_explorer.py:1237`

### _group_quaternion_bundles `def _group_quaternion_bundles(self)`
- Defined: `topogpt2_explorer.py:1249`

### _quaternion_bundle_key `def _quaternion_bundle_key(name, component)`
- Defined: `topogpt2_explorer.py:1263`

### _render_component_stats `def _render_component_stats(self, components)`
- Defined: `topogpt2_explorer.py:1278`

### _render_component_heatmaps `def _render_component_heatmaps(self, components)`
- Defined: `topogpt2_explorer.py:1290`

### _render_component_spectra `def _render_component_spectra(self, components)`
- Defined: `topogpt2_explorer.py:1315`

### _render_unit_norm_distribution `def _render_unit_norm_distribution(self, components)`
- Defined: `topogpt2_explorer.py:1346`

### is_applicable `def is_applicable(self)`
- Defined: `topogpt2_explorer.py:1391`

### render `def render(self)`
- Defined: `topogpt2_explorer.py:1397`

### _pair_kr_ki `def _pair_kr_ki(self)`
- Defined: `topogpt2_explorer.py:1413`

### _reshape_to_2d `def _reshape_to_2d(self, magnitude, phase)`
- Defined: `topogpt2_explorer.py:1428`

### _render_magnitude_phase `def _render_magnitude_phase(self, magnitude, phase, key)`
- Defined: `topogpt2_explorer.py:1439`

### _render_complex_scatter `def _render_complex_scatter(self, complex_kernel, key)`
- Defined: `topogpt2_explorer.py:1470`

### _render_radial_profile `def _render_radial_profile(self, magnitude, key)`
- Defined: `topogpt2_explorer.py:1504`

### is_applicable `def is_applicable(self)`
- Defined: `topogpt2_explorer.py:1544`

### render `def render(self)`
- Defined: `topogpt2_explorer.py:1547`

### _infer_grid `def _infer_grid(self, n_nodes)`
- Defined: `topogpt2_explorer.py:1568`

### _render_headline_metrics `def _render_headline_metrics(self, nodes, edges, radial_bins, angular_bins)`
- Defined: `topogpt2_explorer.py:1578`

### _render_3d_torus `def _render_3d_torus(self, nodes, edges, radial_bins, angular_bins)`
- Defined: `topogpt2_explorer.py:1591`

### _torus_positions `def _torus_positions(self, nodes, radial_bins, angular_bins)`
- Defined: `topogpt2_explorer.py:1605`

### _add_edges `def _add_edges(self, fig, positions, radial_bins, angular_bins, edges)`
- Defined: `topogpt2_explorer.py:1631`

### _edge_label `def _edge_label(edge_type)`
- Defined: `topogpt2_explorer.py:1669`

### _build_segments `def _build_segments(positions, radial_bins, angular_bins)`
- Defined: `topogpt2_explorer.py:1678`

### _add_nodes `def _add_nodes(self, fig, positions, node_colors, n_nodes)`
- Defined: `topogpt2_explorer.py:1697`

### _render_node_correlation `def _render_node_correlation(self, nodes)`
- Defined: `topogpt2_explorer.py:1725`

### _render_edge_quaternions `def _render_edge_quaternions(self, edges)`
- Defined: `topogpt2_explorer.py:1747`

### is_applicable `def is_applicable(self)`
- Defined: `topogpt2_explorer.py:1779`

### render `def render(self)`
- Defined: `topogpt2_explorer.py:1785`

### _infer_head_count `def _infer_head_count(self, matrix, proj)`
- Defined: `topogpt2_explorer.py:1813`

### _render_per_head_norms `def _render_per_head_norms(self, matrix, proj)`
- Defined: `topogpt2_explorer.py:1822`

### _render_per_head_spectrum `def _render_per_head_spectrum(self, matrix, proj, layer)`
- Defined: `topogpt2_explorer.py:1849`

### _render_head_similarity `def _render_head_similarity(self, matrix, proj, layer)`
- Defined: `topogpt2_explorer.py:1881`

### _render_summary_metrics `def _render_summary_metrics(self, metrics)`
- Defined: `topogpt2_explorer.py:1908`

### is_applicable `def is_applicable(self)`
- Defined: `topogpt2_explorer.py:1922`

### render `def render(self)`
- Defined: `topogpt2_explorer.py:1927`

### _render_router_norms `def _render_router_norms(self, router, layer)`
- Defined: `topogpt2_explorer.py:1949`

### _render_routing_probe `def _render_routing_probe(self, router, layer)`
- Defined: `topogpt2_explorer.py:1972`

### _render_expert_similarity `def _render_expert_similarity(self, layer)`
- Defined: `topogpt2_explorer.py:2015`

### _softmax `def _softmax(logits)`
- Defined: `topogpt2_explorer.py:2055`

### is_applicable `def is_applicable(self)`
- Defined: `topogpt2_explorer.py:2067`

### render `def render(self)`
- Defined: `topogpt2_explorer.py:2070`

### _render_metric_grid `def _render_metric_grid(self, role, layers, series)`
- Defined: `topogpt2_explorer.py:2113`

### render `def render(self)`
- Defined: `topogpt2_explorer.py:2157`

### _render_scatter `def _render_scatter(self, emb, labels, roles, sizes, pca)`
- Defined: `topogpt2_explorer.py:2204`

### _render_feature_correlation `def _render_feature_correlation(self, X_std, example)`
- Defined: `topogpt2_explorer.py:2246`

### _build_palette `def _build_palette(n)`
- Defined: `topogpt2_explorer.py:2279`

### __init__ `def __init__(self, context)`
- Defined: `topogpt2_explorer.py:2294`

### register `def register(self, factory)`
- Defined: `topogpt2_explorer.py:2298`
- Doc: Register a visualizer factory.

### build `def build(self)`
- Defined: `topogpt2_explorer.py:2307`
- Doc: Instantiate all registered visualizers.

### applicable `def applicable(self)`
- Defined: `topogpt2_explorer.py:2311`
- Doc: Return the subset of visualizers whose data is present.

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_explorer.py:2319`

### render `def render(self)`
- Defined: `topogpt2_explorer.py:2322`
- Doc: Render the sidebar and return the current selections.

### __init__ `def __init__(self, config)`
- Defined: `topogpt2_explorer.py:2362`

### run `def run(self)`
- Defined: `topogpt2_explorer.py:2372`
- Doc: Entry point used by ``streamlit run``.

### _configure_page `def _configure_page(self)`
- Defined: `topogpt2_explorer.py:2394`

### _render_header `def _render_header(self)`
- Defined: `topogpt2_explorer.py:2401`

### _render_landing `def _render_landing(self)`
- Defined: `topogpt2_explorer.py:2416`

### _resolve_checkpoint `def _resolve_checkpoint(self, selections)`
- Defined: `topogpt2_explorer.py:2437`

### _build_registry `def _build_registry(self, context)`
- Defined: `topogpt2_explorer.py:2452`

### _render_tabs `def _render_tabs(self, registry)`
- Defined: `topogpt2_explorer.py:2465`

### _render_footer `def _render_footer(self)`
- Defined: `topogpt2_explorer.py:2483`

## topogpt2_grid_scaler.py

### _setup_logger `def _setup_logger(name, level)`
- Defined: `topogpt2_grid_scaler.py:169`

### build_parser `def build_parser()`
- Defined: `topogpt2_grid_scaler.py:1070`

### config_from_args `def config_from_args(args)`
- Defined: `topogpt2_grid_scaler.py:1097`

### main `def main()`
- Defined: `topogpt2_grid_scaler.py:1119`

### __post_init__ `def __post_init__(self)`
- Defined: `topogpt2_grid_scaler.py:159`

### load `def load(self, path)`
- Defined: `topogpt2_grid_scaler.py:184`
- Doc: Import and return the topogpt2 module.

### read `def read(self, path, device)`
- Defined: `topogpt2_grid_scaler.py:208`
- Doc: Return (state_dict, optional_embedded_config).

### _extract `def _extract(self, obj)`
- Defined: `topogpt2_grid_scaler.py:225`

### reconstruct `def reconstruct(self, mod, state_dict, embedded)`
- Defined: `topogpt2_grid_scaler.py:245`
- Doc: Return a TopoGPT2Config that matches the loaded weights exactly.

### _infer `def _infer(self, mod, sd)`
- Defined: `topogpt2_grid_scaler.py:259`

### _infer_d_head `def _infer_d_head(sd)`
- Defined: `topogpt2_grid_scaler.py:291`

### _infer_n_kv `def _infer_n_kv(sd, d_head, n_heads)`
- Defined: `topogpt2_grid_scaler.py:298`

### _infer_max_seq `def _infer_max_seq(sd)`
- Defined: `topogpt2_grid_scaler.py:308`

### _infer_torus `def _infer_torus(sd)`
- Defined: `topogpt2_grid_scaler.py:315`

### classify `def classify(self, key, shape)`
- Defined: `topogpt2_grid_scaler.py:340`
- Doc: Return a semantic role string.

### __init__ `def __init__(self, cfg)`
- Defined: `topogpt2_grid_scaler.py:388`

### interpolate_2d `def interpolate_2d(self, W, tgt_rows, tgt_cols)`
- Defined: `topogpt2_grid_scaler.py:391`
- Doc: Scale a 2D weight matrix [M, N] to [M', N'] via spectral interpolation.

### interpolate_1d `def interpolate_1d(self, v, tgt_len)`
- Defined: `topogpt2_grid_scaler.py:421`
- Doc: Scale a 1D vector of length L to length L' via spectral interpolation.

### _resize_spectrum_2d `def _resize_spectrum_2d(self, W_f, tgt_rows, tgt_cols)`
- Defined: `topogpt2_grid_scaler.py:452`
- Doc: Zero-pad or centre-crop a 2D complex spectrum.

### __init__ `def __init__(self, interp, role_clf, logger)`
- Defined: `topogpt2_grid_scaler.py:499`

### scale `def scale(self, src_state, src_cfg, tgt_cfg, mod)`
- Defined: `topogpt2_grid_scaler.py:509`
- Doc: Produce a complete scaled state dict.

### _dispatch `def _dispatch(self, src, tgt_shape, role, key)`
- Defined: `topogpt2_grid_scaler.py:567`
- Doc: Route to the correct interpolation method based on shape and role.

### _scale_spectral_2d_to `def _scale_spectral_2d_to(self, t, tgt_shape, key)`
- Defined: `topogpt2_grid_scaler.py:598`
- Doc: Scale [in_q, out_q, R, Af] to [in_q', out_q', R, Af].

### _bilinear_fallback `def _bilinear_fallback(self, src, tgt_shape)`
- Defined: `topogpt2_grid_scaler.py:626`

### __init__ `def __init__(self, cfg)`
- Defined: `topogpt2_grid_scaler.py:638`

### compute `def compute(self, state, d_model)`
- Defined: `topogpt2_grid_scaler.py:641`
- Doc: Compute all configured validation metrics.

### check_degradation `def check_degradation(self, before, after, logger)`
- Defined: `topogpt2_grid_scaler.py:656`
- Doc: Return True if any metric dropped beyond its tolerance.

### _spectral_concentration `def _spectral_concentration(self, sd)`
- Defined: `topogpt2_grid_scaler.py:690`

### _phase_coherence `def _phase_coherence(self, sd)`
- Defined: `topogpt2_grid_scaler.py:708`

### assemble `def assemble(self, mod, tgt_cfg, scaled_state, logger)`
- Defined: `topogpt2_grid_scaler.py:726`
- Doc: Instantiate the target model and load scaled weights.

### save `def save(self, model, tgt_cfg, src_cfg, metrics_before, metrics_after, out_cfg, step_tag, logger)`
- Defined: `topogpt2_grid_scaler.py:754`
- Doc: Persist scaled checkpoint and metadata. Returns checkpoint path.

### _write_report `def _write_report(self, path, src_cfg, tgt_cfg, before, after, ckpt)`
- Defined: `topogpt2_grid_scaler.py:815`

### __init__ `def __init__(self, cfg)`
- Defined: `topogpt2_grid_scaler.py:872`

### run `def run(self)`
- Defined: `topogpt2_grid_scaler.py:888`
- Doc: Execute the full scaling pipeline. Returns per-step result dicts.

### _build_target_config `def _build_target_config(self, mod, src_cfg, tgt_d)`
- Defined: `topogpt2_grid_scaler.py:1001`
- Doc: Construct a target config with new D_MODEL, preserving torus topology.

### _infer_n_heads `def _infer_n_heads(tgt_d, src_n_heads)`
- Defined: `topogpt2_grid_scaler.py:1018`
- Doc: Find the largest divisor of tgt_d that keeps D_HEAD >= 8.

### _infer_n_kv_heads `def _infer_n_kv_heads(tgt_d, tgt_n_heads, src_n_heads, src_n_kv)`
- Defined: `topogpt2_grid_scaler.py:1033`

### _print_summary `def _print_summary(self, results, src_cfg)`
- Defined: `topogpt2_grid_scaler.py:1047`

### _cfg_dict `def _cfg_dict(c)`
- Defined: `topogpt2_grid_scaler.py:770`

## topogpt2_multi_inference.py

### _setup_logger `def _setup_logger(name, level)`
- Defined: `topogpt2_multi_inference.py:85`

### _fmt_params `def _fmt_params(n)`
- Defined: `topogpt2_multi_inference.py:666`
- Doc: Format parameter counts as human-readable strings (25.1M, 147.5M).

### build_parser `def build_parser()`
- Defined: `topogpt2_multi_inference.py:707`
- Doc: Build the CLI argument parser.

### config_from_args `def config_from_args(args)`
- Defined: `topogpt2_multi_inference.py:780`
- Doc: Build a RunConfig from parsed CLI arguments.

### main `def main()`
- Defined: `topogpt2_multi_inference.py:800`
- Doc: CLI entry point.

### load `def load(self, path)`
- Defined: `topogpt2_multi_inference.py:100`
- Doc: Return the imported module, reusing the cached copy if available.

### resolve `def resolve(self, sources)`
- Defined: `topogpt2_multi_inference.py:127`
- Doc: Expand directories and glob patterns into a sorted list of paths.

### load `def load(self, path, device)`
- Defined: `topogpt2_multi_inference.py:167`
- Doc: Return (state_dict, optional_embedded_config).

### _load_safetensors `def _load_safetensors(self, path, device)`
- Defined: `topogpt2_multi_inference.py:183`

### _load_torch `def _load_torch(self, path, device)`
- Defined: `topogpt2_multi_inference.py:191`

### reconstruct `def reconstruct(self, mod, state_dict, embedded)`
- Defined: `topogpt2_multi_inference.py:222`
- Doc: Return a TopoGPT2Config matching the loaded weights.

### _infer `def _infer(self, mod, sd)`
- Defined: `topogpt2_multi_inference.py:243`

### _infer_d_head `def _infer_d_head(sd)`
- Defined: `topogpt2_multi_inference.py:278`

### _infer_n_kv `def _infer_n_kv(sd, d_head, n_heads)`
- Defined: `topogpt2_multi_inference.py:285`

### _infer_max_seq `def _infer_max_seq(sd)`
- Defined: `topogpt2_multi_inference.py:295`

### _infer_torus `def _infer_torus(sd)`
- Defined: `topogpt2_multi_inference.py:302`

### get `def get(self, mod)`
- Defined: `topogpt2_multi_inference.py:320`
- Doc: Return a shared tokenizer instance (built once per process).

### __init__ `def __init__(self, cfg, device)`
- Defined: `topogpt2_multi_inference.py:330`

### generate `def generate(self, model, tokenizer, prompt)`
- Defined: `topogpt2_multi_inference.py:334`
- Doc: Run generation and return (full_text, n_new_tokens, elapsed_s).

### _fast_generate `def _fast_generate(self, model, input_ids)`
- Defined: `topogpt2_multi_inference.py:361`

### _manual_generate `def _manual_generate(self, model, input_ids)`
- Defined: `topogpt2_multi_inference.py:372`

### _apply_repetition_penalty `def _apply_repetition_penalty(logits, generated, penalty)`
- Defined: `topogpt2_multi_inference.py:412`

### _apply_top_p `def _apply_top_p(logits, p)`
- Defined: `topogpt2_multi_inference.py:424`

### __init__ `def __init__(self, cfg)`
- Defined: `topogpt2_multi_inference.py:453`

### run `def run(self)`
- Defined: `topogpt2_multi_inference.py:462`
- Doc: Execute the full multi-model inference pipeline.

### _run_one `def _run_one(self, ckpt_path, mod, tokenizer, engine)`
- Defined: `topogpt2_multi_inference.py:499`

### _make_label `def _make_label(path)`
- Defined: `topogpt2_multi_inference.py:570`
- Doc: Extract a short human-readable label from a checkpoint path.

### render `def render(self, results, prompt)`
- Defined: `topogpt2_multi_inference.py:590`
- Doc: Print prompt header, per-model outputs, and comparison table.

### _print_prompt_header `def _print_prompt_header(self, prompt)`
- Defined: `topogpt2_multi_inference.py:597`

### _print_model_output `def _print_model_output(self, r)`
- Defined: `topogpt2_multi_inference.py:605`

### _print_comparison_table `def _print_comparison_table(self, results)`
- Defined: `topogpt2_multi_inference.py:628`

### export `def export(self, results, path, prompt)`
- Defined: `topogpt2_multi_inference.py:680`
- Doc: Serialize results to JSON.

## zeroshot.py

### build_logger `def build_logger(name, level)`
- Defined: `zeroshot.py:69`
- Doc: Return a stderr logger with timestamp formatting.

### build_arg_parser `def build_arg_parser()`
- Defined: `zeroshot.py:1709`
- Doc: Construct and return the CLI argument parser.

### main `def main()`
- Defined: `zeroshot.py:1774`
- Doc: CLI entry point.

### validate_geometry `def validate_geometry(self)`
- Defined: `zeroshot.py:140`
- Doc: Raise ValueError for impossible torus configurations.

### src_nodes `def src_nodes(self)`
- Defined: `zeroshot.py:154`

### tgt_nodes `def tgt_nodes(self)`
- Defined: `zeroshot.py:158`

### __post_init__ `def __post_init__(self)`
- Defined: `zeroshot.py:222`

### hamilton_product `def hamilton_product(q1, q2)`
- Defined: `zeroshot.py:258`

### normalize `def normalize(q, eps)`
- Defined: `zeroshot.py:269`

### conjugate `def conjugate(q)`
- Defined: `zeroshot.py:273`

### rotate_vector `def rotate_vector(v, q)`
- Defined: `zeroshot.py:278`

### __init__ `def __init__(self, in_features, out_features, bias)`
- Defined: `zeroshot.py:296`

### forward `def forward(self, x)`
- Defined: `zeroshot.py:310`

### __init__ `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- Defined: `zeroshot.py:329`

### _kernel `def _kernel(self, c)`
- Defined: `zeroshot.py:344`

### _contract `def _contract(self, W, X)`
- Defined: `zeroshot.py:347`

### forward `def forward(self, x)`
- Defined: `zeroshot.py:350`

### __init__ `def __init__(self, config)`
- Defined: `zeroshot.py:382`

### _filter1d `def _filter1d(self, x, kr, ki)`
- Defined: `zeroshot.py:404`

### encode `def encode(self, x)`
- Defined: `zeroshot.py:409`

### decode `def decode(self, z)`
- Defined: `zeroshot.py:412`

### forward `def forward(self, x)`
- Defined: `zeroshot.py:415`

### process_torus_grid `def process_torus_grid(self, grid)`
- Defined: `zeroshot.py:420`

### __init__ `def __init__(self, d_model, config)`
- Defined: `zeroshot.py:443`

### _build_torus_graph `def _build_torus_graph(self)`
- Defined: `zeroshot.py:468`

### _torus_soft_assign `def _torus_soft_assign(self, phi1, phi2)`
- Defined: `zeroshot.py:484`

### _message_passing `def _message_passing(self, node_feat)`
- Defined: `zeroshot.py:495`

### forward `def forward(self, x)`
- Defined: `zeroshot.py:509`

### __init__ `def __init__(self, d_model, expansion, dropout)`
- Defined: `zeroshot.py:540`

### forward `def forward(self, x)`
- Defined: `zeroshot.py:552`

### __init__ `def __init__(self, d_model, config)`
- Defined: `zeroshot.py:565`

### _route `def _route(self, x)`
- Defined: `zeroshot.py:581`

### forward `def forward(self, x)`
- Defined: `zeroshot.py:604`

### __init__ `def __init__(self, d_head, max_seq_len)`
- Defined: `zeroshot.py:618`

### _build_cache `def _build_cache(self, seq_len)`
- Defined: `zeroshot.py:626`

### _rotate_half `def _rotate_half(x)`
- Defined: `zeroshot.py:633`

### forward `def forward(self, q, k, seq_len, offset)`
- Defined: `zeroshot.py:637`

### __init__ `def __init__(self, d_model, eps)`
- Defined: `zeroshot.py:655`

### forward `def forward(self, x)`
- Defined: `zeroshot.py:660`

### __init__ `def __init__(self, d_model, n_heads, config)`
- Defined: `zeroshot.py:671`

### forward `def forward(self, x, is_causal, past_kv)`
- Defined: `zeroshot.py:686`

### __init__ `def __init__(self, d_model, n_heads, config)`
- Defined: `zeroshot.py:725`

### _forward_impl `def _forward_impl(self, x, past_kv)`
- Defined: `zeroshot.py:734`

### forward `def forward(self, x, past_kv)`
- Defined: `zeroshot.py:743`

### __init__ `def __init__(self, config)`
- Defined: `zeroshot.py:757`

### _init_weights `def _init_weights(self)`
- Defined: `zeroshot.py:771`

### forward `def forward(self, token_ids, past_kvs)`
- Defined: `zeroshot.py:778`

### generate `def generate(self, token_ids, max_new_tokens, temperature, top_k)`
- Defined: `zeroshot.py:795`
- Doc: Top-k autoregressive generation with KV cache.

### __init__ `def __init__(self, mode)`
- Defined: `zeroshot.py:837`

### _interp2d `def _interp2d(self, tensor, tgt_h, tgt_w)`
- Defined: `zeroshot.py:840`
- Doc: Interpolate a 4D real tensor [in_q, out_q, h, w] to [in_q, out_q, tgt_h, tgt_w].

### transfer `def transfer(self, src_layer, tgt_layer)`
- Defined: `zeroshot.py:856`
- Doc: Copy and interpolate all kernel parameters from src_layer to tgt_layer.

### __init__ `def __init__(self, mode)`
- Defined: `zeroshot.py:886`

### transfer `def transfer(self, src_embed, src_radial, src_angular, tgt_embed, tgt_radial, tgt_angular)`
- Defined: `zeroshot.py:889`
- Doc: Interpolate src_embed [src_R*src_A, D] into tgt_embed [tgt_R*tgt_A, D].

### __init__ `def __init__(self, spec_interp_mode, node_interp_mode, logger)`
- Defined: `zeroshot.py:936`

### expand `def expand(self, src, tgt)`
- Defined: `zeroshot.py:946`
- Doc: Mutates tgt in-place to carry the expanded weights of src.

### __init__ `def __init__(self, spec_interp_mode, node_interp_mode, logger)`
- Defined: `zeroshot.py:1018`

### expand `def expand(self, src, tgt)`
- Defined: `zeroshot.py:1031`
- Doc: Mutates tgt in-place.

### __init__ `def __init__(self, spec_interp_mode, node_interp_mode, logger)`
- Defined: `zeroshot.py:1072`

### expand `def expand(self, src, tgt)`
- Defined: `zeroshot.py:1085`
- Doc: Expand src into tgt.  Returns tgt with all weights transferred.

### __init__ `def __init__(self, logger)`
- Defined: `zeroshot.py:1126`

### load `def load(self, path, model, device)`
- Defined: `zeroshot.py:1133`
- Doc: Load weights into model from path.  Returns the metadata dict.

### save `def save(self, path, model, metadata)`
- Defined: `zeroshot.py:1177`
- Doc: Save model weights to path.

### __init__ `def __init__(self, logger)`
- Defined: `zeroshot.py:1286`

### _load_shapes `def _load_shapes(self, path)`
- Defined: `zeroshot.py:1289`
- Doc: Return {key: shape} for every tensor in the checkpoint.

### _load_metadata `def _load_metadata(self, path)`
- Defined: `zeroshot.py:1304`
- Doc: Return safetensors string metadata dict (empty when unavailable).

### probe `def probe(self, path, fallback_radial, fallback_angular)`
- Defined: `zeroshot.py:1315`
- Doc: Infer CheckpointArch from the checkpoint at path.

### _infer_d_head_fallback `def _infer_d_head_fallback(d_model, q_out, k_out)`
- Defined: `zeroshot.py:1433`
- Doc: Fallback d_head inference when rope.inv_freq is absent.

### __init__ `def __init__(self, logger)`
- Defined: `zeroshot.py:1474`

### validate `def validate(self, model, prompt)`
- Defined: `zeroshot.py:1477`
- Doc: Return True if all checks pass, False otherwise.

### __init__ `def __init__(self, exp_cfg, logger)`
- Defined: `zeroshot.py:1565`

### _config_from_arch `def _config_from_arch(self, arch, torus_radial, torus_angular)`
- Defined: `zeroshot.py:1570`
- Doc: Build a TopoGPT2Config whose tensor dimensions exactly match arch.

### _build_metadata_for_save `def _build_metadata_for_save(self, src_meta, arch, tgt_radial, tgt_angular)`
- Defined: `zeroshot.py:1609`

### run `def run(self)`
- Defined: `zeroshot.py:1631`
- Doc: Execute the full expansion pipeline.  Returns the expanded model.
