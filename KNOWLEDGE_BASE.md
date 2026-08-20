# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 12 | **Total Symbols Extracted:** 1020 | **Total Imports:** 211

<!-- ranking_model: v1.0 | weights: {ppr:0.45,auth:0.2,test:0.15,doc:0.1,fresh:0.1} | alpha:0.85 | commit:75d209c | date:2026-07-18 -->


## Table of Contents

1. [Statistics Dashboard](#statistics-dashboard)
2. [Architectural Layers](#architectural-layers)
3. [Ranked Context](#ranked-context)
4. [God Nodes](#god-nodes)
5. [Suggested Questions](#suggested-questions)
6. [Hotspot Analysis](#hotspot-analysis)
7. [Change Impact Analysis](#change-impact-analysis)
8. [Suggested Linting Rules](#suggested-linting-rules)
9. [Orphans](#orphans)
10. [Query Recipes](#query-recipes)
11. [Structural Knowledge Map](#structural-knowledge-map)
12. [UML Class Diagram](#uml-class-diagram)
13. [Code Property Graph](#code-property-graph)
14. [Architecture Reference](#architecture-reference)
    - [PY (11 files)](#py-11-files)
    - [SH (1 files)](#sh-1-files)

---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Total Files | 12 |
| Total Symbols | 1020 |
| Total Imports | 211 |
| Call Edges | 6593 |
| Inheritance Edges | 91 |
| Languages | 2 |
| Avg Symbols/File | 85.0 |
| Avg Imports/File | 17.6 |

### Top Files by Import Count (Fan-Out)

| File | Imports | Symbols | Language |
|------|---------|---------|----------|
| `topogpt2_embeddings_navigator.py` | 25 | 149 | py |
| `app.py` | 22 | 126 | py |
| `topogpt2_1.py` | 22 | 126 | py |
| `topogpt2_grid_scaler.py` | 20 | 54 | py |
| `quantize.py` | 19 | 115 | py |
| `topogpt2_explorer.py` | 19 | 155 | py |
| `topogpt2_multi_inference.py` | 19 | 44 | py |
| `zeroshot.py` | 19 | 97 | py |
| `reinforce.py` | 18 | 47 | py |
| `inference2.py` | 17 | 87 | py |

---

## Architectural Layers

Auto-detected from path patterns, naming conventions, and imported frameworks.

| Layer | Files |
|-------|-------|
| utility | 11 |
| infrastructure | 1 |

### utility

- `app.py` (py, 126 symbols)
- `inference.py` (py, 20 symbols)
- `inference2.py` (py, 87 symbols)
- `install.sh` (sh, 0 symbols)
- `quantize.py` (py, 115 symbols)
- `reinforce.py` (py, 47 symbols)
- `topogpt2_1.py` (py, 126 symbols)
- `topogpt2_explorer.py` (py, 155 symbols)
- `topogpt2_grid_scaler.py` (py, 54 symbols)
- `topogpt2_multi_inference.py` (py, 44 symbols)
- `zeroshot.py` (py, 97 symbols)

### infrastructure

- `topogpt2_embeddings_navigator.py` (py, 149 symbols)

---

## Ranked Context

Files ranked by composite score for the current query context. The ranking combines Personalized PageRank (query relevance), global authority, test coverage, documentation coverage, and code freshness. Model: v1.0.

| Rank | File | Composite | PPR | Authority | Test | Doc |
|------|------|-----------|-----|-----------|------|-----|
| 1 | `topogpt2_grid_scaler.py` | 0.0593 | 0.0000 | 0.0000 | 0.00 | 0.59 |
| 2 | `topogpt2_multi_inference.py` | 0.0591 | 0.0000 | 0.0000 | 0.00 | 0.59 |
| 3 | `app.py` | 0.0548 | 0.0000 | 0.0000 | 0.00 | 0.55 |
| 4 | `topogpt2_1.py` | 0.0548 | 0.0000 | 0.0000 | 0.00 | 0.55 |
| 5 | `zeroshot.py` | 0.0454 | 0.0000 | 0.0000 | 0.00 | 0.45 |
| 6 | `topogpt2_explorer.py` | 0.0406 | 0.0000 | 0.0000 | 0.00 | 0.41 |
| 7 | `topogpt2_embeddings_navigator.py` | 0.0369 | 0.0000 | 0.0000 | 0.00 | 0.37 |
| 8 | `inference2.py` | 0.0333 | 0.0000 | 0.0000 | 0.00 | 0.33 |
| 9 | `inference.py` | 0.0250 | 0.0000 | 0.0000 | 0.00 | 0.25 |
| 10 | `reinforce.py` | 0.0191 | 0.0000 | 0.0000 | 0.00 | 0.19 |

---

## God Nodes

Most architecturally central files ranked by combined import/export degree and symbol richness.

| File | Score | Connections | PageRank |
|------|-------|-------------|----------|
| `topogpt2_explorer.py` | 15.5 | | 0.0000 |
| `topogpt2_embeddings_navigator.py` | 14.9 | | 0.0000 |
| `app.py` | 12.6 | | 0.0000 |
| `topogpt2_1.py` | 12.6 | | 0.0000 |
| `quantize.py` | 11.5 | | 0.0000 |
| `zeroshot.py` | 9.7 | | 0.0000 |
| `inference2.py` | 8.7 | | 0.0000 |
| `topogpt2_grid_scaler.py` | 5.4 | | 0.0000 |
| `reinforce.py` | 4.7 | | 0.0000 |
| `topogpt2_multi_inference.py` | 4.4 | | 0.0000 |

---

## Suggested Questions

Auto-generated exploration prompts based on graph structure:

- What does topogpt2_explorer.py depend on, and what depends on it? (0 connections)
- What does topogpt2_embeddings_navigator.py depend on, and what depends on it? (0 connections)
- What does app.py depend on, and what depends on it? (0 connections)
- What is TopoGPT2Config in app.py and how is it used?
- What is InferenceConfig in inference.py and how is it used?

---

## Hotspot Analysis

Files ranked by combined complexity (symbol count) and centrality (connection count). High-scoring files are architecturally critical and may need refactoring attention.

| File | Complexity | Centrality | Combined | Symbols | Connections |
|------|-----------|------------|----------|---------|-------------|
| `topogpt2_grid_scaler.py` | 0.348 | 0.800 | 0.619 | 54 | 20 |
| `topogpt2_multi_inference.py` | 0.284 | 0.760 | 0.570 | 44 | 19 |
| `app.py` | 0.813 | 0.880 | 0.853 | 126 | 22 |
| `topogpt2_1.py` | 0.813 | 0.880 | 0.853 | 126 | 22 |
| `zeroshot.py` | 0.626 | 0.760 | 0.706 | 97 | 19 |
| `topogpt2_explorer.py` | 1.000 | 0.760 | 0.856 | 155 | 19 |
| `topogpt2_embeddings_navigator.py` | 0.961 | 1.000 | 0.985 | 149 | 25 |
| `inference2.py` | 0.561 | 0.680 | 0.632 | 87 | 17 |
| `inference.py` | 0.129 | 0.440 | 0.316 | 20 | 11 |
| `reinforce.py` | 0.303 | 0.720 | 0.553 | 47 | 18 |
| `quantize.py` | 0.742 | 0.760 | 0.753 | 115 | 19 |
| `install.sh` | 0.000 | 0.000 | 0.000 | 0 | 0 |

---

## Change Impact Analysis

Files sorted by how many other files would be affected if they changed. High-impact files should be changed with caution.

| File | Direct Dependents | Transitive Dependents | Total Impact |
|------|------------------|----------------------|--------------|
| `app.py` | 0 | 0 | 0 |
| `inference.py` | 0 | 0 | 0 |
| `inference2.py` | 0 | 0 | 0 |
| `install.sh` | 0 | 0 | 0 |
| `quantize.py` | 0 | 0 | 0 |
| `reinforce.py` | 0 | 0 | 0 |
| `topogpt2_1.py` | 0 | 0 | 0 |
| `topogpt2_embeddings_navigator.py` | 0 | 0 | 0 |
| `topogpt2_explorer.py` | 0 | 0 | 0 |
| `topogpt2_grid_scaler.py` | 0 | 0 | 0 |
| `topogpt2_multi_inference.py` | 0 | 0 | 0 |
| `zeroshot.py` | 0 | 0 | 0 |

---

## Suggested Linting Rules

Automatically suggested linting and security rules based on patterns detected in the codebase. These can be exported as Semgrep rules using the `--export-rules` flag.

| Rule ID | Severity | Description | Language | Matches |
|---------|----------|-------------|----------|---------|
| `RM001` | info | Large number of functions in py: 801 total | py | 801 |
| `RM002` | info | Print statement found (consider logging instead) | python | 55 |

---

## Orphans

Files with no documentation or low connectivity. These are candidates for documentation investment or cleanup.

- `install.sh` (0 symbols, no doc)

---

## Query Recipes

Example queries you can run against this knowledge base using the ranking engine:

```
# Find files most relevant to a concept
readmenator query "Where is the import resolver implemented?"

# Rank files by relevance to a topic
readmenator query "How does documentation generation work?"

# Explain why a file ranks highly
readmenator query "explain readmenator/_documentation.py"

# Trace dependency paths with ranked context
readmenator query "path from CLI to exporter"
```

The ranking model uses the following signals:

- **Personalized PageRank** (45% weight): query-specific relevance via seed propagation
- **Global Authority** (20% weight): structural importance via standard PageRank
- **Test Coverage** (15% weight): fraction of symbols referenced in test files
- **Doc Coverage** (10% weight): presence of docstrings and file-level docs
- **Freshness** (10% weight): recent modification activity

Results include score decomposition and justification paths for each ranked item.

---

## Structural Knowledge Map

```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    topogpt2_embeddings_navigator_py["topogpt2_embeddings_navigator.py (py)"]
    class topogpt2_embeddings_navigator_py mod;
    topogpt2_embeddings_navigator_py_ThemeTokens["ThemeTokens"]
    class topogpt2_embeddings_navigator_py_ThemeTokens cls;
    topogpt2_embeddings_navigator_py --> topogpt2_embeddings_navigator_py_ThemeTokens
    topogpt2_embeddings_navigator_py_PlotTheme["PlotTheme"]
    class topogpt2_embeddings_navigator_py_PlotTheme cls;
    topogpt2_embeddings_navigator_py --> topogpt2_embeddings_navigator_py_PlotTheme
    topogpt2_embeddings_navigator_py_SamplingLimits["SamplingLimits"]
    class topogpt2_embeddings_navigator_py_SamplingLimits cls;
    topogpt2_embeddings_navigator_py --> topogpt2_embeddings_navigator_py_SamplingLimits
    topogpt2_embeddings_navigator_py_MetricsConfig["MetricsConfig"]
    class topogpt2_embeddings_navigator_py_MetricsConfig cls;
    topogpt2_embeddings_navigator_py --> topogpt2_embeddings_navigator_py_MetricsConfig
    topogpt2_embeddings_navigator_py_ProjectionConfig["ProjectionConfig"]
    class topogpt2_embeddings_navigator_py_ProjectionConfig cls;
    topogpt2_embeddings_navigator_py --> topogpt2_embeddings_navigator_py_ProjectionConfig
    app_py["app.py (py)"]
    class app_py mod;
    topogpt2_1_py["topogpt2_1.py (py)"]
    class topogpt2_1_py mod;
    topogpt2_grid_scaler_py["topogpt2_grid_scaler.py (py)"]
    class topogpt2_grid_scaler_py mod;
    topogpt2_explorer_py["topogpt2_explorer.py (py)"]
    class topogpt2_explorer_py mod;
    quantize_py["quantize.py (py)"]
    class quantize_py mod;
    zeroshot_py["zeroshot.py (py)"]
    class zeroshot_py mod;
    topogpt2_multi_inference_py["topogpt2_multi_inference.py (py)"]
    class topogpt2_multi_inference_py mod;
    reinforce_py["reinforce.py (py)"]
    class reinforce_py mod;
    inference2_py["inference2.py (py)"]
    class inference2_py mod;
    inference_py["inference.py (py)"]
    class inference_py mod;
    install_sh["install.sh (sh)"]
    class install_sh mod;
    ext_torch["torch"]
    class ext_torch ext;
    app_py -.->|imports| ext_torch
    ext_torch_nn["torch.nn"]
    class ext_torch_nn ext;
    app_py -.->|imports| ext_torch_nn
    ext_torch_nn_functional["torch.nn.functional"]
    class ext_torch_nn_functional ext;
    app_py -.->|imports| ext_torch_nn_functional
    ext_torch_utils_checkpoint["torch.utils.checkpoint"]
    class ext_torch_utils_checkpoint ext;
    app_py -.->|imports| ext_torch_utils_checkpoint
    ext_safetensors_torch["safetensors.torch"]
    class ext_safetensors_torch ext;
    app_py -.->|imports| ext_safetensors_torch
    ext_numpy["numpy"]
    class ext_numpy ext;
    app_py -.->|imports| ext_numpy
    ext_math["math"]
    class ext_math ext;
    app_py -.->|imports| ext_math
    ext_os["os"]
    class ext_os ext;
    app_py -.->|imports| ext_os
    ext_sys["sys"]
    class ext_sys ext;
    app_py -.->|imports| ext_sys
    ext_time["time"]
    class ext_time ext;
    app_py -.->|imports| ext_time
    ext_json["json"]
    class ext_json ext;
    app_py -.->|imports| ext_json
    ext_hashlib["hashlib"]
    class ext_hashlib ext;
    app_py -.->|imports| ext_hashlib
    ext_logging["logging"]
    class ext_logging ext;
    app_py -.->|imports| ext_logging
    ext_warnings["warnings"]
    class ext_warnings ext;
    app_py -.->|imports| ext_warnings
    ext_argparse["argparse"]
    class ext_argparse ext;
    app_py -.->|imports| ext_argparse
    ext_datetime["datetime"]
    class ext_datetime ext;
    app_py -.->|imports| ext_datetime
    ext_typing["typing"]
    class ext_typing ext;
    app_py -.->|imports| ext_typing
    ext_dataclasses["dataclasses"]
    class ext_dataclasses ext;
    app_py -.->|imports| ext_dataclasses
    ext_collections["collections"]
    class ext_collections ext;
    app_py -.->|imports| ext_collections
    ext_tiktoken["tiktoken"]
    class ext_tiktoken ext;
    app_py -.->|imports| ext_tiktoken
    ext_datasets["datasets"]
    class ext_datasets ext;
    app_py -.->|imports| ext_datasets
    ext_shutil["shutil"]
    class ext_shutil ext;
    app_py -.->|imports| ext_shutil
    inference_py -.->|imports| ext_torch
    inference_py -.->|imports| ext_torch_nn_functional
    ext_importlib_util["importlib.util"]
    class ext_importlib_util ext;
    inference_py -.->|imports| ext_importlib_util
    inference_py -.->|imports| ext_sys
    inference_py -.->|imports| ext_os
    inference_py -.->|imports| ext_argparse
    inference_py -.->|imports| ext_logging
    inference_py -.->|imports| ext_time
    inference_py -.->|imports| ext_dataclasses
    inference_py -.->|imports| ext_typing
    inference_py -.->|imports| ext_safetensors_torch
    ext___future__["__future__"]
    class ext___future__ ext;
    inference2_py -.->|imports| ext___future__
    inference2_py -.->|imports| ext_argparse
    inference2_py -.->|imports| ext_logging
    inference2_py -.->|imports| ext_math
    inference2_py -.->|imports| ext_os
    inference2_py -.->|imports| ext_sys
    inference2_py -.->|imports| ext_time
    inference2_py -.->|imports| ext_warnings
    inference2_py -.->|imports| ext_dataclasses
    ext_pathlib["pathlib"]
    class ext_pathlib ext;
    inference2_py -.->|imports| ext_pathlib
    inference2_py -.->|imports| ext_typing
    inference2_py -.->|imports| ext_torch
    inference2_py -.->|imports| ext_torch_nn
    inference2_py -.->|imports| ext_torch_nn_functional
    inference2_py -.->|imports| ext_safetensors_torch
    inference2_py -.->|imports| ext_tiktoken
    ext_safetensors["safetensors"]
    class ext_safetensors ext;
    inference2_py -.->|imports| ext_safetensors
    quantize_py -.->|imports| ext_argparse
    quantize_py -.->|imports| ext_json
    quantize_py -.->|imports| ext_logging
    quantize_py -.->|imports| ext_math
    quantize_py -.->|imports| ext_os
    quantize_py -.->|imports| ext_sys
    quantize_py -.->|imports| ext_time
    ext_abc["abc"]
    class ext_abc ext;
    quantize_py -.->|imports| ext_abc
    quantize_py -.->|imports| ext_collections
    quantize_py -.->|imports| ext_dataclasses
    ext_enum["enum"]
    class ext_enum ext;
    quantize_py -.->|imports| ext_enum
    quantize_py -.->|imports| ext_typing
    quantize_py -.->|imports| ext_numpy
    quantize_py -.->|imports| ext_torch
    quantize_py -.->|imports| ext_torch_nn
    quantize_py -.->|imports| ext_torch_nn_functional
    quantize_py -.->|imports| ext_safetensors_torch
    ext_torch_utils_data["torch.utils.data"]
    class ext_torch_utils_data ext;
    quantize_py -.->|imports| ext_torch_utils_data
    quantize_py -.->|imports| ext_tiktoken
    reinforce_py -.->|imports| ext_torch
    reinforce_py -.->|imports| ext_torch_nn
    reinforce_py -.->|imports| ext_torch_nn_functional
    reinforce_py -.->|imports| ext_safetensors_torch
    reinforce_py -.->|imports| ext_numpy
    reinforce_py -.->|imports| ext_math
    reinforce_py -.->|imports| ext_os
    reinforce_py -.->|imports| ext_sys
    reinforce_py -.->|imports| ext_time
    reinforce_py -.->|imports| ext_json
    reinforce_py -.->|imports| ext_logging
    reinforce_py -.->|imports| ext_argparse
    reinforce_py -.->|imports| ext_importlib_util
    reinforce_py -.->|imports| ext_datetime
    reinforce_py -.->|imports| ext_typing
    reinforce_py -.->|imports| ext_dataclasses
    reinforce_py -.->|imports| ext_collections
    reinforce_py -.->|imports| ext_enum
    topogpt2_1_py -.->|imports| ext_torch
    topogpt2_1_py -.->|imports| ext_torch_nn
    topogpt2_1_py -.->|imports| ext_torch_nn_functional
    topogpt2_1_py -.->|imports| ext_torch_utils_checkpoint
    topogpt2_1_py -.->|imports| ext_safetensors_torch
    topogpt2_1_py -.->|imports| ext_numpy
    topogpt2_1_py -.->|imports| ext_math
    topogpt2_1_py -.->|imports| ext_os
    topogpt2_1_py -.->|imports| ext_sys
    topogpt2_1_py -.->|imports| ext_time
    topogpt2_1_py -.->|imports| ext_json
    topogpt2_1_py -.->|imports| ext_hashlib
    topogpt2_1_py -.->|imports| ext_logging
    topogpt2_1_py -.->|imports| ext_warnings
    topogpt2_1_py -.->|imports| ext_argparse
    topogpt2_1_py -.->|imports| ext_datetime
    topogpt2_1_py -.->|imports| ext_typing
    topogpt2_1_py -.->|imports| ext_dataclasses
    topogpt2_1_py -.->|imports| ext_collections
    topogpt2_1_py -.->|imports| ext_tiktoken
    topogpt2_1_py -.->|imports| ext_datasets
    topogpt2_1_py -.->|imports| ext_shutil
    topogpt2_embeddings_navigator_py -.->|imports| ext___future__
    topogpt2_embeddings_navigator_py -.->|imports| ext_hashlib
    ext_io["io"]
    class ext_io ext;
    topogpt2_embeddings_navigator_py -.->|imports| ext_io
    topogpt2_embeddings_navigator_py -.->|imports| ext_math
    ext_re["re"]
    class ext_re ext;
    topogpt2_embeddings_navigator_py -.->|imports| ext_re
    topogpt2_embeddings_navigator_py -.->|imports| ext_abc
    topogpt2_embeddings_navigator_py -.->|imports| ext_dataclasses
    topogpt2_embeddings_navigator_py -.->|imports| ext_pathlib
    topogpt2_embeddings_navigator_py -.->|imports| ext_typing
    topogpt2_embeddings_navigator_py -.->|imports| ext_numpy
    ext_plotly_graph_objects["plotly.graph_objects"]
    class ext_plotly_graph_objects ext;
    topogpt2_embeddings_navigator_py -.->|imports| ext_plotly_graph_objects
    ext_streamlit["streamlit"]
    class ext_streamlit ext;
    topogpt2_embeddings_navigator_py -.->|imports| ext_streamlit
    topogpt2_embeddings_navigator_py -.->|imports| ext_torch
    ext_plotly_subplots["plotly.subplots"]
    class ext_plotly_subplots ext;
    topogpt2_embeddings_navigator_py -.->|imports| ext_plotly_subplots
    ext_scipy["scipy"]
    class ext_scipy ext;
    topogpt2_embeddings_navigator_py -.->|imports| ext_scipy
    ext_scipy_sparse["scipy.sparse"]
    class ext_scipy_sparse ext;
    topogpt2_embeddings_navigator_py -.->|imports| ext_scipy_sparse
    topogpt2_embeddings_navigator_py -.->|imports| ext_scipy_sparse
    ext_scipy_spatial_distance["scipy.spatial.distance"]
    class ext_scipy_spatial_distance ext;
    topogpt2_embeddings_navigator_py -.->|imports| ext_scipy_spatial_distance
    ext_sklearn_decomposition["sklearn.decomposition"]
    class ext_sklearn_decomposition ext;
    topogpt2_embeddings_navigator_py -.->|imports| ext_sklearn_decomposition
    ext_sklearn_manifold["sklearn.manifold"]
    class ext_sklearn_manifold ext;
    topogpt2_embeddings_navigator_py -.->|imports| ext_sklearn_manifold
    ext_sklearn_neighbors["sklearn.neighbors"]
    class ext_sklearn_neighbors ext;
    topogpt2_embeddings_navigator_py -.->|imports| ext_sklearn_neighbors
    topogpt2_embeddings_navigator_py -.->|imports| ext_importlib_util
    topogpt2_embeddings_navigator_py -.->|imports| ext_sys
    topogpt2_embeddings_navigator_py -.->|imports| ext_safetensors_torch
    ext_umap["umap"]
    class ext_umap ext;
    topogpt2_embeddings_navigator_py -.->|imports| ext_umap
    topogpt2_explorer_py -.->|imports| ext___future__
    topogpt2_explorer_py -.->|imports| ext_io
    topogpt2_explorer_py -.->|imports| ext_json
    topogpt2_explorer_py -.->|imports| ext_math
    topogpt2_explorer_py -.->|imports| ext_re
    topogpt2_explorer_py -.->|imports| ext_abc
    topogpt2_explorer_py -.->|imports| ext_dataclasses
    topogpt2_explorer_py -.->|imports| ext_pathlib
    topogpt2_explorer_py -.->|imports| ext_typing
    topogpt2_explorer_py -.->|imports| ext_numpy
    topogpt2_explorer_py -.->|imports| ext_plotly_graph_objects
    topogpt2_explorer_py -.->|imports| ext_streamlit
    topogpt2_explorer_py -.->|imports| ext_torch
    topogpt2_explorer_py -.->|imports| ext_plotly_subplots
    topogpt2_explorer_py -.->|imports| ext_scipy
    topogpt2_explorer_py -.->|imports| ext_scipy
    topogpt2_explorer_py -.->|imports| ext_sklearn_decomposition
    ext_sklearn_random_projection["sklearn.random_projection"]
    class ext_sklearn_random_projection ext;
    topogpt2_explorer_py -.->|imports| ext_sklearn_random_projection
    topogpt2_explorer_py -.->|imports| ext_safetensors_torch
    topogpt2_grid_scaler_py -.->|imports| ext___future__
    topogpt2_grid_scaler_py -.->|imports| ext_argparse
    topogpt2_grid_scaler_py -.->|imports| ext_json
    topogpt2_grid_scaler_py -.->|imports| ext_logging
    topogpt2_grid_scaler_py -.->|imports| ext_math
    topogpt2_grid_scaler_py -.->|imports| ext_os
    topogpt2_grid_scaler_py -.->|imports| ext_re
    topogpt2_grid_scaler_py -.->|imports| ext_sys
    topogpt2_grid_scaler_py -.->|imports| ext_time
    topogpt2_grid_scaler_py -.->|imports| ext_dataclasses
    topogpt2_grid_scaler_py -.->|imports| ext_datetime
    topogpt2_grid_scaler_py -.->|imports| ext_pathlib
    topogpt2_grid_scaler_py -.->|imports| ext_typing
    topogpt2_grid_scaler_py -.->|imports| ext_numpy
    topogpt2_grid_scaler_py -.->|imports| ext_torch
    topogpt2_grid_scaler_py -.->|imports| ext_torch_nn_functional
    topogpt2_grid_scaler_py -.->|imports| ext_importlib_util
    topogpt2_grid_scaler_py -.->|imports| ext_warnings
    topogpt2_grid_scaler_py -.->|imports| ext_warnings
    topogpt2_grid_scaler_py -.->|imports| ext_safetensors_torch
    topogpt2_multi_inference_py -.->|imports| ext___future__
    topogpt2_multi_inference_py -.->|imports| ext_argparse
    ext_gc["gc"]
    class ext_gc ext;
    topogpt2_multi_inference_py -.->|imports| ext_gc
    topogpt2_multi_inference_py -.->|imports| ext_importlib_util
    topogpt2_multi_inference_py -.->|imports| ext_json
    topogpt2_multi_inference_py -.->|imports| ext_logging
    topogpt2_multi_inference_py -.->|imports| ext_math
    topogpt2_multi_inference_py -.->|imports| ext_os
    topogpt2_multi_inference_py -.->|imports| ext_re
    topogpt2_multi_inference_py -.->|imports| ext_sys
    topogpt2_multi_inference_py -.->|imports| ext_time
    topogpt2_multi_inference_py -.->|imports| ext_dataclasses
    topogpt2_multi_inference_py -.->|imports| ext_pathlib
    topogpt2_multi_inference_py -.->|imports| ext_typing
    topogpt2_multi_inference_py -.->|imports| ext_torch
    topogpt2_multi_inference_py -.->|imports| ext_torch_nn_functional
    topogpt2_multi_inference_py -.->|imports| ext_safetensors_torch
    topogpt2_multi_inference_py -.->|imports| ext_warnings
    ext_glob["glob"]
    class ext_glob ext;
    topogpt2_multi_inference_py -.->|imports| ext_glob
    zeroshot_py -.->|imports| ext___future__
    zeroshot_py -.->|imports| ext_argparse
    zeroshot_py -.->|imports| ext_json
    zeroshot_py -.->|imports| ext_logging
    zeroshot_py -.->|imports| ext_math
    zeroshot_py -.->|imports| ext_os
    zeroshot_py -.->|imports| ext_sys
    zeroshot_py -.->|imports| ext_warnings
    zeroshot_py -.->|imports| ext_dataclasses
    zeroshot_py -.->|imports| ext_pathlib
    zeroshot_py -.->|imports| ext_typing
    zeroshot_py -.->|imports| ext_torch
    zeroshot_py -.->|imports| ext_torch_nn
    zeroshot_py -.->|imports| ext_torch_nn_functional
    zeroshot_py -.->|imports| ext_safetensors_torch
    zeroshot_py -.->|imports| ext_tiktoken
    zeroshot_py -.->|imports| ext_safetensors
    zeroshot_py -.->|imports| ext_safetensors
    zeroshot_py -.->|imports| ext_tiktoken
```

---

## UML Class Diagram

Auto-generated Mermaid class diagram from parsed class-level symbols. Shows classes, structs, interfaces, traits, and their methods with inheritance and dependency relationships.

```mermaid
classDiagram
  class app_py_TopoGPT2Config {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_QuaternionOps {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_QuaternionLinear {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_QuaternionSpectralLayer {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_SpectralAutoencoder {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_QuaternionTorusBrain {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_RotaryEmbedding {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_RMSNorm {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_SwiGLU {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_TopoMoEBrain {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_MultiHeadAttention {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_TopoGPT2Layer {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_TopoGPT2 {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_BPETokenizer {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_CorpusDownloader {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_TokenizedDataset {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_CheckpointManager {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_TopoGPT2Trainer {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_MechanisticMetrics {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_Phase0_KernelOptimizer {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_Phase1_BatchProspector {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_Phase2_SeedMiner {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_Phase4_AnnealingRefiner {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class app_py_TopoPhasePipeline {
    <<class>>
    +setup_logger(name, level)
    +set_seed(seed, device)
    +main()
    +__post_init__(self)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
    +conjugate(q)
    +rotate_vector(v, q)
    +__init__(self, in_features, out_features, bias)
    +forward(self, x)
  }
  class inference_py_InferenceConfig {
    <<class>>
    +_load_source_module(path)
    +parse_arguments()
    +__init__(self, logger)
    +inspect_kq_head_count(self, checkpoint_path, d_model, n_heads)
    +patch_config(self, config, source_module)
    +_resolve_preset(self, scale)
    +__init__(self, checkpoint_name, logger)
    +load_model(self, config, source_module)
    +__init__(self, config, logger)
    +generate(self, model, tokenizer, prompt_text)
  }
  class inference_py_CheckpointInspector {
    <<class>>
    +_load_source_module(path)
    +parse_arguments()
    +__init__(self, logger)
    +inspect_kq_head_count(self, checkpoint_path, d_model, n_heads)
    +patch_config(self, config, source_module)
    +_resolve_preset(self, scale)
    +__init__(self, checkpoint_name, logger)
    +load_model(self, config, source_module)
    +__init__(self, config, logger)
    +generate(self, model, tokenizer, prompt_text)
  }
  class inference_py_ModelLoader {
    <<class>>
    +_load_source_module(path)
    +parse_arguments()
    +__init__(self, logger)
    +inspect_kq_head_count(self, checkpoint_path, d_model, n_heads)
    +patch_config(self, config, source_module)
    +_resolve_preset(self, scale)
    +__init__(self, checkpoint_name, logger)
    +load_model(self, config, source_module)
    +__init__(self, config, logger)
    +generate(self, model, tokenizer, prompt_text)
  }
  class inference_py_GenerationEngine {
    <<class>>
    +_load_source_module(path)
    +parse_arguments()
    +__init__(self, logger)
    +inspect_kq_head_count(self, checkpoint_path, d_model, n_heads)
    +patch_config(self, config, source_module)
    +_resolve_preset(self, scale)
    +__init__(self, checkpoint_name, logger)
    +load_model(self, config, source_module)
    +__init__(self, config, logger)
    +generate(self, model, tokenizer, prompt_text)
  }
  class inference_py_InferenceRunner {
    <<class>>
    +_load_source_module(path)
    +parse_arguments()
    +__init__(self, logger)
    +inspect_kq_head_count(self, checkpoint_path, d_model, n_heads)
    +patch_config(self, config, source_module)
    +_resolve_preset(self, scale)
    +__init__(self, checkpoint_name, logger)
    +load_model(self, config, source_module)
    +__init__(self, config, logger)
    +generate(self, model, tokenizer, prompt_text)
  }
  class inference2_py_InferenceConfig {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_BPETokenizer {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_QuaternionOps {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_QuaternionLinear {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_QuaternionSpectralLayer {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_SpectralAutoencoder {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_QuaternionTorusBrain {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_SwiGLU {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_TopoMoEBrain {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_RotaryEmbedding {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_RMSNorm {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_MultiHeadAttention {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_TopoGPT2Layer {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_TopoGPT2 {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_ModelConfig {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_CheckpointArchProber {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_CheckpointLoader {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_Sampler {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_GenerationEngine {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_ResultPrinter {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
  class inference2_py_InferencePipeline {
    <<class>>
    +build_logger(name, level)
    +build_arg_parser()
    +main()
    +validate(self)
    +__init__(self)
    +encode(self, text)
    +decode(self, token_ids)
    +decode_single(self, token_id)
    +hamilton_product(q1, q2)
    +normalize(q, eps)
  }
```

---

## Code Property Graph

Machine-readable Code Property Graph (CPG) in JSON-LD format. This block allows AI agents to parse the full structural graph without additional file reads. Compatible with GraphRAG pipelines.

```json
{"@context": "https://schema.org", "analysis": {"communities": [], "god_nodes": [{"node_id": "topogpt2_explorer.py", "score": 15.5}, {"node_id": "topogpt2_embeddings_navigator.py", "score": 14.9}, {"node_id": "app.py", "score": 12.6}, {"node_id": "topogpt2_1.py", "score": 12.6}, {"node_id": "quantize.py", "score": 11.5}, {"node_id": "zeroshot.py", "score": 9.7}, {"node_id": "inference2.py", "score": 8.7}, {"node_id": "topogpt2_grid_scaler.py", "score": 5.4}, {"node_id": "reinforce.py", "score": 4.7}, {"node_id": "topogpt2_multi_inference.py", "score": 4.4}], "surprising_connections": []}, "edges": [{"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "torch.utils.checkpoint"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "tiktoken"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "datasets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference.py", "target": "importlib.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "tiktoken"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "inference2.py", "target": "safetensors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "enum"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "torch.utils.data"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "quantize.py", "target": "tiktoken"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "importlib.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "reinforce.py", "target": "enum"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "torch.utils.checkpoint"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "tiktoken"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "datasets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_1.py", "target": "shutil"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "hashlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "io"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "plotly.graph_objects"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "streamlit"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "plotly.subplots"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "scipy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "scipy.sparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "scipy.sparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "scipy.spatial.distance"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "sklearn.decomposition"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "sklearn.manifold"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "sklearn.neighbors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "importlib.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_embeddings_navigator.py", "target": "umap"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "io"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "plotly.graph_objects"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "streamlit"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "plotly.subplots"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "scipy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "scipy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "sklearn.decomposition"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "sklearn.random_projection"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_explorer.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "importlib.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_grid_scaler.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "gc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "importlib.util"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "topogpt2_multi_inference.py", "target": "glob"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "__future__"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "safetensors.torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "tiktoken"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "safetensors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "safetensors"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "zeroshot.py", "target": "tiktoken"}], "generator": "readmenator", "metadata": {"edge_count": 6895, "file_count": 12, "language_count": 2, "symbol_count": 1020}, "nodes": [{"id": "app.py", "kind": "module", "label": "app.py", "language": "py", "sha256": "9bf82042c0cd41f4", "symbol_count": 126, "symbols": [{"doc": "Configuración completa para TopoGPT2.", "kind": "class", "line": 55, "name": "TopoGPT2Config", "signature": "class TopoGPT2Config"}, {"kind": "method", "line": 155, "name": "setup_logger", "signature": "def setup_logger(name, level)"}, {"kind": "method", "line": 165, "name": "set_seed", "signature": "def set_seed(seed, device)"}, {"doc": "Operaciones de cuaterniones puras en PyTorch.\nRepresentación: [..., 4]  donde last dim = [w, x, y, z]\nq = w + x*i + y*j + z*k", "kind": "class", "line": 177, "name": "QuaternionOps", "signature": "class QuaternionOps"}, {"doc": "Capa lineal con pesos cuaterniones.\n\nImplementa la multiplicación W * x en el álgebra de cuaterniones:\n- W = Ww + Wx*i + Wy*j + Wz*k  (cuaternión de pesos)\n- x = xw + xx*i + xy*j + xz*k  (cuaternión de entrada)\n- out = W * x  (producto de Hamilton extendido a vectores)\n\nParámetros: 4 matrices reales de forma [out_q, in_q]", "kind": "class", "line": 216, "name": "QuaternionLinear", "signature": "class QuaternionLinear(Module)"}, {"doc": "Convolución espectral 2D con cuaterniones y producto de Hamilton completo.\n\nOperación en dominio de frecuencia:\n    P(k) = W(k) ⊗ X(k)  (producto de Hamilton de cuaterniones complejos)\n\nDonde:\n    X(k) = FFT2(x) con 4 canales cuaterniones [Xw, Xx, Xy, Xz]\n    W(k) = kernel complejo aprendible con componentes [Ww, Wx, Wy, Wz]\n\nReglas del producto de Hamilton en dominio de frecuencia:\n    Pw = Ww·Xw - Wx·Xx - Wy·Xy - Wz·Xz\n    Px = Ww·Xx + Wx·Xw + Wy·Xz - Wz·Xy\n    Py = Ww·Xy - Wx·Xz + Wy·Xw + Wz·Xx\n    Pz = Ww·Xz + Wx·Xy - Wy·Xx + Wz·Xw\n\nCada Wc es un kernel complejo (partes real e imaginaria independientes).", "kind": "class", "line": 261, "name": "QuaternionSpectralLayer", "signature": "class QuaternionSpectralLayer(Module)"}, {"doc": "Autoencoder espectral con cuaterniones.\n\nOpera en dos niveles:\n1. Espectral 1D sobre el vector de features (FFT sobre dim D_MODEL):\n   captura la espectrografía global del embedding.\n2. Espectral 2D sobre el grid del toro (QuaternionSpectralLayer):\n   captura correlaciones espaciales en la topología.\n\nDevuelve (latent, recon_loss) para regularización.", "kind": "class", "line": 348, "name": "SpectralAutoencoder", "signature": "class SpectralAutoencoder(Module)"}, {"doc": "Reemplaza el MLP en cada capa del transformer.\n\nPipeline (completamente vectorizado sobre batch Y secuencia):\n\n1. Flatten: [B, S, D] → [B·S, D]\n2. SpectralAutoencoder: filtrado espectral 1D + compresión cuaternión\n3. Proyección al toro:\n   - Calcula 2 ángulos (phi1, phi2) ∈ [-π, π]²\n   - Asignación blanda a los 8 nodos via distancia circular en el toro\n4. Construye grid de nodos: [B·S, N_NODES=8, D_MODEL]\n5. QuaternionSpectralLayer 2D sobre el grid [B·S, 4*D_QUAT, RADIAL, ANGULAR]\n6. Message-passing con rotaciones cuaterniones sobre el grafo toro\n7. Readout: atención sobre los 8 nodos → [B·S, D_MODEL]\n8. Reshape: [B·S, D] → [B, S, D]", "kind": "class", "line": 431, "name": "QuaternionTorusBrain", "signature": "class QuaternionTorusBrain(Module)"}, {"doc": "Rotary Position Embeddings (RoPE) - Su et al., 2021.\nCodifica la posición como rotaciones del espacio de atención,\nnaturalmente relativas y sin parámetros extra.", "kind": "class", "line": 648, "name": "RotaryEmbedding", "signature": "class RotaryEmbedding(Module)"}, {"doc": "Root Mean Square Layer Normalization (sin bias). Más estable que LayerNorm.", "kind": "class", "line": 696, "name": "RMSNorm", "signature": "class RMSNorm(Module)"}, {"doc": "SwiGLU: SiLU(gate(x)) * up(x) -> down\nUsado en LLaMA 2/3, Qwen, Mistral en lugar de GELU-FFN.\nDimension interna: 8/3 * d_model (convención LLaMA, redondeada a múltiplo de 4).", "kind": "class", "line": 713, "name": "SwiGLU", "signature": "class SwiGLU(Module)"}, {"doc": "Mixture of Experts sobre la capa topologica.\n\nArquitectura (inspirada en DeepSeek-MoE / Mixtral):\n  - 1 experto compartido: QuaternionTorusBrain (siempre activo)\n  - N_EXPERTS expertos SwiGLU ligeros (activacion esparsa: Top-K por token)\n  - Router: Linear(D, N_EXPERTS) + softmax → top-K\n\nLoad-balancing loss (auxiliar): penaliza si un experto acapara todos los tokens.\nActiva MOE_TOP_K de N_EXPERTS expertos por token.\n\nSin MoE (MOE_ENABLED=False): se comporta como QuaternionTorusBrain puro.", "kind": "class", "line": 742, "name": "TopoMoEBrain", "signature": "class TopoMoEBrain(Module)"}, {"doc": "Multi-head attention con:\n- Flash Attention (scaled_dot_product_attention de PyTorch 2.0+)\n- Rotary Position Embeddings (RoPE)\n- GQA (Grouped Query Attention): N_KV_HEADS < N_HEADS, reduce VRAM de K/V\n- KV Cache para inferencia autoregresiva eficiente\n- Temperatura termodinámica aprendible", "kind": "class", "line": 847, "name": "MultiHeadAttention", "signature": "class MultiHeadAttention(Module)"}, {"doc": "Capa del transformer con TopoMoEBrain (TopoBrain + MoE SwiGLU experts).\n\nEsquema pre-norm (estilo LLaMA):\n    x = x + Attention_GQA(RMSNorm(x))\n    x = x + TopoMoEBrain(RMSNorm(x))", "kind": "class", "line": 929, "name": "TopoGPT2Layer", "signature": "class TopoGPT2Layer(Module)"}, {"doc": "TopoGPT2: Transformer de lenguaje con TopoBrain cuaternión-espectral.\n\nArquitectura:\n    Embedding de tokens + RoPE (en Attention)\n    N_LAYERS × TopoGPT2Layer (Attention + QuaternionTorusBrain)\n    RMSNorm final\n    Proyección a vocabulario (weight-tied con embeddings)", "kind": "class", "line": 976, "name": "TopoGPT2", "signature": "class TopoGPT2(Module)"}, {"doc": "Wrapper alrededor de tiktoken (GPT-2 compatible).", "kind": "class", "line": 1082, "name": "BPETokenizer", "signature": "class BPETokenizer"}, {"doc": "Descarga corpus de texto para entrenamiento.\n\nSoporta:\n- 'tinystories': ~2GB de cuentos cortos (ideal para pruebas)\n- 'wikitext103': ~500MB de Wikipedia curada\n- 'file': archivo de texto local\n\nUsa HuggingFace 'datasets' para TinyStories y WikiText.", "kind": "class", "line": 1107, "name": "CorpusDownloader", "signature": "class CorpusDownloader"}, {"doc": "Dataset de tokens para language modeling (next-token prediction).\n\nGuarda los tokens tokenizados en disco la primera vez (cache .pt)\npara evitar re-tokenizar en cada ejecucion. La clave de cache incluye\nun hash del contenido del corpus + tokenizador + max_tokens.", "kind": "class", "line": 1170, "name": "TokenizedDataset", "signature": "class TokenizedDataset(Dataset)"}, {"doc": "Gestiona checkpoints de forma acumulativa y segura.\n\nEstructura en disco:\n    checkpoints_topogpt2/\n      latest/\n        model.safetensors   <- pesos del modelo (formato seguro, sin pickle)\n        optimizer.pt        <- estado del optimizador (requiere .pt)\n        state.json          <- metadatos: epoch, step, historial, config\n      best/\n        model.safetensors\n        state.json\n      step_NNNNN/           <- snapshots periodicos (rotados)\n        model.safetensors\n        optimizer.pt\n        state.json\n\nEl historial se ACUMULA entre sesiones de entrenamiento: cada --resume\nagrega nuevas entradas a train_loss[], val_loss[], etc.", "kind": "class", "line": 1220, "name": "CheckpointManager", "signature": "class CheckpointManager"}, {"doc": "Entrenador acumulativo y resumible.\n\nCaracteristicas:\n- Checkpoint automatico en safetensors cada N minutos + cada epoch\n- Historial acumulativo entre sesiones (--resume agrega al historial existente)\n- Guarda el mejor modelo en checkpoints/best/ automaticamente\n- LR schedule: cosine con warmup relativo a los steps de ESTA sesion\n- Mixed Precision (AMP) + acumulacion de gradientes", "kind": "class", "line": 1453, "name": "TopoGPT2Trainer", "signature": "class TopoGPT2Trainer"}, {"doc": "Calcula todas las metricas del diagrama de fases de Book.md.\n\nTodas las metricas se derivan de cantidades medibles (pesos, gradientes):\n\ndelta  (δ): margen de discretizacion.  max|w - round(w)|\n            δ≈0 -> cristal;  δ≈0.49 -> vidrio frio\nkappa  (κ): numero de condicion de la covarianza del gradiente.\n            κ≈1 -> cristalino;  κ>>1 -> amorfo\nT_eff:      temperatura efectiva = (lr/2) * Var(gradiente).\n            T_eff→0 -> congelado; T_eff alto -> ruidoso\nalpha  (α): indice de pureza = -log(δ + ε).\n            α=20 -> perfecto; α<1 -> vidrio\nberry:      fase de Berry de los kernels espectrales imaginarios.\n            |berry|>π/2 con winding≠0 -> insulador topologico\nlc:         complejidad local = 1 - similitud coseno promedio entre filas.\nsp:         superposicion = correlacion promedio inter-fila de pesos.", "kind": "class", "line": 1746, "name": "MechanisticMetrics", "signature": "class MechanisticMetrics"}, {"doc": "Encuentra el ratio imaginario/real optimo para los kernels espectrales.\n\nAnalogia con main.py: evalua la transicion GOE→GUE en el espacio\nde kernels. Un ratio optimo promueve estructura topologica (insulador)\nvs estructura amorfa (vidrio).\n\nMetodo: calibra con un mini-batch y mide la varianza del gradiente\nen funcion del ratio. Ratios que minimizan la varianza de gradiente\n(maxima coherencia espectral) son preferibles.\n\nNo entrena: solo inicializa los kernels con distintos ratios y mide.\nTiempo tipico: < 30 segundos.", "kind": "class", "line": 1983, "name": "Phase0_KernelOptimizer", "signature": "class Phase0_KernelOptimizer"}, {"doc": "Encuentra el batch size optimo testando candidatos con pocos pasos.\n\nDe main.py: el batch size regula la temperatura del horno de cristalizacion.\nBatch sizes demasiado chicos -> ruido excesivo (vidrio frio).\nBatch sizes demasiado grandes -> sin presion annealing (amorfos).\nLa ventana optima empirica de main.py: [24, 128] para Strassen.\n\nPara LM, testeamos candidatos midiendo:\n- delta (δ): velocidad de descenso en prospect_steps pasos\n- T_eff: temperatura efectiva del gradiente\n\nTiempo tipico: < 2 minutos para 3 candidatos × 30 pasos.", "kind": "class", "line": 2058, "name": "Phase1_BatchProspector", "signature": "class Phase1_BatchProspector"}, {"doc": "Encuentra semillas prometedoras midiendo la trayectoria de delta.\n\nDe main.py: una semilla \"buena\" muestra delta descendente en los\nprimeros N pasos (enfriamiento). Una semilla \"mala\" se estanca en\nel plateau vidrioso (~0.49).\n\nCriterio de seleccion:\n1. Semillas con delta_velocity < 0 (enfriando) AND kappa bajo.\n2. Si no hay, semillas solo enfriando.\n3. Fallback: semilla con menor delta final.\n\nTiempo tipico: < 3 minutos para 5 semillas × 50 pasos.", "kind": "class", "line": 2141, "name": "Phase2_SeedMiner", "signature": "class Phase2_SeedMiner"}, {"doc": "Refinamiento post-entrenamiento mediante recocido simulado.\n\nDe main.py: despues de que el modelo converge, una fase de annealing\ncon criterio de aceptacion de Metropolis puede empujar los pesos\nhacia estados de menor energia libre (menor delta o mejor val_loss).\n\nAceptacion de Metropolis:\n    si Δloss < 0: siempre acepta (mejora)\n    si Δloss >= 0: acepta con prob exp(-Δloss / T)\n\nLa temperatura T decae exponencialmente: T(t) = T0 * cooling_rate^t\n\nAl rechazar: restaura el mejor estado conocido.\nSi se estanca: perturbacion termica (ruido gaussiano en pesos).\n\nTiempo: proporcional a refine_epochs (user-controlled).", "kind": "class", "line": 2223, "name": "Phase4_AnnealingRefiner", "signature": "class Phase4_AnnealingRefiner"}, {"doc": "Orquesta las 5 fases de entrenamiento segun main.py + Book.md.\n\nFases:\n  0  Kernel ratio optimization  (GOE-GUE spectral calibration)\n  1  Batch size prospecting      (temperatura del horno de cristalizacion)\n  2  Seed mining                 (seleccion de semilla enfriante)\n  3  Full training               (entrenamiento principal con metricas)\n  4  Annealing refinement        (recocido simulado post-entrenamiento)\n\nLas fases 0-2 son rapidas (prospecting). La fase 3 es el grueso.\nLa fase 4 es opcional (--refine).\n\nPara no ser prohibitivo:\n  --prospect         activa fases 0, 1, 2 antes del entrenamiento\n  --refine-epochs N  activa fase 4 con N epocas de annealing\n  Sin flags: solo fase 3 (comportamiento original, identico a antes)", "kind": "class", "line": 2384, "name": "TopoPhasePipeline", "signature": "class TopoPhasePipeline"}, {"kind": "method", "line": 2506, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 124, "name": "__post_init__", "signature": "def __post_init__(self)"}, {"doc": "Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].", "kind": "method", "line": 185, "name": "hamilton_product", "signature": "def hamilton_product(q1, q2)"}, {"kind": "method", "line": 197, "name": "normalize", "signature": "def normalize(q, eps)"}, {"kind": "method", "line": 201, "name": "conjugate", "signature": "def conjugate(q)"}, {"doc": "Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]", "kind": "method", "line": 206, "name": "rotate_vector", "signature": "def rotate_vector(v, q)"}, {"kind": "method", "line": 228, "name": "__init__", "signature": "def __init__(self, in_features, out_features, bias)"}, {"doc": "x: [..., in_features] → [..., out_features]", "kind": "method", "line": 244, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 281, "name": "__init__", "signature": "def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)"}, {"kind": "method", "line": 300, "name": "_kernel", "signature": "def _kernel(self, c)"}, {"doc": "Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]", "kind": "method", "line": 303, "name": "_contract", "signature": "def _contract(self, W, X)"}, {"doc": "x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)\n→ [B, 4*out_q, H, W]", "kind": "method", "line": 307, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 361, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Filtro espectral 1D: x[..., D] → filtrado[..., D]", "kind": "method", "line": 393, "name": "_filter1d", "signature": "def _filter1d(self, x, kr, ki)"}, {"doc": "x: [..., D_MODEL] → latent: [..., D_LAT]", "kind": "method", "line": 399, "name": "encode", "signature": "def encode(self, x)"}, {"doc": "z: [..., D_LAT] → recon: [..., D_MODEL]", "kind": "method", "line": 404, "name": "decode", "signature": "def decode(self, z)"}, {"doc": "Devuelve (latent, recon_loss)", "kind": "method", "line": 409, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Procesa el grid del toro con QuaternionSpectralLayer.\ngrid: [B, 4*D_QUAT, RADIAL, ANGULAR]  →  [B, 4*D_QUAT, RADIAL, ANGULAR]", "kind": "method", "line": 416, "name": "process_torus_grid", "signature": "def process_torus_grid(self, grid)"}, {"kind": "method", "line": 449, "name": "__init__", "signature": "def __init__(self, d_model, config)"}, {"doc": "Construye las aristas del grafo toro 2×4.\n\nNodos indexados como: node = r * N_ANGULAR + a\n  r ∈ [0, RADIAL-1], a ∈ [0, ANGULAR-1]\n\nAristas angulares: nodo ↔ nodo a la izquierda/derecha (periódico)\nAristas radiales:  nodo ↔ nodo del anillo interior/exterior", "kind": "method", "line": 489, "name": "_build_torus_graph", "signature": "def _build_torus_graph(self)"}, {"doc": "Asignación blanda de tokens a los 8 nodos del toro via distancia circular.\n\nphi1: [BS] ángulo angular ∈ [-π, π]\nphi2: [BS] ángulo radial ∈ [-π, π]\n→ weights: [BS, N_NODES]  (suma a 1, softmax de distancias negativas)", "kind": "method", "line": 523, "name": "_torus_soft_assign", "signature": "def _torus_soft_assign(self, phi1, phi2)"}, {"doc": "Message-passing VECTORIZADO con rotaciones cuaterniones.\nSin bucles Python: todas las aristas se procesan en paralelo.\n\nnode_feat: [BS, N_NODES, D_MODEL]\n→ [BS, N_NODES, D_MODEL]", "kind": "method", "line": 550, "name": "_message_passing", "signature": "def _message_passing(self, node_feat)"}, {"doc": "x: [B, S, D_MODEL]\n→ output: [B, S, D_MODEL], recon_loss: scalar", "kind": "method", "line": 587, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 655, "name": "__init__", "signature": "def __init__(self, d_head, max_seq_len, base)"}, {"kind": "method", "line": 661, "name": "_build_cache", "signature": "def _build_cache(self, seq_len)"}, {"kind": "method", "line": 668, "name": "_rotate_half", "signature": "def _rotate_half(self, x)"}, {"doc": "q, k: [B, n_heads, S_q/S_k, d_head]\noffset: posicion inicial (para KV cache: longitud del cache existente)\nAplica posiciones [offset .. offset+S-1] a q y k.", "kind": "method", "line": 672, "name": "forward", "signature": "def forward(self, q, k, seq_len, offset)"}, {"kind": "method", "line": 699, "name": "__init__", "signature": "def __init__(self, d_model, eps)"}, {"kind": "method", "line": 704, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 720, "name": "__init__", "signature": "def __init__(self, d_model, expansion, dropout)"}, {"kind": "method", "line": 734, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 757, "name": "__init__", "signature": "def __init__(self, d_model, config)"}, {"doc": "x: [N, D] donde N = B*S (tokens aplanados)\nRetorna:\nexpert_out: [N, D]  suma ponderada de top-K expertos\naux_loss:   escalar  load-balancing loss\nRouting vectorizado sin boolean indexing ni sincronizacion CUDA.\nUsa dispatch por indices agrupados (estilo Mixtral/DeepSeek) para\ncompatibilidad total con torch.utils.checkpoint.", "kind": "method", "line": 778, "name": "_route", "signature": "def _route(self, x)"}, {"doc": "x: [B, S, D]\n→ output: [B, S, D], aux_loss: escalar", "kind": "method", "line": 820, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 857, "name": "__init__", "signature": "def __init__(self, d_model, n_heads, config)"}, {"doc": "Args:\n    x:        [B, S, D]\n    is_causal: usar mascara causal\n    past_kv:  (K_cache, V_cache) de pasos anteriores o None\nReturns:\n    out:      [B, S, D]\n    kv_cache: (K, V) completos para cachear en generate()", "kind": "method", "line": 875, "name": "forward", "signature": "def forward(self, x, is_causal, past_kv)"}, {"kind": "method", "line": 938, "name": "__init__", "signature": "def __init__(self, d_model, n_heads, config)"}, {"kind": "method", "line": 947, "name": "_forward_impl", "signature": "def _forward_impl(self, x, past_kv)"}, {"doc": "Retorna (x_out, aux_loss, kv_cache).\nCon gradient checkpointing en training (solo cuando no hay KV cache).", "kind": "method", "line": 956, "name": "forward", "signature": "def forward(self, x, past_kv)"}, {"kind": "method", "line": 987, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1006, "name": "_init_weights", "signature": "def _init_weights(self)"}, {"doc": "token_ids: [B, S]  (enteros)\npast_kvs:  lista de (K, V) por capa, o None para entrenamiento\n→ logits: [B, S, VOCAB_SIZE], aux_loss: scalar, new_kvs: list[(K,V)]", "kind": "method", "line": 1013, "name": "forward", "signature": "def forward(self, token_ids, past_kvs)"}, {"kind": "method", "line": 1036, "name": "count_params", "signature": "def count_params(self)"}, {"doc": "Generacion autoregresiva con KV cache y muestreo top-k.\nEn el primer paso procesa el prompt completo y guarda el cache.\nEn pasos siguientes solo procesa 1 token nuevo (O(n) en lugar de O(n^2)).", "kind": "method", "line": 1042, "name": "generate", "signature": "def generate(self, token_ids, max_new_tokens, temperature, top_k)"}, {"kind": "method", "line": 1085, "name": "__init__", "signature": "def __init__(self, encoding)"}, {"kind": "method", "line": 1093, "name": "encode", "signature": "def encode(self, text)"}, {"kind": "method", "line": 1096, "name": "decode", "signature": "def decode(self, tokens)"}, {"kind": "method", "line": 1099, "name": "eot_token", "signature": "def eot_token(self)"}, {"kind": "method", "line": 1119, "name": "__init__", "signature": "def __init__(self, corpus, data_dir, logger)"}, {"doc": "Devuelve el texto del corpus. Descarga si es necesario.", "kind": "method", "line": 1125, "name": "get_text", "signature": "def get_text(self, split)"}, {"kind": "method", "line": 1150, "name": "_download_hf", "signature": "def _download_hf(self, dataset_name, split, text_column, name)"}, {"kind": "method", "line": 1179, "name": "__init__", "signature": "def __init__(self, text, tokenizer, seq_len, max_tokens, cache_dir, split_tag)"}, {"kind": "method", "line": 1206, "name": "__len__", "signature": "def __len__(self)"}, {"kind": "method", "line": 1209, "name": "__getitem__", "signature": "def __getitem__(self, idx)"}, {"kind": "method", "line": 1245, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS\npara que coincidan con la arquitectura guardada.\nNecesario cuando el codigo cambio GQA despues de guardar el checkpoint.", "kind": "method", "line": 1255, "name": "patch_config_for_resume", "signature": "def patch_config_for_resume(self, cfg)"}, {"kind": "method", "line": 1284, "name": "_save_model", "signature": "def _save_model(self, model, directory)"}, {"kind": "method", "line": 1297, "name": "_load_model", "signature": "def _load_model(self, model, directory)"}, {"kind": "method", "line": 1328, "name": "_save_optimizer", "signature": "def _save_optimizer(self, optimizer, directory)"}, {"kind": "method", "line": 1331, "name": "_load_optimizer", "signature": "def _load_optimizer(self, optimizer, directory, device)"}, {"kind": "method", "line": 1340, "name": "_save_state", "signature": "def _save_state(self, state, directory)"}, {"kind": "method", "line": 1345, "name": "_load_state", "signature": "def _load_state(self, directory)"}, {"kind": "method", "line": 1356, "name": "should_save", "signature": "def should_save(self)"}, {"doc": "Guarda checkpoint completo.\n\nstate debe contener al menos: completed_epochs, global_step,\nbest_val_loss, history, config.", "kind": "method", "line": 1359, "name": "save", "signature": "def save(self, model, optimizer, state, is_best)"}, {"doc": "Carga el ultimo checkpoint guardado.\nDevuelve el state dict (vacio si no hay checkpoint).", "kind": "method", "line": 1404, "name": "load_latest", "signature": "def load_latest(self, model, optimizer)"}, {"doc": "Carga el mejor modelo guardado (solo pesos, sin optimizador).", "kind": "method", "line": 1431, "name": "load_best", "signature": "def load_best(self, model)"}, {"kind": "method", "line": 1443, "name": "has_checkpoint", "signature": "def has_checkpoint(self)"}, {"kind": "method", "line": 1465, "name": "__init__", "signature": "def __init__(self, model, config, tokenizer)"}, {"doc": "Carga el ultimo checkpoint disponible.\nRestaura: pesos del modelo, estado del optimizador, historial acumulado,\nepoch/step completados y mejor val_loss.\nDevuelve True si se cargo un checkpoint, False si empieza de cero.", "kind": "method", "line": 1500, "name": "resume", "signature": "def resume(self)"}, {"doc": "Construye el dict de estado para persistir en state.json.", "kind": "method", "line": 1525, "name": "_current_state", "signature": "def _current_state(self)"}, {"doc": "Cosine decay con warmup. El schedule es relativo a la sesion actual.", "kind": "method", "line": 1536, "name": "_cosine_lr", "signature": "def _cosine_lr(self, step_in_session, total_steps_session)"}, {"kind": "method", "line": 1544, "name": "_set_lr", "signature": "def _set_lr(self, lr)"}, {"doc": "Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.\nEl historial se acumula sobre sesiones previas.", "kind": "method", "line": 1548, "name": "train", "signature": "def train(self, train_dl, val_dl)"}, {"doc": "Genera una muestra de texto al final de cada epoch para monitorear\nla calidad cualitativa del modelo (detecta degeneracion, repeticion, etc.).", "kind": "method", "line": 1684, "name": "_sample_text", "signature": "def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)"}, {"kind": "method", "line": 1716, "name": "evaluate", "signature": "def evaluate(self, dataloader)"}, {"kind": "method", "line": 1766, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1774, "name": "compute_delta", "signature": "def compute_delta(self, model)"}, {"kind": "method", "line": 1781, "name": "compute_alpha", "signature": "def compute_alpha(self, delta)"}, {"doc": "Captura gradientes de forma segura, ignorando tensores corruptos.", "kind": "method", "line": 1786, "name": "update_grad_buffer", "signature": "def update_grad_buffer(self, model)"}, {"doc": "T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva.", "kind": "method", "line": 1812, "name": "compute_t_eff", "signature": "def compute_t_eff(self, lr)"}, {"doc": "κ = λ_max / λ_min de la covarianza del gradiente.\nParámetro de orden para cristalización (κ≈1 = cristal).\nNota: requiere pasadas backward adicionales. Se ejecuta con protección\npara no corromper el estado AMP del trainer principal.", "kind": "method", "line": 1820, "name": "compute_kappa", "signature": "def compute_kappa(self, model, dataloader, n_batches)"}, {"doc": "Fase de Berry de los kernels espectrales imaginarios.\nSurge de los parametros ki_w, ki_x, ki_y, ki_z de QuaternionSpectralLayer.\n|berry|>pi/2 con winding!=0 indica estructura topologica.", "kind": "method", "line": 1878, "name": "compute_berry_phase", "signature": "def compute_berry_phase(self, model)"}, {"doc": "Complejidad local: 1 - similitud coseno promedio entre filas de pesos.", "kind": "method", "line": 1891, "name": "compute_lc", "signature": "def compute_lc(self, model)"}, {"doc": "Superposicion: correlacion inter-fila promedio (entrelazamiento de features).", "kind": "method", "line": 1905, "name": "compute_sp", "signature": "def compute_sp(self, model)"}, {"doc": "Clasificacion de fase segun Book.md:\n\ndiscrete_crystal:       delta<0.05, kappa<1.5\ntopological_insulator:  |berry|>pi/2, winding!=0\ncold_glass:             kappa>>1, delta>0.3\nfunctional_glass:       intermedio (lo mas comun en LM)", "kind": "method", "line": 1921, "name": "classify_phase", "signature": "def classify_phase(self, delta, kappa, berry)"}, {"doc": "Calcula todas las metricas.\ncompute_kappa=True hace pasadas backward adicionales (caro, usar cada N epochs).", "kind": "method", "line": 1940, "name": "compute_all", "signature": "def compute_all(self, model, lr, dataloader, compute_kappa)"}, {"kind": "method", "line": 1965, "name": "format_log", "signature": "def format_log(self, m)"}, {"kind": "method", "line": 2001, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Mide la coherencia espectral para un ratio dado.\nRetorna: varianza del gradiente (menor = mas coherente = mejor).", "kind": "method", "line": 2005, "name": "_measure_ratio", "signature": "def _measure_ratio(self, ratio, sample_batch)"}, {"doc": "Retorna el mejor ratio de inicializacion de kernels espectrales.", "kind": "method", "line": 2034, "name": "optimize", "signature": "def optimize(self, dataloader)"}, {"kind": "method", "line": 2074, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Retorna el mejor batch size segun delta y T_eff.", "kind": "method", "line": 2078, "name": "prospect", "signature": "def prospect(self, candidates, train_dataset, prospect_steps)"}, {"kind": "method", "line": 2157, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Retorna la semilla con la mejor trayectoria de delta.", "kind": "method", "line": 2161, "name": "mine", "signature": "def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)"}, {"kind": "method", "line": 2243, "name": "__init__", "signature": "def __init__(self, trainer, t0, cooling_rate, stagnation_patience)"}, {"doc": "Ejecuta refine_epochs epocas de recocido simulado.\nRetorna el historial de refinamiento.", "kind": "method", "line": 2252, "name": "refine", "signature": "def refine(self, train_dl, val_dl, refine_epochs)"}, {"kind": "method", "line": 2404, "name": "__init__", "signature": "def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)"}, {"kind": "method", "line": 2414, "name": "_make_dataloaders", "signature": "def _make_dataloaders(self, batch_size)"}, {"doc": "Ejecuta el pipeline completo.\nRetorna el trainer con el modelo entrenado.", "kind": "method", "line": 2426, "name": "run", "signature": "def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)"}, {"kind": "method", "line": 964, "name": "ckpt_fn", "signature": "def ckpt_fn(x_in)"}]}, {"id": "inference.py", "kind": "module", "label": "inference.py", "language": "py", "sha256": "684f6ec60ed0abd2", "symbol_count": 20, "symbols": [{"kind": "function", "line": 19, "name": "_load_source_module", "signature": "def _load_source_module(path)"}, {"doc": "Parametric configuration container for inference execution.", "kind": "class", "line": 28, "name": "InferenceConfig", "signature": "class InferenceConfig"}, {"doc": "Reads safetensors metadata to align architecture configuration.", "kind": "class", "line": 45, "name": "CheckpointInspector", "signature": "class CheckpointInspector"}, {"doc": "Loads weights from safetensors and binds to the architectural graph.", "kind": "class", "line": 90, "name": "ModelLoader", "signature": "class ModelLoader"}, {"doc": "Handles autoregressive token generation with controlled sampling.", "kind": "class", "line": 115, "name": "GenerationEngine", "signature": "class GenerationEngine"}, {"doc": "Orchestrates execution flow for prompt processing.", "kind": "class", "line": 140, "name": "InferenceRunner", "signature": "class InferenceRunner"}, {"kind": "method", "line": 178, "name": "parse_arguments", "signature": "def parse_arguments()"}, {"kind": "method", "line": 47, "name": "__init__", "signature": "def __init__(self, logger)"}, {"kind": "method", "line": 50, "name": "inspect_kq_head_count", "signature": "def inspect_kq_head_count(self, checkpoint_path, d_model, n_heads)"}, {"kind": "method", "line": 62, "name": "patch_config", "signature": "def patch_config(self, config, source_module)"}, {"kind": "method", "line": 81, "name": "_resolve_preset", "signature": "def _resolve_preset(self, scale)"}, {"kind": "method", "line": 92, "name": "__init__", "signature": "def __init__(self, checkpoint_name, logger)"}, {"kind": "method", "line": 96, "name": "load_model", "signature": "def load_model(self, config, source_module)"}, {"kind": "method", "line": 117, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"kind": "method", "line": 121, "name": "generate", "signature": "def generate(self, model, tokenizer, prompt_text)"}, {"kind": "method", "line": 132, "name": "sample_logits", "signature": "def sample_logits(self, logits)"}, {"kind": "method", "line": 142, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 146, "name": "_setup_logger", "signature": "def _setup_logger(self)"}, {"kind": "method", "line": 155, "name": "run", "signature": "def run(self)"}, {"kind": "method", "line": 170, "name": "_print_result", "signature": "def _print_result(self, prompt, output)"}]}, {"id": "inference2.py", "kind": "module", "label": "inference2.py", "language": "py", "sha256": "b7dd714096b929e3", "symbol_count": 87, "symbols": [{"doc": "Stderr logger with timestamp formatting.", "kind": "function", "line": 79, "name": "build_logger", "signature": "def build_logger(name, level)"}, {"doc": "All tuneable knobs for the inference pipeline.\n\nAttributes\n----------\ncheckpoint_path : str\n    Path to a .safetensors or .pt/.pth checkpoint file.\ndevice : str\n    Torch device string.\nmax_new_tokens : int\n    Maximum tokens to generate beyond the prompt.\ntemperature : float\n    Softmax temperature.  0 activates greedy decoding.\ntop_k : int\n    Top-k filtering.  0 disables it.\ntop_p : float\n    Nucleus (top-p) filtering.  1.0 disables it.\nrepetition_penalty : float\n    Multiplicative penalty for tokens already in context.  1.0 disables.\nseed : int\n    RNG seed for reproducibility.\nlog_level : str\n    Python logging level name.\nstream : bool\n    Print tokens as they are generated instead of all at once.\nshow_timing : bool\n    Print tokens-per-second after generation.\nprompt : str\n    Default prompt for single-shot mode.\ninteractive : bool\n    Enter a REPL loop instead of generating a single response.\nbenchmark_runs : int\n    If > 0, run this many generation passes and report throughput.", "kind": "class", "line": 97, "name": "InferenceConfig", "signature": "class InferenceConfig"}, {"doc": "Thin wrapper around tiktoken with GPT-2 encoding.", "kind": "class", "line": 170, "name": "BPETokenizer", "signature": "class BPETokenizer"}, {"doc": "Static quaternion algebra operations.", "kind": "class", "line": 196, "name": "QuaternionOps", "signature": "class QuaternionOps"}, {"doc": "Linear layer in the quaternion algebra.\n\nImplements the Hamilton product W ⊗ x using four real weight matrices.\nBoth in_features and out_features must be divisible by 4.", "kind": "class", "line": 219, "name": "QuaternionLinear", "signature": "class QuaternionLinear(Module)"}, {"doc": "2-D spectral convolution using the quaternion Hamilton product in the\nfrequency domain.  Each quaternion component (w, x, y, z) has an\nindependent complex kernel (real + imaginary parts).", "kind": "class", "line": 252, "name": "QuaternionSpectralLayer", "signature": "class QuaternionSpectralLayer(Module)"}, {"doc": "Spectral autoencoder: 1-D FFT filtering + quaternion projection for\nencoding/decoding, plus stacked QuaternionSpectralLayers for the torus grid.", "kind": "class", "line": 306, "name": "SpectralAutoencoder", "signature": "class SpectralAutoencoder(Module)"}, {"doc": "Replaces the MLP in each transformer layer.\n\nFully vectorised pipeline:\n    [B, S, D] -> spectral AE -> torus projection -> soft node assignment\n    -> 2-D spectral layer on grid -> quaternion message-passing -> readout\n    -> [B, S, D]", "kind": "class", "line": 358, "name": "QuaternionTorusBrain", "signature": "class QuaternionTorusBrain(Module)"}, {"doc": "SwiGLU feed-forward block (LLaMA-style).", "kind": "class", "line": 462, "name": "SwiGLU", "signature": "class SwiGLU(Module)"}, {"doc": "Mixture-of-Experts wrapper: one always-active QuaternionTorusBrain plus\nN sparse SwiGLU experts selected by a linear router (top-K per token).\nWhen moe_enabled is False this reduces to a plain QuaternionTorusBrain.", "kind": "class", "line": 481, "name": "TopoMoEBrain", "signature": "class TopoMoEBrain(Module)"}, {"doc": "Rotary Position Embeddings (RoPE) – Su et al., 2021.", "kind": "class", "line": 537, "name": "RotaryEmbedding", "signature": "class RotaryEmbedding(Module)"}, {"doc": "Root Mean Square Layer Normalization (no bias).", "kind": "class", "line": 577, "name": "RMSNorm", "signature": "class RMSNorm(Module)"}, {"doc": "GQA-capable multi-head attention with Flash Attention, RoPE, and KV cache.", "kind": "class", "line": 589, "name": "MultiHeadAttention", "signature": "class MultiHeadAttention(Module)"}, {"doc": "Pre-norm transformer layer: attention + TopoMoEBrain.", "kind": "class", "line": 638, "name": "TopoGPT2Layer", "signature": "class TopoGPT2Layer(Module)"}, {"doc": "TopoGPT2: causal language model with quaternion torus topology.\nEmbedding -> N layers (Attention + QuaternionTorusBrain) -> RMSNorm -> LM head.", "kind": "class", "line": 660, "name": "TopoGPT2", "signature": "class TopoGPT2(Module)"}, {"doc": "All architectural hyperparameters required to instantiate TopoGPT2.\nPopulated entirely from the probed checkpoint shapes.", "kind": "class", "line": 700, "name": "ModelConfig", "signature": "class ModelConfig"}, {"doc": "Infers all ModelConfig fields directly from checkpoint tensor shapes,\nwithout relying on any saved metadata, scale preset, or source file.\n\nKey derivations\n---------------\nd_model        : token_embed.weight shape [V, D] -> D\nvocab_size     : token_embed.weight shape [V, D] -> V\nd_head         : rope.inv_freq shape [d_head // 2] -> d_head\nn_heads        : q_proj.weight shape [n_heads * d_head, D] -> n_heads\nn_kv_heads     : k_proj.weight shape [n_kv * d_head, D] -> n_kv\nn_layers       : count of q_proj keys\ntorus_radial   : torus_spectral.0.kr_w shape [..., freq_h, ...] -> freq_h\ntorus_angular  : torus_spectral.0.kr_w shape [..., freq_w] -> (freq_w-1)*2\nspectral_latent: enc_proj.Ww.weight shape [out_q, in_q] -> out_q * 4\nn_experts      : count of experts.N.gate_proj.weight keys in layer 0\nnum_spec_layers: count of torus_spectral.N.kr_w keys in layer 0", "kind": "class", "line": 735, "name": "CheckpointArchProber", "signature": "class CheckpointArchProber"}, {"doc": "Loads a safetensors or pickle checkpoint into a TopoGPT2 instance.\nRestores weight tying after loading.", "kind": "class", "line": 890, "name": "CheckpointLoader", "signature": "class CheckpointLoader"}, {"doc": "Stateless token sampling with temperature, top-k, top-p, and\nrepetition penalty.  All operations are performed on the logit tensor\nreturned by the model before softmax.", "kind": "class", "line": 943, "name": "Sampler", "signature": "class Sampler"}, {"doc": "Autoregressive generation with KV cache and optional token streaming.\n\nFirst forward pass processes the full prompt and seeds the KV cache.\nSubsequent passes process a single token each, giving O(n) complexity.", "kind": "class", "line": 1003, "name": "GenerationEngine", "signature": "class GenerationEngine"}, {"doc": "Formats and writes generation results to stdout.", "kind": "class", "line": 1082, "name": "ResultPrinter", "signature": "class ResultPrinter"}, {"doc": "Orchestrates the full inference workflow.\n\n1. Validate config.\n2. Probe checkpoint architecture.\n3. Instantiate model.\n4. Load weights.\n5. Run generation in the requested mode.", "kind": "class", "line": 1116, "name": "InferencePipeline", "signature": "class InferencePipeline"}, {"doc": "Construct and return the CLI argument parser.", "kind": "method", "line": 1217, "name": "build_arg_parser", "signature": "def build_arg_parser()"}, {"doc": "CLI entry point.", "kind": "method", "line": 1288, "name": "main", "signature": "def main()"}, {"doc": "Raise ValueError for impossible parameter combinations.", "kind": "method", "line": 148, "name": "validate", "signature": "def validate(self)"}, {"kind": "method", "line": 175, "name": "__init__", "signature": "def __init__(self)"}, {"kind": "method", "line": 182, "name": "encode", "signature": "def encode(self, text)"}, {"kind": "method", "line": 185, "name": "decode", "signature": "def decode(self, token_ids)"}, {"kind": "method", "line": 188, "name": "decode_single", "signature": "def decode_single(self, token_id)"}, {"kind": "method", "line": 200, "name": "hamilton_product", "signature": "def hamilton_product(q1, q2)"}, {"kind": "method", "line": 211, "name": "normalize", "signature": "def normalize(q, eps)"}, {"kind": "method", "line": 215, "name": "conjugate", "signature": "def conjugate(q)"}, {"kind": "method", "line": 227, "name": "__init__", "signature": "def __init__(self, in_features, out_features, bias)"}, {"kind": "method", "line": 241, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 259, "name": "__init__", "signature": "def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)"}, {"kind": "method", "line": 276, "name": "_kernel", "signature": "def _kernel(self, c)"}, {"kind": "method", "line": 279, "name": "_contract", "signature": "def _contract(self, W, X)"}, {"kind": "method", "line": 282, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 312, "name": "__init__", "signature": "def __init__(self, cfg)"}, {"kind": "method", "line": 334, "name": "_filter1d", "signature": "def _filter1d(self, x, kr, ki)"}, {"kind": "method", "line": 341, "name": "encode", "signature": "def encode(self, x)"}, {"kind": "method", "line": 344, "name": "decode", "signature": "def decode(self, z)"}, {"kind": "method", "line": 347, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 351, "name": "process_torus_grid", "signature": "def process_torus_grid(self, grid)"}, {"kind": "method", "line": 370, "name": "__init__", "signature": "def __init__(self, d_model, cfg)"}, {"kind": "method", "line": 395, "name": "_build_torus_graph", "signature": "def _build_torus_graph(self)"}, {"kind": "method", "line": 411, "name": "_torus_soft_assign", "signature": "def _torus_soft_assign(self, phi1, phi2)"}, {"kind": "method", "line": 423, "name": "_message_passing", "signature": "def _message_passing(self, node_feat)"}, {"kind": "method", "line": 437, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 465, "name": "__init__", "signature": "def __init__(self, d_model, expansion, dropout)"}, {"kind": "method", "line": 475, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 488, "name": "__init__", "signature": "def __init__(self, d_model, cfg)"}, {"kind": "method", "line": 503, "name": "_route", "signature": "def _route(self, x)"}, {"kind": "method", "line": 528, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 542, "name": "__init__", "signature": "def __init__(self, d_head, max_seq_len)"}, {"kind": "method", "line": 550, "name": "_build_cache", "signature": "def _build_cache(self, seq_len)"}, {"kind": "method", "line": 557, "name": "_rotate_half", "signature": "def _rotate_half(x)"}, {"kind": "method", "line": 561, "name": "forward", "signature": "def forward(self, q, k, seq_len, offset)"}, {"kind": "method", "line": 580, "name": "__init__", "signature": "def __init__(self, d_model, eps)"}, {"kind": "method", "line": 585, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 594, "name": "__init__", "signature": "def __init__(self, d_model, n_heads, cfg)"}, {"kind": "method", "line": 609, "name": "forward", "signature": "def forward(self, x, is_causal, past_kv)"}, {"kind": "method", "line": 641, "name": "__init__", "signature": "def __init__(self, d_model, n_heads, cfg)"}, {"kind": "method", "line": 649, "name": "forward", "signature": "def forward(self, x, past_kv)"}, {"kind": "method", "line": 666, "name": "__init__", "signature": "def __init__(self, cfg)"}, {"kind": "method", "line": 678, "name": "forward", "signature": "def forward(self, token_ids, past_kvs)"}, {"kind": "method", "line": 723, "name": "d_quat", "signature": "def d_quat(self)"}, {"kind": "method", "line": 727, "name": "gqa_groups", "signature": "def gqa_groups(self)"}, {"kind": "method", "line": 768, "name": "__init__", "signature": "def __init__(self, logger)"}, {"kind": "method", "line": 771, "name": "_load_shapes", "signature": "def _load_shapes(self, path)"}, {"doc": "Return a ModelConfig whose dimensions exactly match the checkpoint.", "kind": "method", "line": 786, "name": "probe", "signature": "def probe(self, path)"}, {"kind": "method", "line": 871, "name": "_fallback_d_head", "signature": "def _fallback_d_head(d_model, q_out, k_out)"}, {"kind": "method", "line": 896, "name": "__init__", "signature": "def __init__(self, logger)"}, {"doc": "Load weights into model in-place.", "kind": "method", "line": 899, "name": "load", "signature": "def load(self, path, model, device)"}, {"kind": "method", "line": 950, "name": "__init__", "signature": "def __init__(self, cfg)"}, {"doc": "Sample one token from logits.\n\nParameters\n----------\nlogits       : [vocab_size] raw logits for the next token position.\ngenerated_ids: token IDs already generated (for repetition penalty).\n\nReturns\n-------\nSampled token id.", "kind": "method", "line": 953, "name": "__call__", "signature": "def __call__(self, logits, generated_ids)"}, {"kind": "method", "line": 1013, "name": "__init__", "signature": "def __init__(self, model, tokenizer, cfg, logger)"}, {"doc": "Generate text from prompt.\n\nReturns\n-------\n(generated_text, tokens_per_second)\ngenerated_text includes the prompt prefix.", "kind": "method", "line": 1027, "name": "generate", "signature": "def generate(self, prompt)"}, {"kind": "method", "line": 1071, "name": "_maybe_stream", "signature": "def _maybe_stream(self, token_id)"}, {"kind": "method", "line": 1087, "name": "print_single", "signature": "def print_single(self, prompt, full_text, tps, show_timing)"}, {"kind": "method", "line": 1100, "name": "print_benchmark", "signature": "def print_benchmark(self, runs, tps_list)"}, {"kind": "method", "line": 1127, "name": "__init__", "signature": "def __init__(self, cfg, logger)"}, {"kind": "method", "line": 1131, "name": "_build_model", "signature": "def _build_model(self)"}, {"kind": "method", "line": 1149, "name": "run", "signature": "def run(self)"}, {"kind": "method", "line": 1164, "name": "_run_single", "signature": "def _run_single(self, engine, printer)"}, {"kind": "method", "line": 1176, "name": "_run_interactive", "signature": "def _run_interactive(self, engine, printer)"}, {"kind": "method", "line": 1199, "name": "_run_benchmark", "signature": "def _run_benchmark(self, engine, printer)"}]}, {"id": "install.sh", "kind": "module", "label": "install.sh", "language": "sh", "sha256": "c907d80fd6734993", "symbol_count": 0, "symbols": []}, {"id": "quantize.py", "kind": "module", "label": "quantize.py", "language": "py", "sha256": "d1584b8e726b65ec", "symbol_count": 115, "symbols": [{"doc": "Centralized configuration for quantized inference. All parameters are explicitly defined.", "kind": "class", "line": 34, "name": "InferenceConfig", "signature": "class InferenceConfig"}, {"doc": "Inspects checkpoint state dict to dynamically resolve architecture parameters.", "kind": "class", "line": 105, "name": "CheckpointInspector", "signature": "class CheckpointInspector"}, {"doc": "Pure quaternion operations in PyTorch. Representation: [..., 4] -> [w, x, y, z].", "kind": "class", "line": 162, "name": "QuaternionOps", "signature": "class QuaternionOps"}, {"kind": "class", "line": 195, "name": "QuaternionLinear", "signature": "class QuaternionLinear(Module)"}, {"kind": "class", "line": 220, "name": "QuaternionSpectralLayer", "signature": "class QuaternionSpectralLayer(Module)"}, {"kind": "class", "line": 262, "name": "SpectralAutoencoder", "signature": "class SpectralAutoencoder(Module)"}, {"kind": "class", "line": 312, "name": "QuaternionTorusBrain", "signature": "class QuaternionTorusBrain(Module)"}, {"kind": "class", "line": 408, "name": "RotaryEmbedding", "signature": "class RotaryEmbedding(Module)"}, {"kind": "class", "line": 440, "name": "RMSNorm", "signature": "class RMSNorm(Module)"}, {"kind": "class", "line": 451, "name": "SwiGLU", "signature": "class SwiGLU(Module)"}, {"kind": "class", "line": 468, "name": "TopoMoEBrain", "signature": "class TopoMoEBrain(Module)"}, {"kind": "class", "line": 522, "name": "MultiHeadAttention", "signature": "class MultiHeadAttention(Module)"}, {"kind": "class", "line": 568, "name": "TopoGPT2Layer", "signature": "class TopoGPT2Layer(Module)"}, {"kind": "class", "line": 590, "name": "TopoGPT2", "signature": "class TopoGPT2(Module)"}, {"kind": "class", "line": 651, "name": "BPETokenizer", "signature": "class BPETokenizer"}, {"kind": "class", "line": 668, "name": "QuantizationFormat", "signature": "class QuantizationFormat(Enum)"}, {"kind": "class", "line": 678, "name": "IQuantizer", "signature": "class IQuantizer(ABC)"}, {"kind": "class", "line": 692, "name": "BitNetQuantizer", "signature": "class BitNetQuantizer(IQuantizer)"}, {"kind": "class", "line": 721, "name": "INT4Quantizer", "signature": "class INT4Quantizer(IQuantizer)"}, {"kind": "class", "line": 746, "name": "INT8Quantizer", "signature": "class INT8Quantizer(IQuantizer)"}, {"kind": "class", "line": 760, "name": "Float16Quantizer", "signature": "class Float16Quantizer(IQuantizer)"}, {"kind": "class", "line": 774, "name": "BFloat16Quantizer", "signature": "class BFloat16Quantizer(IQuantizer)"}, {"kind": "class", "line": 788, "name": "Float32Quantizer", "signature": "class Float32Quantizer(IQuantizer)"}, {"kind": "class", "line": 802, "name": "Float64Quantizer", "signature": "class Float64Quantizer(IQuantizer)"}, {"kind": "class", "line": 816, "name": "QuantizerFactory", "signature": "class QuantizerFactory"}, {"kind": "class", "line": 834, "name": "ModelLoader", "signature": "class ModelLoader"}, {"kind": "class", "line": 883, "name": "InferenceEngine", "signature": "class InferenceEngine"}, {"kind": "class", "line": 907, "name": "QuantizationInferencePipeline", "signature": "class QuantizationInferencePipeline"}, {"kind": "method", "line": 939, "name": "parse_arguments", "signature": "def parse_arguments()"}, {"kind": "method", "line": 965, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 86, "name": "resolve_gqa", "signature": "def resolve_gqa(self)"}, {"kind": "method", "line": 108, "name": "inspect_and_patch", "signature": "def inspect_and_patch(path, config)"}, {"kind": "method", "line": 165, "name": "hamilton_product", "signature": "def hamilton_product(q1, q2)"}, {"kind": "method", "line": 176, "name": "normalize", "signature": "def normalize(q, eps)"}, {"kind": "method", "line": 180, "name": "conjugate", "signature": "def conjugate(q)"}, {"kind": "method", "line": 185, "name": "rotate_vector", "signature": "def rotate_vector(v, q)"}, {"kind": "method", "line": 196, "name": "__init__", "signature": "def __init__(self, in_features, out_features, bias)"}, {"kind": "method", "line": 209, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 221, "name": "__init__", "signature": "def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)"}, {"kind": "method", "line": 233, "name": "_kernel", "signature": "def _kernel(self, c)"}, {"kind": "method", "line": 236, "name": "_contract", "signature": "def _contract(self, W, X)"}, {"kind": "method", "line": 239, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 263, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 286, "name": "_filter1d", "signature": "def _filter1d(self, x, kr, ki)"}, {"kind": "method", "line": 291, "name": "encode", "signature": "def encode(self, x)"}, {"kind": "method", "line": 295, "name": "decode", "signature": "def decode(self, z)"}, {"kind": "method", "line": 299, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 305, "name": "process_torus_grid", "signature": "def process_torus_grid(self, grid)"}, {"kind": "method", "line": 313, "name": "__init__", "signature": "def __init__(self, d_model, config)"}, {"kind": "method", "line": 338, "name": "_build_torus_graph", "signature": "def _build_torus_graph(self)"}, {"kind": "method", "line": 354, "name": "_torus_soft_assign", "signature": "def _torus_soft_assign(self, phi1, phi2)"}, {"kind": "method", "line": 365, "name": "_message_passing", "signature": "def _message_passing(self, node_feat)"}, {"kind": "method", "line": 380, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 409, "name": "__init__", "signature": "def __init__(self, d_head, max_seq_len, base)"}, {"kind": "method", "line": 415, "name": "_build_cache", "signature": "def _build_cache(self, seq_len)"}, {"kind": "method", "line": 422, "name": "_rotate_half", "signature": "def _rotate_half(self, x)"}, {"kind": "method", "line": 426, "name": "forward", "signature": "def forward(self, q, k, seq_len, offset)"}, {"kind": "method", "line": 441, "name": "__init__", "signature": "def __init__(self, d_model, eps)"}, {"kind": "method", "line": 446, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 452, "name": "__init__", "signature": "def __init__(self, d_model, expansion, dropout)"}, {"kind": "method", "line": 464, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 469, "name": "__init__", "signature": "def __init__(self, d_model, config)"}, {"kind": "method", "line": 486, "name": "_route", "signature": "def _route(self, x)"}, {"kind": "method", "line": 509, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 523, "name": "__init__", "signature": "def __init__(self, d_model, n_heads, config)"}, {"kind": "method", "line": 539, "name": "forward", "signature": "def forward(self, x, is_causal, past_kv)"}, {"kind": "method", "line": 569, "name": "__init__", "signature": "def __init__(self, d_model, n_heads, config)"}, {"kind": "method", "line": 579, "name": "_forward_impl", "signature": "def _forward_impl(self, x, past_kv)"}, {"kind": "method", "line": 586, "name": "forward", "signature": "def forward(self, x, past_kv)"}, {"kind": "method", "line": 591, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 606, "name": "_init_weights", "signature": "def _init_weights(self)"}, {"kind": "method", "line": 613, "name": "forward", "signature": "def forward(self, token_ids, past_kvs)"}, {"kind": "method", "line": 627, "name": "generate", "signature": "def generate(self, token_ids, max_new_tokens, temperature, top_k, eos_token_id)"}, {"kind": "method", "line": 652, "name": "__init__", "signature": "def __init__(self, encoding)"}, {"kind": "method", "line": 658, "name": "encode", "signature": "def encode(self, text)"}, {"kind": "method", "line": 661, "name": "decode", "signature": "def decode(self, tokens)"}, {"kind": "method", "line": 664, "name": "eot_token", "signature": "def eot_token(self)"}, {"kind": "method", "line": 680, "name": "quantize", "signature": "def quantize(self, model)"}, {"kind": "method", "line": 684, "name": "get_format_name", "signature": "def get_format_name(self)"}, {"kind": "method", "line": 688, "name": "get_bits_per_weight", "signature": "def get_bits_per_weight(self)"}, {"kind": "method", "line": 693, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 696, "name": "quantize", "signature": "def quantize(self, model)"}, {"kind": "method", "line": 714, "name": "get_format_name", "signature": "def get_format_name(self)"}, {"kind": "method", "line": 717, "name": "get_bits_per_weight", "signature": "def get_bits_per_weight(self)"}, {"kind": "method", "line": 722, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 725, "name": "quantize", "signature": "def quantize(self, model)"}, {"kind": "method", "line": 739, "name": "get_format_name", "signature": "def get_format_name(self)"}, {"kind": "method", "line": 742, "name": "get_bits_per_weight", "signature": "def get_bits_per_weight(self)"}, {"kind": "method", "line": 747, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 750, "name": "quantize", "signature": "def quantize(self, model)"}, {"kind": "method", "line": 753, "name": "get_format_name", "signature": "def get_format_name(self)"}, {"kind": "method", "line": 756, "name": "get_bits_per_weight", "signature": "def get_bits_per_weight(self)"}, {"kind": "method", "line": 761, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 764, "name": "quantize", "signature": "def quantize(self, model)"}, {"kind": "method", "line": 767, "name": "get_format_name", "signature": "def get_format_name(self)"}, {"kind": "method", "line": 770, "name": "get_bits_per_weight", "signature": "def get_bits_per_weight(self)"}, {"kind": "method", "line": 775, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 778, "name": "quantize", "signature": "def quantize(self, model)"}, {"kind": "method", "line": 781, "name": "get_format_name", "signature": "def get_format_name(self)"}, {"kind": "method", "line": 784, "name": "get_bits_per_weight", "signature": "def get_bits_per_weight(self)"}, {"kind": "method", "line": 789, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 792, "name": "quantize", "signature": "def quantize(self, model)"}, {"kind": "method", "line": 795, "name": "get_format_name", "signature": "def get_format_name(self)"}, {"kind": "method", "line": 798, "name": "get_bits_per_weight", "signature": "def get_bits_per_weight(self)"}, {"kind": "method", "line": 803, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 806, "name": "quantize", "signature": "def quantize(self, model)"}, {"kind": "method", "line": 809, "name": "get_format_name", "signature": "def get_format_name(self)"}, {"kind": "method", "line": 812, "name": "get_bits_per_weight", "signature": "def get_bits_per_weight(self)"}, {"kind": "method", "line": 818, "name": "create_quantizer", "signature": "def create_quantizer(fmt, config)"}, {"kind": "method", "line": 835, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"kind": "method", "line": 839, "name": "load_checkpoint", "signature": "def load_checkpoint(self)"}, {"kind": "method", "line": 884, "name": "__init__", "signature": "def __init__(self, config, model, tokenizer)"}, {"kind": "method", "line": 891, "name": "run_inference", "signature": "def run_inference(self, prompt)"}, {"kind": "method", "line": 908, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 919, "name": "execute", "signature": "def execute(self)"}]}, {"id": "reinforce.py", "kind": "module", "label": "reinforce.py", "language": "py", "sha256": "79a3a7344acf247b", "symbol_count": 47, "symbols": [{"doc": "Parametric configuration for RL alignment of TopoGPT2.", "kind": "class", "line": 27, "name": "RLConfig", "signature": "class RLConfig"}, {"doc": "Enumeration of supported reward signal types.", "kind": "class", "line": 72, "name": "RewardSignalType", "signature": "class RewardSignalType(Enum)"}, {"doc": "Inspects checkpoint weights to align architecture configuration before instantiation.", "kind": "class", "line": 84, "name": "CheckpointPatcher", "signature": "class CheckpointPatcher"}, {"doc": "Computes reward signals from mechanistic interpretability metrics.", "kind": "class", "line": 120, "name": "MechanisticRewardCalculator", "signature": "class MechanisticRewardCalculator"}, {"doc": "Lightweight reward model for scoring generated responses.", "kind": "class", "line": 152, "name": "RewardModel", "signature": "class RewardModel(Module)"}, {"doc": "Stores trajectories for PPO training with advantage computation.", "kind": "class", "line": 189, "name": "ExperienceBuffer", "signature": "class ExperienceBuffer"}, {"doc": "Scalar value estimation head attached to TopoGPT2 for PPO.", "kind": "class", "line": 240, "name": "ValueHead", "signature": "class ValueHead(Module)"}, {"doc": "Proximal Policy Optimization trainer for TopoGPT2 alignment.", "kind": "class", "line": 262, "name": "PPOTrainer", "signature": "class PPOTrainer"}, {"doc": "High-level interface for RL-aligned TopoGPT2 as chatbot.", "kind": "class", "line": 519, "name": "ChatAgent", "signature": "class ChatAgent"}, {"kind": "method", "line": 597, "name": "setup_logger", "signature": "def setup_logger(name, level)"}, {"kind": "method", "line": 606, "name": "create_rl_agent_from_checkpoint", "signature": "def create_rl_agent_from_checkpoint(model_path, config, tokenizer, logger)"}, {"kind": "method", "line": 86, "name": "__init__", "signature": "def __init__(self, logger)"}, {"kind": "method", "line": 89, "name": "align_config", "signature": "def align_config(self, model_path, config, source_module)"}, {"kind": "method", "line": 111, "name": "_resolve_preset", "signature": "def _resolve_preset(self, scale)"}, {"kind": "method", "line": 122, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"kind": "method", "line": 129, "name": "compute_lc_reward", "signature": "def compute_lc_reward(self, lc_value)"}, {"kind": "method", "line": 133, "name": "compute_sp_reward", "signature": "def compute_sp_reward(self, sp_value)"}, {"kind": "method", "line": 137, "name": "compute_delta_reward", "signature": "def compute_delta_reward(self, delta_value)"}, {"kind": "method", "line": 142, "name": "compute_mechanistic_reward", "signature": "def compute_mechanistic_reward(self, metrics)"}, {"kind": "method", "line": 154, "name": "__init__", "signature": "def __init__(self, config, vocab_size, d_model)"}, {"kind": "method", "line": 173, "name": "_init_weights", "signature": "def _init_weights(self)"}, {"kind": "method", "line": 180, "name": "forward", "signature": "def forward(self, input_ids, attention_mask)"}, {"kind": "method", "line": 191, "name": "__init__", "signature": "def __init__(self, config, capacity)"}, {"kind": "method", "line": 198, "name": "add", "signature": "def add(self, experience)"}, {"kind": "method", "line": 201, "name": "compute_advantages", "signature": "def compute_advantages(self, values, rewards, masks)"}, {"kind": "method", "line": 215, "name": "sample_minibatches", "signature": "def sample_minibatches(self, batch_size)"}, {"kind": "method", "line": 226, "name": "_collate", "signature": "def _collate(self, batch)"}, {"kind": "method", "line": 237, "name": "clear", "signature": "def clear(self)"}, {"kind": "method", "line": 242, "name": "__init__", "signature": "def __init__(self, d_model, hidden_dim)"}, {"kind": "method", "line": 251, "name": "_init_weights", "signature": "def _init_weights(self)"}, {"kind": "method", "line": 258, "name": "forward", "signature": "def forward(self, hidden_states)"}, {"kind": "method", "line": 264, "name": "__init__", "signature": "def __init__(self, policy_model, config, reward_model, ref_model, logger)"}, {"kind": "method", "line": 294, "name": "generate_with_policy", "signature": "def generate_with_policy(self, prompt_ids, max_new_tokens)"}, {"kind": "method", "line": 306, "name": "compute_kl_divergence", "signature": "def compute_kl_divergence(self, policy_logits, ref_logits)"}, {"kind": "method", "line": 317, "name": "compute_reward", "signature": "def compute_reward(self, responses, prompts, metrics)"}, {"kind": "method", "line": 336, "name": "collect_experience", "signature": "def collect_experience(self, prompts, num_samples)"}, {"kind": "method", "line": 367, "name": "_extract_mechanistic_metrics", "signature": "def _extract_mechanistic_metrics(self, tokens)"}, {"kind": "method", "line": 398, "name": "ppo_update", "signature": "def ppo_update(self, batch)"}, {"kind": "method", "line": 460, "name": "train_step", "signature": "def train_step(self, prompts)"}, {"kind": "method", "line": 482, "name": "_save_checkpoint", "signature": "def _save_checkpoint(self)"}, {"kind": "method", "line": 498, "name": "load_checkpoint", "signature": "def load_checkpoint(self, path)"}, {"kind": "method", "line": 521, "name": "__init__", "signature": "def __init__(self, policy_model, config, tokenizer, logger)"}, {"kind": "method", "line": 530, "name": "attach_trainer", "signature": "def attach_trainer(self, trainer)"}, {"kind": "method", "line": 533, "name": "respond", "signature": "def respond(self, user_message, max_new_tokens)"}, {"kind": "method", "line": 553, "name": "_format_conversation", "signature": "def _format_conversation(self)"}, {"kind": "method", "line": 562, "name": "train_on_feedback", "signature": "def train_on_feedback(self, user_message, response, reward_score)"}, {"kind": "method", "line": 594, "name": "reset_conversation", "signature": "def reset_conversation(self)"}]}, {"id": "topogpt2_1.py", "kind": "module", "label": "topogpt2_1.py", "language": "py", "sha256": "28f93aa1f0651b03", "symbol_count": 126, "symbols": [{"doc": "Configuración completa para TopoGPT2.", "kind": "class", "line": 55, "name": "TopoGPT2Config", "signature": "class TopoGPT2Config"}, {"kind": "method", "line": 155, "name": "setup_logger", "signature": "def setup_logger(name, level)"}, {"kind": "method", "line": 165, "name": "set_seed", "signature": "def set_seed(seed, device)"}, {"doc": "Operaciones de cuaterniones puras en PyTorch.\nRepresentación: [..., 4]  donde last dim = [w, x, y, z]\nq = w + x*i + y*j + z*k", "kind": "class", "line": 177, "name": "QuaternionOps", "signature": "class QuaternionOps"}, {"doc": "Capa lineal con pesos cuaterniones.\n\nImplementa la multiplicación W * x en el álgebra de cuaterniones:\n- W = Ww + Wx*i + Wy*j + Wz*k  (cuaternión de pesos)\n- x = xw + xx*i + xy*j + xz*k  (cuaternión de entrada)\n- out = W * x  (producto de Hamilton extendido a vectores)\n\nParámetros: 4 matrices reales de forma [out_q, in_q]", "kind": "class", "line": 216, "name": "QuaternionLinear", "signature": "class QuaternionLinear(Module)"}, {"doc": "Convolución espectral 2D con cuaterniones y producto de Hamilton completo.\n\nOperación en dominio de frecuencia:\n    P(k) = W(k) ⊗ X(k)  (producto de Hamilton de cuaterniones complejos)\n\nDonde:\n    X(k) = FFT2(x) con 4 canales cuaterniones [Xw, Xx, Xy, Xz]\n    W(k) = kernel complejo aprendible con componentes [Ww, Wx, Wy, Wz]\n\nReglas del producto de Hamilton en dominio de frecuencia:\n    Pw = Ww·Xw - Wx·Xx - Wy·Xy - Wz·Xz\n    Px = Ww·Xx + Wx·Xw + Wy·Xz - Wz·Xy\n    Py = Ww·Xy - Wx·Xz + Wy·Xw + Wz·Xx\n    Pz = Ww·Xz + Wx·Xy - Wy·Xx + Wz·Xw\n\nCada Wc es un kernel complejo (partes real e imaginaria independientes).", "kind": "class", "line": 261, "name": "QuaternionSpectralLayer", "signature": "class QuaternionSpectralLayer(Module)"}, {"doc": "Autoencoder espectral con cuaterniones.\n\nOpera en dos niveles:\n1. Espectral 1D sobre el vector de features (FFT sobre dim D_MODEL):\n   captura la espectrografía global del embedding.\n2. Espectral 2D sobre el grid del toro (QuaternionSpectralLayer):\n   captura correlaciones espaciales en la topología.\n\nDevuelve (latent, recon_loss) para regularización.", "kind": "class", "line": 348, "name": "SpectralAutoencoder", "signature": "class SpectralAutoencoder(Module)"}, {"doc": "Reemplaza el MLP en cada capa del transformer.\n\nPipeline (completamente vectorizado sobre batch Y secuencia):\n\n1. Flatten: [B, S, D] → [B·S, D]\n2. SpectralAutoencoder: filtrado espectral 1D + compresión cuaternión\n3. Proyección al toro:\n   - Calcula 2 ángulos (phi1, phi2) ∈ [-π, π]²\n   - Asignación blanda a los 8 nodos via distancia circular en el toro\n4. Construye grid de nodos: [B·S, N_NODES=8, D_MODEL]\n5. QuaternionSpectralLayer 2D sobre el grid [B·S, 4*D_QUAT, RADIAL, ANGULAR]\n6. Message-passing con rotaciones cuaterniones sobre el grafo toro\n7. Readout: atención sobre los 8 nodos → [B·S, D_MODEL]\n8. Reshape: [B·S, D] → [B, S, D]", "kind": "class", "line": 431, "name": "QuaternionTorusBrain", "signature": "class QuaternionTorusBrain(Module)"}, {"doc": "Rotary Position Embeddings (RoPE) - Su et al., 2021.\nCodifica la posición como rotaciones del espacio de atención,\nnaturalmente relativas y sin parámetros extra.", "kind": "class", "line": 648, "name": "RotaryEmbedding", "signature": "class RotaryEmbedding(Module)"}, {"doc": "Root Mean Square Layer Normalization (sin bias). Más estable que LayerNorm.", "kind": "class", "line": 696, "name": "RMSNorm", "signature": "class RMSNorm(Module)"}, {"doc": "SwiGLU: SiLU(gate(x)) * up(x) -> down\nUsado en LLaMA 2/3, Qwen, Mistral en lugar de GELU-FFN.\nDimension interna: 8/3 * d_model (convención LLaMA, redondeada a múltiplo de 4).", "kind": "class", "line": 713, "name": "SwiGLU", "signature": "class SwiGLU(Module)"}, {"doc": "Mixture of Experts sobre la capa topologica.\n\nArquitectura (inspirada en DeepSeek-MoE / Mixtral):\n  - 1 experto compartido: QuaternionTorusBrain (siempre activo)\n  - N_EXPERTS expertos SwiGLU ligeros (activacion esparsa: Top-K por token)\n  - Router: Linear(D, N_EXPERTS) + softmax → top-K\n\nLoad-balancing loss (auxiliar): penaliza si un experto acapara todos los tokens.\nActiva MOE_TOP_K de N_EXPERTS expertos por token.\n\nSin MoE (MOE_ENABLED=False): se comporta como QuaternionTorusBrain puro.", "kind": "class", "line": 742, "name": "TopoMoEBrain", "signature": "class TopoMoEBrain(Module)"}, {"doc": "Multi-head attention con:\n- Flash Attention (scaled_dot_product_attention de PyTorch 2.0+)\n- Rotary Position Embeddings (RoPE)\n- GQA (Grouped Query Attention): N_KV_HEADS < N_HEADS, reduce VRAM de K/V\n- KV Cache para inferencia autoregresiva eficiente\n- Temperatura termodinámica aprendible", "kind": "class", "line": 847, "name": "MultiHeadAttention", "signature": "class MultiHeadAttention(Module)"}, {"doc": "Capa del transformer con TopoMoEBrain (TopoBrain + MoE SwiGLU experts).\n\nEsquema pre-norm (estilo LLaMA):\n    x = x + Attention_GQA(RMSNorm(x))\n    x = x + TopoMoEBrain(RMSNorm(x))", "kind": "class", "line": 929, "name": "TopoGPT2Layer", "signature": "class TopoGPT2Layer(Module)"}, {"doc": "TopoGPT2: Transformer de lenguaje con TopoBrain cuaternión-espectral.\n\nArquitectura:\n    Embedding de tokens + RoPE (en Attention)\n    N_LAYERS × TopoGPT2Layer (Attention + QuaternionTorusBrain)\n    RMSNorm final\n    Proyección a vocabulario (weight-tied con embeddings)", "kind": "class", "line": 976, "name": "TopoGPT2", "signature": "class TopoGPT2(Module)"}, {"doc": "Wrapper alrededor de tiktoken (GPT-2 compatible).", "kind": "class", "line": 1082, "name": "BPETokenizer", "signature": "class BPETokenizer"}, {"doc": "Descarga corpus de texto para entrenamiento.\n\nSoporta:\n- 'tinystories': ~2GB de cuentos cortos (ideal para pruebas)\n- 'wikitext103': ~500MB de Wikipedia curada\n- 'file': archivo de texto local\n\nUsa HuggingFace 'datasets' para TinyStories y WikiText.", "kind": "class", "line": 1107, "name": "CorpusDownloader", "signature": "class CorpusDownloader"}, {"doc": "Dataset de tokens para language modeling (next-token prediction).\n\nGuarda los tokens tokenizados en disco la primera vez (cache .pt)\npara evitar re-tokenizar en cada ejecucion. La clave de cache incluye\nun hash del contenido del corpus + tokenizador + max_tokens.", "kind": "class", "line": 1170, "name": "TokenizedDataset", "signature": "class TokenizedDataset(Dataset)"}, {"doc": "Gestiona checkpoints de forma acumulativa y segura.\n\nEstructura en disco:\n    checkpoints_topogpt2/\n      latest/\n        model.safetensors   <- pesos del modelo (formato seguro, sin pickle)\n        optimizer.pt        <- estado del optimizador (requiere .pt)\n        state.json          <- metadatos: epoch, step, historial, config\n      best/\n        model.safetensors\n        state.json\n      step_NNNNN/           <- snapshots periodicos (rotados)\n        model.safetensors\n        optimizer.pt\n        state.json\n\nEl historial se ACUMULA entre sesiones de entrenamiento: cada --resume\nagrega nuevas entradas a train_loss[], val_loss[], etc.", "kind": "class", "line": 1220, "name": "CheckpointManager", "signature": "class CheckpointManager"}, {"doc": "Entrenador acumulativo y resumible.\n\nCaracteristicas:\n- Checkpoint automatico en safetensors cada N minutos + cada epoch\n- Historial acumulativo entre sesiones (--resume agrega al historial existente)\n- Guarda el mejor modelo en checkpoints/best/ automaticamente\n- LR schedule: cosine con warmup relativo a los steps de ESTA sesion\n- Mixed Precision (AMP) + acumulacion de gradientes", "kind": "class", "line": 1453, "name": "TopoGPT2Trainer", "signature": "class TopoGPT2Trainer"}, {"doc": "Calcula todas las metricas del diagrama de fases de Book.md.\n\nTodas las metricas se derivan de cantidades medibles (pesos, gradientes):\n\ndelta  (δ): margen de discretizacion.  max|w - round(w)|\n            δ≈0 -> cristal;  δ≈0.49 -> vidrio frio\nkappa  (κ): numero de condicion de la covarianza del gradiente.\n            κ≈1 -> cristalino;  κ>>1 -> amorfo\nT_eff:      temperatura efectiva = (lr/2) * Var(gradiente).\n            T_eff→0 -> congelado; T_eff alto -> ruidoso\nalpha  (α): indice de pureza = -log(δ + ε).\n            α=20 -> perfecto; α<1 -> vidrio\nberry:      fase de Berry de los kernels espectrales imaginarios.\n            |berry|>π/2 con winding≠0 -> insulador topologico\nlc:         complejidad local = 1 - similitud coseno promedio entre filas.\nsp:         superposicion = correlacion promedio inter-fila de pesos.", "kind": "class", "line": 1746, "name": "MechanisticMetrics", "signature": "class MechanisticMetrics"}, {"doc": "Encuentra el ratio imaginario/real optimo para los kernels espectrales.\n\nAnalogia con main.py: evalua la transicion GOE→GUE en el espacio\nde kernels. Un ratio optimo promueve estructura topologica (insulador)\nvs estructura amorfa (vidrio).\n\nMetodo: calibra con un mini-batch y mide la varianza del gradiente\nen funcion del ratio. Ratios que minimizan la varianza de gradiente\n(maxima coherencia espectral) son preferibles.\n\nNo entrena: solo inicializa los kernels con distintos ratios y mide.\nTiempo tipico: < 30 segundos.", "kind": "class", "line": 1983, "name": "Phase0_KernelOptimizer", "signature": "class Phase0_KernelOptimizer"}, {"doc": "Encuentra el batch size optimo testando candidatos con pocos pasos.\n\nDe main.py: el batch size regula la temperatura del horno de cristalizacion.\nBatch sizes demasiado chicos -> ruido excesivo (vidrio frio).\nBatch sizes demasiado grandes -> sin presion annealing (amorfos).\nLa ventana optima empirica de main.py: [24, 128] para Strassen.\n\nPara LM, testeamos candidatos midiendo:\n- delta (δ): velocidad de descenso en prospect_steps pasos\n- T_eff: temperatura efectiva del gradiente\n\nTiempo tipico: < 2 minutos para 3 candidatos × 30 pasos.", "kind": "class", "line": 2058, "name": "Phase1_BatchProspector", "signature": "class Phase1_BatchProspector"}, {"doc": "Encuentra semillas prometedoras midiendo la trayectoria de delta.\n\nDe main.py: una semilla \"buena\" muestra delta descendente en los\nprimeros N pasos (enfriamiento). Una semilla \"mala\" se estanca en\nel plateau vidrioso (~0.49).\n\nCriterio de seleccion:\n1. Semillas con delta_velocity < 0 (enfriando) AND kappa bajo.\n2. Si no hay, semillas solo enfriando.\n3. Fallback: semilla con menor delta final.\n\nTiempo tipico: < 3 minutos para 5 semillas × 50 pasos.", "kind": "class", "line": 2141, "name": "Phase2_SeedMiner", "signature": "class Phase2_SeedMiner"}, {"doc": "Refinamiento post-entrenamiento mediante recocido simulado.\n\nDe main.py: despues de que el modelo converge, una fase de annealing\ncon criterio de aceptacion de Metropolis puede empujar los pesos\nhacia estados de menor energia libre (menor delta o mejor val_loss).\n\nAceptacion de Metropolis:\n    si Δloss < 0: siempre acepta (mejora)\n    si Δloss >= 0: acepta con prob exp(-Δloss / T)\n\nLa temperatura T decae exponencialmente: T(t) = T0 * cooling_rate^t\n\nAl rechazar: restaura el mejor estado conocido.\nSi se estanca: perturbacion termica (ruido gaussiano en pesos).\n\nTiempo: proporcional a refine_epochs (user-controlled).", "kind": "class", "line": 2223, "name": "Phase4_AnnealingRefiner", "signature": "class Phase4_AnnealingRefiner"}, {"doc": "Orquesta las 5 fases de entrenamiento segun main.py + Book.md.\n\nFases:\n  0  Kernel ratio optimization  (GOE-GUE spectral calibration)\n  1  Batch size prospecting      (temperatura del horno de cristalizacion)\n  2  Seed mining                 (seleccion de semilla enfriante)\n  3  Full training               (entrenamiento principal con metricas)\n  4  Annealing refinement        (recocido simulado post-entrenamiento)\n\nLas fases 0-2 son rapidas (prospecting). La fase 3 es el grueso.\nLa fase 4 es opcional (--refine).\n\nPara no ser prohibitivo:\n  --prospect         activa fases 0, 1, 2 antes del entrenamiento\n  --refine-epochs N  activa fase 4 con N epocas de annealing\n  Sin flags: solo fase 3 (comportamiento original, identico a antes)", "kind": "class", "line": 2384, "name": "TopoPhasePipeline", "signature": "class TopoPhasePipeline"}, {"kind": "method", "line": 2506, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 124, "name": "__post_init__", "signature": "def __post_init__(self)"}, {"doc": "Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].", "kind": "method", "line": 185, "name": "hamilton_product", "signature": "def hamilton_product(q1, q2)"}, {"kind": "method", "line": 197, "name": "normalize", "signature": "def normalize(q, eps)"}, {"kind": "method", "line": 201, "name": "conjugate", "signature": "def conjugate(q)"}, {"doc": "Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]", "kind": "method", "line": 206, "name": "rotate_vector", "signature": "def rotate_vector(v, q)"}, {"kind": "method", "line": 228, "name": "__init__", "signature": "def __init__(self, in_features, out_features, bias)"}, {"doc": "x: [..., in_features] → [..., out_features]", "kind": "method", "line": 244, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 281, "name": "__init__", "signature": "def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)"}, {"kind": "method", "line": 300, "name": "_kernel", "signature": "def _kernel(self, c)"}, {"doc": "Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]", "kind": "method", "line": 303, "name": "_contract", "signature": "def _contract(self, W, X)"}, {"doc": "x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)\n→ [B, 4*out_q, H, W]", "kind": "method", "line": 307, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 361, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Filtro espectral 1D: x[..., D] → filtrado[..., D]", "kind": "method", "line": 393, "name": "_filter1d", "signature": "def _filter1d(self, x, kr, ki)"}, {"doc": "x: [..., D_MODEL] → latent: [..., D_LAT]", "kind": "method", "line": 399, "name": "encode", "signature": "def encode(self, x)"}, {"doc": "z: [..., D_LAT] → recon: [..., D_MODEL]", "kind": "method", "line": 404, "name": "decode", "signature": "def decode(self, z)"}, {"doc": "Devuelve (latent, recon_loss)", "kind": "method", "line": 409, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Procesa el grid del toro con QuaternionSpectralLayer.\ngrid: [B, 4*D_QUAT, RADIAL, ANGULAR]  →  [B, 4*D_QUAT, RADIAL, ANGULAR]", "kind": "method", "line": 416, "name": "process_torus_grid", "signature": "def process_torus_grid(self, grid)"}, {"kind": "method", "line": 449, "name": "__init__", "signature": "def __init__(self, d_model, config)"}, {"doc": "Construye las aristas del grafo toro 2×4.\n\nNodos indexados como: node = r * N_ANGULAR + a\n  r ∈ [0, RADIAL-1], a ∈ [0, ANGULAR-1]\n\nAristas angulares: nodo ↔ nodo a la izquierda/derecha (periódico)\nAristas radiales:  nodo ↔ nodo del anillo interior/exterior", "kind": "method", "line": 489, "name": "_build_torus_graph", "signature": "def _build_torus_graph(self)"}, {"doc": "Asignación blanda de tokens a los 8 nodos del toro via distancia circular.\n\nphi1: [BS] ángulo angular ∈ [-π, π]\nphi2: [BS] ángulo radial ∈ [-π, π]\n→ weights: [BS, N_NODES]  (suma a 1, softmax de distancias negativas)", "kind": "method", "line": 523, "name": "_torus_soft_assign", "signature": "def _torus_soft_assign(self, phi1, phi2)"}, {"doc": "Message-passing VECTORIZADO con rotaciones cuaterniones.\nSin bucles Python: todas las aristas se procesan en paralelo.\n\nnode_feat: [BS, N_NODES, D_MODEL]\n→ [BS, N_NODES, D_MODEL]", "kind": "method", "line": 550, "name": "_message_passing", "signature": "def _message_passing(self, node_feat)"}, {"doc": "x: [B, S, D_MODEL]\n→ output: [B, S, D_MODEL], recon_loss: scalar", "kind": "method", "line": 587, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 655, "name": "__init__", "signature": "def __init__(self, d_head, max_seq_len, base)"}, {"kind": "method", "line": 661, "name": "_build_cache", "signature": "def _build_cache(self, seq_len)"}, {"kind": "method", "line": 668, "name": "_rotate_half", "signature": "def _rotate_half(self, x)"}, {"doc": "q, k: [B, n_heads, S_q/S_k, d_head]\noffset: posicion inicial (para KV cache: longitud del cache existente)\nAplica posiciones [offset .. offset+S-1] a q y k.", "kind": "method", "line": 672, "name": "forward", "signature": "def forward(self, q, k, seq_len, offset)"}, {"kind": "method", "line": 699, "name": "__init__", "signature": "def __init__(self, d_model, eps)"}, {"kind": "method", "line": 704, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 720, "name": "__init__", "signature": "def __init__(self, d_model, expansion, dropout)"}, {"kind": "method", "line": 734, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 757, "name": "__init__", "signature": "def __init__(self, d_model, config)"}, {"doc": "x: [N, D] donde N = B*S (tokens aplanados)\nRetorna:\nexpert_out: [N, D]  suma ponderada de top-K expertos\naux_loss:   escalar  load-balancing loss\nRouting vectorizado sin boolean indexing ni sincronizacion CUDA.\nUsa dispatch por indices agrupados (estilo Mixtral/DeepSeek) para\ncompatibilidad total con torch.utils.checkpoint.", "kind": "method", "line": 778, "name": "_route", "signature": "def _route(self, x)"}, {"doc": "x: [B, S, D]\n→ output: [B, S, D], aux_loss: escalar", "kind": "method", "line": 820, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 857, "name": "__init__", "signature": "def __init__(self, d_model, n_heads, config)"}, {"doc": "Args:\n    x:        [B, S, D]\n    is_causal: usar mascara causal\n    past_kv:  (K_cache, V_cache) de pasos anteriores o None\nReturns:\n    out:      [B, S, D]\n    kv_cache: (K, V) completos para cachear en generate()", "kind": "method", "line": 875, "name": "forward", "signature": "def forward(self, x, is_causal, past_kv)"}, {"kind": "method", "line": 938, "name": "__init__", "signature": "def __init__(self, d_model, n_heads, config)"}, {"kind": "method", "line": 947, "name": "_forward_impl", "signature": "def _forward_impl(self, x, past_kv)"}, {"doc": "Retorna (x_out, aux_loss, kv_cache).\nCon gradient checkpointing en training (solo cuando no hay KV cache).", "kind": "method", "line": 956, "name": "forward", "signature": "def forward(self, x, past_kv)"}, {"kind": "method", "line": 987, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1006, "name": "_init_weights", "signature": "def _init_weights(self)"}, {"doc": "token_ids: [B, S]  (enteros)\npast_kvs:  lista de (K, V) por capa, o None para entrenamiento\n→ logits: [B, S, VOCAB_SIZE], aux_loss: scalar, new_kvs: list[(K,V)]", "kind": "method", "line": 1013, "name": "forward", "signature": "def forward(self, token_ids, past_kvs)"}, {"kind": "method", "line": 1036, "name": "count_params", "signature": "def count_params(self)"}, {"doc": "Generacion autoregresiva con KV cache y muestreo top-k.\nEn el primer paso procesa el prompt completo y guarda el cache.\nEn pasos siguientes solo procesa 1 token nuevo (O(n) en lugar de O(n^2)).", "kind": "method", "line": 1042, "name": "generate", "signature": "def generate(self, token_ids, max_new_tokens, temperature, top_k)"}, {"kind": "method", "line": 1085, "name": "__init__", "signature": "def __init__(self, encoding)"}, {"kind": "method", "line": 1093, "name": "encode", "signature": "def encode(self, text)"}, {"kind": "method", "line": 1096, "name": "decode", "signature": "def decode(self, tokens)"}, {"kind": "method", "line": 1099, "name": "eot_token", "signature": "def eot_token(self)"}, {"kind": "method", "line": 1119, "name": "__init__", "signature": "def __init__(self, corpus, data_dir, logger)"}, {"doc": "Devuelve el texto del corpus. Descarga si es necesario.", "kind": "method", "line": 1125, "name": "get_text", "signature": "def get_text(self, split)"}, {"kind": "method", "line": 1150, "name": "_download_hf", "signature": "def _download_hf(self, dataset_name, split, text_column, name)"}, {"kind": "method", "line": 1179, "name": "__init__", "signature": "def __init__(self, text, tokenizer, seq_len, max_tokens, cache_dir, split_tag)"}, {"kind": "method", "line": 1206, "name": "__len__", "signature": "def __len__(self)"}, {"kind": "method", "line": 1209, "name": "__getitem__", "signature": "def __getitem__(self, idx)"}, {"kind": "method", "line": 1245, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS\npara que coincidan con la arquitectura guardada.\nNecesario cuando el codigo cambio GQA despues de guardar el checkpoint.", "kind": "method", "line": 1255, "name": "patch_config_for_resume", "signature": "def patch_config_for_resume(self, cfg)"}, {"kind": "method", "line": 1284, "name": "_save_model", "signature": "def _save_model(self, model, directory)"}, {"kind": "method", "line": 1297, "name": "_load_model", "signature": "def _load_model(self, model, directory)"}, {"kind": "method", "line": 1328, "name": "_save_optimizer", "signature": "def _save_optimizer(self, optimizer, directory)"}, {"kind": "method", "line": 1331, "name": "_load_optimizer", "signature": "def _load_optimizer(self, optimizer, directory, device)"}, {"kind": "method", "line": 1340, "name": "_save_state", "signature": "def _save_state(self, state, directory)"}, {"kind": "method", "line": 1345, "name": "_load_state", "signature": "def _load_state(self, directory)"}, {"kind": "method", "line": 1356, "name": "should_save", "signature": "def should_save(self)"}, {"doc": "Guarda checkpoint completo.\n\nstate debe contener al menos: completed_epochs, global_step,\nbest_val_loss, history, config.", "kind": "method", "line": 1359, "name": "save", "signature": "def save(self, model, optimizer, state, is_best)"}, {"doc": "Carga el ultimo checkpoint guardado.\nDevuelve el state dict (vacio si no hay checkpoint).", "kind": "method", "line": 1404, "name": "load_latest", "signature": "def load_latest(self, model, optimizer)"}, {"doc": "Carga el mejor modelo guardado (solo pesos, sin optimizador).", "kind": "method", "line": 1431, "name": "load_best", "signature": "def load_best(self, model)"}, {"kind": "method", "line": 1443, "name": "has_checkpoint", "signature": "def has_checkpoint(self)"}, {"kind": "method", "line": 1465, "name": "__init__", "signature": "def __init__(self, model, config, tokenizer)"}, {"doc": "Carga el ultimo checkpoint disponible.\nRestaura: pesos del modelo, estado del optimizador, historial acumulado,\nepoch/step completados y mejor val_loss.\nDevuelve True si se cargo un checkpoint, False si empieza de cero.", "kind": "method", "line": 1500, "name": "resume", "signature": "def resume(self)"}, {"doc": "Construye el dict de estado para persistir en state.json.", "kind": "method", "line": 1525, "name": "_current_state", "signature": "def _current_state(self)"}, {"doc": "Cosine decay con warmup. El schedule es relativo a la sesion actual.", "kind": "method", "line": 1536, "name": "_cosine_lr", "signature": "def _cosine_lr(self, step_in_session, total_steps_session)"}, {"kind": "method", "line": 1544, "name": "_set_lr", "signature": "def _set_lr(self, lr)"}, {"doc": "Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.\nEl historial se acumula sobre sesiones previas.", "kind": "method", "line": 1548, "name": "train", "signature": "def train(self, train_dl, val_dl)"}, {"doc": "Genera una muestra de texto al final de cada epoch para monitorear\nla calidad cualitativa del modelo (detecta degeneracion, repeticion, etc.).", "kind": "method", "line": 1684, "name": "_sample_text", "signature": "def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)"}, {"kind": "method", "line": 1716, "name": "evaluate", "signature": "def evaluate(self, dataloader)"}, {"kind": "method", "line": 1766, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 1774, "name": "compute_delta", "signature": "def compute_delta(self, model)"}, {"kind": "method", "line": 1781, "name": "compute_alpha", "signature": "def compute_alpha(self, delta)"}, {"doc": "Captura gradientes de forma segura, ignorando tensores corruptos.", "kind": "method", "line": 1786, "name": "update_grad_buffer", "signature": "def update_grad_buffer(self, model)"}, {"doc": "T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva.", "kind": "method", "line": 1812, "name": "compute_t_eff", "signature": "def compute_t_eff(self, lr)"}, {"doc": "κ = λ_max / λ_min de la covarianza del gradiente.\nParámetro de orden para cristalización (κ≈1 = cristal).\nNota: requiere pasadas backward adicionales. Se ejecuta con protección\npara no corromper el estado AMP del trainer principal.", "kind": "method", "line": 1820, "name": "compute_kappa", "signature": "def compute_kappa(self, model, dataloader, n_batches)"}, {"doc": "Fase de Berry de los kernels espectrales imaginarios.\nSurge de los parametros ki_w, ki_x, ki_y, ki_z de QuaternionSpectralLayer.\n|berry|>pi/2 con winding!=0 indica estructura topologica.", "kind": "method", "line": 1878, "name": "compute_berry_phase", "signature": "def compute_berry_phase(self, model)"}, {"doc": "Complejidad local: 1 - similitud coseno promedio entre filas de pesos.", "kind": "method", "line": 1891, "name": "compute_lc", "signature": "def compute_lc(self, model)"}, {"doc": "Superposicion: correlacion inter-fila promedio (entrelazamiento de features).", "kind": "method", "line": 1905, "name": "compute_sp", "signature": "def compute_sp(self, model)"}, {"doc": "Clasificacion de fase segun Book.md:\n\ndiscrete_crystal:       delta<0.05, kappa<1.5\ntopological_insulator:  |berry|>pi/2, winding!=0\ncold_glass:             kappa>>1, delta>0.3\nfunctional_glass:       intermedio (lo mas comun en LM)", "kind": "method", "line": 1921, "name": "classify_phase", "signature": "def classify_phase(self, delta, kappa, berry)"}, {"doc": "Calcula todas las metricas.\ncompute_kappa=True hace pasadas backward adicionales (caro, usar cada N epochs).", "kind": "method", "line": 1940, "name": "compute_all", "signature": "def compute_all(self, model, lr, dataloader, compute_kappa)"}, {"kind": "method", "line": 1965, "name": "format_log", "signature": "def format_log(self, m)"}, {"kind": "method", "line": 2001, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Mide la coherencia espectral para un ratio dado.\nRetorna: varianza del gradiente (menor = mas coherente = mejor).", "kind": "method", "line": 2005, "name": "_measure_ratio", "signature": "def _measure_ratio(self, ratio, sample_batch)"}, {"doc": "Retorna el mejor ratio de inicializacion de kernels espectrales.", "kind": "method", "line": 2034, "name": "optimize", "signature": "def optimize(self, dataloader)"}, {"kind": "method", "line": 2074, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Retorna el mejor batch size segun delta y T_eff.", "kind": "method", "line": 2078, "name": "prospect", "signature": "def prospect(self, candidates, train_dataset, prospect_steps)"}, {"kind": "method", "line": 2157, "name": "__init__", "signature": "def __init__(self, config, logger)"}, {"doc": "Retorna la semilla con la mejor trayectoria de delta.", "kind": "method", "line": 2161, "name": "mine", "signature": "def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)"}, {"kind": "method", "line": 2243, "name": "__init__", "signature": "def __init__(self, trainer, t0, cooling_rate, stagnation_patience)"}, {"doc": "Ejecuta refine_epochs epocas de recocido simulado.\nRetorna el historial de refinamiento.", "kind": "method", "line": 2252, "name": "refine", "signature": "def refine(self, train_dl, val_dl, refine_epochs)"}, {"kind": "method", "line": 2404, "name": "__init__", "signature": "def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)"}, {"kind": "method", "line": 2414, "name": "_make_dataloaders", "signature": "def _make_dataloaders(self, batch_size)"}, {"doc": "Ejecuta el pipeline completo.\nRetorna el trainer con el modelo entrenado.", "kind": "method", "line": 2426, "name": "run", "signature": "def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)"}, {"kind": "method", "line": 964, "name": "ckpt_fn", "signature": "def ckpt_fn(x_in)"}]}, {"id": "topogpt2_embeddings_navigator.py", "kind": "module", "label": "topogpt2_embeddings_navigator.py", "language": "py", "sha256": "8fc8c15139a532fd", "symbol_count": 149, "symbols": [{"doc": "Palette and CSS tokens for the navigator.", "kind": "class", "line": 86, "name": "ThemeTokens", "signature": "class ThemeTokens"}, {"doc": "Plot-level theme.", "kind": "class", "line": 103, "name": "PlotTheme", "signature": "class PlotTheme"}, {"doc": "Safety caps to keep the UI responsive.", "kind": "class", "line": 118, "name": "SamplingLimits", "signature": "class SamplingLimits"}, {"doc": "Numerical stability thresholds.", "kind": "class", "line": 132, "name": "MetricsConfig", "signature": "class MetricsConfig"}, {"doc": "Projection hyperparameters.", "kind": "class", "line": 146, "name": "ProjectionConfig", "signature": "class ProjectionConfig"}, {"doc": "Top-level configuration.", "kind": "class", "line": 156, "name": "NavigatorConfig", "signature": "class NavigatorConfig"}, {"doc": "Injects the navigator's CSS once per session.", "kind": "class", "line": 189, "name": "StyleInjector", "signature": "class StyleInjector"}, {"doc": "Holds a loaded TopoGPT2 model along with its config and tokenizer.", "kind": "class", "line": 263, "name": "CheckpointBundle", "signature": "class CheckpointBundle"}, {"doc": "Builds a ``CheckpointBundle`` from a checkpoint on disk or in memory.", "kind": "class", "line": 312, "name": "ModelLoader", "signature": "class ModelLoader"}, {"doc": "Extracts per-layer residual-stream activations via forward hooks.", "kind": "class", "line": 522, "name": "ActivationCapture", "signature": "class ActivationCapture"}, {"doc": "Computes the full geometric and topological metric suite.", "kind": "class", "line": 600, "name": "MetricSuite", "signature": "class MetricSuite"}, {"doc": "Projects point clouds into 2D or 3D with multiple algorithms.", "kind": "class", "line": 1068, "name": "Projector", "signature": "class Projector"}, {"doc": "Consistent Plotly styling for every figure.", "kind": "class", "line": 1195, "name": "FigureStyler", "signature": "class FigureStyler"}, {"doc": "Bundle passed to every view during rendering.", "kind": "class", "line": 1243, "name": "RenderContext", "signature": "class RenderContext"}, {"doc": "Abstract base for navigator views.", "kind": "class", "line": 1255, "name": "BaseEmbeddingView", "signature": "class BaseEmbeddingView(ABC)"}, {"doc": "Token table, per-layer scalar metric evolution, summary panel.", "kind": "class", "line": 1274, "name": "OverviewView", "signature": "class OverviewView(BaseEmbeddingView)"}, {"doc": "Interactive 3D cloud of one layer's residual-stream activations.", "kind": "class", "line": 1352, "name": "CloudView", "signature": "class CloudView(BaseEmbeddingView)"}, {"doc": "Detailed per-layer metric card for a selected layer.", "kind": "class", "line": 1475, "name": "MetricsView", "signature": "class MetricsView(BaseEmbeddingView)"}, {"doc": "Persistence diagram and barcode for H0 and H1.", "kind": "class", "line": 1569, "name": "PersistenceView", "signature": "class PersistenceView(BaseEmbeddingView)"}, {"doc": "Berry phase and winding number analysis of the token trajectory.", "kind": "class", "line": 1666, "name": "BerryPhaseView", "signature": "class BerryPhaseView(BaseEmbeddingView)"}, {"doc": "Local Lipschitz profile and trajectory geometry (speed/curvature/torsion).", "kind": "class", "line": 1758, "name": "LipschitzView", "signature": "class LipschitzView(BaseEmbeddingView)"}, {"doc": "kNN graph and neighborhood statistics.", "kind": "class", "line": 1834, "name": "NeighborhoodView", "signature": "class NeighborhoodView(BaseEmbeddingView)"}, {"doc": "Per-token drift across the residual stream.", "kind": "class", "line": 1933, "name": "CrossLayerView", "signature": "class CrossLayerView(BaseEmbeddingView)"}, {"doc": "Quaternion decomposition of activations (w, x, y, z sub-channels).", "kind": "class", "line": 1994, "name": "QuaternionView", "signature": "class QuaternionView(BaseEmbeddingView)"}, {"doc": "Raw activation heatmap (tokens x features).", "kind": "class", "line": 2108, "name": "RawView", "signature": "class RawView(BaseEmbeddingView)"}, {"doc": "Collects and instantiates views.", "kind": "class", "line": 2145, "name": "ViewRegistry", "signature": "class ViewRegistry"}, {"doc": "Sidebar inputs (checkpoint, text, kNN, model script path).", "kind": "class", "line": 2161, "name": "SidebarController", "signature": "class SidebarController"}, {"doc": "Imports ``topogpt2_1.py`` from a user-supplied filesystem path.", "kind": "class", "line": 2217, "name": "ModuleImporter", "signature": "class ModuleImporter"}, {"doc": "Top-level orchestrator.", "kind": "class", "line": 2255, "name": "NavigatorApp", "signature": "class NavigatorApp"}, {"doc": "Streamlit script entry point.", "kind": "method", "line": 2418, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 192, "name": "__init__", "signature": "def __init__(self, theme)"}, {"doc": "Render the CSS block in the current Streamlit page.", "kind": "method", "line": 195, "name": "inject", "signature": "def inject(self)"}, {"kind": "method", "line": 266, "name": "__init__", "signature": "def __init__(self, model, config, tokenizer, source_name)"}, {"doc": "Return the underlying nn.Module in eval mode.", "kind": "method", "line": 279, "name": "model", "signature": "def model(self)"}, {"doc": "Return the model config object.", "kind": "method", "line": 284, "name": "config", "signature": "def config(self)"}, {"doc": "Return the BPE tokenizer.", "kind": "method", "line": 289, "name": "tokenizer", "signature": "def tokenizer(self)"}, {"doc": "Return the original file name of the checkpoint.", "kind": "method", "line": 294, "name": "source_name", "signature": "def source_name(self)"}, {"doc": "Return the device the model is currently placed on.", "kind": "method", "line": 299, "name": "device", "signature": "def device(self)"}, {"doc": "Return the number of transformer layers in the model.", "kind": "method", "line": 303, "name": "num_layers", "signature": "def num_layers(self)"}, {"doc": "Return the model hidden size.", "kind": "method", "line": 307, "name": "embedding_dim", "signature": "def embedding_dim(self)"}, {"kind": "method", "line": 315, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Load a checkpoint and instantiate the corresponding model.\n\nArgs:\n    source: Either a filesystem path or a Streamlit UploadedFile.\n    topogpt2_module: Already-imported ``topogpt2_1`` module providing\n        ``TopoGPT2``, ``TopoGPT2Config``, and ``BPETokenizer``.\n\nReturns:\n    A :class:`CheckpointBundle` with model, config, and tokenizer.\n\nRaises:\n    ValueError: if the checkpoint extension is not supported or if\n        the model config cannot be reconstructed.", "kind": "method", "line": 318, "name": "load", "signature": "def load(self, source, topogpt2_module)"}, {"kind": "method", "line": 344, "name": "_read_state_dict", "signature": "def _read_state_dict(self, source)"}, {"kind": "method", "line": 366, "name": "_materialize", "signature": "def _materialize(self, source)"}, {"kind": "method", "line": 374, "name": "_extract_payload", "signature": "def _extract_payload(self, obj)"}, {"kind": "method", "line": 391, "name": "_build_config", "signature": "def _build_config(self, topogpt2_module, embedded_cfg, state_dict)"}, {"kind": "method", "line": 405, "name": "_infer_config", "signature": "def _infer_config(self, topogpt2_module, state_dict)"}, {"kind": "method", "line": 433, "name": "_infer_d_model", "signature": "def _infer_d_model(state_dict)"}, {"kind": "method", "line": 439, "name": "_infer_num_layers", "signature": "def _infer_num_layers(state_dict)"}, {"kind": "method", "line": 450, "name": "_infer_n_heads", "signature": "def _infer_n_heads(state_dict, d_model)"}, {"kind": "method", "line": 467, "name": "_infer_max_seq_len", "signature": "def _infer_max_seq_len(state_dict)"}, {"doc": "Infer the number of key/value heads for GQA.\n\nIn GQA the ``k_proj`` (and ``v_proj``) output dimension equals\n``n_kv_heads * d_head``. When the checkpoint was trained with\nstandard multi-head attention ``n_kv_heads`` equals ``n_heads``.\nPassing the explicit value via ``N_KV_HEADS`` avoids the automatic\n``N_HEADS // 4`` heuristic in ``TopoGPT2Config`` which would\notherwise produce a shape mismatch at load time.", "kind": "method", "line": 475, "name": "_infer_n_kv_heads", "signature": "def _infer_n_kv_heads(state_dict, d_head, n_heads)"}, {"kind": "method", "line": 505, "name": "_infer_torus_grid", "signature": "def _infer_torus_grid(state_dict)"}, {"kind": "method", "line": 514, "name": "_validate_load", "signature": "def _validate_load(missing, unexpected)"}, {"kind": "method", "line": 525, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Run a single forward pass and return activations and tokens.\n\nArgs:\n    bundle: The loaded :class:`CheckpointBundle`.\n    text: The input text to encode.\n\nReturns:\n    A dictionary with keys ``tokens`` (list of decoded pieces),\n    ``ids`` (list of token ids), ``embedding`` (initial token\n    embeddings), ``layers`` (list of per-layer residual-stream\n    activations of shape ``[S, D]``), and ``final`` (the post\n    final-norm activations).", "kind": "method", "line": 528, "name": "run", "signature": "def run(self, bundle, text)"}, {"kind": "method", "line": 589, "name": "_decode_pieces", "signature": "def _decode_pieces(tokenizer, ids)"}, {"kind": "method", "line": 603, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute every metric on a point cloud ``[N, D]``.\n\nArgs:\n    points: Array of shape ``[N, D]`` with ``N >= 4``.\n    knn: Number of neighbours for the kNN graph.\n\nReturns:\n    Dictionary with scalar and array metrics.", "kind": "method", "line": 606, "name": "compute", "signature": "def compute(self, points, knn)"}, {"kind": "method", "line": 642, "name": "_sanitize", "signature": "def _sanitize(self, points)"}, {"kind": "method", "line": 645, "name": "_trivial", "signature": "def _trivial(self, base)"}, {"kind": "method", "line": 675, "name": "_pairwise", "signature": "def _pairwise(self, points)"}, {"kind": "method", "line": 678, "name": "_shortest_paths", "signature": "def _shortest_paths(self, points, knn)"}, {"kind": "method", "line": 698, "name": "_sp_metrics", "signature": "def _sp_metrics(self, dist_eucl, dist_geo)"}, {"doc": "Local curvature proxy from the chord-vs-arc ratio.\n\nFor every point and every nearby pair (a, b) we compare the\nEuclidean chord 0.5*(d_E(i,a) + d_E(i,b)) to the geodesic arc\n0.5*(d_G(i,a) + d_G(i,b)). When the ratio chord/arc is near 1 the\nlocal neighbourhood is flat; when it is less than 1 the arc bends\noutward (spherical-like, positive curvature). The returned scalar\nkappa = 1 - (chord/arc)^2, bounded in [0, 1] for positive curvature\nand scale-free so it can be compared across layers.", "kind": "method", "line": 718, "name": "_kappa", "signature": "def _kappa(self, dist_eucl, dist_geo)"}, {"kind": "method", "line": 759, "name": "_gromov_delta", "signature": "def _gromov_delta(self, dist_geo)"}, {"kind": "method", "line": 783, "name": "_persistence", "signature": "def _persistence(self, points, dist_eucl)"}, {"kind": "method", "line": 810, "name": "_h0_from_mst", "signature": "def _h0_from_mst(self, edges, n)"}, {"doc": "Estimate H1 persistence bars from a distance-sorted edge list.\n\nWhen an edge is added that does not reduce the number of\nconnected components, it closes a loop. The birth of that H1\nfeature is the filtration level at which the loop appears. We\nestimate the death as the minimum filtration level at which the\nloop is filled in by a 2-simplex in the Vietoris-Rips complex\nformed from the same edges. When no such filling appears within\nthe edge budget, the bar is marked as surviving to the maximum\nscale.", "kind": "method", "line": 845, "name": "_h1_from_edges", "signature": "def _h1_from_edges(self, edges, n)"}, {"kind": "method", "line": 905, "name": "_berry_phases", "signature": "def _berry_phases(self, points)"}, {"kind": "method", "line": 920, "name": "_winding_numbers", "signature": "def _winding_numbers(self, points)"}, {"kind": "method", "line": 936, "name": "_planar_winding", "signature": "def _planar_winding(self, xs, ys)"}, {"kind": "method", "line": 947, "name": "_lipschitz", "signature": "def _lipschitz(self, points)"}, {"doc": "Frenet-Serret differential geometry of the token trajectory.\n\nSpeed is computed in the full ambient space. Curvature and torsion\nare well-defined in 3D, so they are evaluated on the top-3 PCA\nprojection of the sequence; this preserves geometry while giving a\nclean, interpretable scalar per position.", "kind": "method", "line": 954, "name": "_trajectory_geometry", "signature": "def _trajectory_geometry(self, points)"}, {"kind": "method", "line": 1017, "name": "_safe_pca3", "signature": "def _safe_pca3(self, points)"}, {"kind": "method", "line": 1030, "name": "_spectral_properties", "signature": "def _spectral_properties(self, points)"}, {"kind": "method", "line": 1071, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Project ``[N, D]`` points to ``n_components`` dims.\n\nArgs:\n    points: Input point cloud of shape ``[N, D]``.\n    method: ``\"pca\"``, ``\"isomap\"``, ``\"umap\"``, ``\"random\"`` or\n        ``\"sphere\"``.\n    n_components: Desired output dimensionality.\n\nReturns:\n    Tuple ``(embedding, info)`` where ``info`` contains method\n    specific diagnostics (explained variance, etc.).", "kind": "method", "line": 1074, "name": "project", "signature": "def project(self, points, method, n_components)"}, {"kind": "method", "line": 1105, "name": "_pca", "signature": "def _pca(self, points, n_components)"}, {"kind": "method", "line": 1123, "name": "_isomap", "signature": "def _isomap(self, points, n_components)"}, {"kind": "method", "line": 1144, "name": "_umap", "signature": "def _umap(self, points, n_components)"}, {"kind": "method", "line": 1171, "name": "_random", "signature": "def _random(self, points, n_components)"}, {"kind": "method", "line": 1181, "name": "_sphere", "signature": "def _sphere(self, points, n_components)"}, {"kind": "method", "line": 1198, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Apply 3D styling.", "kind": "method", "line": 1201, "name": "style_3d", "signature": "def style_3d(self, fig, title, height)"}, {"doc": "Apply 2D styling.", "kind": "method", "line": 1223, "name": "style_2d", "signature": "def style_2d(self, fig, title, height)"}, {"kind": "method", "line": 1261, "name": "__init__", "signature": "def __init__(self, ctx)"}, {"doc": "Return the shared render context.", "kind": "method", "line": 1265, "name": "ctx", "signature": "def ctx(self)"}, {"doc": "Render the view into the current Streamlit container.", "kind": "method", "line": 1270, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1280, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1284, "name": "_render_tokens", "signature": "def _render_tokens(self)"}, {"kind": "method", "line": 1310, "name": "_render_layer_evolution", "signature": "def _render_layer_evolution(self)"}, {"kind": "method", "line": 1358, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1378, "name": "_choose", "signature": "def _choose(self, acts, selection)"}, {"kind": "method", "line": 1386, "name": "_render_trajectory", "signature": "def _render_trajectory(self, emb, tokens, ids, norms, stage, method, info)"}, {"kind": "method", "line": 1442, "name": "_render_residual_streams", "signature": "def _render_residual_streams(self, acts, method)"}, {"kind": "method", "line": 1481, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1490, "name": "_get_metrics", "signature": "def _get_metrics(self, stage)"}, {"kind": "method", "line": 1496, "name": "_render_card", "signature": "def _render_card(self, m)"}, {"kind": "method", "line": 1521, "name": "_render_kappa", "signature": "def _render_kappa(self, m)"}, {"kind": "method", "line": 1544, "name": "_render_path_metrics", "signature": "def _render_path_metrics(self, m)"}, {"kind": "method", "line": 1575, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1583, "name": "_stage_metrics", "signature": "def _stage_metrics(self, stage)"}, {"kind": "method", "line": 1591, "name": "_render_diagram", "signature": "def _render_diagram(self, m)"}, {"kind": "method", "line": 1633, "name": "_render_barcode", "signature": "def _render_barcode(self, m)"}, {"kind": "method", "line": 1672, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1680, "name": "_stage_metrics", "signature": "def _stage_metrics(self, stage)"}, {"kind": "method", "line": 1688, "name": "_render_berry", "signature": "def _render_berry(self, m, stage)"}, {"kind": "method", "line": 1720, "name": "_render_winding", "signature": "def _render_winding(self, m, stage)"}, {"kind": "method", "line": 1764, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1772, "name": "_stage_metrics", "signature": "def _stage_metrics(self, stage)"}, {"kind": "method", "line": 1780, "name": "_render_lc", "signature": "def _render_lc(self, m)"}, {"kind": "method", "line": 1807, "name": "_render_dynamics", "signature": "def _render_dynamics(self, m)"}, {"kind": "method", "line": 1840, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1849, "name": "_stage_metrics", "signature": "def _stage_metrics(self, stage)"}, {"kind": "method", "line": 1857, "name": "_stage_points", "signature": "def _stage_points(self, stage)"}, {"kind": "method", "line": 1864, "name": "_render_graph", "signature": "def _render_graph(self, points, m)"}, {"kind": "method", "line": 1911, "name": "_render_coherence", "signature": "def _render_coherence(self, points)"}, {"kind": "method", "line": 1939, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1962, "name": "_cosine_diag", "signature": "def _cosine_diag(self, A, B)"}, {"kind": "method", "line": 1968, "name": "_render_heatmap", "signature": "def _render_heatmap(self, title, z, xlabels, tokens, diverging)"}, {"kind": "method", "line": 2000, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 2021, "name": "_points", "signature": "def _points(self, stage)"}, {"kind": "method", "line": 2029, "name": "_render_component_norms", "signature": "def _render_component_norms(self, comps)"}, {"kind": "method", "line": 2054, "name": "_render_quaternion_norms", "signature": "def _render_quaternion_norms(self, comps)"}, {"kind": "method", "line": 2070, "name": "_render_sphere", "signature": "def _render_sphere(self, comps)"}, {"kind": "method", "line": 2114, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 2136, "name": "_points", "signature": "def _points(self, stage)"}, {"kind": "method", "line": 2148, "name": "__init__", "signature": "def __init__(self, context)"}, {"doc": "Register a view factory.", "kind": "method", "line": 2152, "name": "register", "signature": "def register(self, factory)"}, {"doc": "Instantiate every registered view.", "kind": "method", "line": 2156, "name": "build", "signature": "def build(self)"}, {"kind": "method", "line": 2164, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Render the sidebar and return user selections.", "kind": "method", "line": 2167, "name": "render", "signature": "def render(self)"}, {"doc": "Dynamically import the TopoGPT2 module.\n\nArgs:\n    path: Path to ``topogpt2_1.py``.\n\nReturns:\n    The imported module object.\n\nRaises:\n    FileNotFoundError: if the path does not exist.\n    ImportError: if the module cannot be loaded.", "kind": "method", "line": 2220, "name": "load", "signature": "def load(self, path)"}, {"kind": "method", "line": 2258, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Entry point for ``streamlit run``.", "kind": "method", "line": 2269, "name": "run", "signature": "def run(self)"}, {"kind": "method", "line": 2307, "name": "_render_header", "signature": "def _render_header(self)"}, {"kind": "method", "line": 2324, "name": "_render_landing", "signature": "def _render_landing(self)"}, {"kind": "method", "line": 2335, "name": "_try_load_bundle", "signature": "def _try_load_bundle(self, selections)"}, {"kind": "method", "line": 2351, "name": "_compute_all_metrics", "signature": "def _compute_all_metrics(self, activations, knn)"}, {"kind": "method", "line": 2367, "name": "_render_meta", "signature": "def _render_meta(self, bundle, activations, knn)"}, {"kind": "method", "line": 2380, "name": "_build_registry", "signature": "def _build_registry(self, ctx)"}, {"kind": "method", "line": 2394, "name": "_render_tabs", "signature": "def _render_tabs(self, registry)"}, {"kind": "method", "line": 2408, "name": "_render_footer", "signature": "def _render_footer(self)"}, {"kind": "method", "line": 561, "name": "hook", "signature": "def hook(_module, _inputs, output)"}, {"kind": "method", "line": 818, "name": "find", "signature": "def find(x)"}, {"kind": "method", "line": 824, "name": "union", "signature": "def union(x, y)"}, {"kind": "method", "line": 864, "name": "find", "signature": "def find(x)"}, {"kind": "method", "line": 870, "name": "union", "signature": "def union(x, y)"}]}, {"id": "topogpt2_explorer.py", "kind": "module", "label": "topogpt2_explorer.py", "language": "py", "sha256": "03e43e8965c27ba5", "symbol_count": 155, "symbols": [{"doc": "Design tokens for the explorer's dark scientific theme.", "kind": "class", "line": 59, "name": "ThemeTokens", "signature": "class ThemeTokens"}, {"doc": "Plot-level theme constants.", "kind": "class", "line": 76, "name": "PlotTheme", "signature": "class PlotTheme"}, {"doc": "Hard caps to keep the UI responsive regardless of model size.", "kind": "class", "line": 91, "name": "SamplingLimits", "signature": "class SamplingLimits"}, {"doc": "Numerical stability thresholds for metrics.", "kind": "class", "line": 108, "name": "MetricsConfig", "signature": "class MetricsConfig"}, {"doc": "Random-projection and synthetic probe parameters.", "kind": "class", "line": 120, "name": "GenerationLimits", "signature": "class GenerationLimits"}, {"doc": "Top-level configuration container.", "kind": "class", "line": 129, "name": "ExplorerConfig", "signature": "class ExplorerConfig"}, {"doc": "Injects the global CSS for the explorer into the Streamlit page.", "kind": "class", "line": 168, "name": "StyleInjector", "signature": "class StyleInjector"}, {"doc": "Classifies tensor keys from a TopoGPT2 checkpoint by semantic role.\n\nThe classifier parses the parameter name and extracts:\n  * a coarse role (\"attention\", \"moe_router\", \"spectral_kernel\", etc.)\n  * the layer index if present\n  * the quaternion component (w, x, y, z) if present\n  * whether the tensor represents a frequency-domain kernel", "kind": "class", "line": 244, "name": "TensorClassifier", "signature": "class TensorClassifier"}, {"doc": "Loads raw tensor dictionaries from disk.\n\nSupports both ``safetensors`` files and plain PyTorch pickles produced\nby ``torch.save``. The loader returns CPU float32 tensors exclusively to\nguarantee downstream compatibility with NumPy.", "kind": "class", "line": 337, "name": "CheckpointLoader", "signature": "class CheckpointLoader"}, {"doc": "Holds a checkpoint's tensors along with per-tensor metadata.", "kind": "class", "line": 429, "name": "TensorInventory", "signature": "class TensorInventory"}, {"doc": "Projects arbitrary tensors into 2D matrices and 3D point clouds.\n\nResponsibilities:\n  * Reduce N-dimensional tensors to a 2D matrix of rows (samples) vs\n    columns (features) while preserving interpretability.\n  * Subsample rows/columns to respect the configured limits.\n  * Compute 3D embeddings (PCA or Gaussian random projection) with\n    deterministic seeding.", "kind": "class", "line": 515, "name": "TensorProjector", "signature": "class TensorProjector"}, {"doc": "Computes mechanistic-interpretability metrics for parameter matrices.\n\nResults are memoized by the ``id`` of the input array to guarantee that\nrepeated requests for the same subsampled matrix (common across tabs) do\nnot re-run expensive SVDs.", "kind": "class", "line": 635, "name": "MetricCalculator", "signature": "class MetricCalculator"}, {"doc": "Applies consistent styling to Plotly figures.", "kind": "class", "line": 836, "name": "FigureStyler", "signature": "class FigureStyler"}, {"doc": "Context passed to visualizers at render time.", "kind": "class", "line": 883, "name": "VisualizationContext", "signature": "class VisualizationContext(Protocol)"}, {"doc": "Concrete visualization context implementation.", "kind": "class", "line": 894, "name": "RenderContext", "signature": "class RenderContext"}, {"doc": "Abstract base class for all visualizers.\n\nSubclasses implement :meth:`render` and :meth:`is_applicable`. The registry\nwill instantiate them only when :meth:`is_applicable` returns ``True``.", "kind": "class", "line": 904, "name": "BaseVisualizer", "signature": "class BaseVisualizer(ABC)"}, {"doc": "Top-level summary of the checkpoint: counts, roles, and inventory table.", "kind": "class", "line": 931, "name": "OverviewVisualizer", "signature": "class OverviewVisualizer(BaseVisualizer)"}, {"doc": "Deep-dive into a single tensor: 3D cloud, heatmap, histograms, spectrum.", "kind": "class", "line": 999, "name": "TensorExplorerVisualizer", "signature": "class TensorExplorerVisualizer(BaseVisualizer)"}, {"doc": "Visualize QuaternionLinear layers by their (Ww, Wx, Wy, Wz) components.", "kind": "class", "line": 1227, "name": "QuaternionDecompositionVisualizer", "signature": "class QuaternionDecompositionVisualizer(BaseVisualizer)"}, {"doc": "Visualize complex spectral kernels (kr/ki pairs) in the frequency plane.", "kind": "class", "line": 1385, "name": "SpectralKernelVisualizer", "signature": "class SpectralKernelVisualizer(BaseVisualizer)"}, {"doc": "3D torus graph of the QuaternionTorusBrain node embeddings and edges.", "kind": "class", "line": 1538, "name": "TorusTopologyVisualizer", "signature": "class TorusTopologyVisualizer(BaseVisualizer)"}, {"doc": "Per-layer attention Q/K/V/O projection analysis with per-head split.", "kind": "class", "line": 1773, "name": "AttentionVisualizer", "signature": "class AttentionVisualizer(BaseVisualizer)"}, {"doc": "Router logit landscape and expert weight geometry.", "kind": "class", "line": 1916, "name": "MoEVisualizer", "signature": "class MoEVisualizer(BaseVisualizer)"}, {"doc": "Track how metrics evolve across transformer layers for a chosen role.", "kind": "class", "line": 2061, "name": "LayerEvolutionVisualizer", "signature": "class LayerEvolutionVisualizer(BaseVisualizer)"}, {"doc": "Cross-tensor geometry: embed every weight matrix as a 3D point via summary features.", "kind": "class", "line": 2151, "name": "GlobalGeometryVisualizer", "signature": "class GlobalGeometryVisualizer(BaseVisualizer)"}, {"doc": "Collects visualizer classes and dispatches to them by label.", "kind": "class", "line": 2291, "name": "VisualizerRegistry", "signature": "class VisualizerRegistry"}, {"doc": "Renders the sidebar controls and returns user selections.", "kind": "class", "line": 2316, "name": "SidebarController", "signature": "class SidebarController"}, {"doc": "Top-level orchestration: composes loader, registry, and layout.", "kind": "class", "line": 2359, "name": "ExplorerApp", "signature": "class ExplorerApp"}, {"doc": "Streamlit script entry point.", "kind": "method", "line": 2493, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 171, "name": "__init__", "signature": "def __init__(self, theme)"}, {"kind": "method", "line": 174, "name": "_build_css", "signature": "def _build_css(self)"}, {"doc": "Render the CSS block inside the current Streamlit page.", "kind": "method", "line": 239, "name": "inject", "signature": "def inject(self)"}, {"doc": "Return structured metadata for a checkpoint tensor.\n\nArgs:\n    name: Full dotted parameter name.\n    shape: Tensor shape.\n\nReturns:\n    A dictionary with keys ``role``, ``layer``, ``component``,\n    ``is_spectral``, ``is_complex_kernel``, ``shape``.", "kind": "method", "line": 258, "name": "classify", "signature": "def classify(self, name, shape)"}, {"kind": "method", "line": 286, "name": "_classify_role", "signature": "def _classify_role(self, name)"}, {"kind": "method", "line": 328, "name": "_extract_layer", "signature": "def _extract_layer(self, name)"}, {"kind": "method", "line": 332, "name": "_extract_quaternion_component", "signature": "def _extract_quaternion_component(self, name)"}, {"kind": "method", "line": 345, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Load a checkpoint from a file path or an uploaded file-like.\n\nArgs:\n    source: Either a path (``str`` or ``Path``) or a Streamlit\n        ``UploadedFile`` object.\n\nReturns:\n    Dictionary mapping tensor name to CPU ``torch.Tensor``.\n\nRaises:\n    ValueError: If the extension is not supported.\n    RuntimeError: If deserialization fails.", "kind": "method", "line": 348, "name": "load", "signature": "def load(self, source)"}, {"kind": "method", "line": 373, "name": "_materialize", "signature": "def _materialize(self, source)"}, {"kind": "method", "line": 382, "name": "_load_safetensors", "signature": "def _load_safetensors(self, buffer)"}, {"kind": "method", "line": 389, "name": "_load_torch", "signature": "def _load_torch(self, buffer)"}, {"kind": "method", "line": 399, "name": "_extract_state_dict", "signature": "def _extract_state_dict(self, obj)"}, {"kind": "method", "line": 413, "name": "_looks_like_state_dict", "signature": "def _looks_like_state_dict(obj)"}, {"kind": "method", "line": 420, "name": "_to_cpu_float32", "signature": "def _to_cpu_float32(tensor)"}, {"kind": "method", "line": 432, "name": "__init__", "signature": "def __init__(self, tensors, classifier)"}, {"doc": "Return all tensor names sorted alphabetically.", "kind": "method", "line": 443, "name": "names", "signature": "def names(self)"}, {"doc": "Retrieve a tensor by name.", "kind": "method", "line": 447, "name": "tensor", "signature": "def tensor(self, name)"}, {"doc": "Retrieve structured metadata for a tensor.", "kind": "method", "line": 451, "name": "meta", "signature": "def meta(self, name)"}, {"doc": "Return all unique layer indices present in the checkpoint.", "kind": "method", "line": 455, "name": "layers", "signature": "def layers(self)"}, {"doc": "Return the distinct roles present in the checkpoint.", "kind": "method", "line": 460, "name": "roles", "signature": "def roles(self)"}, {"doc": "Return tensor names matching the supplied filters.", "kind": "method", "line": 464, "name": "filter", "signature": "def filter(self, role, layer, component, spectral_only)"}, {"doc": "Total parameter count across the checkpoint.", "kind": "method", "line": 485, "name": "total_parameters", "signature": "def total_parameters(self)"}, {"doc": "Return a list of per-tensor rows suitable for a Streamlit table.", "kind": "method", "line": 489, "name": "summary_rows", "signature": "def summary_rows(self)"}, {"kind": "method", "line": 526, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Convert a tensor to a 2D ``float64`` matrix.\n\nComplex tensors are stacked as ``[real, imag]`` along the feature axis\nbefore flattening, which preserves their dimensionality information.", "kind": "method", "line": 531, "name": "to_matrix", "signature": "def to_matrix(self, tensor)"}, {"doc": "Return a row/column subsample bounded by the configured caps.", "kind": "method", "line": 553, "name": "subsample", "signature": "def subsample(self, matrix, max_rows, max_cols, seed)"}, {"doc": "Project a matrix to 3D using PCA or Gaussian random projection.\n\nArgs:\n    matrix: Row-major 2D matrix ``[N, F]``.\n    method: Either ``\"pca\"`` or ``\"random\"``.\n\nReturns:\n    A pair ``(embedding[N, 3], info)`` where ``info`` contains the\n    explained variance ratio (PCA) or the Johnson-Lindenstrauss\n    ``eps`` used (random projection).", "kind": "method", "line": 575, "name": "project_3d", "signature": "def project_3d(self, matrix, method)"}, {"kind": "method", "line": 606, "name": "_pca_3d", "signature": "def _pca_3d(self, matrix)"}, {"kind": "method", "line": 617, "name": "_random_3d", "signature": "def _random_3d(self, matrix)"}, {"kind": "method", "line": 643, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute the full metrics dictionary in one pass.\n\nUses a lightweight cache keyed by ``(id(matrix), shape)`` so that\nrecomputation across visualizers is avoided when the same subsampled\nmatrix is analyzed multiple times in one render cycle.", "kind": "method", "line": 649, "name": "compute_all", "signature": "def compute_all(self, matrix)"}, {"doc": "Compute singular values once, reused by rank and participation ratio.", "kind": "method", "line": 681, "name": "_svd_safe", "signature": "def _svd_safe(self, matrix)"}, {"kind": "method", "line": 690, "name": "_effective_rank_from_svd", "signature": "def _effective_rank_from_svd(self, svd_values, shape)"}, {"kind": "method", "line": 707, "name": "_participation_from_svd", "signature": "def _participation_from_svd(self, svd_values, shape)"}, {"doc": "Fraction of entries whose absolute value is below ``threshold``.", "kind": "method", "line": 720, "name": "sparsity", "signature": "def sparsity(self, matrix, threshold)"}, {"doc": "Shannon entropy (nats) of the discrete value histogram.\n\nUses probability mass (not density), which guarantees a non-negative\nresult bounded above by ``log(histogram_bins)``. This is the standard\nconvention for interpretability dashboards.", "kind": "method", "line": 727, "name": "entropy", "signature": "def entropy(self, matrix)"}, {"doc": "Effective rank via the exponential of the entropy of singular values.", "kind": "method", "line": 748, "name": "effective_rank", "signature": "def effective_rank(self, matrix)"}, {"doc": "Participation ratio of the singular value spectrum.\n\nDefined as ``(sum s)^2 / sum(s^2)`` which equals the effective number\nof nonzero singular directions.", "kind": "method", "line": 753, "name": "participation_ratio", "signature": "def participation_ratio(self, matrix)"}, {"doc": "Approximate the effective embedding dimension via PCA.\n\nCounts the number of principal components whose explained variance\nexceeds ``default_fractal_variance_floor``.", "kind": "method", "line": 762, "name": "fractal_dimension", "signature": "def fractal_dimension(self, matrix)"}, {"doc": "Maximum and mean absolute cosine similarity between rows.", "kind": "method", "line": 781, "name": "coherence", "signature": "def coherence(self, matrix)"}, {"doc": "Spectral flatness (Wiener entropy) in dB averaged over rows.", "kind": "method", "line": 796, "name": "spectral_flatness", "signature": "def spectral_flatness(self, matrix)"}, {"doc": "Index of the dominant non-zero frequency bin of row 0.", "kind": "method", "line": 814, "name": "dominant_frequency", "signature": "def dominant_frequency(self, matrix)"}, {"kind": "method", "line": 824, "name": "_subsample_for_svd", "signature": "def _subsample_for_svd(self, matrix)"}, {"kind": "method", "line": 830, "name": "_subsample_for_pca", "signature": "def _subsample_for_pca(self, matrix)"}, {"kind": "method", "line": 839, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Apply the standard 3D scene styling.", "kind": "method", "line": 842, "name": "style_3d", "signature": "def style_3d(self, fig, title)"}, {"doc": "Apply the standard 2D figure styling.", "kind": "method", "line": 864, "name": "style_2d", "signature": "def style_2d(self, fig, title, height)"}, {"kind": "method", "line": 914, "name": "__init__", "signature": "def __init__(self, context)"}, {"doc": "Return the render context bound to this visualizer.", "kind": "method", "line": 918, "name": "ctx", "signature": "def ctx(self)"}, {"doc": "Return ``True`` if there is data in the inventory to render.", "kind": "method", "line": 922, "name": "is_applicable", "signature": "def is_applicable(self)"}, {"doc": "Render the visualizer into the current Streamlit container.", "kind": "method", "line": 927, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 937, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 950, "name": "_render_headline", "signature": "def _render_headline(self, total_params, num_tensors, num_layers)"}, {"kind": "method", "line": 957, "name": "_render_role_breakdown", "signature": "def _render_role_breakdown(self, role_counts, role_params)"}, {"kind": "method", "line": 984, "name": "_render_inventory_table", "signature": "def _render_inventory_table(self, rows)"}, {"kind": "method", "line": 1005, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1042, "name": "_render_meta", "signature": "def _render_meta(self, meta)"}, {"kind": "method", "line": 1050, "name": "_render_metric_grid", "signature": "def _render_metric_grid(self, metrics)"}, {"kind": "method", "line": 1069, "name": "_render_point_cloud", "signature": "def _render_point_cloud(self, matrix, name, method)"}, {"kind": "method", "line": 1103, "name": "_render_heatmap", "signature": "def _render_heatmap(self, matrix, name)"}, {"kind": "method", "line": 1125, "name": "_render_distribution", "signature": "def _render_distribution(self, matrix, name)"}, {"kind": "method", "line": 1149, "name": "_render_spectrum", "signature": "def _render_spectrum(self, matrix, name)"}, {"kind": "method", "line": 1180, "name": "_render_singular_spectrum", "signature": "def _render_singular_spectrum(self, matrix, name)"}, {"kind": "method", "line": 1233, "name": "is_applicable", "signature": "def is_applicable(self)"}, {"kind": "method", "line": 1237, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1249, "name": "_group_quaternion_bundles", "signature": "def _group_quaternion_bundles(self)"}, {"kind": "method", "line": 1263, "name": "_quaternion_bundle_key", "signature": "def _quaternion_bundle_key(name, component)"}, {"kind": "method", "line": 1278, "name": "_render_component_stats", "signature": "def _render_component_stats(self, components)"}, {"kind": "method", "line": 1290, "name": "_render_component_heatmaps", "signature": "def _render_component_heatmaps(self, components)"}, {"kind": "method", "line": 1315, "name": "_render_component_spectra", "signature": "def _render_component_spectra(self, components)"}, {"kind": "method", "line": 1346, "name": "_render_unit_norm_distribution", "signature": "def _render_unit_norm_distribution(self, components)"}, {"kind": "method", "line": 1391, "name": "is_applicable", "signature": "def is_applicable(self)"}, {"kind": "method", "line": 1397, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1413, "name": "_pair_kr_ki", "signature": "def _pair_kr_ki(self)"}, {"kind": "method", "line": 1428, "name": "_reshape_to_2d", "signature": "def _reshape_to_2d(self, magnitude, phase)"}, {"kind": "method", "line": 1439, "name": "_render_magnitude_phase", "signature": "def _render_magnitude_phase(self, magnitude, phase, key)"}, {"kind": "method", "line": 1470, "name": "_render_complex_scatter", "signature": "def _render_complex_scatter(self, complex_kernel, key)"}, {"kind": "method", "line": 1504, "name": "_render_radial_profile", "signature": "def _render_radial_profile(self, magnitude, key)"}, {"kind": "method", "line": 1544, "name": "is_applicable", "signature": "def is_applicable(self)"}, {"kind": "method", "line": 1547, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1568, "name": "_infer_grid", "signature": "def _infer_grid(self, n_nodes)"}, {"kind": "method", "line": 1578, "name": "_render_headline_metrics", "signature": "def _render_headline_metrics(self, nodes, edges, radial_bins, angular_bins)"}, {"kind": "method", "line": 1591, "name": "_render_3d_torus", "signature": "def _render_3d_torus(self, nodes, edges, radial_bins, angular_bins)"}, {"kind": "method", "line": 1605, "name": "_torus_positions", "signature": "def _torus_positions(self, nodes, radial_bins, angular_bins)"}, {"kind": "method", "line": 1631, "name": "_add_edges", "signature": "def _add_edges(self, fig, positions, radial_bins, angular_bins, edges)"}, {"kind": "method", "line": 1669, "name": "_edge_label", "signature": "def _edge_label(edge_type)"}, {"kind": "method", "line": 1678, "name": "_build_segments", "signature": "def _build_segments(positions, radial_bins, angular_bins)"}, {"kind": "method", "line": 1697, "name": "_add_nodes", "signature": "def _add_nodes(self, fig, positions, node_colors, n_nodes)"}, {"kind": "method", "line": 1725, "name": "_render_node_correlation", "signature": "def _render_node_correlation(self, nodes)"}, {"kind": "method", "line": 1747, "name": "_render_edge_quaternions", "signature": "def _render_edge_quaternions(self, edges)"}, {"kind": "method", "line": 1779, "name": "is_applicable", "signature": "def is_applicable(self)"}, {"kind": "method", "line": 1785, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1813, "name": "_infer_head_count", "signature": "def _infer_head_count(self, matrix, proj)"}, {"kind": "method", "line": 1822, "name": "_render_per_head_norms", "signature": "def _render_per_head_norms(self, matrix, proj)"}, {"kind": "method", "line": 1849, "name": "_render_per_head_spectrum", "signature": "def _render_per_head_spectrum(self, matrix, proj, layer)"}, {"kind": "method", "line": 1881, "name": "_render_head_similarity", "signature": "def _render_head_similarity(self, matrix, proj, layer)"}, {"kind": "method", "line": 1908, "name": "_render_summary_metrics", "signature": "def _render_summary_metrics(self, metrics)"}, {"kind": "method", "line": 1922, "name": "is_applicable", "signature": "def is_applicable(self)"}, {"kind": "method", "line": 1927, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 1949, "name": "_render_router_norms", "signature": "def _render_router_norms(self, router, layer)"}, {"kind": "method", "line": 1972, "name": "_render_routing_probe", "signature": "def _render_routing_probe(self, router, layer)"}, {"kind": "method", "line": 2015, "name": "_render_expert_similarity", "signature": "def _render_expert_similarity(self, layer)"}, {"kind": "method", "line": 2055, "name": "_softmax", "signature": "def _softmax(logits)"}, {"kind": "method", "line": 2067, "name": "is_applicable", "signature": "def is_applicable(self)"}, {"kind": "method", "line": 2070, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 2113, "name": "_render_metric_grid", "signature": "def _render_metric_grid(self, role, layers, series)"}, {"kind": "method", "line": 2157, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 2204, "name": "_render_scatter", "signature": "def _render_scatter(self, emb, labels, roles, sizes, pca)"}, {"kind": "method", "line": 2246, "name": "_render_feature_correlation", "signature": "def _render_feature_correlation(self, X_std, example)"}, {"kind": "method", "line": 2279, "name": "_build_palette", "signature": "def _build_palette(n)"}, {"kind": "method", "line": 2294, "name": "__init__", "signature": "def __init__(self, context)"}, {"doc": "Register a visualizer factory.\n\nArgs:\n    factory: Callable producing a :class:`BaseVisualizer` instance\n        given the shared render context.", "kind": "method", "line": 2298, "name": "register", "signature": "def register(self, factory)"}, {"doc": "Instantiate all registered visualizers.", "kind": "method", "line": 2307, "name": "build", "signature": "def build(self)"}, {"doc": "Return the subset of visualizers whose data is present.", "kind": "method", "line": 2311, "name": "applicable", "signature": "def applicable(self)"}, {"kind": "method", "line": 2319, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Render the sidebar and return the current selections.", "kind": "method", "line": 2322, "name": "render", "signature": "def render(self)"}, {"kind": "method", "line": 2362, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Entry point used by ``streamlit run``.", "kind": "method", "line": 2372, "name": "run", "signature": "def run(self)"}, {"kind": "method", "line": 2394, "name": "_configure_page", "signature": "def _configure_page(self)"}, {"kind": "method", "line": 2401, "name": "_render_header", "signature": "def _render_header(self)"}, {"kind": "method", "line": 2416, "name": "_render_landing", "signature": "def _render_landing(self)"}, {"kind": "method", "line": 2437, "name": "_resolve_checkpoint", "signature": "def _resolve_checkpoint(self, selections)"}, {"kind": "method", "line": 2452, "name": "_build_registry", "signature": "def _build_registry(self, context)"}, {"kind": "method", "line": 2465, "name": "_render_tabs", "signature": "def _render_tabs(self, registry)"}, {"kind": "method", "line": 2483, "name": "_render_footer", "signature": "def _render_footer(self)"}]}, {"id": "topogpt2_grid_scaler.py", "kind": "module", "label": "topogpt2_grid_scaler.py", "language": "py", "sha256": "453351a7952fa330", "symbol_count": 54, "symbols": [{"doc": "Controls the spectral weight interpolation.", "kind": "class", "line": 97, "name": "InterpolationConfig", "signature": "class InterpolationConfig"}, {"doc": "What to measure after each scaling step.", "kind": "class", "line": 108, "name": "ValidationConfig", "signature": "class ValidationConfig"}, {"doc": "Multi-hop scaling strategy.", "kind": "class", "line": 121, "name": "ProgressiveConfig", "signature": "class ProgressiveConfig"}, {"doc": "Output files.", "kind": "class", "line": 131, "name": "OutputConfig", "signature": "class OutputConfig"}, {"doc": "Top-level configuration — mirrors scaler_config_128.toml.", "kind": "class", "line": 141, "name": "TopoScalerConfig", "signature": "class TopoScalerConfig"}, {"kind": "method", "line": 169, "name": "_setup_logger", "signature": "def _setup_logger(name, level)"}, {"doc": "Dynamically imports topogpt2_1.py from any path.", "kind": "class", "line": 181, "name": "ModuleImporter", "signature": "class ModuleImporter"}, {"doc": "Reads a TopoGPT2 checkpoint and any embedded config.", "kind": "class", "line": 205, "name": "CheckpointReader", "signature": "class CheckpointReader"}, {"doc": "Reconstructs TopoGPT2Config from weights, inferring all dimensions.", "kind": "class", "line": 242, "name": "ConfigReconstructor", "signature": "class ConfigReconstructor"}, {"doc": "Classifies every state-dict key by its D_MODEL scaling role.", "kind": "class", "line": 328, "name": "TensorRole", "signature": "class TensorRole"}, {"doc": "Interpolates weight tensors via Fourier-space zero-padding or cropping.\n\nThis is the core of the technique — identical in principle to the\nWillmore Crystal scaler's Fourier interpolation of spectral kernels,\nadapted to weight matrices of arbitrary shape.", "kind": "class", "line": 380, "name": "SpectralInterpolator", "signature": "class SpectralInterpolator"}, {"doc": "Scales every tensor in a state dict from src_d to tgt_d.\n\nRouting table:\n  topo_graph   → verbatim copy\n  edge_quat    → verbatim copy\n  rope         → rebuilt from scratch for new D_HEAD\n  spectral_2d  → interpolate channel dims (D_q axes); topo dims verbatim\n  spectral_1d  → interpolate 1D frequency axis (D//2+1 → D'//2+1)\n  node_embed   → interpolate feature axis (D → D')\n  quat_linear  → 2D spectral interpolation [out_q, in_q] → [out_q', in_q']\n  matrix       → 2D spectral interpolation on D-dependent axes\n  vector       → 1D spectral interpolation\n  scalar       → verbatim copy", "kind": "class", "line": 483, "name": "StateScaler", "signature": "class StateScaler"}, {"doc": "Measures spectral structure preservation before and after scaling.", "kind": "class", "line": 635, "name": "ScalingValidator", "signature": "class ScalingValidator"}, {"doc": "Loads scaled weights into a fresh TopoGPT2.", "kind": "class", "line": 723, "name": "ModelAssembler", "signature": "class ModelAssembler"}, {"doc": "Saves checkpoint, metrics JSON, and text report.", "kind": "class", "line": 751, "name": "CheckpointSaver", "signature": "class CheckpointSaver"}, {"doc": "Main orchestrator.\n\nMirrors the Willmore Crystal scaler pipeline:\n\n  source_grid_size = D_MODEL_src\n  target_grid_sizes = [D1, D2, ...]  (progressive)\n\nThe torus topology is the structural invariant: RADIAL, ANGULAR,\nN_TORUS_NODES, edges_i/j/type, edge_quat are never modified.", "kind": "class", "line": 860, "name": "TopoGPT2DModelScaler", "signature": "class TopoGPT2DModelScaler"}, {"kind": "method", "line": 1070, "name": "build_parser", "signature": "def build_parser()"}, {"kind": "method", "line": 1097, "name": "config_from_args", "signature": "def config_from_args(args)"}, {"kind": "method", "line": 1119, "name": "main", "signature": "def main()"}, {"kind": "method", "line": 159, "name": "__post_init__", "signature": "def __post_init__(self)"}, {"doc": "Import and return the topogpt2 module.", "kind": "method", "line": 184, "name": "load", "signature": "def load(self, path)"}, {"doc": "Return (state_dict, optional_embedded_config).", "kind": "method", "line": 208, "name": "read", "signature": "def read(self, path, device)"}, {"kind": "method", "line": 225, "name": "_extract", "signature": "def _extract(self, obj)"}, {"doc": "Return a TopoGPT2Config that matches the loaded weights exactly.", "kind": "method", "line": 245, "name": "reconstruct", "signature": "def reconstruct(self, mod, state_dict, embedded)"}, {"kind": "method", "line": 259, "name": "_infer", "signature": "def _infer(self, mod, sd)"}, {"kind": "method", "line": 291, "name": "_infer_d_head", "signature": "def _infer_d_head(sd)"}, {"kind": "method", "line": 298, "name": "_infer_n_kv", "signature": "def _infer_n_kv(sd, d_head, n_heads)"}, {"kind": "method", "line": 308, "name": "_infer_max_seq", "signature": "def _infer_max_seq(sd)"}, {"kind": "method", "line": 315, "name": "_infer_torus", "signature": "def _infer_torus(sd)"}, {"doc": "Return a semantic role string.\n\nRoles:\n  topo_graph    — graph index buffers (topology invariant, verbatim)\n  edge_quat     — learned edge quaternions (topology invariant, verbatim)\n  rope          — RoPE cache (rebuilt for new D_HEAD)\n  spectral_2d   — 2D quaternion spectral kernels [D_q, D_q, R, Af]\n  spectral_1d   — 1D spectral AE filters [D//2+1]\n  node_embed    — torus node embeddings [N_NODES, D]\n  quat_linear   — QuaternionLinear component weights [out_q, in_q]\n  matrix        — any other 2D weight [M, N] where both dims scale with D\n  vector        — any 1D parameter [D] (norms, biases)\n  scalar        — 0D parameter (temperature)\n  verbatim      — anything not classified above", "kind": "method", "line": 340, "name": "classify", "signature": "def classify(self, key, shape)"}, {"kind": "method", "line": 388, "name": "__init__", "signature": "def __init__(self, cfg)"}, {"doc": "Scale a 2D weight matrix [M, N] to [M', N'] via spectral interpolation.\n\nSteps:\n  1. FFT2 of W.\n  2. Zero-pad or centre-crop frequency spectrum to (M', N').\n  3. IFFT2.\n  4. Amplitude normalisation: ||W'||_F = ||W||_F.", "kind": "method", "line": 391, "name": "interpolate_2d", "signature": "def interpolate_2d(self, W, tgt_rows, tgt_cols)"}, {"doc": "Scale a 1D vector of length L to length L' via spectral interpolation.", "kind": "method", "line": 421, "name": "interpolate_1d", "signature": "def interpolate_1d(self, v, tgt_len)"}, {"doc": "Zero-pad or centre-crop a 2D complex spectrum.", "kind": "method", "line": 452, "name": "_resize_spectrum_2d", "signature": "def _resize_spectrum_2d(self, W_f, tgt_rows, tgt_cols)"}, {"kind": "method", "line": 499, "name": "__init__", "signature": "def __init__(self, interp, role_clf, logger)"}, {"doc": "Produce a complete scaled state dict.", "kind": "method", "line": 509, "name": "scale", "signature": "def scale(self, src_state, src_cfg, tgt_cfg, mod)"}, {"doc": "Route to the correct interpolation method based on shape and role.", "kind": "method", "line": 567, "name": "_dispatch", "signature": "def _dispatch(self, src, tgt_shape, role, key)"}, {"doc": "Scale [in_q, out_q, R, Af] to [in_q', out_q', R, Af].\n\nR and Af are topo-invariant and must not change.", "kind": "method", "line": 598, "name": "_scale_spectral_2d_to", "signature": "def _scale_spectral_2d_to(self, t, tgt_shape, key)"}, {"kind": "method", "line": 626, "name": "_bilinear_fallback", "signature": "def _bilinear_fallback(self, src, tgt_shape)"}, {"kind": "method", "line": 638, "name": "__init__", "signature": "def __init__(self, cfg)"}, {"doc": "Compute all configured validation metrics.", "kind": "method", "line": 641, "name": "compute", "signature": "def compute(self, state, d_model)"}, {"doc": "Return True if any metric dropped beyond its tolerance.", "kind": "method", "line": 656, "name": "check_degradation", "signature": "def check_degradation(self, before, after, logger)"}, {"kind": "method", "line": 690, "name": "_spectral_concentration", "signature": "def _spectral_concentration(self, sd)"}, {"kind": "method", "line": 708, "name": "_phase_coherence", "signature": "def _phase_coherence(self, sd)"}, {"doc": "Instantiate the target model and load scaled weights.", "kind": "method", "line": 726, "name": "assemble", "signature": "def assemble(self, mod, tgt_cfg, scaled_state, logger)"}, {"doc": "Persist scaled checkpoint and metadata. Returns checkpoint path.", "kind": "method", "line": 754, "name": "save", "signature": "def save(self, model, tgt_cfg, src_cfg, metrics_before, metrics_after, out_cfg, step_tag, logger)"}, {"kind": "method", "line": 815, "name": "_write_report", "signature": "def _write_report(self, path, src_cfg, tgt_cfg, before, after, ckpt)"}, {"kind": "method", "line": 872, "name": "__init__", "signature": "def __init__(self, cfg)"}, {"doc": "Execute the full scaling pipeline. Returns per-step result dicts.", "kind": "method", "line": 888, "name": "run", "signature": "def run(self)"}, {"doc": "Construct a target config with new D_MODEL, preserving torus topology.", "kind": "method", "line": 1001, "name": "_build_target_config", "signature": "def _build_target_config(self, mod, src_cfg, tgt_d)"}, {"doc": "Find the largest divisor of tgt_d that keeps D_HEAD >= 8.", "kind": "method", "line": 1018, "name": "_infer_n_heads", "signature": "def _infer_n_heads(tgt_d, src_n_heads)"}, {"kind": "method", "line": 1033, "name": "_infer_n_kv_heads", "signature": "def _infer_n_kv_heads(tgt_d, tgt_n_heads, src_n_heads, src_n_kv)"}, {"kind": "method", "line": 1047, "name": "_print_summary", "signature": "def _print_summary(self, results, src_cfg)"}, {"kind": "method", "line": 770, "name": "_cfg_dict", "signature": "def _cfg_dict(c)"}]}, {"id": "topogpt2_multi_inference.py", "kind": "module", "label": "topogpt2_multi_inference.py", "language": "py", "sha256": "506a1cd290961f9d", "symbol_count": 44, "symbols": [{"doc": "Generation hyper-parameters.", "kind": "class", "line": 60, "name": "SamplingConfig", "signature": "class SamplingConfig"}, {"doc": "Top-level execution configuration.", "kind": "class", "line": 72, "name": "RunConfig", "signature": "class RunConfig"}, {"kind": "method", "line": 85, "name": "_setup_logger", "signature": "def _setup_logger(name, level)"}, {"doc": "Imports topogpt2_1.py from any filesystem path (cached per process).", "kind": "class", "line": 95, "name": "ModuleImporter", "signature": "class ModuleImporter"}, {"doc": "Resolves a mixed list of files and directories to concrete checkpoint paths.", "kind": "class", "line": 122, "name": "CheckpointDiscovery", "signature": "class CheckpointDiscovery"}, {"doc": "Loads state dicts and any embedded config from checkpoint files.", "kind": "class", "line": 164, "name": "CheckpointLoader", "signature": "class CheckpointLoader"}, {"doc": "Reconstructs a TopoGPT2Config from weights, inferring every dimension.", "kind": "class", "line": 219, "name": "ConfigReconstructor", "signature": "class ConfigReconstructor"}, {"doc": "Builds and caches BPETokenizer instances.", "kind": "class", "line": 315, "name": "TokenizerFactory", "signature": "class TokenizerFactory"}, {"doc": "Autoregressive generation with top-k, top-p, and repetition penalty.", "kind": "class", "line": 327, "name": "GenerationEngine", "signature": "class GenerationEngine"}, {"doc": "Result from running one checkpoint.", "kind": "class", "line": 433, "name": "ModelResult", "signature": "class ModelResult"}, {"doc": "Runs one prompt through every checkpoint and collects results.", "kind": "class", "line": 450, "name": "MultiInferenceRunner", "signature": "class MultiInferenceRunner"}, {"doc": "Formats and prints inference results.", "kind": "class", "line": 584, "name": "ResultRenderer", "signature": "class ResultRenderer"}, {"doc": "Format parameter counts as human-readable strings (25.1M, 147.5M).", "kind": "method", "line": 666, "name": "_fmt_params", "signature": "def _fmt_params(n)"}, {"doc": "Saves results to a JSON file for later analysis.", "kind": "class", "line": 677, "name": "JsonExporter", "signature": "class JsonExporter"}, {"doc": "Build the CLI argument parser.", "kind": "method", "line": 707, "name": "build_parser", "signature": "def build_parser()"}, {"doc": "Build a RunConfig from parsed CLI arguments.", "kind": "method", "line": 780, "name": "config_from_args", "signature": "def config_from_args(args)"}, {"doc": "CLI entry point.", "kind": "method", "line": 800, "name": "main", "signature": "def main()"}, {"doc": "Return the imported module, reusing the cached copy if available.", "kind": "method", "line": 100, "name": "load", "signature": "def load(self, path)"}, {"doc": "Expand directories and glob patterns into a sorted list of paths.\n\nArgs:\n    sources: File paths, directory paths, or glob patterns.\n\nReturns:\n    Deduplicated, sorted list of existing checkpoint paths.", "kind": "method", "line": 127, "name": "resolve", "signature": "def resolve(self, sources)"}, {"doc": "Return (state_dict, optional_embedded_config).\n\nHandles:\n  - .safetensors (raw state dict)\n  - .pt / .pth with {'model_state_dict': ..., 'config': ...}\n    (produced by the scaler)\n  - .pt / .pth plain state dicts", "kind": "method", "line": 167, "name": "load", "signature": "def load(self, path, device)"}, {"kind": "method", "line": 183, "name": "_load_safetensors", "signature": "def _load_safetensors(self, path, device)"}, {"kind": "method", "line": 191, "name": "_load_torch", "signature": "def _load_torch(self, path, device)"}, {"doc": "Return a TopoGPT2Config matching the loaded weights.\n\nPrefers the embedded config (saved by the scaler) but falls back\nto full inference from tensor shapes so that original checkpoints\nwork without any embedded metadata.", "kind": "method", "line": 222, "name": "reconstruct", "signature": "def reconstruct(self, mod, state_dict, embedded)"}, {"kind": "method", "line": 243, "name": "_infer", "signature": "def _infer(self, mod, sd)"}, {"kind": "method", "line": 278, "name": "_infer_d_head", "signature": "def _infer_d_head(sd)"}, {"kind": "method", "line": 285, "name": "_infer_n_kv", "signature": "def _infer_n_kv(sd, d_head, n_heads)"}, {"kind": "method", "line": 295, "name": "_infer_max_seq", "signature": "def _infer_max_seq(sd)"}, {"kind": "method", "line": 302, "name": "_infer_torus", "signature": "def _infer_torus(sd)"}, {"doc": "Return a shared tokenizer instance (built once per process).", "kind": "method", "line": 320, "name": "get", "signature": "def get(self, mod)"}, {"kind": "method", "line": 330, "name": "__init__", "signature": "def __init__(self, cfg, device)"}, {"doc": "Run generation and return (full_text, n_new_tokens, elapsed_s).\n\nUses the model's built-in .generate() when repetition_penalty == 1.0\nand top_p == 1.0, otherwise falls back to a manual loop that supports\nthe full sampling configuration.", "kind": "method", "line": 334, "name": "generate", "signature": "def generate(self, model, tokenizer, prompt)"}, {"kind": "method", "line": 361, "name": "_fast_generate", "signature": "def _fast_generate(self, model, input_ids)"}, {"kind": "method", "line": 372, "name": "_manual_generate", "signature": "def _manual_generate(self, model, input_ids)"}, {"kind": "method", "line": 412, "name": "_apply_repetition_penalty", "signature": "def _apply_repetition_penalty(logits, generated, penalty)"}, {"kind": "method", "line": 424, "name": "_apply_top_p", "signature": "def _apply_top_p(logits, p)"}, {"kind": "method", "line": 453, "name": "__init__", "signature": "def __init__(self, cfg)"}, {"doc": "Execute the full multi-model inference pipeline.", "kind": "method", "line": 462, "name": "run", "signature": "def run(self)"}, {"kind": "method", "line": 499, "name": "_run_one", "signature": "def _run_one(self, ckpt_path, mod, tokenizer, engine)"}, {"doc": "Extract a short human-readable label from a checkpoint path.", "kind": "method", "line": 570, "name": "_make_label", "signature": "def _make_label(path)"}, {"doc": "Print prompt header, per-model outputs, and comparison table.", "kind": "method", "line": 590, "name": "render", "signature": "def render(self, results, prompt)"}, {"kind": "method", "line": 597, "name": "_print_prompt_header", "signature": "def _print_prompt_header(self, prompt)"}, {"kind": "method", "line": 605, "name": "_print_model_output", "signature": "def _print_model_output(self, r)"}, {"kind": "method", "line": 628, "name": "_print_comparison_table", "signature": "def _print_comparison_table(self, results)"}, {"doc": "Serialize results to JSON.", "kind": "method", "line": 680, "name": "export", "signature": "def export(self, results, path, prompt)"}]}, {"id": "zeroshot.py", "kind": "module", "label": "zeroshot.py", "language": "py", "sha256": "1abf767820977f0e", "symbol_count": 97, "symbols": [{"doc": "Return a stderr logger with timestamp formatting.", "kind": "function", "line": 69, "name": "build_logger", "signature": "def build_logger(name, level)"}, {"doc": "All tuneable knobs for the zero-shot expansion procedure.\n\nAttributes\n----------\nsrc_path : str\n    Path to the source safetensors checkpoint.\ndst_path : str\n    Path where the expanded checkpoint will be written.\nsrc_radial : int\n    Source TORUS_RADIAL_BINS (read from the checkpoint metadata when\n    available; otherwise taken from the model scale preset).\nsrc_angular : int\n    Source TORUS_ANGULAR_BINS.\ntgt_radial : int\n    Target TORUS_RADIAL_BINS after expansion.\ntgt_angular : int\n    Target TORUS_ANGULAR_BINS after expansion.\nscale : str\n    Model scale preset: micro | small | medium | gpt2.\ndevice : str\n    Torch device for weight manipulation.\nvalidate : bool\n    Run a forward-pass sanity check on the expanded model.\nvalidate_prompt : str\n    Prompt text for the sanity check (requires tiktoken).\nlog_level : str\n    Python logging level name.\nspectral_interp_mode : str\n    How to interpolate spectral kernels: 'bilinear' or 'nearest'.\nnode_embed_interp_mode : str\n    How to interpolate node embeddings: 'bilinear' or 'nearest'.", "kind": "class", "line": 87, "name": "ExpansionConfig", "signature": "class ExpansionConfig"}, {"doc": "Minimal reproduction of the model-architecture fields from the original\nTopoGPT2Config.  Only the fields required to instantiate the neural\nnetwork are present here.", "kind": "class", "line": 169, "name": "TopoGPT2Config", "signature": "class TopoGPT2Config"}, {"doc": "Static quaternion algebra operations in PyTorch.", "kind": "class", "line": 254, "name": "QuaternionOps", "signature": "class QuaternionOps"}, {"doc": "Quaternion-valued linear layer.\n\nPerforms the Hamilton product W ⊗ x in the quaternion algebra,\nusing four real weight matrices (one per quaternion component).\nBoth in_features and out_features must be divisible by 4.", "kind": "class", "line": 287, "name": "QuaternionLinear", "signature": "class QuaternionLinear(Module)"}, {"doc": "2D spectral convolution with quaternion Hamilton product in frequency domain.\n\nKernel tensors are registered for each quaternion component (w, x, y, z),\neach with separate real and imaginary parts for the complex frequency domain.", "kind": "class", "line": 321, "name": "QuaternionSpectralLayer", "signature": "class QuaternionSpectralLayer(Module)"}, {"doc": "Spectral autoencoder operating in both 1D (feature axis) and 2D (torus grid).\n\nEncodes via FFT filtering and quaternion projection to a latent space;\ndecodes back for reconstruction regularisation.  Also exposes a method\nfor processing the torus grid through stacked QuaternionSpectralLayers.", "kind": "class", "line": 373, "name": "SpectralAutoencoder", "signature": "class SpectralAutoencoder(Module)"}, {"doc": "Replaces the MLP in each transformer layer.\n\nVectorised pipeline:\n    1. Flatten [B, S, D] -> [BS, D]\n    2. SpectralAutoencoder (1D filter + quaternion projection)\n    3. Project to torus angles (phi1, phi2)\n    4. Soft-assign each token to N_NODES via circular distances\n    5. Build node grid [BS, N_NODES, D]\n    6. QuaternionSpectralLayer 2D on the torus grid\n    7. Quaternion message-passing on the torus graph\n    8. Readout: weighted sum over nodes -> [BS, D]\n    9. Reshape to [B, S, D]", "kind": "class", "line": 427, "name": "QuaternionTorusBrain", "signature": "class QuaternionTorusBrain(Module)"}, {"doc": "SwiGLU feed-forward block (LLaMA-style).\ninner dimension = round(d_model * expansion) up to multiple of 4.", "kind": "class", "line": 534, "name": "SwiGLU", "signature": "class SwiGLU(Module)"}, {"doc": "Mixture-of-Experts wrapper around QuaternionTorusBrain.\n\nOne always-active shared expert (QuaternionTorusBrain) plus N_EXPERTS\nsparse SwiGLU experts selected by a linear router (top-K per token).\nWhen MOE_ENABLED is False this reduces to a plain QuaternionTorusBrain.", "kind": "class", "line": 556, "name": "TopoMoEBrain", "signature": "class TopoMoEBrain(Module)"}, {"doc": "Rotary Position Embeddings (RoPE) – Su et al., 2021.", "kind": "class", "line": 613, "name": "RotaryEmbedding", "signature": "class RotaryEmbedding(Module)"}, {"doc": "Root Mean Square Layer Normalization (no bias).", "kind": "class", "line": 652, "name": "RMSNorm", "signature": "class RMSNorm(Module)"}, {"doc": "Multi-head attention with Flash Attention, RoPE, and Grouped Query Attention.\nSupports an optional KV cache for autoregressive generation.", "kind": "class", "line": 665, "name": "MultiHeadAttention", "signature": "class MultiHeadAttention(Module)"}, {"doc": "Single transformer layer: pre-norm attention + pre-norm TopoMoEBrain.\nGradient checkpointing is disabled during inference/expansion.", "kind": "class", "line": 719, "name": "TopoGPT2Layer", "signature": "class TopoGPT2Layer(Module)"}, {"doc": "TopoGPT2: causal language model with quaternion torus topology.\n\nEmbedding -> N_LAYERS x (Attention + QuaternionTorusBrain) -> RMSNorm -> LM head.\nThe embedding and LM head share weights (weight tying).", "kind": "class", "line": 749, "name": "TopoGPT2", "signature": "class TopoGPT2(Module)"}, {"doc": "Interpolates QuaternionSpectralLayer kernels to a new (grid_h, grid_w).\n\nThe kernels live in frequency space with shape [in_q, out_q, freq_h, freq_w]\nwhere freq_w = grid_w // 2 + 1.  We treat (freq_h, freq_w) as a 2D spatial\ngrid and apply torch.nn.functional.interpolate.", "kind": "class", "line": 828, "name": "SpectralKernelInterpolator", "signature": "class SpectralKernelInterpolator"}, {"doc": "Interpolates the torus node embedding table to a new (n_radial, n_angular).\n\nnode_embed has shape [n_nodes, d_model] = [n_radial * n_angular, d_model].\nWe reshape to a 2D spatial grid [n_radial, n_angular, d_model], transpose\nto [d_model, n_radial, n_angular], interpolate per feature dimension, then\nreshape back.", "kind": "class", "line": 876, "name": "NodeEmbedInterpolator", "signature": "class NodeEmbedInterpolator"}, {"doc": "Transfers weights from a source QuaternionTorusBrain to a target one with\na different torus resolution.\n\nTransfer strategy per sub-module\n---------------------------------\nspectral_ae.enc_kr/ki, dec_kr/ki  : copy verbatim (1D feature-axis filters,\n                                     independent of torus resolution)\nspectral_ae.enc_proj, dec_proj     : copy verbatim (QuaternionLinear, no torus)\nspectral_ae.torus_spectral[i]      : interpolate each QuaternionSpectralLayer\n                                     kernel to new (tgt_radial, tgt_angular)\ntorus_proj                         : copy verbatim (projects to angles, not nodes)\nnode_embed                         : bilinear interpolation over the torus grid\nedge_quat                          : copy verbatim (4 edge types, always 4)\nnode_net                           : copy verbatim (QuaternionLinear, pointwise)\nreadout                            : copy verbatim (pointwise MLP)", "kind": "class", "line": 917, "name": "TorusBrainExpander", "signature": "class TorusBrainExpander"}, {"doc": "Transfers weights from a source TopoMoEBrain to a target one.\n\nThe shared QuaternionTorusBrain is expanded via TorusBrainExpander.\nAll SwiGLU expert weights and the router are copied verbatim (they do not\ndepend on torus resolution – they process flat token embeddings).", "kind": "class", "line": 1009, "name": "TopoMoEBrainExpander", "signature": "class TopoMoEBrainExpander"}, {"doc": "Zero-shot torus expansion of a complete TopoGPT2 model.\n\nAll weights that are resolution-independent are copied verbatim.\nThe torus-dependent weights inside each TopoMoEBrain are interpolated\nby TopoMoEBrainExpander.\n\nResolution-independent weights (copied verbatim)\n-------------------------------------------------\ntoken_embed, lm_head (weight-tied)\nfinal_norm\nper-layer: norm1, norm2, attn (all projections + temperature + rope)\nper-layer: topo_brain -> experts, router\n\nResolution-dependent weights (interpolated)\n-------------------------------------------\nper-layer: topo_brain -> shared_expert (QuaternionTorusBrain)", "kind": "class", "line": 1052, "name": "TopoGPT2Expander", "signature": "class TopoGPT2Expander"}, {"doc": "Loads and saves TopoGPT2 weights using safetensors.\nFalls back to torch.save / torch.load when safetensors is unavailable.", "kind": "class", "line": 1120, "name": "CheckpointIO", "signature": "class CheckpointIO"}, {"doc": "Architecture hyperparameters inferred directly from checkpoint tensor shapes.\n\nAll fields that affect tensor dimensions are recovered so that the source\nmodel can be instantiated to exactly match the saved weights, regardless of\nwhat the CLI scale preset would compute.", "kind": "class", "line": 1216, "name": "CheckpointArch", "signature": "class CheckpointArch"}, {"doc": "Infers all architecture hyperparameters from the raw tensor shapes stored\nin a checkpoint, without relying on any saved metadata or scale presets.\n\nProbing strategy (all derivable from tensor names and shapes)\n-------------------------------------------------------------\nd_model         : token_embed.weight  shape [vocab, D] -> D\nvocab_size      : token_embed.weight  shape [V, D]     -> V\nn_heads         : layers.0.attn.q_proj.weight [n_heads*d_head, D]\n                  with d_head = D // n_heads; since q always uses n_heads,\n                  shape is [D, D] when n_heads = n_kv_heads.\n                  We read n_heads from q_proj: out = n_heads * d_head = D\n                  (always), so d_head = D // n_heads.  We look at the\n                  actual out dim of q_proj.\nn_kv_heads      : layers.0.attn.k_proj.weight [n_kv*d_head, D]\n                  -> n_kv = out_dim // d_head\nn_layers        : count of \"layers.N.attn.q_proj.weight\" keys\ntorus_radial    : layers.0.topo_brain.shared_expert.spectral_ae\n                  .torus_spectral.0.kr_w  shape [in_q, out_q, freq_h, freq_w]\n                  grid_h = freq_h  (no //2+1 on h),  we store it directly\ntorus_angular   : freq_w = grid_w // 2 + 1  -> grid_w = (freq_w - 1) * 2\nspectral_latent : layers.0.topo_brain.shared_expert.spectral_ae\n                  .enc_proj.Ww.weight  shape [out_q, in_q]\n                  latent_dim = out_q * 4\nn_experts       : count of \"layers.0.topo_brain.experts.N.gate_proj.weight\"\n                  keys; 0 means moe_enabled=False\nnum_spec_layers : count of torus_spectral keys for layer 0\nn_freq_1d       : layers.0.topo_brain.shared_expert.spectral_ae.enc_kr\n                  shape [n_freq]  where n_freq = d_model // 2 + 1", "kind": "class", "line": 1239, "name": "CheckpointArchProber", "signature": "class CheckpointArchProber"}, {"doc": "Runs a forward-pass sanity check on the expanded model.\n\nChecks:\n- The model produces finite logits for a random token sequence.\n- The model produces finite logits for the given text prompt (if tiktoken\n  is available).\n- The model can generate a short sequence without crashing.", "kind": "class", "line": 1463, "name": "ExpansionValidator", "signature": "class ExpansionValidator"}, {"doc": "Orchestrates the full zero-shot expansion workflow:\n\n1. Read source torus geometry from checkpoint metadata (or config defaults).\n2. Build source and target TopoGPT2 configs.\n3. Instantiate source and target models.\n4. Load source weights into the source model.\n5. Expand weights via TopoGPT2Expander.\n6. Optionally validate the expanded model.\n7. Save the expanded model.\n\nNo training is performed at any stage.", "kind": "class", "line": 1550, "name": "ZeroShotExpansionPipeline", "signature": "class ZeroShotExpansionPipeline"}, {"doc": "Construct and return the CLI argument parser.", "kind": "method", "line": 1709, "name": "build_arg_parser", "signature": "def build_arg_parser()"}, {"doc": "CLI entry point.", "kind": "method", "line": 1774, "name": "main", "signature": "def main()"}, {"doc": "Raise ValueError for impossible torus configurations.", "kind": "method", "line": 140, "name": "validate_geometry", "signature": "def validate_geometry(self)"}, {"kind": "method", "line": 154, "name": "src_nodes", "signature": "def src_nodes(self)"}, {"kind": "method", "line": 158, "name": "tgt_nodes", "signature": "def tgt_nodes(self)"}, {"kind": "method", "line": 222, "name": "__post_init__", "signature": "def __post_init__(self)"}, {"kind": "method", "line": 258, "name": "hamilton_product", "signature": "def hamilton_product(q1, q2)"}, {"kind": "method", "line": 269, "name": "normalize", "signature": "def normalize(q, eps)"}, {"kind": "method", "line": 273, "name": "conjugate", "signature": "def conjugate(q)"}, {"kind": "method", "line": 278, "name": "rotate_vector", "signature": "def rotate_vector(v, q)"}, {"kind": "method", "line": 296, "name": "__init__", "signature": "def __init__(self, in_features, out_features, bias)"}, {"kind": "method", "line": 310, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 329, "name": "__init__", "signature": "def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)"}, {"kind": "method", "line": 344, "name": "_kernel", "signature": "def _kernel(self, c)"}, {"kind": "method", "line": 347, "name": "_contract", "signature": "def _contract(self, W, X)"}, {"kind": "method", "line": 350, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 382, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 404, "name": "_filter1d", "signature": "def _filter1d(self, x, kr, ki)"}, {"kind": "method", "line": 409, "name": "encode", "signature": "def encode(self, x)"}, {"kind": "method", "line": 412, "name": "decode", "signature": "def decode(self, z)"}, {"kind": "method", "line": 415, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 420, "name": "process_torus_grid", "signature": "def process_torus_grid(self, grid)"}, {"kind": "method", "line": 443, "name": "__init__", "signature": "def __init__(self, d_model, config)"}, {"kind": "method", "line": 468, "name": "_build_torus_graph", "signature": "def _build_torus_graph(self)"}, {"kind": "method", "line": 484, "name": "_torus_soft_assign", "signature": "def _torus_soft_assign(self, phi1, phi2)"}, {"kind": "method", "line": 495, "name": "_message_passing", "signature": "def _message_passing(self, node_feat)"}, {"kind": "method", "line": 509, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 540, "name": "__init__", "signature": "def __init__(self, d_model, expansion, dropout)"}, {"kind": "method", "line": 552, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 565, "name": "__init__", "signature": "def __init__(self, d_model, config)"}, {"kind": "method", "line": 581, "name": "_route", "signature": "def _route(self, x)"}, {"kind": "method", "line": 604, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 618, "name": "__init__", "signature": "def __init__(self, d_head, max_seq_len)"}, {"kind": "method", "line": 626, "name": "_build_cache", "signature": "def _build_cache(self, seq_len)"}, {"kind": "method", "line": 633, "name": "_rotate_half", "signature": "def _rotate_half(x)"}, {"kind": "method", "line": 637, "name": "forward", "signature": "def forward(self, q, k, seq_len, offset)"}, {"kind": "method", "line": 655, "name": "__init__", "signature": "def __init__(self, d_model, eps)"}, {"kind": "method", "line": 660, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 671, "name": "__init__", "signature": "def __init__(self, d_model, n_heads, config)"}, {"kind": "method", "line": 686, "name": "forward", "signature": "def forward(self, x, is_causal, past_kv)"}, {"kind": "method", "line": 725, "name": "__init__", "signature": "def __init__(self, d_model, n_heads, config)"}, {"kind": "method", "line": 734, "name": "_forward_impl", "signature": "def _forward_impl(self, x, past_kv)"}, {"kind": "method", "line": 743, "name": "forward", "signature": "def forward(self, x, past_kv)"}, {"kind": "method", "line": 757, "name": "__init__", "signature": "def __init__(self, config)"}, {"kind": "method", "line": 771, "name": "_init_weights", "signature": "def _init_weights(self)"}, {"kind": "method", "line": 778, "name": "forward", "signature": "def forward(self, token_ids, past_kvs)"}, {"doc": "Top-k autoregressive generation with KV cache.", "kind": "method", "line": 795, "name": "generate", "signature": "def generate(self, token_ids, max_new_tokens, temperature, top_k)"}, {"kind": "method", "line": 837, "name": "__init__", "signature": "def __init__(self, mode)"}, {"doc": "Interpolate a 4D real tensor [in_q, out_q, h, w] to [in_q, out_q, tgt_h, tgt_w].", "kind": "method", "line": 840, "name": "_interp2d", "signature": "def _interp2d(self, tensor, tgt_h, tgt_w)"}, {"doc": "Copy and interpolate all kernel parameters from src_layer to tgt_layer.", "kind": "method", "line": 856, "name": "transfer", "signature": "def transfer(self, src_layer, tgt_layer)"}, {"kind": "method", "line": 886, "name": "__init__", "signature": "def __init__(self, mode)"}, {"doc": "Interpolate src_embed [src_R*src_A, D] into tgt_embed [tgt_R*tgt_A, D].", "kind": "method", "line": 889, "name": "transfer", "signature": "def transfer(self, src_embed, src_radial, src_angular, tgt_embed, tgt_radial, tgt_angular)"}, {"kind": "method", "line": 936, "name": "__init__", "signature": "def __init__(self, spec_interp_mode, node_interp_mode, logger)"}, {"doc": "Mutates tgt in-place to carry the expanded weights of src.", "kind": "method", "line": 946, "name": "expand", "signature": "def expand(self, src, tgt)"}, {"kind": "method", "line": 1018, "name": "__init__", "signature": "def __init__(self, spec_interp_mode, node_interp_mode, logger)"}, {"doc": "Mutates tgt in-place.", "kind": "method", "line": 1031, "name": "expand", "signature": "def expand(self, src, tgt)"}, {"kind": "method", "line": 1072, "name": "__init__", "signature": "def __init__(self, spec_interp_mode, node_interp_mode, logger)"}, {"doc": "Expand src into tgt.  Returns tgt with all weights transferred.\ntgt must have already been instantiated with the target config.", "kind": "method", "line": 1085, "name": "expand", "signature": "def expand(self, src, tgt)"}, {"kind": "method", "line": 1126, "name": "__init__", "signature": "def __init__(self, logger)"}, {"doc": "Load weights into model from path.  Returns the metadata dict.\nSupports: .safetensors, .pt, .pth (state_dict or wrapped dict).\n\nWeight tying: checkpoints saved by this script omit lm_head.weight\n(it is redundant with token_embed.weight).  After loading, the tie is\nrestored by pointing lm_head.weight at token_embed.weight.", "kind": "method", "line": 1133, "name": "load", "signature": "def load(self, path, model, device)"}, {"doc": "Save model weights to path.\n\nWeight tying: token_embed.weight and lm_head.weight share the same\nstorage tensor.  safetensors rejects aliased tensors with a RuntimeError.\nWe exclude lm_head.weight from the state dict before saving (it is\nredundant) and record the tie in metadata so load() can restore it.", "kind": "method", "line": 1177, "name": "save", "signature": "def save(self, path, model, metadata)"}, {"kind": "method", "line": 1286, "name": "__init__", "signature": "def __init__(self, logger)"}, {"doc": "Return {key: shape} for every tensor in the checkpoint.", "kind": "method", "line": 1289, "name": "_load_shapes", "signature": "def _load_shapes(self, path)"}, {"doc": "Return safetensors string metadata dict (empty when unavailable).", "kind": "method", "line": 1304, "name": "_load_metadata", "signature": "def _load_metadata(self, path)"}, {"doc": "Infer CheckpointArch from the checkpoint at path.\n\nParameters\n----------\npath            : checkpoint file path\nfallback_radial : used only when torus_spectral key is absent\nfallback_angular: used only when torus_spectral key is absent", "kind": "method", "line": 1315, "name": "probe", "signature": "def probe(self, path, fallback_radial, fallback_angular)"}, {"doc": "Fallback d_head inference when rope.inv_freq is absent.\n\nd_head must divide both q_out and d_model, and n_heads % n_kv_heads == 0.\nReturns the largest valid candidate (most heads, smallest d_head is wrong\nintuition; we pick the value that makes n_kv_heads a proper divisor of n_heads\nand n_heads a standard power-of-2 count).", "kind": "method", "line": 1433, "name": "_infer_d_head_fallback", "signature": "def _infer_d_head_fallback(d_model, q_out, k_out)"}, {"kind": "method", "line": 1474, "name": "__init__", "signature": "def __init__(self, logger)"}, {"doc": "Return True if all checks pass, False otherwise.\nDoes not raise; errors are logged as warnings.", "kind": "method", "line": 1477, "name": "validate", "signature": "def validate(self, model, prompt)"}, {"kind": "method", "line": 1565, "name": "__init__", "signature": "def __init__(self, exp_cfg, logger)"}, {"doc": "Build a TopoGPT2Config whose tensor dimensions exactly match arch.\n\nThe scale preset is applied first (to get sane defaults for fields not\ncovered by arch), then every field that affects tensor shapes is\noverwritten with the probed value.  This guarantees that the\ninstantiated model accepts the checkpoint weights without size mismatches.", "kind": "method", "line": 1570, "name": "_config_from_arch", "signature": "def _config_from_arch(self, arch, torus_radial, torus_angular)"}, {"kind": "method", "line": 1609, "name": "_build_metadata_for_save", "signature": "def _build_metadata_for_save(self, src_meta, arch, tgt_radial, tgt_angular)"}, {"doc": "Execute the full expansion pipeline.  Returns the expanded model.", "kind": "method", "line": 1631, "name": "run", "signature": "def run(self)"}]}], "type": "CodePropertyGraph", "version": "1.0"}
```

---

## Architecture Reference

### PY (11 files)

#### `app.py`
**Path:** `app.py`

**Classes:**
- `TopoGPT2Config` (line 55) `class TopoGPT2Config` - *Configuración completa para TopoGPT2.*
- `QuaternionOps` (line 177) `class QuaternionOps` - *Operaciones de cuaterniones puras en PyTorch.
Representación: [..., 4]  donde last dim = [w, x, y, z]
q = w + x*i + y*j + z*k*
- `QuaternionLinear` (line 216) `class QuaternionLinear(Module)` - *Capa lineal con pesos cuaterniones.

Implementa la multiplicación W * x en el álgebra de cuaterniones:
- W = Ww + Wx*i + Wy*j + Wz*k  (cuaternión de pesos)
- x = xw + xx*i + xy*j + xz*k  (cuaternión de entrada)
- out = W * x  (producto de Hamilton extendido a vectores)

Parámetros: 4 matrices reales de forma [out_q, in_q]*
- `QuaternionSpectralLayer` (line 261) `class QuaternionSpectralLayer(Module)` - *Convolución espectral 2D con cuaterniones y producto de Hamilton completo.

Operación en dominio de frecuencia:
    P(k) = W(k) ⊗ X(k)  (producto de Hamilton de cuaterniones complejos)

Donde:
    X(k) = FFT2(x) con 4 canales cuaterniones [Xw, Xx, Xy, Xz]
    W(k) = kernel complejo aprendible con componentes [Ww, Wx, Wy, Wz]

Reglas del producto de Hamilton en dominio de frecuencia:
    Pw = Ww·Xw - Wx·Xx - Wy·Xy - Wz·Xz
    Px = Ww·Xx + Wx·Xw + Wy·Xz - Wz·Xy
    Py = Ww·Xy - Wx·Xz + Wy·Xw + Wz·Xx
    Pz = Ww·Xz + Wx·Xy - Wy·Xx + Wz·Xw

Cada Wc es un kernel complejo (partes real e imaginaria independientes).*
- `SpectralAutoencoder` (line 348) `class SpectralAutoencoder(Module)` - *Autoencoder espectral con cuaterniones.

Opera en dos niveles:
1. Espectral 1D sobre el vector de features (FFT sobre dim D_MODEL):
   captura la espectrografía global del embedding.
2. Espectral 2D sobre el grid del toro (QuaternionSpectralLayer):
   captura correlaciones espaciales en la topología.

Devuelve (latent, recon_loss) para regularización.*
- `QuaternionTorusBrain` (line 431) `class QuaternionTorusBrain(Module)` - *Reemplaza el MLP en cada capa del transformer.

Pipeline (completamente vectorizado sobre batch Y secuencia):

1. Flatten: [B, S, D] → [B·S, D]
2. SpectralAutoencoder: filtrado espectral 1D + compresión cuaternión
3. Proyección al toro:
   - Calcula 2 ángulos (phi1, phi2) ∈ [-π, π]²
   - Asignación blanda a los 8 nodos via distancia circular en el toro
4. Construye grid de nodos: [B·S, N_NODES=8, D_MODEL]
5. QuaternionSpectralLayer 2D sobre el grid [B·S, 4*D_QUAT, RADIAL, ANGULAR]
6. Message-passing con rotaciones cuaterniones sobre el grafo toro
7. Readout: atención sobre los 8 nodos → [B·S, D_MODEL]
8. Reshape: [B·S, D] → [B, S, D]*
- `RotaryEmbedding` (line 648) `class RotaryEmbedding(Module)` - *Rotary Position Embeddings (RoPE) - Su et al., 2021.
Codifica la posición como rotaciones del espacio de atención,
naturalmente relativas y sin parámetros extra.*
- `RMSNorm` (line 696) `class RMSNorm(Module)` - *Root Mean Square Layer Normalization (sin bias). Más estable que LayerNorm.*
- `SwiGLU` (line 713) `class SwiGLU(Module)` - *SwiGLU: SiLU(gate(x)) * up(x) -> down
Usado en LLaMA 2/3, Qwen, Mistral en lugar de GELU-FFN.
Dimension interna: 8/3 * d_model (convención LLaMA, redondeada a múltiplo de 4).*
- `TopoMoEBrain` (line 742) `class TopoMoEBrain(Module)` - *Mixture of Experts sobre la capa topologica.

Arquitectura (inspirada en DeepSeek-MoE / Mixtral):
  - 1 experto compartido: QuaternionTorusBrain (siempre activo)
  - N_EXPERTS expertos SwiGLU ligeros (activacion esparsa: Top-K por token)
  - Router: Linear(D, N_EXPERTS) + softmax → top-K

Load-balancing loss (auxiliar): penaliza si un experto acapara todos los tokens.
Activa MOE_TOP_K de N_EXPERTS expertos por token.

Sin MoE (MOE_ENABLED=False): se comporta como QuaternionTorusBrain puro.*
- `MultiHeadAttention` (line 847) `class MultiHeadAttention(Module)` - *Multi-head attention con:
- Flash Attention (scaled_dot_product_attention de PyTorch 2.0+)
- Rotary Position Embeddings (RoPE)
- GQA (Grouped Query Attention): N_KV_HEADS < N_HEADS, reduce VRAM de K/V
- KV Cache para inferencia autoregresiva eficiente
- Temperatura termodinámica aprendible*
- `TopoGPT2Layer` (line 929) `class TopoGPT2Layer(Module)` - *Capa del transformer con TopoMoEBrain (TopoBrain + MoE SwiGLU experts).

Esquema pre-norm (estilo LLaMA):
    x = x + Attention_GQA(RMSNorm(x))
    x = x + TopoMoEBrain(RMSNorm(x))*
- `TopoGPT2` (line 976) `class TopoGPT2(Module)` - *TopoGPT2: Transformer de lenguaje con TopoBrain cuaternión-espectral.

Arquitectura:
    Embedding de tokens + RoPE (en Attention)
    N_LAYERS × TopoGPT2Layer (Attention + QuaternionTorusBrain)
    RMSNorm final
    Proyección a vocabulario (weight-tied con embeddings)*
- `BPETokenizer` (line 1082) `class BPETokenizer` - *Wrapper alrededor de tiktoken (GPT-2 compatible).*
- `CorpusDownloader` (line 1107) `class CorpusDownloader` - *Descarga corpus de texto para entrenamiento.

Soporta:
- 'tinystories': ~2GB de cuentos cortos (ideal para pruebas)
- 'wikitext103': ~500MB de Wikipedia curada
- 'file': archivo de texto local

Usa HuggingFace 'datasets' para TinyStories y WikiText.*
- `TokenizedDataset` (line 1170) `class TokenizedDataset(Dataset)` - *Dataset de tokens para language modeling (next-token prediction).

Guarda los tokens tokenizados en disco la primera vez (cache .pt)
para evitar re-tokenizar en cada ejecucion. La clave de cache incluye
un hash del contenido del corpus + tokenizador + max_tokens.*
- `CheckpointManager` (line 1220) `class CheckpointManager` - *Gestiona checkpoints de forma acumulativa y segura.

Estructura en disco:
    checkpoints_topogpt2/
      latest/
        model.safetensors   <- pesos del modelo (formato seguro, sin pickle)
        optimizer.pt        <- estado del optimizador (requiere .pt)
        state.json          <- metadatos: epoch, step, historial, config
      best/
        model.safetensors
        state.json
      step_NNNNN/           <- snapshots periodicos (rotados)
        model.safetensors
        optimizer.pt
        state.json

El historial se ACUMULA entre sesiones de entrenamiento: cada --resume
agrega nuevas entradas a train_loss[], val_loss[], etc.*
- `TopoGPT2Trainer` (line 1453) `class TopoGPT2Trainer` - *Entrenador acumulativo y resumible.

Caracteristicas:
- Checkpoint automatico en safetensors cada N minutos + cada epoch
- Historial acumulativo entre sesiones (--resume agrega al historial existente)
- Guarda el mejor modelo en checkpoints/best/ automaticamente
- LR schedule: cosine con warmup relativo a los steps de ESTA sesion
- Mixed Precision (AMP) + acumulacion de gradientes*
- `MechanisticMetrics` (line 1746) `class MechanisticMetrics` - *Calcula todas las metricas del diagrama de fases de Book.md.

Todas las metricas se derivan de cantidades medibles (pesos, gradientes):

delta  (δ): margen de discretizacion.  max|w - round(w)|
            δ≈0 -> cristal;  δ≈0.49 -> vidrio frio
kappa  (κ): numero de condicion de la covarianza del gradiente.
            κ≈1 -> cristalino;  κ>>1 -> amorfo
T_eff:      temperatura efectiva = (lr/2) * Var(gradiente).
            T_eff→0 -> congelado; T_eff alto -> ruidoso
alpha  (α): indice de pureza = -log(δ + ε).
            α=20 -> perfecto; α<1 -> vidrio
berry:      fase de Berry de los kernels espectrales imaginarios.
            |berry|>π/2 con winding≠0 -> insulador topologico
lc:         complejidad local = 1 - similitud coseno promedio entre filas.
sp:         superposicion = correlacion promedio inter-fila de pesos.*
- `Phase0_KernelOptimizer` (line 1983) `class Phase0_KernelOptimizer` - *Encuentra el ratio imaginario/real optimo para los kernels espectrales.

Analogia con main.py: evalua la transicion GOE→GUE en el espacio
de kernels. Un ratio optimo promueve estructura topologica (insulador)
vs estructura amorfa (vidrio).

Metodo: calibra con un mini-batch y mide la varianza del gradiente
en funcion del ratio. Ratios que minimizan la varianza de gradiente
(maxima coherencia espectral) son preferibles.

No entrena: solo inicializa los kernels con distintos ratios y mide.
Tiempo tipico: < 30 segundos.*
- `Phase1_BatchProspector` (line 2058) `class Phase1_BatchProspector` - *Encuentra el batch size optimo testando candidatos con pocos pasos.

De main.py: el batch size regula la temperatura del horno de cristalizacion.
Batch sizes demasiado chicos -> ruido excesivo (vidrio frio).
Batch sizes demasiado grandes -> sin presion annealing (amorfos).
La ventana optima empirica de main.py: [24, 128] para Strassen.

Para LM, testeamos candidatos midiendo:
- delta (δ): velocidad de descenso en prospect_steps pasos
- T_eff: temperatura efectiva del gradiente

Tiempo tipico: < 2 minutos para 3 candidatos × 30 pasos.*
- `Phase2_SeedMiner` (line 2141) `class Phase2_SeedMiner` - *Encuentra semillas prometedoras midiendo la trayectoria de delta.

De main.py: una semilla "buena" muestra delta descendente en los
primeros N pasos (enfriamiento). Una semilla "mala" se estanca en
el plateau vidrioso (~0.49).

Criterio de seleccion:
1. Semillas con delta_velocity < 0 (enfriando) AND kappa bajo.
2. Si no hay, semillas solo enfriando.
3. Fallback: semilla con menor delta final.

Tiempo tipico: < 3 minutos para 5 semillas × 50 pasos.*
- `Phase4_AnnealingRefiner` (line 2223) `class Phase4_AnnealingRefiner` - *Refinamiento post-entrenamiento mediante recocido simulado.

De main.py: despues de que el modelo converge, una fase de annealing
con criterio de aceptacion de Metropolis puede empujar los pesos
hacia estados de menor energia libre (menor delta o mejor val_loss).

Aceptacion de Metropolis:
    si Δloss < 0: siempre acepta (mejora)
    si Δloss >= 0: acepta con prob exp(-Δloss / T)

La temperatura T decae exponencialmente: T(t) = T0 * cooling_rate^t

Al rechazar: restaura el mejor estado conocido.
Si se estanca: perturbacion termica (ruido gaussiano en pesos).

Tiempo: proporcional a refine_epochs (user-controlled).*
- `TopoPhasePipeline` (line 2384) `class TopoPhasePipeline` - *Orquesta las 5 fases de entrenamiento segun main.py + Book.md.

Fases:
  0  Kernel ratio optimization  (GOE-GUE spectral calibration)
  1  Batch size prospecting      (temperatura del horno de cristalizacion)
  2  Seed mining                 (seleccion de semilla enfriante)
  3  Full training               (entrenamiento principal con metricas)
  4  Annealing refinement        (recocido simulado post-entrenamiento)

Las fases 0-2 son rapidas (prospecting). La fase 3 es el grueso.
La fase 4 es opcional (--refine).

Para no ser prohibitivo:
  --prospect         activa fases 0, 1, 2 antes del entrenamiento
  --refine-epochs N  activa fase 4 con N epocas de annealing
  Sin flags: solo fase 3 (comportamiento original, identico a antes)*

**Methods:**
- `setup_logger` (line 155) `def setup_logger(name, level)`
- `set_seed` (line 165) `def set_seed(seed, device)`
- `main` (line 2506) `def main()`
- `__post_init__` (line 124) `def __post_init__(self)`
- `hamilton_product` (line 185) `def hamilton_product(q1, q2)` - *Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].*
- `normalize` (line 197) `def normalize(q, eps)`
- `conjugate` (line 201) `def conjugate(q)`
- `rotate_vector` (line 206) `def rotate_vector(v, q)` - *Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]*
- `__init__` (line 228) `def __init__(self, in_features, out_features, bias)`
- `forward` (line 244) `def forward(self, x)` - *x: [..., in_features] → [..., out_features]*
- `__init__` (line 281) `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- `_kernel` (line 300) `def _kernel(self, c)`
- `_contract` (line 303) `def _contract(self, W, X)` - *Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]*
- `forward` (line 307) `def forward(self, x)` - *x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)
→ [B, 4*out_q, H, W]*
- `__init__` (line 361) `def __init__(self, config)`
- `_filter1d` (line 393) `def _filter1d(self, x, kr, ki)` - *Filtro espectral 1D: x[..., D] → filtrado[..., D]*
- `encode` (line 399) `def encode(self, x)` - *x: [..., D_MODEL] → latent: [..., D_LAT]*
- `decode` (line 404) `def decode(self, z)` - *z: [..., D_LAT] → recon: [..., D_MODEL]*
- `forward` (line 409) `def forward(self, x)` - *Devuelve (latent, recon_loss)*
- `process_torus_grid` (line 416) `def process_torus_grid(self, grid)` - *Procesa el grid del toro con QuaternionSpectralLayer.
grid: [B, 4*D_QUAT, RADIAL, ANGULAR]  →  [B, 4*D_QUAT, RADIAL, ANGULAR]*
- `__init__` (line 449) `def __init__(self, d_model, config)`
- `_build_torus_graph` (line 489) `def _build_torus_graph(self)` - *Construye las aristas del grafo toro 2×4.

Nodos indexados como: node = r * N_ANGULAR + a
  r ∈ [0, RADIAL-1], a ∈ [0, ANGULAR-1]

Aristas angulares: nodo ↔ nodo a la izquierda/derecha (periódico)
Aristas radiales:  nodo ↔ nodo del anillo interior/exterior*
- `_torus_soft_assign` (line 523) `def _torus_soft_assign(self, phi1, phi2)` - *Asignación blanda de tokens a los 8 nodos del toro via distancia circular.

phi1: [BS] ángulo angular ∈ [-π, π]
phi2: [BS] ángulo radial ∈ [-π, π]
→ weights: [BS, N_NODES]  (suma a 1, softmax de distancias negativas)*
- `_message_passing` (line 550) `def _message_passing(self, node_feat)` - *Message-passing VECTORIZADO con rotaciones cuaterniones.
Sin bucles Python: todas las aristas se procesan en paralelo.

node_feat: [BS, N_NODES, D_MODEL]
→ [BS, N_NODES, D_MODEL]*
- `forward` (line 587) `def forward(self, x)` - *x: [B, S, D_MODEL]
→ output: [B, S, D_MODEL], recon_loss: scalar*
- `__init__` (line 655) `def __init__(self, d_head, max_seq_len, base)`
- `_build_cache` (line 661) `def _build_cache(self, seq_len)`
- `_rotate_half` (line 668) `def _rotate_half(self, x)`
- `forward` (line 672) `def forward(self, q, k, seq_len, offset)` - *q, k: [B, n_heads, S_q/S_k, d_head]
offset: posicion inicial (para KV cache: longitud del cache existente)
Aplica posiciones [offset .. offset+S-1] a q y k.*
- `__init__` (line 699) `def __init__(self, d_model, eps)`
- `forward` (line 704) `def forward(self, x)`
- `__init__` (line 720) `def __init__(self, d_model, expansion, dropout)`
- `forward` (line 734) `def forward(self, x)`
- `__init__` (line 757) `def __init__(self, d_model, config)`
- `_route` (line 778) `def _route(self, x)` - *x: [N, D] donde N = B*S (tokens aplanados)
Retorna:
expert_out: [N, D]  suma ponderada de top-K expertos
aux_loss:   escalar  load-balancing loss
Routing vectorizado sin boolean indexing ni sincronizacion CUDA.
Usa dispatch por indices agrupados (estilo Mixtral/DeepSeek) para
compatibilidad total con torch.utils.checkpoint.*
- `forward` (line 820) `def forward(self, x)` - *x: [B, S, D]
→ output: [B, S, D], aux_loss: escalar*
- `__init__` (line 857) `def __init__(self, d_model, n_heads, config)`
- `forward` (line 875) `def forward(self, x, is_causal, past_kv)` - *Args:
    x:        [B, S, D]
    is_causal: usar mascara causal
    past_kv:  (K_cache, V_cache) de pasos anteriores o None
Returns:
    out:      [B, S, D]
    kv_cache: (K, V) completos para cachear en generate()*
- `__init__` (line 938) `def __init__(self, d_model, n_heads, config)`
- `_forward_impl` (line 947) `def _forward_impl(self, x, past_kv)`
- `forward` (line 956) `def forward(self, x, past_kv)` - *Retorna (x_out, aux_loss, kv_cache).
Con gradient checkpointing en training (solo cuando no hay KV cache).*
- `__init__` (line 987) `def __init__(self, config)`
- `_init_weights` (line 1006) `def _init_weights(self)`
- `forward` (line 1013) `def forward(self, token_ids, past_kvs)` - *token_ids: [B, S]  (enteros)
past_kvs:  lista de (K, V) por capa, o None para entrenamiento
→ logits: [B, S, VOCAB_SIZE], aux_loss: scalar, new_kvs: list[(K,V)]*
- `count_params` (line 1036) `def count_params(self)`
- `generate` (line 1042) `def generate(self, token_ids, max_new_tokens, temperature, top_k)` - *Generacion autoregresiva con KV cache y muestreo top-k.
En el primer paso procesa el prompt completo y guarda el cache.
En pasos siguientes solo procesa 1 token nuevo (O(n) en lugar de O(n^2)).*
- `__init__` (line 1085) `def __init__(self, encoding)`
- `encode` (line 1093) `def encode(self, text)`
- `decode` (line 1096) `def decode(self, tokens)`
- `eot_token` (line 1099) `def eot_token(self)`
- `__init__` (line 1119) `def __init__(self, corpus, data_dir, logger)`
- `get_text` (line 1125) `def get_text(self, split)` - *Devuelve el texto del corpus. Descarga si es necesario.*
- `_download_hf` (line 1150) `def _download_hf(self, dataset_name, split, text_column, name)`
- `__init__` (line 1179) `def __init__(self, text, tokenizer, seq_len, max_tokens, cache_dir, split_tag)`
- `__len__` (line 1206) `def __len__(self)`
- `__getitem__` (line 1209) `def __getitem__(self, idx)`
- `__init__` (line 1245) `def __init__(self, config, logger)`
- `patch_config_for_resume` (line 1255) `def patch_config_for_resume(self, cfg)` - *Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS
para que coincidan con la arquitectura guardada.
Necesario cuando el codigo cambio GQA despues de guardar el checkpoint.*
- `_save_model` (line 1284) `def _save_model(self, model, directory)`
- `_load_model` (line 1297) `def _load_model(self, model, directory)`
- `_save_optimizer` (line 1328) `def _save_optimizer(self, optimizer, directory)`
- `_load_optimizer` (line 1331) `def _load_optimizer(self, optimizer, directory, device)`
- `_save_state` (line 1340) `def _save_state(self, state, directory)`
- `_load_state` (line 1345) `def _load_state(self, directory)`
- `should_save` (line 1356) `def should_save(self)`
- `save` (line 1359) `def save(self, model, optimizer, state, is_best)` - *Guarda checkpoint completo.

state debe contener al menos: completed_epochs, global_step,
best_val_loss, history, config.*
- `load_latest` (line 1404) `def load_latest(self, model, optimizer)` - *Carga el ultimo checkpoint guardado.
Devuelve el state dict (vacio si no hay checkpoint).*
- `load_best` (line 1431) `def load_best(self, model)` - *Carga el mejor modelo guardado (solo pesos, sin optimizador).*
- `has_checkpoint` (line 1443) `def has_checkpoint(self)`
- `__init__` (line 1465) `def __init__(self, model, config, tokenizer)`
- `resume` (line 1500) `def resume(self)` - *Carga el ultimo checkpoint disponible.
Restaura: pesos del modelo, estado del optimizador, historial acumulado,
epoch/step completados y mejor val_loss.
Devuelve True si se cargo un checkpoint, False si empieza de cero.*
- `_current_state` (line 1525) `def _current_state(self)` - *Construye el dict de estado para persistir en state.json.*
- `_cosine_lr` (line 1536) `def _cosine_lr(self, step_in_session, total_steps_session)` - *Cosine decay con warmup. El schedule es relativo a la sesion actual.*
- `_set_lr` (line 1544) `def _set_lr(self, lr)`
- `train` (line 1548) `def train(self, train_dl, val_dl)` - *Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.
El historial se acumula sobre sesiones previas.*
- `_sample_text` (line 1684) `def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)` - *Genera una muestra de texto al final de cada epoch para monitorear
la calidad cualitativa del modelo (detecta degeneracion, repeticion, etc.).*
- `evaluate` (line 1716) `def evaluate(self, dataloader)`
- `__init__` (line 1766) `def __init__(self, config)`
- `compute_delta` (line 1774) `def compute_delta(self, model)`
- `compute_alpha` (line 1781) `def compute_alpha(self, delta)`
- `update_grad_buffer` (line 1786) `def update_grad_buffer(self, model)` - *Captura gradientes de forma segura, ignorando tensores corruptos.*
- `compute_t_eff` (line 1812) `def compute_t_eff(self, lr)` - *T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva.*
- `compute_kappa` (line 1820) `def compute_kappa(self, model, dataloader, n_batches)` - *κ = λ_max / λ_min de la covarianza del gradiente.
Parámetro de orden para cristalización (κ≈1 = cristal).
Nota: requiere pasadas backward adicionales. Se ejecuta con protección
para no corromper el estado AMP del trainer principal.*
- `compute_berry_phase` (line 1878) `def compute_berry_phase(self, model)` - *Fase de Berry de los kernels espectrales imaginarios.
Surge de los parametros ki_w, ki_x, ki_y, ki_z de QuaternionSpectralLayer.
|berry|>pi/2 con winding!=0 indica estructura topologica.*
- `compute_lc` (line 1891) `def compute_lc(self, model)` - *Complejidad local: 1 - similitud coseno promedio entre filas de pesos.*
- `compute_sp` (line 1905) `def compute_sp(self, model)` - *Superposicion: correlacion inter-fila promedio (entrelazamiento de features).*
- `classify_phase` (line 1921) `def classify_phase(self, delta, kappa, berry)` - *Clasificacion de fase segun Book.md:

discrete_crystal:       delta<0.05, kappa<1.5
topological_insulator:  |berry|>pi/2, winding!=0
cold_glass:             kappa>>1, delta>0.3
functional_glass:       intermedio (lo mas comun en LM)*
- `compute_all` (line 1940) `def compute_all(self, model, lr, dataloader, compute_kappa)` - *Calcula todas las metricas.
compute_kappa=True hace pasadas backward adicionales (caro, usar cada N epochs).*
- `format_log` (line 1965) `def format_log(self, m)`
- `__init__` (line 2001) `def __init__(self, config, logger)`
- `_measure_ratio` (line 2005) `def _measure_ratio(self, ratio, sample_batch)` - *Mide la coherencia espectral para un ratio dado.
Retorna: varianza del gradiente (menor = mas coherente = mejor).*
- `optimize` (line 2034) `def optimize(self, dataloader)` - *Retorna el mejor ratio de inicializacion de kernels espectrales.*
- `__init__` (line 2074) `def __init__(self, config, logger)`
- `prospect` (line 2078) `def prospect(self, candidates, train_dataset, prospect_steps)` - *Retorna el mejor batch size segun delta y T_eff.*
- `__init__` (line 2157) `def __init__(self, config, logger)`
- `mine` (line 2161) `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)` - *Retorna la semilla con la mejor trayectoria de delta.*
- `__init__` (line 2243) `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)`
- `refine` (line 2252) `def refine(self, train_dl, val_dl, refine_epochs)` - *Ejecuta refine_epochs epocas de recocido simulado.
Retorna el historial de refinamiento.*
- `__init__` (line 2404) `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)`
- `_make_dataloaders` (line 2414) `def _make_dataloaders(self, batch_size)`
- `run` (line 2426) `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)` - *Ejecuta el pipeline completo.
Retorna el trainer con el modelo entrenado.*
- `ckpt_fn` (line 964) `def ckpt_fn(x_in)`

#### `inference.py`
**Path:** `inference.py`

**Classes:**
- `InferenceConfig` (line 28) `class InferenceConfig` - *Parametric configuration container for inference execution.*
- `CheckpointInspector` (line 45) `class CheckpointInspector` - *Reads safetensors metadata to align architecture configuration.*
- `ModelLoader` (line 90) `class ModelLoader` - *Loads weights from safetensors and binds to the architectural graph.*
- `GenerationEngine` (line 115) `class GenerationEngine` - *Handles autoregressive token generation with controlled sampling.*
- `InferenceRunner` (line 140) `class InferenceRunner` - *Orchestrates execution flow for prompt processing.*

**Functions:**
- `_load_source_module` (line 19) `def _load_source_module(path)`

**Methods:**
- `parse_arguments` (line 178) `def parse_arguments()`
- `__init__` (line 47) `def __init__(self, logger)`
- `inspect_kq_head_count` (line 50) `def inspect_kq_head_count(self, checkpoint_path, d_model, n_heads)`
- `patch_config` (line 62) `def patch_config(self, config, source_module)`
- `_resolve_preset` (line 81) `def _resolve_preset(self, scale)`
- `__init__` (line 92) `def __init__(self, checkpoint_name, logger)`
- `load_model` (line 96) `def load_model(self, config, source_module)`
- `__init__` (line 117) `def __init__(self, config, logger)`
- `generate` (line 121) `def generate(self, model, tokenizer, prompt_text)`
- `sample_logits` (line 132) `def sample_logits(self, logits)`
- `__init__` (line 142) `def __init__(self, config)`
- `_setup_logger` (line 146) `def _setup_logger(self)`
- `run` (line 155) `def run(self)`
- `_print_result` (line 170) `def _print_result(self, prompt, output)`

#### `inference2.py`
**Path:** `inference2.py`

**Classes:**
- `InferenceConfig` (line 97) `class InferenceConfig` - *All tuneable knobs for the inference pipeline.

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
    If > 0, run this many generation passes and report throughput.*
- `BPETokenizer` (line 170) `class BPETokenizer` - *Thin wrapper around tiktoken with GPT-2 encoding.*
- `QuaternionOps` (line 196) `class QuaternionOps` - *Static quaternion algebra operations.*
- `QuaternionLinear` (line 219) `class QuaternionLinear(Module)` - *Linear layer in the quaternion algebra.

Implements the Hamilton product W ⊗ x using four real weight matrices.
Both in_features and out_features must be divisible by 4.*
- `QuaternionSpectralLayer` (line 252) `class QuaternionSpectralLayer(Module)` - *2-D spectral convolution using the quaternion Hamilton product in the
frequency domain.  Each quaternion component (w, x, y, z) has an
independent complex kernel (real + imaginary parts).*
- `SpectralAutoencoder` (line 306) `class SpectralAutoencoder(Module)` - *Spectral autoencoder: 1-D FFT filtering + quaternion projection for
encoding/decoding, plus stacked QuaternionSpectralLayers for the torus grid.*
- `QuaternionTorusBrain` (line 358) `class QuaternionTorusBrain(Module)` - *Replaces the MLP in each transformer layer.

Fully vectorised pipeline:
    [B, S, D] -> spectral AE -> torus projection -> soft node assignment
    -> 2-D spectral layer on grid -> quaternion message-passing -> readout
    -> [B, S, D]*
- `SwiGLU` (line 462) `class SwiGLU(Module)` - *SwiGLU feed-forward block (LLaMA-style).*
- `TopoMoEBrain` (line 481) `class TopoMoEBrain(Module)` - *Mixture-of-Experts wrapper: one always-active QuaternionTorusBrain plus
N sparse SwiGLU experts selected by a linear router (top-K per token).
When moe_enabled is False this reduces to a plain QuaternionTorusBrain.*
- `RotaryEmbedding` (line 537) `class RotaryEmbedding(Module)` - *Rotary Position Embeddings (RoPE) – Su et al., 2021.*
- `RMSNorm` (line 577) `class RMSNorm(Module)` - *Root Mean Square Layer Normalization (no bias).*
- `MultiHeadAttention` (line 589) `class MultiHeadAttention(Module)` - *GQA-capable multi-head attention with Flash Attention, RoPE, and KV cache.*
- `TopoGPT2Layer` (line 638) `class TopoGPT2Layer(Module)` - *Pre-norm transformer layer: attention + TopoMoEBrain.*
- `TopoGPT2` (line 660) `class TopoGPT2(Module)` - *TopoGPT2: causal language model with quaternion torus topology.
Embedding -> N layers (Attention + QuaternionTorusBrain) -> RMSNorm -> LM head.*
- `ModelConfig` (line 700) `class ModelConfig` - *All architectural hyperparameters required to instantiate TopoGPT2.
Populated entirely from the probed checkpoint shapes.*
- `CheckpointArchProber` (line 735) `class CheckpointArchProber` - *Infers all ModelConfig fields directly from checkpoint tensor shapes,
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
num_spec_layers: count of torus_spectral.N.kr_w keys in layer 0*
- `CheckpointLoader` (line 890) `class CheckpointLoader` - *Loads a safetensors or pickle checkpoint into a TopoGPT2 instance.
Restores weight tying after loading.*
- `Sampler` (line 943) `class Sampler` - *Stateless token sampling with temperature, top-k, top-p, and
repetition penalty.  All operations are performed on the logit tensor
returned by the model before softmax.*
- `GenerationEngine` (line 1003) `class GenerationEngine` - *Autoregressive generation with KV cache and optional token streaming.

First forward pass processes the full prompt and seeds the KV cache.
Subsequent passes process a single token each, giving O(n) complexity.*
- `ResultPrinter` (line 1082) `class ResultPrinter` - *Formats and writes generation results to stdout.*
- `InferencePipeline` (line 1116) `class InferencePipeline` - *Orchestrates the full inference workflow.

1. Validate config.
2. Probe checkpoint architecture.
3. Instantiate model.
4. Load weights.
5. Run generation in the requested mode.*

**Functions:**
- `build_logger` (line 79) `def build_logger(name, level)` - *Stderr logger with timestamp formatting.*

**Methods:**
- `build_arg_parser` (line 1217) `def build_arg_parser()` - *Construct and return the CLI argument parser.*
- `main` (line 1288) `def main()` - *CLI entry point.*
- `validate` (line 148) `def validate(self)` - *Raise ValueError for impossible parameter combinations.*
- `__init__` (line 175) `def __init__(self)`
- `encode` (line 182) `def encode(self, text)`
- `decode` (line 185) `def decode(self, token_ids)`
- `decode_single` (line 188) `def decode_single(self, token_id)`
- `hamilton_product` (line 200) `def hamilton_product(q1, q2)`
- `normalize` (line 211) `def normalize(q, eps)`
- `conjugate` (line 215) `def conjugate(q)`
- `__init__` (line 227) `def __init__(self, in_features, out_features, bias)`
- `forward` (line 241) `def forward(self, x)`
- `__init__` (line 259) `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- `_kernel` (line 276) `def _kernel(self, c)`
- `_contract` (line 279) `def _contract(self, W, X)`
- `forward` (line 282) `def forward(self, x)`
- `__init__` (line 312) `def __init__(self, cfg)`
- `_filter1d` (line 334) `def _filter1d(self, x, kr, ki)`
- `encode` (line 341) `def encode(self, x)`
- `decode` (line 344) `def decode(self, z)`
- `forward` (line 347) `def forward(self, x)`
- `process_torus_grid` (line 351) `def process_torus_grid(self, grid)`
- `__init__` (line 370) `def __init__(self, d_model, cfg)`
- `_build_torus_graph` (line 395) `def _build_torus_graph(self)`
- `_torus_soft_assign` (line 411) `def _torus_soft_assign(self, phi1, phi2)`
- `_message_passing` (line 423) `def _message_passing(self, node_feat)`
- `forward` (line 437) `def forward(self, x)`
- `__init__` (line 465) `def __init__(self, d_model, expansion, dropout)`
- `forward` (line 475) `def forward(self, x)`
- `__init__` (line 488) `def __init__(self, d_model, cfg)`
- `_route` (line 503) `def _route(self, x)`
- `forward` (line 528) `def forward(self, x)`
- `__init__` (line 542) `def __init__(self, d_head, max_seq_len)`
- `_build_cache` (line 550) `def _build_cache(self, seq_len)`
- `_rotate_half` (line 557) `def _rotate_half(x)`
- `forward` (line 561) `def forward(self, q, k, seq_len, offset)`
- `__init__` (line 580) `def __init__(self, d_model, eps)`
- `forward` (line 585) `def forward(self, x)`
- `__init__` (line 594) `def __init__(self, d_model, n_heads, cfg)`
- `forward` (line 609) `def forward(self, x, is_causal, past_kv)`
- `__init__` (line 641) `def __init__(self, d_model, n_heads, cfg)`
- `forward` (line 649) `def forward(self, x, past_kv)`
- `__init__` (line 666) `def __init__(self, cfg)`
- `forward` (line 678) `def forward(self, token_ids, past_kvs)`
- `d_quat` (line 723) `def d_quat(self)`
- `gqa_groups` (line 727) `def gqa_groups(self)`
- `__init__` (line 768) `def __init__(self, logger)`
- `_load_shapes` (line 771) `def _load_shapes(self, path)`
- `probe` (line 786) `def probe(self, path)` - *Return a ModelConfig whose dimensions exactly match the checkpoint.*
- `_fallback_d_head` (line 871) `def _fallback_d_head(d_model, q_out, k_out)`
- `__init__` (line 896) `def __init__(self, logger)`
- `load` (line 899) `def load(self, path, model, device)` - *Load weights into model in-place.*
- `__init__` (line 950) `def __init__(self, cfg)`
- `__call__` (line 953) `def __call__(self, logits, generated_ids)` - *Sample one token from logits.

Parameters
----------
logits       : [vocab_size] raw logits for the next token position.
generated_ids: token IDs already generated (for repetition penalty).

Returns
-------
Sampled token id.*
- `__init__` (line 1013) `def __init__(self, model, tokenizer, cfg, logger)`
- `generate` (line 1027) `def generate(self, prompt)` - *Generate text from prompt.

Returns
-------
(generated_text, tokens_per_second)
generated_text includes the prompt prefix.*
- `_maybe_stream` (line 1071) `def _maybe_stream(self, token_id)`
- `print_single` (line 1087) `def print_single(self, prompt, full_text, tps, show_timing)`
- `print_benchmark` (line 1100) `def print_benchmark(self, runs, tps_list)`
- `__init__` (line 1127) `def __init__(self, cfg, logger)`
- `_build_model` (line 1131) `def _build_model(self)`
- `run` (line 1149) `def run(self)`
- `_run_single` (line 1164) `def _run_single(self, engine, printer)`
- `_run_interactive` (line 1176) `def _run_interactive(self, engine, printer)`
- `_run_benchmark` (line 1199) `def _run_benchmark(self, engine, printer)`

#### `quantize.py`
**Path:** `quantize.py`

**Classes:**
- `InferenceConfig` (line 34) `class InferenceConfig` - *Centralized configuration for quantized inference. All parameters are explicitly defined.*
- `CheckpointInspector` (line 105) `class CheckpointInspector` - *Inspects checkpoint state dict to dynamically resolve architecture parameters.*
- `QuaternionOps` (line 162) `class QuaternionOps` - *Pure quaternion operations in PyTorch. Representation: [..., 4] -> [w, x, y, z].*
- `QuaternionLinear` (line 195) `class QuaternionLinear(Module)`
- `QuaternionSpectralLayer` (line 220) `class QuaternionSpectralLayer(Module)`
- `SpectralAutoencoder` (line 262) `class SpectralAutoencoder(Module)`
- `QuaternionTorusBrain` (line 312) `class QuaternionTorusBrain(Module)`
- `RotaryEmbedding` (line 408) `class RotaryEmbedding(Module)`
- `RMSNorm` (line 440) `class RMSNorm(Module)`
- `SwiGLU` (line 451) `class SwiGLU(Module)`
- `TopoMoEBrain` (line 468) `class TopoMoEBrain(Module)`
- `MultiHeadAttention` (line 522) `class MultiHeadAttention(Module)`
- `TopoGPT2Layer` (line 568) `class TopoGPT2Layer(Module)`
- `TopoGPT2` (line 590) `class TopoGPT2(Module)`
- `BPETokenizer` (line 651) `class BPETokenizer`
- `QuantizationFormat` (line 668) `class QuantizationFormat(Enum)`
- `IQuantizer` (line 678) `class IQuantizer(ABC)`
- `BitNetQuantizer` (line 692) `class BitNetQuantizer(IQuantizer)`
- `INT4Quantizer` (line 721) `class INT4Quantizer(IQuantizer)`
- `INT8Quantizer` (line 746) `class INT8Quantizer(IQuantizer)`
- `Float16Quantizer` (line 760) `class Float16Quantizer(IQuantizer)`
- `BFloat16Quantizer` (line 774) `class BFloat16Quantizer(IQuantizer)`
- `Float32Quantizer` (line 788) `class Float32Quantizer(IQuantizer)`
- `Float64Quantizer` (line 802) `class Float64Quantizer(IQuantizer)`
- `QuantizerFactory` (line 816) `class QuantizerFactory`
- `ModelLoader` (line 834) `class ModelLoader`
- `InferenceEngine` (line 883) `class InferenceEngine`
- `QuantizationInferencePipeline` (line 907) `class QuantizationInferencePipeline`

**Methods:**
- `parse_arguments` (line 939) `def parse_arguments()`
- `main` (line 965) `def main()`
- `resolve_gqa` (line 86) `def resolve_gqa(self)`
- `inspect_and_patch` (line 108) `def inspect_and_patch(path, config)`
- `hamilton_product` (line 165) `def hamilton_product(q1, q2)`
- `normalize` (line 176) `def normalize(q, eps)`
- `conjugate` (line 180) `def conjugate(q)`
- `rotate_vector` (line 185) `def rotate_vector(v, q)`
- `__init__` (line 196) `def __init__(self, in_features, out_features, bias)`
- `forward` (line 209) `def forward(self, x)`
- `__init__` (line 221) `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- `_kernel` (line 233) `def _kernel(self, c)`
- `_contract` (line 236) `def _contract(self, W, X)`
- `forward` (line 239) `def forward(self, x)`
- `__init__` (line 263) `def __init__(self, config)`
- `_filter1d` (line 286) `def _filter1d(self, x, kr, ki)`
- `encode` (line 291) `def encode(self, x)`
- `decode` (line 295) `def decode(self, z)`
- `forward` (line 299) `def forward(self, x)`
- `process_torus_grid` (line 305) `def process_torus_grid(self, grid)`
- `__init__` (line 313) `def __init__(self, d_model, config)`
- `_build_torus_graph` (line 338) `def _build_torus_graph(self)`
- `_torus_soft_assign` (line 354) `def _torus_soft_assign(self, phi1, phi2)`
- `_message_passing` (line 365) `def _message_passing(self, node_feat)`
- `forward` (line 380) `def forward(self, x)`
- `__init__` (line 409) `def __init__(self, d_head, max_seq_len, base)`
- `_build_cache` (line 415) `def _build_cache(self, seq_len)`
- `_rotate_half` (line 422) `def _rotate_half(self, x)`
- `forward` (line 426) `def forward(self, q, k, seq_len, offset)`
- `__init__` (line 441) `def __init__(self, d_model, eps)`
- `forward` (line 446) `def forward(self, x)`
- `__init__` (line 452) `def __init__(self, d_model, expansion, dropout)`
- `forward` (line 464) `def forward(self, x)`
- `__init__` (line 469) `def __init__(self, d_model, config)`
- `_route` (line 486) `def _route(self, x)`
- `forward` (line 509) `def forward(self, x)`
- `__init__` (line 523) `def __init__(self, d_model, n_heads, config)`
- `forward` (line 539) `def forward(self, x, is_causal, past_kv)`
- `__init__` (line 569) `def __init__(self, d_model, n_heads, config)`
- `_forward_impl` (line 579) `def _forward_impl(self, x, past_kv)`
- `forward` (line 586) `def forward(self, x, past_kv)`
- `__init__` (line 591) `def __init__(self, config)`
- `_init_weights` (line 606) `def _init_weights(self)`
- `forward` (line 613) `def forward(self, token_ids, past_kvs)`
- `generate` (line 627) `def generate(self, token_ids, max_new_tokens, temperature, top_k, eos_token_id)`
- `__init__` (line 652) `def __init__(self, encoding)`
- `encode` (line 658) `def encode(self, text)`
- `decode` (line 661) `def decode(self, tokens)`
- `eot_token` (line 664) `def eot_token(self)`
- `quantize` (line 680) `def quantize(self, model)`
- `get_format_name` (line 684) `def get_format_name(self)`
- `get_bits_per_weight` (line 688) `def get_bits_per_weight(self)`
- `__init__` (line 693) `def __init__(self, config)`
- `quantize` (line 696) `def quantize(self, model)`
- `get_format_name` (line 714) `def get_format_name(self)`
- `get_bits_per_weight` (line 717) `def get_bits_per_weight(self)`
- `__init__` (line 722) `def __init__(self, config)`
- `quantize` (line 725) `def quantize(self, model)`
- `get_format_name` (line 739) `def get_format_name(self)`
- `get_bits_per_weight` (line 742) `def get_bits_per_weight(self)`
- `__init__` (line 747) `def __init__(self, config)`
- `quantize` (line 750) `def quantize(self, model)`
- `get_format_name` (line 753) `def get_format_name(self)`
- `get_bits_per_weight` (line 756) `def get_bits_per_weight(self)`
- `__init__` (line 761) `def __init__(self, config)`
- `quantize` (line 764) `def quantize(self, model)`
- `get_format_name` (line 767) `def get_format_name(self)`
- `get_bits_per_weight` (line 770) `def get_bits_per_weight(self)`
- `__init__` (line 775) `def __init__(self, config)`
- `quantize` (line 778) `def quantize(self, model)`
- `get_format_name` (line 781) `def get_format_name(self)`
- `get_bits_per_weight` (line 784) `def get_bits_per_weight(self)`
- `__init__` (line 789) `def __init__(self, config)`
- `quantize` (line 792) `def quantize(self, model)`
- `get_format_name` (line 795) `def get_format_name(self)`
- `get_bits_per_weight` (line 798) `def get_bits_per_weight(self)`
- `__init__` (line 803) `def __init__(self, config)`
- `quantize` (line 806) `def quantize(self, model)`
- `get_format_name` (line 809) `def get_format_name(self)`
- `get_bits_per_weight` (line 812) `def get_bits_per_weight(self)`
- `create_quantizer` (line 818) `def create_quantizer(fmt, config)`
- `__init__` (line 835) `def __init__(self, config, logger)`
- `load_checkpoint` (line 839) `def load_checkpoint(self)`
- `__init__` (line 884) `def __init__(self, config, model, tokenizer)`
- `run_inference` (line 891) `def run_inference(self, prompt)`
- `__init__` (line 908) `def __init__(self, config)`
- `execute` (line 919) `def execute(self)`

#### `reinforce.py`
**Path:** `reinforce.py`

**Classes:**
- `RLConfig` (line 27) `class RLConfig` - *Parametric configuration for RL alignment of TopoGPT2.*
- `RewardSignalType` (line 72) `class RewardSignalType(Enum)` - *Enumeration of supported reward signal types.*
- `CheckpointPatcher` (line 84) `class CheckpointPatcher` - *Inspects checkpoint weights to align architecture configuration before instantiation.*
- `MechanisticRewardCalculator` (line 120) `class MechanisticRewardCalculator` - *Computes reward signals from mechanistic interpretability metrics.*
- `RewardModel` (line 152) `class RewardModel(Module)` - *Lightweight reward model for scoring generated responses.*
- `ExperienceBuffer` (line 189) `class ExperienceBuffer` - *Stores trajectories for PPO training with advantage computation.*
- `ValueHead` (line 240) `class ValueHead(Module)` - *Scalar value estimation head attached to TopoGPT2 for PPO.*
- `PPOTrainer` (line 262) `class PPOTrainer` - *Proximal Policy Optimization trainer for TopoGPT2 alignment.*
- `ChatAgent` (line 519) `class ChatAgent` - *High-level interface for RL-aligned TopoGPT2 as chatbot.*

**Methods:**
- `setup_logger` (line 597) `def setup_logger(name, level)`
- `create_rl_agent_from_checkpoint` (line 606) `def create_rl_agent_from_checkpoint(model_path, config, tokenizer, logger)`
- `__init__` (line 86) `def __init__(self, logger)`
- `align_config` (line 89) `def align_config(self, model_path, config, source_module)`
- `_resolve_preset` (line 111) `def _resolve_preset(self, scale)`
- `__init__` (line 122) `def __init__(self, config, logger)`
- `compute_lc_reward` (line 129) `def compute_lc_reward(self, lc_value)`
- `compute_sp_reward` (line 133) `def compute_sp_reward(self, sp_value)`
- `compute_delta_reward` (line 137) `def compute_delta_reward(self, delta_value)`
- `compute_mechanistic_reward` (line 142) `def compute_mechanistic_reward(self, metrics)`
- `__init__` (line 154) `def __init__(self, config, vocab_size, d_model)`
- `_init_weights` (line 173) `def _init_weights(self)`
- `forward` (line 180) `def forward(self, input_ids, attention_mask)`
- `__init__` (line 191) `def __init__(self, config, capacity)`
- `add` (line 198) `def add(self, experience)`
- `compute_advantages` (line 201) `def compute_advantages(self, values, rewards, masks)`
- `sample_minibatches` (line 215) `def sample_minibatches(self, batch_size)`
- `_collate` (line 226) `def _collate(self, batch)`
- `clear` (line 237) `def clear(self)`
- `__init__` (line 242) `def __init__(self, d_model, hidden_dim)`
- `_init_weights` (line 251) `def _init_weights(self)`
- `forward` (line 258) `def forward(self, hidden_states)`
- `__init__` (line 264) `def __init__(self, policy_model, config, reward_model, ref_model, logger)`
- `generate_with_policy` (line 294) `def generate_with_policy(self, prompt_ids, max_new_tokens)`
- `compute_kl_divergence` (line 306) `def compute_kl_divergence(self, policy_logits, ref_logits)`
- `compute_reward` (line 317) `def compute_reward(self, responses, prompts, metrics)`
- `collect_experience` (line 336) `def collect_experience(self, prompts, num_samples)`
- `_extract_mechanistic_metrics` (line 367) `def _extract_mechanistic_metrics(self, tokens)`
- `ppo_update` (line 398) `def ppo_update(self, batch)`
- `train_step` (line 460) `def train_step(self, prompts)`
- `_save_checkpoint` (line 482) `def _save_checkpoint(self)`
- `load_checkpoint` (line 498) `def load_checkpoint(self, path)`
- `__init__` (line 521) `def __init__(self, policy_model, config, tokenizer, logger)`
- `attach_trainer` (line 530) `def attach_trainer(self, trainer)`
- `respond` (line 533) `def respond(self, user_message, max_new_tokens)`
- `_format_conversation` (line 553) `def _format_conversation(self)`
- `train_on_feedback` (line 562) `def train_on_feedback(self, user_message, response, reward_score)`
- `reset_conversation` (line 594) `def reset_conversation(self)`

#### `topogpt2_1.py`
**Path:** `topogpt2_1.py`

**Classes:**
- `TopoGPT2Config` (line 55) `class TopoGPT2Config` - *Configuración completa para TopoGPT2.*
- `QuaternionOps` (line 177) `class QuaternionOps` - *Operaciones de cuaterniones puras en PyTorch.
Representación: [..., 4]  donde last dim = [w, x, y, z]
q = w + x*i + y*j + z*k*
- `QuaternionLinear` (line 216) `class QuaternionLinear(Module)` - *Capa lineal con pesos cuaterniones.

Implementa la multiplicación W * x en el álgebra de cuaterniones:
- W = Ww + Wx*i + Wy*j + Wz*k  (cuaternión de pesos)
- x = xw + xx*i + xy*j + xz*k  (cuaternión de entrada)
- out = W * x  (producto de Hamilton extendido a vectores)

Parámetros: 4 matrices reales de forma [out_q, in_q]*
- `QuaternionSpectralLayer` (line 261) `class QuaternionSpectralLayer(Module)` - *Convolución espectral 2D con cuaterniones y producto de Hamilton completo.

Operación en dominio de frecuencia:
    P(k) = W(k) ⊗ X(k)  (producto de Hamilton de cuaterniones complejos)

Donde:
    X(k) = FFT2(x) con 4 canales cuaterniones [Xw, Xx, Xy, Xz]
    W(k) = kernel complejo aprendible con componentes [Ww, Wx, Wy, Wz]

Reglas del producto de Hamilton en dominio de frecuencia:
    Pw = Ww·Xw - Wx·Xx - Wy·Xy - Wz·Xz
    Px = Ww·Xx + Wx·Xw + Wy·Xz - Wz·Xy
    Py = Ww·Xy - Wx·Xz + Wy·Xw + Wz·Xx
    Pz = Ww·Xz + Wx·Xy - Wy·Xx + Wz·Xw

Cada Wc es un kernel complejo (partes real e imaginaria independientes).*
- `SpectralAutoencoder` (line 348) `class SpectralAutoencoder(Module)` - *Autoencoder espectral con cuaterniones.

Opera en dos niveles:
1. Espectral 1D sobre el vector de features (FFT sobre dim D_MODEL):
   captura la espectrografía global del embedding.
2. Espectral 2D sobre el grid del toro (QuaternionSpectralLayer):
   captura correlaciones espaciales en la topología.

Devuelve (latent, recon_loss) para regularización.*
- `QuaternionTorusBrain` (line 431) `class QuaternionTorusBrain(Module)` - *Reemplaza el MLP en cada capa del transformer.

Pipeline (completamente vectorizado sobre batch Y secuencia):

1. Flatten: [B, S, D] → [B·S, D]
2. SpectralAutoencoder: filtrado espectral 1D + compresión cuaternión
3. Proyección al toro:
   - Calcula 2 ángulos (phi1, phi2) ∈ [-π, π]²
   - Asignación blanda a los 8 nodos via distancia circular en el toro
4. Construye grid de nodos: [B·S, N_NODES=8, D_MODEL]
5. QuaternionSpectralLayer 2D sobre el grid [B·S, 4*D_QUAT, RADIAL, ANGULAR]
6. Message-passing con rotaciones cuaterniones sobre el grafo toro
7. Readout: atención sobre los 8 nodos → [B·S, D_MODEL]
8. Reshape: [B·S, D] → [B, S, D]*
- `RotaryEmbedding` (line 648) `class RotaryEmbedding(Module)` - *Rotary Position Embeddings (RoPE) - Su et al., 2021.
Codifica la posición como rotaciones del espacio de atención,
naturalmente relativas y sin parámetros extra.*
- `RMSNorm` (line 696) `class RMSNorm(Module)` - *Root Mean Square Layer Normalization (sin bias). Más estable que LayerNorm.*
- `SwiGLU` (line 713) `class SwiGLU(Module)` - *SwiGLU: SiLU(gate(x)) * up(x) -> down
Usado en LLaMA 2/3, Qwen, Mistral en lugar de GELU-FFN.
Dimension interna: 8/3 * d_model (convención LLaMA, redondeada a múltiplo de 4).*
- `TopoMoEBrain` (line 742) `class TopoMoEBrain(Module)` - *Mixture of Experts sobre la capa topologica.

Arquitectura (inspirada en DeepSeek-MoE / Mixtral):
  - 1 experto compartido: QuaternionTorusBrain (siempre activo)
  - N_EXPERTS expertos SwiGLU ligeros (activacion esparsa: Top-K por token)
  - Router: Linear(D, N_EXPERTS) + softmax → top-K

Load-balancing loss (auxiliar): penaliza si un experto acapara todos los tokens.
Activa MOE_TOP_K de N_EXPERTS expertos por token.

Sin MoE (MOE_ENABLED=False): se comporta como QuaternionTorusBrain puro.*
- `MultiHeadAttention` (line 847) `class MultiHeadAttention(Module)` - *Multi-head attention con:
- Flash Attention (scaled_dot_product_attention de PyTorch 2.0+)
- Rotary Position Embeddings (RoPE)
- GQA (Grouped Query Attention): N_KV_HEADS < N_HEADS, reduce VRAM de K/V
- KV Cache para inferencia autoregresiva eficiente
- Temperatura termodinámica aprendible*
- `TopoGPT2Layer` (line 929) `class TopoGPT2Layer(Module)` - *Capa del transformer con TopoMoEBrain (TopoBrain + MoE SwiGLU experts).

Esquema pre-norm (estilo LLaMA):
    x = x + Attention_GQA(RMSNorm(x))
    x = x + TopoMoEBrain(RMSNorm(x))*
- `TopoGPT2` (line 976) `class TopoGPT2(Module)` - *TopoGPT2: Transformer de lenguaje con TopoBrain cuaternión-espectral.

Arquitectura:
    Embedding de tokens + RoPE (en Attention)
    N_LAYERS × TopoGPT2Layer (Attention + QuaternionTorusBrain)
    RMSNorm final
    Proyección a vocabulario (weight-tied con embeddings)*
- `BPETokenizer` (line 1082) `class BPETokenizer` - *Wrapper alrededor de tiktoken (GPT-2 compatible).*
- `CorpusDownloader` (line 1107) `class CorpusDownloader` - *Descarga corpus de texto para entrenamiento.

Soporta:
- 'tinystories': ~2GB de cuentos cortos (ideal para pruebas)
- 'wikitext103': ~500MB de Wikipedia curada
- 'file': archivo de texto local

Usa HuggingFace 'datasets' para TinyStories y WikiText.*
- `TokenizedDataset` (line 1170) `class TokenizedDataset(Dataset)` - *Dataset de tokens para language modeling (next-token prediction).

Guarda los tokens tokenizados en disco la primera vez (cache .pt)
para evitar re-tokenizar en cada ejecucion. La clave de cache incluye
un hash del contenido del corpus + tokenizador + max_tokens.*
- `CheckpointManager` (line 1220) `class CheckpointManager` - *Gestiona checkpoints de forma acumulativa y segura.

Estructura en disco:
    checkpoints_topogpt2/
      latest/
        model.safetensors   <- pesos del modelo (formato seguro, sin pickle)
        optimizer.pt        <- estado del optimizador (requiere .pt)
        state.json          <- metadatos: epoch, step, historial, config
      best/
        model.safetensors
        state.json
      step_NNNNN/           <- snapshots periodicos (rotados)
        model.safetensors
        optimizer.pt
        state.json

El historial se ACUMULA entre sesiones de entrenamiento: cada --resume
agrega nuevas entradas a train_loss[], val_loss[], etc.*
- `TopoGPT2Trainer` (line 1453) `class TopoGPT2Trainer` - *Entrenador acumulativo y resumible.

Caracteristicas:
- Checkpoint automatico en safetensors cada N minutos + cada epoch
- Historial acumulativo entre sesiones (--resume agrega al historial existente)
- Guarda el mejor modelo en checkpoints/best/ automaticamente
- LR schedule: cosine con warmup relativo a los steps de ESTA sesion
- Mixed Precision (AMP) + acumulacion de gradientes*
- `MechanisticMetrics` (line 1746) `class MechanisticMetrics` - *Calcula todas las metricas del diagrama de fases de Book.md.

Todas las metricas se derivan de cantidades medibles (pesos, gradientes):

delta  (δ): margen de discretizacion.  max|w - round(w)|
            δ≈0 -> cristal;  δ≈0.49 -> vidrio frio
kappa  (κ): numero de condicion de la covarianza del gradiente.
            κ≈1 -> cristalino;  κ>>1 -> amorfo
T_eff:      temperatura efectiva = (lr/2) * Var(gradiente).
            T_eff→0 -> congelado; T_eff alto -> ruidoso
alpha  (α): indice de pureza = -log(δ + ε).
            α=20 -> perfecto; α<1 -> vidrio
berry:      fase de Berry de los kernels espectrales imaginarios.
            |berry|>π/2 con winding≠0 -> insulador topologico
lc:         complejidad local = 1 - similitud coseno promedio entre filas.
sp:         superposicion = correlacion promedio inter-fila de pesos.*
- `Phase0_KernelOptimizer` (line 1983) `class Phase0_KernelOptimizer` - *Encuentra el ratio imaginario/real optimo para los kernels espectrales.

Analogia con main.py: evalua la transicion GOE→GUE en el espacio
de kernels. Un ratio optimo promueve estructura topologica (insulador)
vs estructura amorfa (vidrio).

Metodo: calibra con un mini-batch y mide la varianza del gradiente
en funcion del ratio. Ratios que minimizan la varianza de gradiente
(maxima coherencia espectral) son preferibles.

No entrena: solo inicializa los kernels con distintos ratios y mide.
Tiempo tipico: < 30 segundos.*
- `Phase1_BatchProspector` (line 2058) `class Phase1_BatchProspector` - *Encuentra el batch size optimo testando candidatos con pocos pasos.

De main.py: el batch size regula la temperatura del horno de cristalizacion.
Batch sizes demasiado chicos -> ruido excesivo (vidrio frio).
Batch sizes demasiado grandes -> sin presion annealing (amorfos).
La ventana optima empirica de main.py: [24, 128] para Strassen.

Para LM, testeamos candidatos midiendo:
- delta (δ): velocidad de descenso en prospect_steps pasos
- T_eff: temperatura efectiva del gradiente

Tiempo tipico: < 2 minutos para 3 candidatos × 30 pasos.*
- `Phase2_SeedMiner` (line 2141) `class Phase2_SeedMiner` - *Encuentra semillas prometedoras midiendo la trayectoria de delta.

De main.py: una semilla "buena" muestra delta descendente en los
primeros N pasos (enfriamiento). Una semilla "mala" se estanca en
el plateau vidrioso (~0.49).

Criterio de seleccion:
1. Semillas con delta_velocity < 0 (enfriando) AND kappa bajo.
2. Si no hay, semillas solo enfriando.
3. Fallback: semilla con menor delta final.

Tiempo tipico: < 3 minutos para 5 semillas × 50 pasos.*
- `Phase4_AnnealingRefiner` (line 2223) `class Phase4_AnnealingRefiner` - *Refinamiento post-entrenamiento mediante recocido simulado.

De main.py: despues de que el modelo converge, una fase de annealing
con criterio de aceptacion de Metropolis puede empujar los pesos
hacia estados de menor energia libre (menor delta o mejor val_loss).

Aceptacion de Metropolis:
    si Δloss < 0: siempre acepta (mejora)
    si Δloss >= 0: acepta con prob exp(-Δloss / T)

La temperatura T decae exponencialmente: T(t) = T0 * cooling_rate^t

Al rechazar: restaura el mejor estado conocido.
Si se estanca: perturbacion termica (ruido gaussiano en pesos).

Tiempo: proporcional a refine_epochs (user-controlled).*
- `TopoPhasePipeline` (line 2384) `class TopoPhasePipeline` - *Orquesta las 5 fases de entrenamiento segun main.py + Book.md.

Fases:
  0  Kernel ratio optimization  (GOE-GUE spectral calibration)
  1  Batch size prospecting      (temperatura del horno de cristalizacion)
  2  Seed mining                 (seleccion de semilla enfriante)
  3  Full training               (entrenamiento principal con metricas)
  4  Annealing refinement        (recocido simulado post-entrenamiento)

Las fases 0-2 son rapidas (prospecting). La fase 3 es el grueso.
La fase 4 es opcional (--refine).

Para no ser prohibitivo:
  --prospect         activa fases 0, 1, 2 antes del entrenamiento
  --refine-epochs N  activa fase 4 con N epocas de annealing
  Sin flags: solo fase 3 (comportamiento original, identico a antes)*

**Methods:**
- `setup_logger` (line 155) `def setup_logger(name, level)`
- `set_seed` (line 165) `def set_seed(seed, device)`
- `main` (line 2506) `def main()`
- `__post_init__` (line 124) `def __post_init__(self)`
- `hamilton_product` (line 185) `def hamilton_product(q1, q2)` - *Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].*
- `normalize` (line 197) `def normalize(q, eps)`
- `conjugate` (line 201) `def conjugate(q)`
- `rotate_vector` (line 206) `def rotate_vector(v, q)` - *Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]*
- `__init__` (line 228) `def __init__(self, in_features, out_features, bias)`
- `forward` (line 244) `def forward(self, x)` - *x: [..., in_features] → [..., out_features]*
- `__init__` (line 281) `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- `_kernel` (line 300) `def _kernel(self, c)`
- `_contract` (line 303) `def _contract(self, W, X)` - *Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]*
- `forward` (line 307) `def forward(self, x)` - *x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)
→ [B, 4*out_q, H, W]*
- `__init__` (line 361) `def __init__(self, config)`
- `_filter1d` (line 393) `def _filter1d(self, x, kr, ki)` - *Filtro espectral 1D: x[..., D] → filtrado[..., D]*
- `encode` (line 399) `def encode(self, x)` - *x: [..., D_MODEL] → latent: [..., D_LAT]*
- `decode` (line 404) `def decode(self, z)` - *z: [..., D_LAT] → recon: [..., D_MODEL]*
- `forward` (line 409) `def forward(self, x)` - *Devuelve (latent, recon_loss)*
- `process_torus_grid` (line 416) `def process_torus_grid(self, grid)` - *Procesa el grid del toro con QuaternionSpectralLayer.
grid: [B, 4*D_QUAT, RADIAL, ANGULAR]  →  [B, 4*D_QUAT, RADIAL, ANGULAR]*
- `__init__` (line 449) `def __init__(self, d_model, config)`
- `_build_torus_graph` (line 489) `def _build_torus_graph(self)` - *Construye las aristas del grafo toro 2×4.

Nodos indexados como: node = r * N_ANGULAR + a
  r ∈ [0, RADIAL-1], a ∈ [0, ANGULAR-1]

Aristas angulares: nodo ↔ nodo a la izquierda/derecha (periódico)
Aristas radiales:  nodo ↔ nodo del anillo interior/exterior*
- `_torus_soft_assign` (line 523) `def _torus_soft_assign(self, phi1, phi2)` - *Asignación blanda de tokens a los 8 nodos del toro via distancia circular.

phi1: [BS] ángulo angular ∈ [-π, π]
phi2: [BS] ángulo radial ∈ [-π, π]
→ weights: [BS, N_NODES]  (suma a 1, softmax de distancias negativas)*
- `_message_passing` (line 550) `def _message_passing(self, node_feat)` - *Message-passing VECTORIZADO con rotaciones cuaterniones.
Sin bucles Python: todas las aristas se procesan en paralelo.

node_feat: [BS, N_NODES, D_MODEL]
→ [BS, N_NODES, D_MODEL]*
- `forward` (line 587) `def forward(self, x)` - *x: [B, S, D_MODEL]
→ output: [B, S, D_MODEL], recon_loss: scalar*
- `__init__` (line 655) `def __init__(self, d_head, max_seq_len, base)`
- `_build_cache` (line 661) `def _build_cache(self, seq_len)`
- `_rotate_half` (line 668) `def _rotate_half(self, x)`
- `forward` (line 672) `def forward(self, q, k, seq_len, offset)` - *q, k: [B, n_heads, S_q/S_k, d_head]
offset: posicion inicial (para KV cache: longitud del cache existente)
Aplica posiciones [offset .. offset+S-1] a q y k.*
- `__init__` (line 699) `def __init__(self, d_model, eps)`
- `forward` (line 704) `def forward(self, x)`
- `__init__` (line 720) `def __init__(self, d_model, expansion, dropout)`
- `forward` (line 734) `def forward(self, x)`
- `__init__` (line 757) `def __init__(self, d_model, config)`
- `_route` (line 778) `def _route(self, x)` - *x: [N, D] donde N = B*S (tokens aplanados)
Retorna:
expert_out: [N, D]  suma ponderada de top-K expertos
aux_loss:   escalar  load-balancing loss
Routing vectorizado sin boolean indexing ni sincronizacion CUDA.
Usa dispatch por indices agrupados (estilo Mixtral/DeepSeek) para
compatibilidad total con torch.utils.checkpoint.*
- `forward` (line 820) `def forward(self, x)` - *x: [B, S, D]
→ output: [B, S, D], aux_loss: escalar*
- `__init__` (line 857) `def __init__(self, d_model, n_heads, config)`
- `forward` (line 875) `def forward(self, x, is_causal, past_kv)` - *Args:
    x:        [B, S, D]
    is_causal: usar mascara causal
    past_kv:  (K_cache, V_cache) de pasos anteriores o None
Returns:
    out:      [B, S, D]
    kv_cache: (K, V) completos para cachear en generate()*
- `__init__` (line 938) `def __init__(self, d_model, n_heads, config)`
- `_forward_impl` (line 947) `def _forward_impl(self, x, past_kv)`
- `forward` (line 956) `def forward(self, x, past_kv)` - *Retorna (x_out, aux_loss, kv_cache).
Con gradient checkpointing en training (solo cuando no hay KV cache).*
- `__init__` (line 987) `def __init__(self, config)`
- `_init_weights` (line 1006) `def _init_weights(self)`
- `forward` (line 1013) `def forward(self, token_ids, past_kvs)` - *token_ids: [B, S]  (enteros)
past_kvs:  lista de (K, V) por capa, o None para entrenamiento
→ logits: [B, S, VOCAB_SIZE], aux_loss: scalar, new_kvs: list[(K,V)]*
- `count_params` (line 1036) `def count_params(self)`
- `generate` (line 1042) `def generate(self, token_ids, max_new_tokens, temperature, top_k)` - *Generacion autoregresiva con KV cache y muestreo top-k.
En el primer paso procesa el prompt completo y guarda el cache.
En pasos siguientes solo procesa 1 token nuevo (O(n) en lugar de O(n^2)).*
- `__init__` (line 1085) `def __init__(self, encoding)`
- `encode` (line 1093) `def encode(self, text)`
- `decode` (line 1096) `def decode(self, tokens)`
- `eot_token` (line 1099) `def eot_token(self)`
- `__init__` (line 1119) `def __init__(self, corpus, data_dir, logger)`
- `get_text` (line 1125) `def get_text(self, split)` - *Devuelve el texto del corpus. Descarga si es necesario.*
- `_download_hf` (line 1150) `def _download_hf(self, dataset_name, split, text_column, name)`
- `__init__` (line 1179) `def __init__(self, text, tokenizer, seq_len, max_tokens, cache_dir, split_tag)`
- `__len__` (line 1206) `def __len__(self)`
- `__getitem__` (line 1209) `def __getitem__(self, idx)`
- `__init__` (line 1245) `def __init__(self, config, logger)`
- `patch_config_for_resume` (line 1255) `def patch_config_for_resume(self, cfg)` - *Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS
para que coincidan con la arquitectura guardada.
Necesario cuando el codigo cambio GQA despues de guardar el checkpoint.*
- `_save_model` (line 1284) `def _save_model(self, model, directory)`
- `_load_model` (line 1297) `def _load_model(self, model, directory)`
- `_save_optimizer` (line 1328) `def _save_optimizer(self, optimizer, directory)`
- `_load_optimizer` (line 1331) `def _load_optimizer(self, optimizer, directory, device)`
- `_save_state` (line 1340) `def _save_state(self, state, directory)`
- `_load_state` (line 1345) `def _load_state(self, directory)`
- `should_save` (line 1356) `def should_save(self)`
- `save` (line 1359) `def save(self, model, optimizer, state, is_best)` - *Guarda checkpoint completo.

state debe contener al menos: completed_epochs, global_step,
best_val_loss, history, config.*
- `load_latest` (line 1404) `def load_latest(self, model, optimizer)` - *Carga el ultimo checkpoint guardado.
Devuelve el state dict (vacio si no hay checkpoint).*
- `load_best` (line 1431) `def load_best(self, model)` - *Carga el mejor modelo guardado (solo pesos, sin optimizador).*
- `has_checkpoint` (line 1443) `def has_checkpoint(self)`
- `__init__` (line 1465) `def __init__(self, model, config, tokenizer)`
- `resume` (line 1500) `def resume(self)` - *Carga el ultimo checkpoint disponible.
Restaura: pesos del modelo, estado del optimizador, historial acumulado,
epoch/step completados y mejor val_loss.
Devuelve True si se cargo un checkpoint, False si empieza de cero.*
- `_current_state` (line 1525) `def _current_state(self)` - *Construye el dict de estado para persistir en state.json.*
- `_cosine_lr` (line 1536) `def _cosine_lr(self, step_in_session, total_steps_session)` - *Cosine decay con warmup. El schedule es relativo a la sesion actual.*
- `_set_lr` (line 1544) `def _set_lr(self, lr)`
- `train` (line 1548) `def train(self, train_dl, val_dl)` - *Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.
El historial se acumula sobre sesiones previas.*
- `_sample_text` (line 1684) `def _sample_text(self, tokenizer, prompts, max_new, temperature, top_k)` - *Genera una muestra de texto al final de cada epoch para monitorear
la calidad cualitativa del modelo (detecta degeneracion, repeticion, etc.).*
- `evaluate` (line 1716) `def evaluate(self, dataloader)`
- `__init__` (line 1766) `def __init__(self, config)`
- `compute_delta` (line 1774) `def compute_delta(self, model)`
- `compute_alpha` (line 1781) `def compute_alpha(self, delta)`
- `update_grad_buffer` (line 1786) `def update_grad_buffer(self, model)` - *Captura gradientes de forma segura, ignorando tensores corruptos.*
- `compute_t_eff` (line 1812) `def compute_t_eff(self, lr)` - *T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva.*
- `compute_kappa` (line 1820) `def compute_kappa(self, model, dataloader, n_batches)` - *κ = λ_max / λ_min de la covarianza del gradiente.
Parámetro de orden para cristalización (κ≈1 = cristal).
Nota: requiere pasadas backward adicionales. Se ejecuta con protección
para no corromper el estado AMP del trainer principal.*
- `compute_berry_phase` (line 1878) `def compute_berry_phase(self, model)` - *Fase de Berry de los kernels espectrales imaginarios.
Surge de los parametros ki_w, ki_x, ki_y, ki_z de QuaternionSpectralLayer.
|berry|>pi/2 con winding!=0 indica estructura topologica.*
- `compute_lc` (line 1891) `def compute_lc(self, model)` - *Complejidad local: 1 - similitud coseno promedio entre filas de pesos.*
- `compute_sp` (line 1905) `def compute_sp(self, model)` - *Superposicion: correlacion inter-fila promedio (entrelazamiento de features).*
- `classify_phase` (line 1921) `def classify_phase(self, delta, kappa, berry)` - *Clasificacion de fase segun Book.md:

discrete_crystal:       delta<0.05, kappa<1.5
topological_insulator:  |berry|>pi/2, winding!=0
cold_glass:             kappa>>1, delta>0.3
functional_glass:       intermedio (lo mas comun en LM)*
- `compute_all` (line 1940) `def compute_all(self, model, lr, dataloader, compute_kappa)` - *Calcula todas las metricas.
compute_kappa=True hace pasadas backward adicionales (caro, usar cada N epochs).*
- `format_log` (line 1965) `def format_log(self, m)`
- `__init__` (line 2001) `def __init__(self, config, logger)`
- `_measure_ratio` (line 2005) `def _measure_ratio(self, ratio, sample_batch)` - *Mide la coherencia espectral para un ratio dado.
Retorna: varianza del gradiente (menor = mas coherente = mejor).*
- `optimize` (line 2034) `def optimize(self, dataloader)` - *Retorna el mejor ratio de inicializacion de kernels espectrales.*
- `__init__` (line 2074) `def __init__(self, config, logger)`
- `prospect` (line 2078) `def prospect(self, candidates, train_dataset, prospect_steps)` - *Retorna el mejor batch size segun delta y T_eff.*
- `__init__` (line 2157) `def __init__(self, config, logger)`
- `mine` (line 2161) `def mine(self, seed_start, n_seeds, train_dataset, prospect_steps)` - *Retorna la semilla con la mejor trayectoria de delta.*
- `__init__` (line 2243) `def __init__(self, trainer, t0, cooling_rate, stagnation_patience)`
- `refine` (line 2252) `def refine(self, train_dl, val_dl, refine_epochs)` - *Ejecuta refine_epochs epocas de recocido simulado.
Retorna el historial de refinamiento.*
- `__init__` (line 2404) `def __init__(self, config, train_dataset, val_dataset, tokenizer, logger)`
- `_make_dataloaders` (line 2414) `def _make_dataloaders(self, batch_size)`
- `run` (line 2426) `def run(self, run_prospect, refine_epochs, resume, prospect_steps, probe_seeds, seed_start)` - *Ejecuta el pipeline completo.
Retorna el trainer con el modelo entrenado.*
- `ckpt_fn` (line 964) `def ckpt_fn(x_in)`

#### `topogpt2_embeddings_navigator.py`
**Path:** `topogpt2_embeddings_navigator.py`

**Classes:**
- `ThemeTokens` (line 86) `class ThemeTokens` - *Palette and CSS tokens for the navigator.*
- `PlotTheme` (line 103) `class PlotTheme` - *Plot-level theme.*
- `SamplingLimits` (line 118) `class SamplingLimits` - *Safety caps to keep the UI responsive.*
- `MetricsConfig` (line 132) `class MetricsConfig` - *Numerical stability thresholds.*
- `ProjectionConfig` (line 146) `class ProjectionConfig` - *Projection hyperparameters.*
- `NavigatorConfig` (line 156) `class NavigatorConfig` - *Top-level configuration.*
- `StyleInjector` (line 189) `class StyleInjector` - *Injects the navigator's CSS once per session.*
- `CheckpointBundle` (line 263) `class CheckpointBundle` - *Holds a loaded TopoGPT2 model along with its config and tokenizer.*
- `ModelLoader` (line 312) `class ModelLoader` - *Builds a ``CheckpointBundle`` from a checkpoint on disk or in memory.*
- `ActivationCapture` (line 522) `class ActivationCapture` - *Extracts per-layer residual-stream activations via forward hooks.*
- `MetricSuite` (line 600) `class MetricSuite` - *Computes the full geometric and topological metric suite.*
- `Projector` (line 1068) `class Projector` - *Projects point clouds into 2D or 3D with multiple algorithms.*
- `FigureStyler` (line 1195) `class FigureStyler` - *Consistent Plotly styling for every figure.*
- `RenderContext` (line 1243) `class RenderContext` - *Bundle passed to every view during rendering.*
- `BaseEmbeddingView` (line 1255) `class BaseEmbeddingView(ABC)` - *Abstract base for navigator views.*
- `OverviewView` (line 1274) `class OverviewView(BaseEmbeddingView)` - *Token table, per-layer scalar metric evolution, summary panel.*
- `CloudView` (line 1352) `class CloudView(BaseEmbeddingView)` - *Interactive 3D cloud of one layer's residual-stream activations.*
- `MetricsView` (line 1475) `class MetricsView(BaseEmbeddingView)` - *Detailed per-layer metric card for a selected layer.*
- `PersistenceView` (line 1569) `class PersistenceView(BaseEmbeddingView)` - *Persistence diagram and barcode for H0 and H1.*
- `BerryPhaseView` (line 1666) `class BerryPhaseView(BaseEmbeddingView)` - *Berry phase and winding number analysis of the token trajectory.*
- `LipschitzView` (line 1758) `class LipschitzView(BaseEmbeddingView)` - *Local Lipschitz profile and trajectory geometry (speed/curvature/torsion).*
- `NeighborhoodView` (line 1834) `class NeighborhoodView(BaseEmbeddingView)` - *kNN graph and neighborhood statistics.*
- `CrossLayerView` (line 1933) `class CrossLayerView(BaseEmbeddingView)` - *Per-token drift across the residual stream.*
- `QuaternionView` (line 1994) `class QuaternionView(BaseEmbeddingView)` - *Quaternion decomposition of activations (w, x, y, z sub-channels).*
- `RawView` (line 2108) `class RawView(BaseEmbeddingView)` - *Raw activation heatmap (tokens x features).*
- `ViewRegistry` (line 2145) `class ViewRegistry` - *Collects and instantiates views.*
- `SidebarController` (line 2161) `class SidebarController` - *Sidebar inputs (checkpoint, text, kNN, model script path).*
- `ModuleImporter` (line 2217) `class ModuleImporter` - *Imports ``topogpt2_1.py`` from a user-supplied filesystem path.*
- `NavigatorApp` (line 2255) `class NavigatorApp` - *Top-level orchestrator.*

**Methods:**
- `main` (line 2418) `def main()` - *Streamlit script entry point.*
- `__init__` (line 192) `def __init__(self, theme)`
- `inject` (line 195) `def inject(self)` - *Render the CSS block in the current Streamlit page.*
- `__init__` (line 266) `def __init__(self, model, config, tokenizer, source_name)`
- `model` (line 279) `def model(self)` - *Return the underlying nn.Module in eval mode.*
- `config` (line 284) `def config(self)` - *Return the model config object.*
- `tokenizer` (line 289) `def tokenizer(self)` - *Return the BPE tokenizer.*
- `source_name` (line 294) `def source_name(self)` - *Return the original file name of the checkpoint.*
- `device` (line 299) `def device(self)` - *Return the device the model is currently placed on.*
- `num_layers` (line 303) `def num_layers(self)` - *Return the number of transformer layers in the model.*
- `embedding_dim` (line 307) `def embedding_dim(self)` - *Return the model hidden size.*
- `__init__` (line 315) `def __init__(self, config)`
- `load` (line 318) `def load(self, source, topogpt2_module)` - *Load a checkpoint and instantiate the corresponding model.

Args:
    source: Either a filesystem path or a Streamlit UploadedFile.
    topogpt2_module: Already-imported ``topogpt2_1`` module providing
        ``TopoGPT2``, ``TopoGPT2Config``, and ``BPETokenizer``.

Returns:
    A :class:`CheckpointBundle` with model, config, and tokenizer.

Raises:
    ValueError: if the checkpoint extension is not supported or if
        the model config cannot be reconstructed.*
- `_read_state_dict` (line 344) `def _read_state_dict(self, source)`
- `_materialize` (line 366) `def _materialize(self, source)`
- `_extract_payload` (line 374) `def _extract_payload(self, obj)`
- `_build_config` (line 391) `def _build_config(self, topogpt2_module, embedded_cfg, state_dict)`
- `_infer_config` (line 405) `def _infer_config(self, topogpt2_module, state_dict)`
- `_infer_d_model` (line 433) `def _infer_d_model(state_dict)`
- `_infer_num_layers` (line 439) `def _infer_num_layers(state_dict)`
- `_infer_n_heads` (line 450) `def _infer_n_heads(state_dict, d_model)`
- `_infer_max_seq_len` (line 467) `def _infer_max_seq_len(state_dict)`
- `_infer_n_kv_heads` (line 475) `def _infer_n_kv_heads(state_dict, d_head, n_heads)` - *Infer the number of key/value heads for GQA.

In GQA the ``k_proj`` (and ``v_proj``) output dimension equals
``n_kv_heads * d_head``. When the checkpoint was trained with
standard multi-head attention ``n_kv_heads`` equals ``n_heads``.
Passing the explicit value via ``N_KV_HEADS`` avoids the automatic
``N_HEADS // 4`` heuristic in ``TopoGPT2Config`` which would
otherwise produce a shape mismatch at load time.*
- `_infer_torus_grid` (line 505) `def _infer_torus_grid(state_dict)`
- `_validate_load` (line 514) `def _validate_load(missing, unexpected)`
- `__init__` (line 525) `def __init__(self, config)`
- `run` (line 528) `def run(self, bundle, text)` - *Run a single forward pass and return activations and tokens.

Args:
    bundle: The loaded :class:`CheckpointBundle`.
    text: The input text to encode.

Returns:
    A dictionary with keys ``tokens`` (list of decoded pieces),
    ``ids`` (list of token ids), ``embedding`` (initial token
    embeddings), ``layers`` (list of per-layer residual-stream
    activations of shape ``[S, D]``), and ``final`` (the post
    final-norm activations).*
- `_decode_pieces` (line 589) `def _decode_pieces(tokenizer, ids)`
- `__init__` (line 603) `def __init__(self, config)`
- `compute` (line 606) `def compute(self, points, knn)` - *Compute every metric on a point cloud ``[N, D]``.

Args:
    points: Array of shape ``[N, D]`` with ``N >= 4``.
    knn: Number of neighbours for the kNN graph.

Returns:
    Dictionary with scalar and array metrics.*
- `_sanitize` (line 642) `def _sanitize(self, points)`
- `_trivial` (line 645) `def _trivial(self, base)`
- `_pairwise` (line 675) `def _pairwise(self, points)`
- `_shortest_paths` (line 678) `def _shortest_paths(self, points, knn)`
- `_sp_metrics` (line 698) `def _sp_metrics(self, dist_eucl, dist_geo)`
- `_kappa` (line 718) `def _kappa(self, dist_eucl, dist_geo)` - *Local curvature proxy from the chord-vs-arc ratio.

For every point and every nearby pair (a, b) we compare the
Euclidean chord 0.5*(d_E(i,a) + d_E(i,b)) to the geodesic arc
0.5*(d_G(i,a) + d_G(i,b)). When the ratio chord/arc is near 1 the
local neighbourhood is flat; when it is less than 1 the arc bends
outward (spherical-like, positive curvature). The returned scalar
kappa = 1 - (chord/arc)^2, bounded in [0, 1] for positive curvature
and scale-free so it can be compared across layers.*
- `_gromov_delta` (line 759) `def _gromov_delta(self, dist_geo)`
- `_persistence` (line 783) `def _persistence(self, points, dist_eucl)`
- `_h0_from_mst` (line 810) `def _h0_from_mst(self, edges, n)`
- `_h1_from_edges` (line 845) `def _h1_from_edges(self, edges, n)` - *Estimate H1 persistence bars from a distance-sorted edge list.

When an edge is added that does not reduce the number of
connected components, it closes a loop. The birth of that H1
feature is the filtration level at which the loop appears. We
estimate the death as the minimum filtration level at which the
loop is filled in by a 2-simplex in the Vietoris-Rips complex
formed from the same edges. When no such filling appears within
the edge budget, the bar is marked as surviving to the maximum
scale.*
- `_berry_phases` (line 905) `def _berry_phases(self, points)`
- `_winding_numbers` (line 920) `def _winding_numbers(self, points)`
- `_planar_winding` (line 936) `def _planar_winding(self, xs, ys)`
- `_lipschitz` (line 947) `def _lipschitz(self, points)`
- `_trajectory_geometry` (line 954) `def _trajectory_geometry(self, points)` - *Frenet-Serret differential geometry of the token trajectory.

Speed is computed in the full ambient space. Curvature and torsion
are well-defined in 3D, so they are evaluated on the top-3 PCA
projection of the sequence; this preserves geometry while giving a
clean, interpretable scalar per position.*
- `_safe_pca3` (line 1017) `def _safe_pca3(self, points)`
- `_spectral_properties` (line 1030) `def _spectral_properties(self, points)`
- `__init__` (line 1071) `def __init__(self, config)`
- `project` (line 1074) `def project(self, points, method, n_components)` - *Project ``[N, D]`` points to ``n_components`` dims.

Args:
    points: Input point cloud of shape ``[N, D]``.
    method: ``"pca"``, ``"isomap"``, ``"umap"``, ``"random"`` or
        ``"sphere"``.
    n_components: Desired output dimensionality.

Returns:
    Tuple ``(embedding, info)`` where ``info`` contains method
    specific diagnostics (explained variance, etc.).*
- `_pca` (line 1105) `def _pca(self, points, n_components)`
- `_isomap` (line 1123) `def _isomap(self, points, n_components)`
- `_umap` (line 1144) `def _umap(self, points, n_components)`
- `_random` (line 1171) `def _random(self, points, n_components)`
- `_sphere` (line 1181) `def _sphere(self, points, n_components)`
- `__init__` (line 1198) `def __init__(self, config)`
- `style_3d` (line 1201) `def style_3d(self, fig, title, height)` - *Apply 3D styling.*
- `style_2d` (line 1223) `def style_2d(self, fig, title, height)` - *Apply 2D styling.*
- `__init__` (line 1261) `def __init__(self, ctx)`
- `ctx` (line 1265) `def ctx(self)` - *Return the shared render context.*
- `render` (line 1270) `def render(self)` - *Render the view into the current Streamlit container.*
- `render` (line 1280) `def render(self)`
- `_render_tokens` (line 1284) `def _render_tokens(self)`
- `_render_layer_evolution` (line 1310) `def _render_layer_evolution(self)`
- `render` (line 1358) `def render(self)`
- `_choose` (line 1378) `def _choose(self, acts, selection)`
- `_render_trajectory` (line 1386) `def _render_trajectory(self, emb, tokens, ids, norms, stage, method, info)`
- `_render_residual_streams` (line 1442) `def _render_residual_streams(self, acts, method)`
- `render` (line 1481) `def render(self)`
- `_get_metrics` (line 1490) `def _get_metrics(self, stage)`
- `_render_card` (line 1496) `def _render_card(self, m)`
- `_render_kappa` (line 1521) `def _render_kappa(self, m)`
- `_render_path_metrics` (line 1544) `def _render_path_metrics(self, m)`
- `render` (line 1575) `def render(self)`
- `_stage_metrics` (line 1583) `def _stage_metrics(self, stage)`
- `_render_diagram` (line 1591) `def _render_diagram(self, m)`
- `_render_barcode` (line 1633) `def _render_barcode(self, m)`
- `render` (line 1672) `def render(self)`
- `_stage_metrics` (line 1680) `def _stage_metrics(self, stage)`
- `_render_berry` (line 1688) `def _render_berry(self, m, stage)`
- `_render_winding` (line 1720) `def _render_winding(self, m, stage)`
- `render` (line 1764) `def render(self)`
- `_stage_metrics` (line 1772) `def _stage_metrics(self, stage)`
- `_render_lc` (line 1780) `def _render_lc(self, m)`
- `_render_dynamics` (line 1807) `def _render_dynamics(self, m)`
- `render` (line 1840) `def render(self)`
- `_stage_metrics` (line 1849) `def _stage_metrics(self, stage)`
- `_stage_points` (line 1857) `def _stage_points(self, stage)`
- `_render_graph` (line 1864) `def _render_graph(self, points, m)`
- `_render_coherence` (line 1911) `def _render_coherence(self, points)`
- `render` (line 1939) `def render(self)`
- `_cosine_diag` (line 1962) `def _cosine_diag(self, A, B)`
- `_render_heatmap` (line 1968) `def _render_heatmap(self, title, z, xlabels, tokens, diverging)`
- `render` (line 2000) `def render(self)`
- `_points` (line 2021) `def _points(self, stage)`
- `_render_component_norms` (line 2029) `def _render_component_norms(self, comps)`
- `_render_quaternion_norms` (line 2054) `def _render_quaternion_norms(self, comps)`
- `_render_sphere` (line 2070) `def _render_sphere(self, comps)`
- `render` (line 2114) `def render(self)`
- `_points` (line 2136) `def _points(self, stage)`
- `__init__` (line 2148) `def __init__(self, context)`
- `register` (line 2152) `def register(self, factory)` - *Register a view factory.*
- `build` (line 2156) `def build(self)` - *Instantiate every registered view.*
- `__init__` (line 2164) `def __init__(self, config)`
- `render` (line 2167) `def render(self)` - *Render the sidebar and return user selections.*
- `load` (line 2220) `def load(self, path)` - *Dynamically import the TopoGPT2 module.

Args:
    path: Path to ``topogpt2_1.py``.

Returns:
    The imported module object.

Raises:
    FileNotFoundError: if the path does not exist.
    ImportError: if the module cannot be loaded.*
- `__init__` (line 2258) `def __init__(self, config)`
- `run` (line 2269) `def run(self)` - *Entry point for ``streamlit run``.*
- `_render_header` (line 2307) `def _render_header(self)`
- `_render_landing` (line 2324) `def _render_landing(self)`
- `_try_load_bundle` (line 2335) `def _try_load_bundle(self, selections)`
- `_compute_all_metrics` (line 2351) `def _compute_all_metrics(self, activations, knn)`
- `_render_meta` (line 2367) `def _render_meta(self, bundle, activations, knn)`
- `_build_registry` (line 2380) `def _build_registry(self, ctx)`
- `_render_tabs` (line 2394) `def _render_tabs(self, registry)`
- `_render_footer` (line 2408) `def _render_footer(self)`
- `hook` (line 561) `def hook(_module, _inputs, output)`
- `find` (line 818) `def find(x)`
- `union` (line 824) `def union(x, y)`
- `find` (line 864) `def find(x)`
- `union` (line 870) `def union(x, y)`

#### `topogpt2_explorer.py`
**Path:** `topogpt2_explorer.py`

**Classes:**
- `ThemeTokens` (line 59) `class ThemeTokens` - *Design tokens for the explorer's dark scientific theme.*
- `PlotTheme` (line 76) `class PlotTheme` - *Plot-level theme constants.*
- `SamplingLimits` (line 91) `class SamplingLimits` - *Hard caps to keep the UI responsive regardless of model size.*
- `MetricsConfig` (line 108) `class MetricsConfig` - *Numerical stability thresholds for metrics.*
- `GenerationLimits` (line 120) `class GenerationLimits` - *Random-projection and synthetic probe parameters.*
- `ExplorerConfig` (line 129) `class ExplorerConfig` - *Top-level configuration container.*
- `StyleInjector` (line 168) `class StyleInjector` - *Injects the global CSS for the explorer into the Streamlit page.*
- `TensorClassifier` (line 244) `class TensorClassifier` - *Classifies tensor keys from a TopoGPT2 checkpoint by semantic role.

The classifier parses the parameter name and extracts:
  * a coarse role ("attention", "moe_router", "spectral_kernel", etc.)
  * the layer index if present
  * the quaternion component (w, x, y, z) if present
  * whether the tensor represents a frequency-domain kernel*
- `CheckpointLoader` (line 337) `class CheckpointLoader` - *Loads raw tensor dictionaries from disk.

Supports both ``safetensors`` files and plain PyTorch pickles produced
by ``torch.save``. The loader returns CPU float32 tensors exclusively to
guarantee downstream compatibility with NumPy.*
- `TensorInventory` (line 429) `class TensorInventory` - *Holds a checkpoint's tensors along with per-tensor metadata.*
- `TensorProjector` (line 515) `class TensorProjector` - *Projects arbitrary tensors into 2D matrices and 3D point clouds.

Responsibilities:
  * Reduce N-dimensional tensors to a 2D matrix of rows (samples) vs
    columns (features) while preserving interpretability.
  * Subsample rows/columns to respect the configured limits.
  * Compute 3D embeddings (PCA or Gaussian random projection) with
    deterministic seeding.*
- `MetricCalculator` (line 635) `class MetricCalculator` - *Computes mechanistic-interpretability metrics for parameter matrices.

Results are memoized by the ``id`` of the input array to guarantee that
repeated requests for the same subsampled matrix (common across tabs) do
not re-run expensive SVDs.*
- `FigureStyler` (line 836) `class FigureStyler` - *Applies consistent styling to Plotly figures.*
- `VisualizationContext` (line 883) `class VisualizationContext(Protocol)` - *Context passed to visualizers at render time.*
- `RenderContext` (line 894) `class RenderContext` - *Concrete visualization context implementation.*
- `BaseVisualizer` (line 904) `class BaseVisualizer(ABC)` - *Abstract base class for all visualizers.

Subclasses implement :meth:`render` and :meth:`is_applicable`. The registry
will instantiate them only when :meth:`is_applicable` returns ``True``.*
- `OverviewVisualizer` (line 931) `class OverviewVisualizer(BaseVisualizer)` - *Top-level summary of the checkpoint: counts, roles, and inventory table.*
- `TensorExplorerVisualizer` (line 999) `class TensorExplorerVisualizer(BaseVisualizer)` - *Deep-dive into a single tensor: 3D cloud, heatmap, histograms, spectrum.*
- `QuaternionDecompositionVisualizer` (line 1227) `class QuaternionDecompositionVisualizer(BaseVisualizer)` - *Visualize QuaternionLinear layers by their (Ww, Wx, Wy, Wz) components.*
- `SpectralKernelVisualizer` (line 1385) `class SpectralKernelVisualizer(BaseVisualizer)` - *Visualize complex spectral kernels (kr/ki pairs) in the frequency plane.*
- `TorusTopologyVisualizer` (line 1538) `class TorusTopologyVisualizer(BaseVisualizer)` - *3D torus graph of the QuaternionTorusBrain node embeddings and edges.*
- `AttentionVisualizer` (line 1773) `class AttentionVisualizer(BaseVisualizer)` - *Per-layer attention Q/K/V/O projection analysis with per-head split.*
- `MoEVisualizer` (line 1916) `class MoEVisualizer(BaseVisualizer)` - *Router logit landscape and expert weight geometry.*
- `LayerEvolutionVisualizer` (line 2061) `class LayerEvolutionVisualizer(BaseVisualizer)` - *Track how metrics evolve across transformer layers for a chosen role.*
- `GlobalGeometryVisualizer` (line 2151) `class GlobalGeometryVisualizer(BaseVisualizer)` - *Cross-tensor geometry: embed every weight matrix as a 3D point via summary features.*
- `VisualizerRegistry` (line 2291) `class VisualizerRegistry` - *Collects visualizer classes and dispatches to them by label.*
- `SidebarController` (line 2316) `class SidebarController` - *Renders the sidebar controls and returns user selections.*
- `ExplorerApp` (line 2359) `class ExplorerApp` - *Top-level orchestration: composes loader, registry, and layout.*

**Methods:**
- `main` (line 2493) `def main()` - *Streamlit script entry point.*
- `__init__` (line 171) `def __init__(self, theme)`
- `_build_css` (line 174) `def _build_css(self)`
- `inject` (line 239) `def inject(self)` - *Render the CSS block inside the current Streamlit page.*
- `classify` (line 258) `def classify(self, name, shape)` - *Return structured metadata for a checkpoint tensor.

Args:
    name: Full dotted parameter name.
    shape: Tensor shape.

Returns:
    A dictionary with keys ``role``, ``layer``, ``component``,
    ``is_spectral``, ``is_complex_kernel``, ``shape``.*
- `_classify_role` (line 286) `def _classify_role(self, name)`
- `_extract_layer` (line 328) `def _extract_layer(self, name)`
- `_extract_quaternion_component` (line 332) `def _extract_quaternion_component(self, name)`
- `__init__` (line 345) `def __init__(self, config)`
- `load` (line 348) `def load(self, source)` - *Load a checkpoint from a file path or an uploaded file-like.

Args:
    source: Either a path (``str`` or ``Path``) or a Streamlit
        ``UploadedFile`` object.

Returns:
    Dictionary mapping tensor name to CPU ``torch.Tensor``.

Raises:
    ValueError: If the extension is not supported.
    RuntimeError: If deserialization fails.*
- `_materialize` (line 373) `def _materialize(self, source)`
- `_load_safetensors` (line 382) `def _load_safetensors(self, buffer)`
- `_load_torch` (line 389) `def _load_torch(self, buffer)`
- `_extract_state_dict` (line 399) `def _extract_state_dict(self, obj)`
- `_looks_like_state_dict` (line 413) `def _looks_like_state_dict(obj)`
- `_to_cpu_float32` (line 420) `def _to_cpu_float32(tensor)`
- `__init__` (line 432) `def __init__(self, tensors, classifier)`
- `names` (line 443) `def names(self)` - *Return all tensor names sorted alphabetically.*
- `tensor` (line 447) `def tensor(self, name)` - *Retrieve a tensor by name.*
- `meta` (line 451) `def meta(self, name)` - *Retrieve structured metadata for a tensor.*
- `layers` (line 455) `def layers(self)` - *Return all unique layer indices present in the checkpoint.*
- `roles` (line 460) `def roles(self)` - *Return the distinct roles present in the checkpoint.*
- `filter` (line 464) `def filter(self, role, layer, component, spectral_only)` - *Return tensor names matching the supplied filters.*
- `total_parameters` (line 485) `def total_parameters(self)` - *Total parameter count across the checkpoint.*
- `summary_rows` (line 489) `def summary_rows(self)` - *Return a list of per-tensor rows suitable for a Streamlit table.*
- `__init__` (line 526) `def __init__(self, config)`
- `to_matrix` (line 531) `def to_matrix(self, tensor)` - *Convert a tensor to a 2D ``float64`` matrix.

Complex tensors are stacked as ``[real, imag]`` along the feature axis
before flattening, which preserves their dimensionality information.*
- `subsample` (line 553) `def subsample(self, matrix, max_rows, max_cols, seed)` - *Return a row/column subsample bounded by the configured caps.*
- `project_3d` (line 575) `def project_3d(self, matrix, method)` - *Project a matrix to 3D using PCA or Gaussian random projection.

Args:
    matrix: Row-major 2D matrix ``[N, F]``.
    method: Either ``"pca"`` or ``"random"``.

Returns:
    A pair ``(embedding[N, 3], info)`` where ``info`` contains the
    explained variance ratio (PCA) or the Johnson-Lindenstrauss
    ``eps`` used (random projection).*
- `_pca_3d` (line 606) `def _pca_3d(self, matrix)`
- `_random_3d` (line 617) `def _random_3d(self, matrix)`
- `__init__` (line 643) `def __init__(self, config)`
- `compute_all` (line 649) `def compute_all(self, matrix)` - *Compute the full metrics dictionary in one pass.

Uses a lightweight cache keyed by ``(id(matrix), shape)`` so that
recomputation across visualizers is avoided when the same subsampled
matrix is analyzed multiple times in one render cycle.*
- `_svd_safe` (line 681) `def _svd_safe(self, matrix)` - *Compute singular values once, reused by rank and participation ratio.*
- `_effective_rank_from_svd` (line 690) `def _effective_rank_from_svd(self, svd_values, shape)`
- `_participation_from_svd` (line 707) `def _participation_from_svd(self, svd_values, shape)`
- `sparsity` (line 720) `def sparsity(self, matrix, threshold)` - *Fraction of entries whose absolute value is below ``threshold``.*
- `entropy` (line 727) `def entropy(self, matrix)` - *Shannon entropy (nats) of the discrete value histogram.

Uses probability mass (not density), which guarantees a non-negative
result bounded above by ``log(histogram_bins)``. This is the standard
convention for interpretability dashboards.*
- `effective_rank` (line 748) `def effective_rank(self, matrix)` - *Effective rank via the exponential of the entropy of singular values.*
- `participation_ratio` (line 753) `def participation_ratio(self, matrix)` - *Participation ratio of the singular value spectrum.

Defined as ``(sum s)^2 / sum(s^2)`` which equals the effective number
of nonzero singular directions.*
- `fractal_dimension` (line 762) `def fractal_dimension(self, matrix)` - *Approximate the effective embedding dimension via PCA.

Counts the number of principal components whose explained variance
exceeds ``default_fractal_variance_floor``.*
- `coherence` (line 781) `def coherence(self, matrix)` - *Maximum and mean absolute cosine similarity between rows.*
- `spectral_flatness` (line 796) `def spectral_flatness(self, matrix)` - *Spectral flatness (Wiener entropy) in dB averaged over rows.*
- `dominant_frequency` (line 814) `def dominant_frequency(self, matrix)` - *Index of the dominant non-zero frequency bin of row 0.*
- `_subsample_for_svd` (line 824) `def _subsample_for_svd(self, matrix)`
- `_subsample_for_pca` (line 830) `def _subsample_for_pca(self, matrix)`
- `__init__` (line 839) `def __init__(self, config)`
- `style_3d` (line 842) `def style_3d(self, fig, title)` - *Apply the standard 3D scene styling.*
- `style_2d` (line 864) `def style_2d(self, fig, title, height)` - *Apply the standard 2D figure styling.*
- `__init__` (line 914) `def __init__(self, context)`
- `ctx` (line 918) `def ctx(self)` - *Return the render context bound to this visualizer.*
- `is_applicable` (line 922) `def is_applicable(self)` - *Return ``True`` if there is data in the inventory to render.*
- `render` (line 927) `def render(self)` - *Render the visualizer into the current Streamlit container.*
- `render` (line 937) `def render(self)`
- `_render_headline` (line 950) `def _render_headline(self, total_params, num_tensors, num_layers)`
- `_render_role_breakdown` (line 957) `def _render_role_breakdown(self, role_counts, role_params)`
- `_render_inventory_table` (line 984) `def _render_inventory_table(self, rows)`
- `render` (line 1005) `def render(self)`
- `_render_meta` (line 1042) `def _render_meta(self, meta)`
- `_render_metric_grid` (line 1050) `def _render_metric_grid(self, metrics)`
- `_render_point_cloud` (line 1069) `def _render_point_cloud(self, matrix, name, method)`
- `_render_heatmap` (line 1103) `def _render_heatmap(self, matrix, name)`
- `_render_distribution` (line 1125) `def _render_distribution(self, matrix, name)`
- `_render_spectrum` (line 1149) `def _render_spectrum(self, matrix, name)`
- `_render_singular_spectrum` (line 1180) `def _render_singular_spectrum(self, matrix, name)`
- `is_applicable` (line 1233) `def is_applicable(self)`
- `render` (line 1237) `def render(self)`
- `_group_quaternion_bundles` (line 1249) `def _group_quaternion_bundles(self)`
- `_quaternion_bundle_key` (line 1263) `def _quaternion_bundle_key(name, component)`
- `_render_component_stats` (line 1278) `def _render_component_stats(self, components)`
- `_render_component_heatmaps` (line 1290) `def _render_component_heatmaps(self, components)`
- `_render_component_spectra` (line 1315) `def _render_component_spectra(self, components)`
- `_render_unit_norm_distribution` (line 1346) `def _render_unit_norm_distribution(self, components)`
- `is_applicable` (line 1391) `def is_applicable(self)`
- `render` (line 1397) `def render(self)`
- `_pair_kr_ki` (line 1413) `def _pair_kr_ki(self)`
- `_reshape_to_2d` (line 1428) `def _reshape_to_2d(self, magnitude, phase)`
- `_render_magnitude_phase` (line 1439) `def _render_magnitude_phase(self, magnitude, phase, key)`
- `_render_complex_scatter` (line 1470) `def _render_complex_scatter(self, complex_kernel, key)`
- `_render_radial_profile` (line 1504) `def _render_radial_profile(self, magnitude, key)`
- `is_applicable` (line 1544) `def is_applicable(self)`
- `render` (line 1547) `def render(self)`
- `_infer_grid` (line 1568) `def _infer_grid(self, n_nodes)`
- `_render_headline_metrics` (line 1578) `def _render_headline_metrics(self, nodes, edges, radial_bins, angular_bins)`
- `_render_3d_torus` (line 1591) `def _render_3d_torus(self, nodes, edges, radial_bins, angular_bins)`
- `_torus_positions` (line 1605) `def _torus_positions(self, nodes, radial_bins, angular_bins)`
- `_add_edges` (line 1631) `def _add_edges(self, fig, positions, radial_bins, angular_bins, edges)`
- `_edge_label` (line 1669) `def _edge_label(edge_type)`
- `_build_segments` (line 1678) `def _build_segments(positions, radial_bins, angular_bins)`
- `_add_nodes` (line 1697) `def _add_nodes(self, fig, positions, node_colors, n_nodes)`
- `_render_node_correlation` (line 1725) `def _render_node_correlation(self, nodes)`
- `_render_edge_quaternions` (line 1747) `def _render_edge_quaternions(self, edges)`
- `is_applicable` (line 1779) `def is_applicable(self)`
- `render` (line 1785) `def render(self)`
- `_infer_head_count` (line 1813) `def _infer_head_count(self, matrix, proj)`
- `_render_per_head_norms` (line 1822) `def _render_per_head_norms(self, matrix, proj)`
- `_render_per_head_spectrum` (line 1849) `def _render_per_head_spectrum(self, matrix, proj, layer)`
- `_render_head_similarity` (line 1881) `def _render_head_similarity(self, matrix, proj, layer)`
- `_render_summary_metrics` (line 1908) `def _render_summary_metrics(self, metrics)`
- `is_applicable` (line 1922) `def is_applicable(self)`
- `render` (line 1927) `def render(self)`
- `_render_router_norms` (line 1949) `def _render_router_norms(self, router, layer)`
- `_render_routing_probe` (line 1972) `def _render_routing_probe(self, router, layer)`
- `_render_expert_similarity` (line 2015) `def _render_expert_similarity(self, layer)`
- `_softmax` (line 2055) `def _softmax(logits)`
- `is_applicable` (line 2067) `def is_applicable(self)`
- `render` (line 2070) `def render(self)`
- `_render_metric_grid` (line 2113) `def _render_metric_grid(self, role, layers, series)`
- `render` (line 2157) `def render(self)`
- `_render_scatter` (line 2204) `def _render_scatter(self, emb, labels, roles, sizes, pca)`
- `_render_feature_correlation` (line 2246) `def _render_feature_correlation(self, X_std, example)`
- `_build_palette` (line 2279) `def _build_palette(n)`
- `__init__` (line 2294) `def __init__(self, context)`
- `register` (line 2298) `def register(self, factory)` - *Register a visualizer factory.

Args:
    factory: Callable producing a :class:`BaseVisualizer` instance
        given the shared render context.*
- `build` (line 2307) `def build(self)` - *Instantiate all registered visualizers.*
- `applicable` (line 2311) `def applicable(self)` - *Return the subset of visualizers whose data is present.*
- `__init__` (line 2319) `def __init__(self, config)`
- `render` (line 2322) `def render(self)` - *Render the sidebar and return the current selections.*
- `__init__` (line 2362) `def __init__(self, config)`
- `run` (line 2372) `def run(self)` - *Entry point used by ``streamlit run``.*
- `_configure_page` (line 2394) `def _configure_page(self)`
- `_render_header` (line 2401) `def _render_header(self)`
- `_render_landing` (line 2416) `def _render_landing(self)`
- `_resolve_checkpoint` (line 2437) `def _resolve_checkpoint(self, selections)`
- `_build_registry` (line 2452) `def _build_registry(self, context)`
- `_render_tabs` (line 2465) `def _render_tabs(self, registry)`
- `_render_footer` (line 2483) `def _render_footer(self)`

#### `topogpt2_grid_scaler.py`
**Path:** `topogpt2_grid_scaler.py`

**Classes:**
- `InterpolationConfig` (line 97) `class InterpolationConfig` - *Controls the spectral weight interpolation.*
- `ValidationConfig` (line 108) `class ValidationConfig` - *What to measure after each scaling step.*
- `ProgressiveConfig` (line 121) `class ProgressiveConfig` - *Multi-hop scaling strategy.*
- `OutputConfig` (line 131) `class OutputConfig` - *Output files.*
- `TopoScalerConfig` (line 141) `class TopoScalerConfig` - *Top-level configuration — mirrors scaler_config_128.toml.*
- `ModuleImporter` (line 181) `class ModuleImporter` - *Dynamically imports topogpt2_1.py from any path.*
- `CheckpointReader` (line 205) `class CheckpointReader` - *Reads a TopoGPT2 checkpoint and any embedded config.*
- `ConfigReconstructor` (line 242) `class ConfigReconstructor` - *Reconstructs TopoGPT2Config from weights, inferring all dimensions.*
- `TensorRole` (line 328) `class TensorRole` - *Classifies every state-dict key by its D_MODEL scaling role.*
- `SpectralInterpolator` (line 380) `class SpectralInterpolator` - *Interpolates weight tensors via Fourier-space zero-padding or cropping.

This is the core of the technique — identical in principle to the
Willmore Crystal scaler's Fourier interpolation of spectral kernels,
adapted to weight matrices of arbitrary shape.*
- `StateScaler` (line 483) `class StateScaler` - *Scales every tensor in a state dict from src_d to tgt_d.

Routing table:
  topo_graph   → verbatim copy
  edge_quat    → verbatim copy
  rope         → rebuilt from scratch for new D_HEAD
  spectral_2d  → interpolate channel dims (D_q axes); topo dims verbatim
  spectral_1d  → interpolate 1D frequency axis (D//2+1 → D'//2+1)
  node_embed   → interpolate feature axis (D → D')
  quat_linear  → 2D spectral interpolation [out_q, in_q] → [out_q', in_q']
  matrix       → 2D spectral interpolation on D-dependent axes
  vector       → 1D spectral interpolation
  scalar       → verbatim copy*
- `ScalingValidator` (line 635) `class ScalingValidator` - *Measures spectral structure preservation before and after scaling.*
- `ModelAssembler` (line 723) `class ModelAssembler` - *Loads scaled weights into a fresh TopoGPT2.*
- `CheckpointSaver` (line 751) `class CheckpointSaver` - *Saves checkpoint, metrics JSON, and text report.*
- `TopoGPT2DModelScaler` (line 860) `class TopoGPT2DModelScaler` - *Main orchestrator.

Mirrors the Willmore Crystal scaler pipeline:

  source_grid_size = D_MODEL_src
  target_grid_sizes = [D1, D2, ...]  (progressive)

The torus topology is the structural invariant: RADIAL, ANGULAR,
N_TORUS_NODES, edges_i/j/type, edge_quat are never modified.*

**Methods:**
- `_setup_logger` (line 169) `def _setup_logger(name, level)`
- `build_parser` (line 1070) `def build_parser()`
- `config_from_args` (line 1097) `def config_from_args(args)`
- `main` (line 1119) `def main()`
- `__post_init__` (line 159) `def __post_init__(self)`
- `load` (line 184) `def load(self, path)` - *Import and return the topogpt2 module.*
- `read` (line 208) `def read(self, path, device)` - *Return (state_dict, optional_embedded_config).*
- `_extract` (line 225) `def _extract(self, obj)`
- `reconstruct` (line 245) `def reconstruct(self, mod, state_dict, embedded)` - *Return a TopoGPT2Config that matches the loaded weights exactly.*
- `_infer` (line 259) `def _infer(self, mod, sd)`
- `_infer_d_head` (line 291) `def _infer_d_head(sd)`
- `_infer_n_kv` (line 298) `def _infer_n_kv(sd, d_head, n_heads)`
- `_infer_max_seq` (line 308) `def _infer_max_seq(sd)`
- `_infer_torus` (line 315) `def _infer_torus(sd)`
- `classify` (line 340) `def classify(self, key, shape)` - *Return a semantic role string.

Roles:
  topo_graph    — graph index buffers (topology invariant, verbatim)
  edge_quat     — learned edge quaternions (topology invariant, verbatim)
  rope          — RoPE cache (rebuilt for new D_HEAD)
  spectral_2d   — 2D quaternion spectral kernels [D_q, D_q, R, Af]
  spectral_1d   — 1D spectral AE filters [D//2+1]
  node_embed    — torus node embeddings [N_NODES, D]
  quat_linear   — QuaternionLinear component weights [out_q, in_q]
  matrix        — any other 2D weight [M, N] where both dims scale with D
  vector        — any 1D parameter [D] (norms, biases)
  scalar        — 0D parameter (temperature)
  verbatim      — anything not classified above*
- `__init__` (line 388) `def __init__(self, cfg)`
- `interpolate_2d` (line 391) `def interpolate_2d(self, W, tgt_rows, tgt_cols)` - *Scale a 2D weight matrix [M, N] to [M', N'] via spectral interpolation.

Steps:
  1. FFT2 of W.
  2. Zero-pad or centre-crop frequency spectrum to (M', N').
  3. IFFT2.
  4. Amplitude normalisation: ||W'||_F = ||W||_F.*
- `interpolate_1d` (line 421) `def interpolate_1d(self, v, tgt_len)` - *Scale a 1D vector of length L to length L' via spectral interpolation.*
- `_resize_spectrum_2d` (line 452) `def _resize_spectrum_2d(self, W_f, tgt_rows, tgt_cols)` - *Zero-pad or centre-crop a 2D complex spectrum.*
- `__init__` (line 499) `def __init__(self, interp, role_clf, logger)`
- `scale` (line 509) `def scale(self, src_state, src_cfg, tgt_cfg, mod)` - *Produce a complete scaled state dict.*
- `_dispatch` (line 567) `def _dispatch(self, src, tgt_shape, role, key)` - *Route to the correct interpolation method based on shape and role.*
- `_scale_spectral_2d_to` (line 598) `def _scale_spectral_2d_to(self, t, tgt_shape, key)` - *Scale [in_q, out_q, R, Af] to [in_q', out_q', R, Af].

R and Af are topo-invariant and must not change.*
- `_bilinear_fallback` (line 626) `def _bilinear_fallback(self, src, tgt_shape)`
- `__init__` (line 638) `def __init__(self, cfg)`
- `compute` (line 641) `def compute(self, state, d_model)` - *Compute all configured validation metrics.*
- `check_degradation` (line 656) `def check_degradation(self, before, after, logger)` - *Return True if any metric dropped beyond its tolerance.*
- `_spectral_concentration` (line 690) `def _spectral_concentration(self, sd)`
- `_phase_coherence` (line 708) `def _phase_coherence(self, sd)`
- `assemble` (line 726) `def assemble(self, mod, tgt_cfg, scaled_state, logger)` - *Instantiate the target model and load scaled weights.*
- `save` (line 754) `def save(self, model, tgt_cfg, src_cfg, metrics_before, metrics_after, out_cfg, step_tag, logger)` - *Persist scaled checkpoint and metadata. Returns checkpoint path.*
- `_write_report` (line 815) `def _write_report(self, path, src_cfg, tgt_cfg, before, after, ckpt)`
- `__init__` (line 872) `def __init__(self, cfg)`
- `run` (line 888) `def run(self)` - *Execute the full scaling pipeline. Returns per-step result dicts.*
- `_build_target_config` (line 1001) `def _build_target_config(self, mod, src_cfg, tgt_d)` - *Construct a target config with new D_MODEL, preserving torus topology.*
- `_infer_n_heads` (line 1018) `def _infer_n_heads(tgt_d, src_n_heads)` - *Find the largest divisor of tgt_d that keeps D_HEAD >= 8.*
- `_infer_n_kv_heads` (line 1033) `def _infer_n_kv_heads(tgt_d, tgt_n_heads, src_n_heads, src_n_kv)`
- `_print_summary` (line 1047) `def _print_summary(self, results, src_cfg)`
- `_cfg_dict` (line 770) `def _cfg_dict(c)`

#### `topogpt2_multi_inference.py`
**Path:** `topogpt2_multi_inference.py`

**Classes:**
- `SamplingConfig` (line 60) `class SamplingConfig` - *Generation hyper-parameters.*
- `RunConfig` (line 72) `class RunConfig` - *Top-level execution configuration.*
- `ModuleImporter` (line 95) `class ModuleImporter` - *Imports topogpt2_1.py from any filesystem path (cached per process).*
- `CheckpointDiscovery` (line 122) `class CheckpointDiscovery` - *Resolves a mixed list of files and directories to concrete checkpoint paths.*
- `CheckpointLoader` (line 164) `class CheckpointLoader` - *Loads state dicts and any embedded config from checkpoint files.*
- `ConfigReconstructor` (line 219) `class ConfigReconstructor` - *Reconstructs a TopoGPT2Config from weights, inferring every dimension.*
- `TokenizerFactory` (line 315) `class TokenizerFactory` - *Builds and caches BPETokenizer instances.*
- `GenerationEngine` (line 327) `class GenerationEngine` - *Autoregressive generation with top-k, top-p, and repetition penalty.*
- `ModelResult` (line 433) `class ModelResult` - *Result from running one checkpoint.*
- `MultiInferenceRunner` (line 450) `class MultiInferenceRunner` - *Runs one prompt through every checkpoint and collects results.*
- `ResultRenderer` (line 584) `class ResultRenderer` - *Formats and prints inference results.*
- `JsonExporter` (line 677) `class JsonExporter` - *Saves results to a JSON file for later analysis.*

**Methods:**
- `_setup_logger` (line 85) `def _setup_logger(name, level)`
- `_fmt_params` (line 666) `def _fmt_params(n)` - *Format parameter counts as human-readable strings (25.1M, 147.5M).*
- `build_parser` (line 707) `def build_parser()` - *Build the CLI argument parser.*
- `config_from_args` (line 780) `def config_from_args(args)` - *Build a RunConfig from parsed CLI arguments.*
- `main` (line 800) `def main()` - *CLI entry point.*
- `load` (line 100) `def load(self, path)` - *Return the imported module, reusing the cached copy if available.*
- `resolve` (line 127) `def resolve(self, sources)` - *Expand directories and glob patterns into a sorted list of paths.

Args:
    sources: File paths, directory paths, or glob patterns.

Returns:
    Deduplicated, sorted list of existing checkpoint paths.*
- `load` (line 167) `def load(self, path, device)` - *Return (state_dict, optional_embedded_config).

Handles:
  - .safetensors (raw state dict)
  - .pt / .pth with {'model_state_dict': ..., 'config': ...}
    (produced by the scaler)
  - .pt / .pth plain state dicts*
- `_load_safetensors` (line 183) `def _load_safetensors(self, path, device)`
- `_load_torch` (line 191) `def _load_torch(self, path, device)`
- `reconstruct` (line 222) `def reconstruct(self, mod, state_dict, embedded)` - *Return a TopoGPT2Config matching the loaded weights.

Prefers the embedded config (saved by the scaler) but falls back
to full inference from tensor shapes so that original checkpoints
work without any embedded metadata.*
- `_infer` (line 243) `def _infer(self, mod, sd)`
- `_infer_d_head` (line 278) `def _infer_d_head(sd)`
- `_infer_n_kv` (line 285) `def _infer_n_kv(sd, d_head, n_heads)`
- `_infer_max_seq` (line 295) `def _infer_max_seq(sd)`
- `_infer_torus` (line 302) `def _infer_torus(sd)`
- `get` (line 320) `def get(self, mod)` - *Return a shared tokenizer instance (built once per process).*
- `__init__` (line 330) `def __init__(self, cfg, device)`
- `generate` (line 334) `def generate(self, model, tokenizer, prompt)` - *Run generation and return (full_text, n_new_tokens, elapsed_s).

Uses the model's built-in .generate() when repetition_penalty == 1.0
and top_p == 1.0, otherwise falls back to a manual loop that supports
the full sampling configuration.*
- `_fast_generate` (line 361) `def _fast_generate(self, model, input_ids)`
- `_manual_generate` (line 372) `def _manual_generate(self, model, input_ids)`
- `_apply_repetition_penalty` (line 412) `def _apply_repetition_penalty(logits, generated, penalty)`
- `_apply_top_p` (line 424) `def _apply_top_p(logits, p)`
- `__init__` (line 453) `def __init__(self, cfg)`
- `run` (line 462) `def run(self)` - *Execute the full multi-model inference pipeline.*
- `_run_one` (line 499) `def _run_one(self, ckpt_path, mod, tokenizer, engine)`
- `_make_label` (line 570) `def _make_label(path)` - *Extract a short human-readable label from a checkpoint path.*
- `render` (line 590) `def render(self, results, prompt)` - *Print prompt header, per-model outputs, and comparison table.*
- `_print_prompt_header` (line 597) `def _print_prompt_header(self, prompt)`
- `_print_model_output` (line 605) `def _print_model_output(self, r)`
- `_print_comparison_table` (line 628) `def _print_comparison_table(self, results)`
- `export` (line 680) `def export(self, results, path, prompt)` - *Serialize results to JSON.*

#### `zeroshot.py`
**Path:** `zeroshot.py`

**Classes:**
- `ExpansionConfig` (line 87) `class ExpansionConfig` - *All tuneable knobs for the zero-shot expansion procedure.

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
    How to interpolate node embeddings: 'bilinear' or 'nearest'.*
- `TopoGPT2Config` (line 169) `class TopoGPT2Config` - *Minimal reproduction of the model-architecture fields from the original
TopoGPT2Config.  Only the fields required to instantiate the neural
network are present here.*
- `QuaternionOps` (line 254) `class QuaternionOps` - *Static quaternion algebra operations in PyTorch.*
- `QuaternionLinear` (line 287) `class QuaternionLinear(Module)` - *Quaternion-valued linear layer.

Performs the Hamilton product W ⊗ x in the quaternion algebra,
using four real weight matrices (one per quaternion component).
Both in_features and out_features must be divisible by 4.*
- `QuaternionSpectralLayer` (line 321) `class QuaternionSpectralLayer(Module)` - *2D spectral convolution with quaternion Hamilton product in frequency domain.

Kernel tensors are registered for each quaternion component (w, x, y, z),
each with separate real and imaginary parts for the complex frequency domain.*
- `SpectralAutoencoder` (line 373) `class SpectralAutoencoder(Module)` - *Spectral autoencoder operating in both 1D (feature axis) and 2D (torus grid).

Encodes via FFT filtering and quaternion projection to a latent space;
decodes back for reconstruction regularisation.  Also exposes a method
for processing the torus grid through stacked QuaternionSpectralLayers.*
- `QuaternionTorusBrain` (line 427) `class QuaternionTorusBrain(Module)` - *Replaces the MLP in each transformer layer.

Vectorised pipeline:
    1. Flatten [B, S, D] -> [BS, D]
    2. SpectralAutoencoder (1D filter + quaternion projection)
    3. Project to torus angles (phi1, phi2)
    4. Soft-assign each token to N_NODES via circular distances
    5. Build node grid [BS, N_NODES, D]
    6. QuaternionSpectralLayer 2D on the torus grid
    7. Quaternion message-passing on the torus graph
    8. Readout: weighted sum over nodes -> [BS, D]
    9. Reshape to [B, S, D]*
- `SwiGLU` (line 534) `class SwiGLU(Module)` - *SwiGLU feed-forward block (LLaMA-style).
inner dimension = round(d_model * expansion) up to multiple of 4.*
- `TopoMoEBrain` (line 556) `class TopoMoEBrain(Module)` - *Mixture-of-Experts wrapper around QuaternionTorusBrain.

One always-active shared expert (QuaternionTorusBrain) plus N_EXPERTS
sparse SwiGLU experts selected by a linear router (top-K per token).
When MOE_ENABLED is False this reduces to a plain QuaternionTorusBrain.*
- `RotaryEmbedding` (line 613) `class RotaryEmbedding(Module)` - *Rotary Position Embeddings (RoPE) – Su et al., 2021.*
- `RMSNorm` (line 652) `class RMSNorm(Module)` - *Root Mean Square Layer Normalization (no bias).*
- `MultiHeadAttention` (line 665) `class MultiHeadAttention(Module)` - *Multi-head attention with Flash Attention, RoPE, and Grouped Query Attention.
Supports an optional KV cache for autoregressive generation.*
- `TopoGPT2Layer` (line 719) `class TopoGPT2Layer(Module)` - *Single transformer layer: pre-norm attention + pre-norm TopoMoEBrain.
Gradient checkpointing is disabled during inference/expansion.*
- `TopoGPT2` (line 749) `class TopoGPT2(Module)` - *TopoGPT2: causal language model with quaternion torus topology.

Embedding -> N_LAYERS x (Attention + QuaternionTorusBrain) -> RMSNorm -> LM head.
The embedding and LM head share weights (weight tying).*
- `SpectralKernelInterpolator` (line 828) `class SpectralKernelInterpolator` - *Interpolates QuaternionSpectralLayer kernels to a new (grid_h, grid_w).

The kernels live in frequency space with shape [in_q, out_q, freq_h, freq_w]
where freq_w = grid_w // 2 + 1.  We treat (freq_h, freq_w) as a 2D spatial
grid and apply torch.nn.functional.interpolate.*
- `NodeEmbedInterpolator` (line 876) `class NodeEmbedInterpolator` - *Interpolates the torus node embedding table to a new (n_radial, n_angular).

node_embed has shape [n_nodes, d_model] = [n_radial * n_angular, d_model].
We reshape to a 2D spatial grid [n_radial, n_angular, d_model], transpose
to [d_model, n_radial, n_angular], interpolate per feature dimension, then
reshape back.*
- `TorusBrainExpander` (line 917) `class TorusBrainExpander` - *Transfers weights from a source QuaternionTorusBrain to a target one with
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
readout                            : copy verbatim (pointwise MLP)*
- `TopoMoEBrainExpander` (line 1009) `class TopoMoEBrainExpander` - *Transfers weights from a source TopoMoEBrain to a target one.

The shared QuaternionTorusBrain is expanded via TorusBrainExpander.
All SwiGLU expert weights and the router are copied verbatim (they do not
depend on torus resolution – they process flat token embeddings).*
- `TopoGPT2Expander` (line 1052) `class TopoGPT2Expander` - *Zero-shot torus expansion of a complete TopoGPT2 model.

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
per-layer: topo_brain -> shared_expert (QuaternionTorusBrain)*
- `CheckpointIO` (line 1120) `class CheckpointIO` - *Loads and saves TopoGPT2 weights using safetensors.
Falls back to torch.save / torch.load when safetensors is unavailable.*
- `CheckpointArch` (line 1216) `class CheckpointArch` - *Architecture hyperparameters inferred directly from checkpoint tensor shapes.

All fields that affect tensor dimensions are recovered so that the source
model can be instantiated to exactly match the saved weights, regardless of
what the CLI scale preset would compute.*
- `CheckpointArchProber` (line 1239) `class CheckpointArchProber` - *Infers all architecture hyperparameters from the raw tensor shapes stored
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
                  shape [n_freq]  where n_freq = d_model // 2 + 1*
- `ExpansionValidator` (line 1463) `class ExpansionValidator` - *Runs a forward-pass sanity check on the expanded model.

Checks:
- The model produces finite logits for a random token sequence.
- The model produces finite logits for the given text prompt (if tiktoken
  is available).
- The model can generate a short sequence without crashing.*
- `ZeroShotExpansionPipeline` (line 1550) `class ZeroShotExpansionPipeline` - *Orchestrates the full zero-shot expansion workflow:

1. Read source torus geometry from checkpoint metadata (or config defaults).
2. Build source and target TopoGPT2 configs.
3. Instantiate source and target models.
4. Load source weights into the source model.
5. Expand weights via TopoGPT2Expander.
6. Optionally validate the expanded model.
7. Save the expanded model.

No training is performed at any stage.*

**Functions:**
- `build_logger` (line 69) `def build_logger(name, level)` - *Return a stderr logger with timestamp formatting.*

**Methods:**
- `build_arg_parser` (line 1709) `def build_arg_parser()` - *Construct and return the CLI argument parser.*
- `main` (line 1774) `def main()` - *CLI entry point.*
- `validate_geometry` (line 140) `def validate_geometry(self)` - *Raise ValueError for impossible torus configurations.*
- `src_nodes` (line 154) `def src_nodes(self)`
- `tgt_nodes` (line 158) `def tgt_nodes(self)`
- `__post_init__` (line 222) `def __post_init__(self)`
- `hamilton_product` (line 258) `def hamilton_product(q1, q2)`
- `normalize` (line 269) `def normalize(q, eps)`
- `conjugate` (line 273) `def conjugate(q)`
- `rotate_vector` (line 278) `def rotate_vector(v, q)`
- `__init__` (line 296) `def __init__(self, in_features, out_features, bias)`
- `forward` (line 310) `def forward(self, x)`
- `__init__` (line 329) `def __init__(self, in_q, out_q, grid_h, grid_w, init_scale)`
- `_kernel` (line 344) `def _kernel(self, c)`
- `_contract` (line 347) `def _contract(self, W, X)`
- `forward` (line 350) `def forward(self, x)`
- `__init__` (line 382) `def __init__(self, config)`
- `_filter1d` (line 404) `def _filter1d(self, x, kr, ki)`
- `encode` (line 409) `def encode(self, x)`
- `decode` (line 412) `def decode(self, z)`
- `forward` (line 415) `def forward(self, x)`
- `process_torus_grid` (line 420) `def process_torus_grid(self, grid)`
- `__init__` (line 443) `def __init__(self, d_model, config)`
- `_build_torus_graph` (line 468) `def _build_torus_graph(self)`
- `_torus_soft_assign` (line 484) `def _torus_soft_assign(self, phi1, phi2)`
- `_message_passing` (line 495) `def _message_passing(self, node_feat)`
- `forward` (line 509) `def forward(self, x)`
- `__init__` (line 540) `def __init__(self, d_model, expansion, dropout)`
- `forward` (line 552) `def forward(self, x)`
- `__init__` (line 565) `def __init__(self, d_model, config)`
- `_route` (line 581) `def _route(self, x)`
- `forward` (line 604) `def forward(self, x)`
- `__init__` (line 618) `def __init__(self, d_head, max_seq_len)`
- `_build_cache` (line 626) `def _build_cache(self, seq_len)`
- `_rotate_half` (line 633) `def _rotate_half(x)`
- `forward` (line 637) `def forward(self, q, k, seq_len, offset)`
- `__init__` (line 655) `def __init__(self, d_model, eps)`
- `forward` (line 660) `def forward(self, x)`
- `__init__` (line 671) `def __init__(self, d_model, n_heads, config)`
- `forward` (line 686) `def forward(self, x, is_causal, past_kv)`
- `__init__` (line 725) `def __init__(self, d_model, n_heads, config)`
- `_forward_impl` (line 734) `def _forward_impl(self, x, past_kv)`
- `forward` (line 743) `def forward(self, x, past_kv)`
- `__init__` (line 757) `def __init__(self, config)`
- `_init_weights` (line 771) `def _init_weights(self)`
- `forward` (line 778) `def forward(self, token_ids, past_kvs)`
- `generate` (line 795) `def generate(self, token_ids, max_new_tokens, temperature, top_k)` - *Top-k autoregressive generation with KV cache.*
- `__init__` (line 837) `def __init__(self, mode)`
- `_interp2d` (line 840) `def _interp2d(self, tensor, tgt_h, tgt_w)` - *Interpolate a 4D real tensor [in_q, out_q, h, w] to [in_q, out_q, tgt_h, tgt_w].*
- `transfer` (line 856) `def transfer(self, src_layer, tgt_layer)` - *Copy and interpolate all kernel parameters from src_layer to tgt_layer.*
- `__init__` (line 886) `def __init__(self, mode)`
- `transfer` (line 889) `def transfer(self, src_embed, src_radial, src_angular, tgt_embed, tgt_radial, tgt_angular)` - *Interpolate src_embed [src_R*src_A, D] into tgt_embed [tgt_R*tgt_A, D].*
- `__init__` (line 936) `def __init__(self, spec_interp_mode, node_interp_mode, logger)`
- `expand` (line 946) `def expand(self, src, tgt)` - *Mutates tgt in-place to carry the expanded weights of src.*
- `__init__` (line 1018) `def __init__(self, spec_interp_mode, node_interp_mode, logger)`
- `expand` (line 1031) `def expand(self, src, tgt)` - *Mutates tgt in-place.*
- `__init__` (line 1072) `def __init__(self, spec_interp_mode, node_interp_mode, logger)`
- `expand` (line 1085) `def expand(self, src, tgt)` - *Expand src into tgt.  Returns tgt with all weights transferred.
tgt must have already been instantiated with the target config.*
- `__init__` (line 1126) `def __init__(self, logger)`
- `load` (line 1133) `def load(self, path, model, device)` - *Load weights into model from path.  Returns the metadata dict.
Supports: .safetensors, .pt, .pth (state_dict or wrapped dict).

Weight tying: checkpoints saved by this script omit lm_head.weight
(it is redundant with token_embed.weight).  After loading, the tie is
restored by pointing lm_head.weight at token_embed.weight.*
- `save` (line 1177) `def save(self, path, model, metadata)` - *Save model weights to path.

Weight tying: token_embed.weight and lm_head.weight share the same
storage tensor.  safetensors rejects aliased tensors with a RuntimeError.
We exclude lm_head.weight from the state dict before saving (it is
redundant) and record the tie in metadata so load() can restore it.*
- `__init__` (line 1286) `def __init__(self, logger)`
- `_load_shapes` (line 1289) `def _load_shapes(self, path)` - *Return {key: shape} for every tensor in the checkpoint.*
- `_load_metadata` (line 1304) `def _load_metadata(self, path)` - *Return safetensors string metadata dict (empty when unavailable).*
- `probe` (line 1315) `def probe(self, path, fallback_radial, fallback_angular)` - *Infer CheckpointArch from the checkpoint at path.

Parameters
----------
path            : checkpoint file path
fallback_radial : used only when torus_spectral key is absent
fallback_angular: used only when torus_spectral key is absent*
- `_infer_d_head_fallback` (line 1433) `def _infer_d_head_fallback(d_model, q_out, k_out)` - *Fallback d_head inference when rope.inv_freq is absent.

d_head must divide both q_out and d_model, and n_heads % n_kv_heads == 0.
Returns the largest valid candidate (most heads, smallest d_head is wrong
intuition; we pick the value that makes n_kv_heads a proper divisor of n_heads
and n_heads a standard power-of-2 count).*
- `__init__` (line 1474) `def __init__(self, logger)`
- `validate` (line 1477) `def validate(self, model, prompt)` - *Return True if all checks pass, False otherwise.
Does not raise; errors are logged as warnings.*
- `__init__` (line 1565) `def __init__(self, exp_cfg, logger)`
- `_config_from_arch` (line 1570) `def _config_from_arch(self, arch, torus_radial, torus_angular)` - *Build a TopoGPT2Config whose tensor dimensions exactly match arch.

The scale preset is applied first (to get sane defaults for fields not
covered by arch), then every field that affects tensor shapes is
overwritten with the probed value.  This guarantees that the
instantiated model accepts the checkpoint weights without size mismatches.*
- `_build_metadata_for_save` (line 1609) `def _build_metadata_for_save(self, src_meta, arch, tgt_radial, tgt_angular)`
- `run` (line 1631) `def run(self)` - *Execute the full expansion pipeline.  Returns the expanded model.*

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
