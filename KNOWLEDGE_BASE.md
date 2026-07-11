# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis.

**Total Files Parsed:** 12 | **Total Symbols Extracted:** 1020 | **Total Imports:** 211

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray: 5 5,color:#aaa;
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
    app_py_TopoGPT2Config["TopoGPT2Config"]
    class app_py_TopoGPT2Config cls;
    app_py --> app_py_TopoGPT2Config
    app_py_setup_logger["setup_logger"]
    class app_py_setup_logger fn;
    app_py --> app_py_setup_logger
    app_py_set_seed["set_seed"]
    class app_py_set_seed fn;
    app_py --> app_py_set_seed
    app_py_QuaternionOps["QuaternionOps"]
    class app_py_QuaternionOps cls;
    app_py --> app_py_QuaternionOps
    app_py_QuaternionLinear["QuaternionLinear"]
    class app_py_QuaternionLinear cls;
    app_py --> app_py_QuaternionLinear
    topogpt2_1_py["topogpt2_1.py (py)"]
    class topogpt2_1_py mod;
    topogpt2_1_py_TopoGPT2Config["TopoGPT2Config"]
    class topogpt2_1_py_TopoGPT2Config cls;
    topogpt2_1_py --> topogpt2_1_py_TopoGPT2Config
    topogpt2_1_py_setup_logger["setup_logger"]
    class topogpt2_1_py_setup_logger fn;
    topogpt2_1_py --> topogpt2_1_py_setup_logger
    topogpt2_1_py_set_seed["set_seed"]
    class topogpt2_1_py_set_seed fn;
    topogpt2_1_py --> topogpt2_1_py_set_seed
    topogpt2_1_py_QuaternionOps["QuaternionOps"]
    class topogpt2_1_py_QuaternionOps cls;
    topogpt2_1_py --> topogpt2_1_py_QuaternionOps
    topogpt2_1_py_QuaternionLinear["QuaternionLinear"]
    class topogpt2_1_py_QuaternionLinear cls;
    topogpt2_1_py --> topogpt2_1_py_QuaternionLinear
    topogpt2_grid_scaler_py["topogpt2_grid_scaler.py (py)"]
    class topogpt2_grid_scaler_py mod;
    topogpt2_grid_scaler_py_InterpolationConfig["InterpolationConfig"]
    class topogpt2_grid_scaler_py_InterpolationConfig cls;
    topogpt2_grid_scaler_py --> topogpt2_grid_scaler_py_InterpolationConfig
    topogpt2_grid_scaler_py_ValidationConfig["ValidationConfig"]
    class topogpt2_grid_scaler_py_ValidationConfig cls;
    topogpt2_grid_scaler_py --> topogpt2_grid_scaler_py_ValidationConfig
    topogpt2_grid_scaler_py_ProgressiveConfig["ProgressiveConfig"]
    class topogpt2_grid_scaler_py_ProgressiveConfig cls;
    topogpt2_grid_scaler_py --> topogpt2_grid_scaler_py_ProgressiveConfig
    topogpt2_grid_scaler_py_OutputConfig["OutputConfig"]
    class topogpt2_grid_scaler_py_OutputConfig cls;
    topogpt2_grid_scaler_py --> topogpt2_grid_scaler_py_OutputConfig
    topogpt2_grid_scaler_py_TopoScalerConfig["TopoScalerConfig"]
    class topogpt2_grid_scaler_py_TopoScalerConfig cls;
    topogpt2_grid_scaler_py --> topogpt2_grid_scaler_py_TopoScalerConfig
    topogpt2_explorer_py["topogpt2_explorer.py (py)"]
    class topogpt2_explorer_py mod;
    topogpt2_explorer_py_ThemeTokens["ThemeTokens"]
    class topogpt2_explorer_py_ThemeTokens cls;
    topogpt2_explorer_py --> topogpt2_explorer_py_ThemeTokens
    topogpt2_explorer_py_PlotTheme["PlotTheme"]
    class topogpt2_explorer_py_PlotTheme cls;
    topogpt2_explorer_py --> topogpt2_explorer_py_PlotTheme
    topogpt2_explorer_py_SamplingLimits["SamplingLimits"]
    class topogpt2_explorer_py_SamplingLimits cls;
    topogpt2_explorer_py --> topogpt2_explorer_py_SamplingLimits
    topogpt2_explorer_py_MetricsConfig["MetricsConfig"]
    class topogpt2_explorer_py_MetricsConfig cls;
    topogpt2_explorer_py --> topogpt2_explorer_py_MetricsConfig
    topogpt2_explorer_py_GenerationLimits["GenerationLimits"]
    class topogpt2_explorer_py_GenerationLimits cls;
    topogpt2_explorer_py --> topogpt2_explorer_py_GenerationLimits
    quantize_py["quantize.py (py)"]
    class quantize_py mod;
    quantize_py_InferenceConfig["InferenceConfig"]
    class quantize_py_InferenceConfig cls;
    quantize_py --> quantize_py_InferenceConfig
    quantize_py_CheckpointInspector["CheckpointInspector"]
    class quantize_py_CheckpointInspector cls;
    quantize_py --> quantize_py_CheckpointInspector
    quantize_py_QuaternionOps["QuaternionOps"]
    class quantize_py_QuaternionOps cls;
    quantize_py --> quantize_py_QuaternionOps
    quantize_py_QuaternionLinear["QuaternionLinear"]
    class quantize_py_QuaternionLinear cls;
    quantize_py --> quantize_py_QuaternionLinear
    quantize_py_QuaternionSpectralLayer["QuaternionSpectralLayer"]
    class quantize_py_QuaternionSpectralLayer cls;
    quantize_py --> quantize_py_QuaternionSpectralLayer
    zeroshot_py["zeroshot.py (py)"]
    class zeroshot_py mod;
    zeroshot_py_build_logger["build_logger"]
    class zeroshot_py_build_logger fn;
    zeroshot_py --> zeroshot_py_build_logger
    zeroshot_py_ExpansionConfig["ExpansionConfig"]
    class zeroshot_py_ExpansionConfig cls;
    zeroshot_py --> zeroshot_py_ExpansionConfig
    zeroshot_py_TopoGPT2Config["TopoGPT2Config"]
    class zeroshot_py_TopoGPT2Config cls;
    zeroshot_py --> zeroshot_py_TopoGPT2Config
    zeroshot_py_QuaternionOps["QuaternionOps"]
    class zeroshot_py_QuaternionOps cls;
    zeroshot_py --> zeroshot_py_QuaternionOps
    zeroshot_py_QuaternionLinear["QuaternionLinear"]
    class zeroshot_py_QuaternionLinear cls;
    zeroshot_py --> zeroshot_py_QuaternionLinear
    topogpt2_multi_inference_py["topogpt2_multi_inference.py (py)"]
    class topogpt2_multi_inference_py mod;
    topogpt2_multi_inference_py_SamplingConfig["SamplingConfig"]
    class topogpt2_multi_inference_py_SamplingConfig cls;
    topogpt2_multi_inference_py --> topogpt2_multi_inference_py_SamplingConfig
    topogpt2_multi_inference_py_RunConfig["RunConfig"]
    class topogpt2_multi_inference_py_RunConfig cls;
    topogpt2_multi_inference_py --> topogpt2_multi_inference_py_RunConfig
    topogpt2_multi_inference_py__setup_logger["_setup_logger"]
    class topogpt2_multi_inference_py__setup_logger fn;
    topogpt2_multi_inference_py --> topogpt2_multi_inference_py__setup_logger
    topogpt2_multi_inference_py_ModuleImporter["ModuleImporter"]
    class topogpt2_multi_inference_py_ModuleImporter cls;
    topogpt2_multi_inference_py --> topogpt2_multi_inference_py_ModuleImporter
    topogpt2_multi_inference_py_CheckpointDiscovery["CheckpointDiscovery"]
    class topogpt2_multi_inference_py_CheckpointDiscovery cls;
    topogpt2_multi_inference_py --> topogpt2_multi_inference_py_CheckpointDiscovery
    reinforce_py["reinforce.py (py)"]
    class reinforce_py mod;
    reinforce_py_RLConfig["RLConfig"]
    class reinforce_py_RLConfig cls;
    reinforce_py --> reinforce_py_RLConfig
    reinforce_py_RewardSignalType["RewardSignalType"]
    class reinforce_py_RewardSignalType cls;
    reinforce_py --> reinforce_py_RewardSignalType
    reinforce_py_CheckpointPatcher["CheckpointPatcher"]
    class reinforce_py_CheckpointPatcher cls;
    reinforce_py --> reinforce_py_CheckpointPatcher
    reinforce_py_MechanisticRewardCalculator["MechanisticRewardCalculator"]
    class reinforce_py_MechanisticRewardCalculator cls;
    reinforce_py --> reinforce_py_MechanisticRewardCalculator
    reinforce_py_RewardModel["RewardModel"]
    class reinforce_py_RewardModel cls;
    reinforce_py --> reinforce_py_RewardModel
    inference2_py["inference2.py (py)"]
    class inference2_py mod;
    inference2_py_build_logger["build_logger"]
    class inference2_py_build_logger fn;
    inference2_py --> inference2_py_build_logger
    inference2_py_InferenceConfig["InferenceConfig"]
    class inference2_py_InferenceConfig cls;
    inference2_py --> inference2_py_InferenceConfig
    inference2_py_BPETokenizer["BPETokenizer"]
    class inference2_py_BPETokenizer cls;
    inference2_py --> inference2_py_BPETokenizer
    inference2_py_QuaternionOps["QuaternionOps"]
    class inference2_py_QuaternionOps cls;
    inference2_py --> inference2_py_QuaternionOps
    inference2_py_QuaternionLinear["QuaternionLinear"]
    class inference2_py_QuaternionLinear cls;
    inference2_py --> inference2_py_QuaternionLinear
    inference_py["inference.py (py)"]
    class inference_py mod;
    inference_py__load_source_module["_load_source_module"]
    class inference_py__load_source_module fn;
    inference_py --> inference_py__load_source_module
    inference_py_InferenceConfig["InferenceConfig"]
    class inference_py_InferenceConfig cls;
    inference_py --> inference_py_InferenceConfig
    inference_py_CheckpointInspector["CheckpointInspector"]
    class inference_py_CheckpointInspector cls;
    inference_py --> inference_py_CheckpointInspector
    inference_py_ModelLoader["ModelLoader"]
    class inference_py_ModelLoader cls;
    inference_py --> inference_py_ModelLoader
    inference_py_GenerationEngine["GenerationEngine"]
    class inference_py_GenerationEngine cls;
    inference_py --> inference_py_GenerationEngine
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

## Architecture Reference

### PY (11 files)

#### `app.py`
**Path:** `app.py`

**Classs:**
- `TopoGPT2Config` (line 55) - *Configuración completa para TopoGPT2.*
- `QuaternionOps` (line 177) - *Operaciones de cuaterniones puras en PyTorch.
Representación: [..., 4]  donde last dim = [w, x, y, z]
q = w + x*i + y*j + z*k*
- `QuaternionLinear` (line 216) - *Capa lineal con pesos cuaterniones.

Implementa la multiplicación W * x en el álgebra de cuaterniones:
- W = Ww + Wx*i + Wy*j + Wz*k  (cuaternión de pesos)
- x = xw + xx*i + xy*j + xz*k  (cuaternión de entrada)
- out = W * x  (producto de Hamilton extendido a vectores)

Parámetros: 4 matrices reales de forma [out_q, in_q]*
- `QuaternionSpectralLayer` (line 261) - *Convolución espectral 2D con cuaterniones y producto de Hamilton completo.

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
- `SpectralAutoencoder` (line 348) - *Autoencoder espectral con cuaterniones.

Opera en dos niveles:
1. Espectral 1D sobre el vector de features (FFT sobre dim D_MODEL):
   captura la espectrografía global del embedding.
2. Espectral 2D sobre el grid del toro (QuaternionSpectralLayer):
   captura correlaciones espaciales en la topología.

Devuelve (latent, recon_loss) para regularización.*
- `QuaternionTorusBrain` (line 431) - *Reemplaza el MLP en cada capa del transformer.

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
- `RotaryEmbedding` (line 648) - *Rotary Position Embeddings (RoPE) - Su et al., 2021.
Codifica la posición como rotaciones del espacio de atención,
naturalmente relativas y sin parámetros extra.*
- `RMSNorm` (line 696) - *Root Mean Square Layer Normalization (sin bias). Más estable que LayerNorm.*
- `SwiGLU` (line 713) - *SwiGLU: SiLU(gate(x)) * up(x) -> down
Usado en LLaMA 2/3, Qwen, Mistral en lugar de GELU-FFN.
Dimension interna: 8/3 * d_model (convención LLaMA, redondeada a múltiplo de 4).*
- `TopoMoEBrain` (line 742) - *Mixture of Experts sobre la capa topologica.

Arquitectura (inspirada en DeepSeek-MoE / Mixtral):
  - 1 experto compartido: QuaternionTorusBrain (siempre activo)
  - N_EXPERTS expertos SwiGLU ligeros (activacion esparsa: Top-K por token)
  - Router: Linear(D, N_EXPERTS) + softmax → top-K

Load-balancing loss (auxiliar): penaliza si un experto acapara todos los tokens.
Activa MOE_TOP_K de N_EXPERTS expertos por token.

Sin MoE (MOE_ENABLED=False): se comporta como QuaternionTorusBrain puro.*
- `MultiHeadAttention` (line 847) - *Multi-head attention con:
- Flash Attention (scaled_dot_product_attention de PyTorch 2.0+)
- Rotary Position Embeddings (RoPE)
- GQA (Grouped Query Attention): N_KV_HEADS < N_HEADS, reduce VRAM de K/V
- KV Cache para inferencia autoregresiva eficiente
- Temperatura termodinámica aprendible*
- `TopoGPT2Layer` (line 929) - *Capa del transformer con TopoMoEBrain (TopoBrain + MoE SwiGLU experts).

Esquema pre-norm (estilo LLaMA):
    x = x + Attention_GQA(RMSNorm(x))
    x = x + TopoMoEBrain(RMSNorm(x))*
- `TopoGPT2` (line 976) - *TopoGPT2: Transformer de lenguaje con TopoBrain cuaternión-espectral.

Arquitectura:
    Embedding de tokens + RoPE (en Attention)
    N_LAYERS × TopoGPT2Layer (Attention + QuaternionTorusBrain)
    RMSNorm final
    Proyección a vocabulario (weight-tied con embeddings)*
- `BPETokenizer` (line 1082) - *Wrapper alrededor de tiktoken (GPT-2 compatible).*
- `CorpusDownloader` (line 1107) - *Descarga corpus de texto para entrenamiento.

Soporta:
- 'tinystories': ~2GB de cuentos cortos (ideal para pruebas)
- 'wikitext103': ~500MB de Wikipedia curada
- 'file': archivo de texto local

Usa HuggingFace 'datasets' para TinyStories y WikiText.*
- `TokenizedDataset` (line 1170) - *Dataset de tokens para language modeling (next-token prediction).

Guarda los tokens tokenizados en disco la primera vez (cache .pt)
para evitar re-tokenizar en cada ejecucion. La clave de cache incluye
un hash del contenido del corpus + tokenizador + max_tokens.*
- `CheckpointManager` (line 1220) - *Gestiona checkpoints de forma acumulativa y segura.

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
- `TopoGPT2Trainer` (line 1453) - *Entrenador acumulativo y resumible.

Caracteristicas:
- Checkpoint automatico en safetensors cada N minutos + cada epoch
- Historial acumulativo entre sesiones (--resume agrega al historial existente)
- Guarda el mejor modelo en checkpoints/best/ automaticamente
- LR schedule: cosine con warmup relativo a los steps de ESTA sesion
- Mixed Precision (AMP) + acumulacion de gradientes*
- `MechanisticMetrics` (line 1746) - *Calcula todas las metricas del diagrama de fases de Book.md.

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
- `Phase0_KernelOptimizer` (line 1983) - *Encuentra el ratio imaginario/real optimo para los kernels espectrales.

Analogia con main.py: evalua la transicion GOE→GUE en el espacio
de kernels. Un ratio optimo promueve estructura topologica (insulador)
vs estructura amorfa (vidrio).

Metodo: calibra con un mini-batch y mide la varianza del gradiente
en funcion del ratio. Ratios que minimizan la varianza de gradiente
(maxima coherencia espectral) son preferibles.

No entrena: solo inicializa los kernels con distintos ratios y mide.
Tiempo tipico: < 30 segundos.*
- `Phase1_BatchProspector` (line 2058) - *Encuentra el batch size optimo testando candidatos con pocos pasos.

De main.py: el batch size regula la temperatura del horno de cristalizacion.
Batch sizes demasiado chicos -> ruido excesivo (vidrio frio).
Batch sizes demasiado grandes -> sin presion annealing (amorfos).
La ventana optima empirica de main.py: [24, 128] para Strassen.

Para LM, testeamos candidatos midiendo:
- delta (δ): velocidad de descenso en prospect_steps pasos
- T_eff: temperatura efectiva del gradiente

Tiempo tipico: < 2 minutos para 3 candidatos × 30 pasos.*
- `Phase2_SeedMiner` (line 2141) - *Encuentra semillas prometedoras midiendo la trayectoria de delta.

De main.py: una semilla "buena" muestra delta descendente en los
primeros N pasos (enfriamiento). Una semilla "mala" se estanca en
el plateau vidrioso (~0.49).

Criterio de seleccion:
1. Semillas con delta_velocity < 0 (enfriando) AND kappa bajo.
2. Si no hay, semillas solo enfriando.
3. Fallback: semilla con menor delta final.

Tiempo tipico: < 3 minutos para 5 semillas × 50 pasos.*
- `Phase4_AnnealingRefiner` (line 2223) - *Refinamiento post-entrenamiento mediante recocido simulado.

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
- `TopoPhasePipeline` (line 2384) - *Orquesta las 5 fases de entrenamiento segun main.py + Book.md.

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

**Functions:**
- `setup_logger` (line 155)
- `set_seed` (line 165)
- `main` (line 2506)
- `__post_init__` (line 124)
- `hamilton_product` (line 185) - *Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].*
- `normalize` (line 197)
- `conjugate` (line 201)
- `rotate_vector` (line 206) - *Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]*
- `__init__` (line 228)
- `forward` (line 244) - *x: [..., in_features] → [..., out_features]*
- `__init__` (line 281)
- `_kernel` (line 300)
- `_contract` (line 303) - *Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]*
- `forward` (line 307) - *x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)
→ [B, 4*out_q, H, W]*
- `__init__` (line 361)
- `_filter1d` (line 393) - *Filtro espectral 1D: x[..., D] → filtrado[..., D]*
- `encode` (line 399) - *x: [..., D_MODEL] → latent: [..., D_LAT]*
- `decode` (line 404) - *z: [..., D_LAT] → recon: [..., D_MODEL]*
- `forward` (line 409) - *Devuelve (latent, recon_loss)*
- `process_torus_grid` (line 416) - *Procesa el grid del toro con QuaternionSpectralLayer.
grid: [B, 4*D_QUAT, RADIAL, ANGULAR]  →  [B, 4*D_QUAT, RADIAL, ANGULAR]*
- `__init__` (line 449)
- `_build_torus_graph` (line 489) - *Construye las aristas del grafo toro 2×4.

Nodos indexados como: node = r * N_ANGULAR + a
  r ∈ [0, RADIAL-1], a ∈ [0, ANGULAR-1]

Aristas angulares: nodo ↔ nodo a la izquierda/derecha (periódico)
Aristas radiales:  nodo ↔ nodo del anillo interior/exterior*
- `_torus_soft_assign` (line 523) - *Asignación blanda de tokens a los 8 nodos del toro via distancia circular.

phi1: [BS] ángulo angular ∈ [-π, π]
phi2: [BS] ángulo radial ∈ [-π, π]
→ weights: [BS, N_NODES]  (suma a 1, softmax de distancias negativas)*
- `_message_passing` (line 550) - *Message-passing VECTORIZADO con rotaciones cuaterniones.
Sin bucles Python: todas las aristas se procesan en paralelo.

node_feat: [BS, N_NODES, D_MODEL]
→ [BS, N_NODES, D_MODEL]*
- `forward` (line 587) - *x: [B, S, D_MODEL]
→ output: [B, S, D_MODEL], recon_loss: scalar*
- `__init__` (line 655)
- `_build_cache` (line 661)
- `_rotate_half` (line 668)
- `forward` (line 672) - *q, k: [B, n_heads, S_q/S_k, d_head]
offset: posicion inicial (para KV cache: longitud del cache existente)
Aplica posiciones [offset .. offset+S-1] a q y k.*
- `__init__` (line 699)
- `forward` (line 704)
- `__init__` (line 720)
- `forward` (line 734)
- `__init__` (line 757)
- `_route` (line 778) - *x: [N, D] donde N = B*S (tokens aplanados)
Retorna:
expert_out: [N, D]  suma ponderada de top-K expertos
aux_loss:   escalar  load-balancing loss
Routing vectorizado sin boolean indexing ni sincronizacion CUDA.
Usa dispatch por indices agrupados (estilo Mixtral/DeepSeek) para
compatibilidad total con torch.utils.checkpoint.*
- `forward` (line 820) - *x: [B, S, D]
→ output: [B, S, D], aux_loss: escalar*
- `__init__` (line 857)
- `forward` (line 875) - *Args:
    x:        [B, S, D]
    is_causal: usar mascara causal
    past_kv:  (K_cache, V_cache) de pasos anteriores o None
Returns:
    out:      [B, S, D]
    kv_cache: (K, V) completos para cachear en generate()*
- `__init__` (line 938)
- `_forward_impl` (line 947)
- `forward` (line 956) - *Retorna (x_out, aux_loss, kv_cache).
Con gradient checkpointing en training (solo cuando no hay KV cache).*
- `__init__` (line 987)
- `_init_weights` (line 1006)
- `forward` (line 1013) - *token_ids: [B, S]  (enteros)
past_kvs:  lista de (K, V) por capa, o None para entrenamiento
→ logits: [B, S, VOCAB_SIZE], aux_loss: scalar, new_kvs: list[(K,V)]*
- `count_params` (line 1036)
- `generate` (line 1042) - *Generacion autoregresiva con KV cache y muestreo top-k.
En el primer paso procesa el prompt completo y guarda el cache.
En pasos siguientes solo procesa 1 token nuevo (O(n) en lugar de O(n^2)).*
- `__init__` (line 1085)
- `encode` (line 1093)
- `decode` (line 1096)
- `eot_token` (line 1099)
- `__init__` (line 1119)
- `get_text` (line 1125) - *Devuelve el texto del corpus. Descarga si es necesario.*
- `_download_hf` (line 1150)
- `__init__` (line 1179)
- `__len__` (line 1206)
- `__getitem__` (line 1209)
- `__init__` (line 1245)
- `patch_config_for_resume` (line 1255) - *Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS
para que coincidan con la arquitectura guardada.
Necesario cuando el codigo cambio GQA despues de guardar el checkpoint.*
- `_save_model` (line 1284)
- `_load_model` (line 1297)
- `_save_optimizer` (line 1328)
- `_load_optimizer` (line 1331)
- `_save_state` (line 1340)
- `_load_state` (line 1345)
- `should_save` (line 1356)
- `save` (line 1359) - *Guarda checkpoint completo.

state debe contener al menos: completed_epochs, global_step,
best_val_loss, history, config.*
- `load_latest` (line 1404) - *Carga el ultimo checkpoint guardado.
Devuelve el state dict (vacio si no hay checkpoint).*
- `load_best` (line 1431) - *Carga el mejor modelo guardado (solo pesos, sin optimizador).*
- `has_checkpoint` (line 1443)
- `__init__` (line 1465)
- `resume` (line 1500) - *Carga el ultimo checkpoint disponible.
Restaura: pesos del modelo, estado del optimizador, historial acumulado,
epoch/step completados y mejor val_loss.
Devuelve True si se cargo un checkpoint, False si empieza de cero.*
- `_current_state` (line 1525) - *Construye el dict de estado para persistir en state.json.*
- `_cosine_lr` (line 1536) - *Cosine decay con warmup. El schedule es relativo a la sesion actual.*
- `_set_lr` (line 1544)
- `train` (line 1548) - *Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.
El historial se acumula sobre sesiones previas.*
- `_sample_text` (line 1684) - *Genera una muestra de texto al final de cada epoch para monitorear
la calidad cualitativa del modelo (detecta degeneracion, repeticion, etc.).*
- `evaluate` (line 1716)
- `__init__` (line 1766)
- `compute_delta` (line 1774)
- `compute_alpha` (line 1781)
- `update_grad_buffer` (line 1786) - *Captura gradientes de forma segura, ignorando tensores corruptos.*
- `compute_t_eff` (line 1812) - *T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva.*
- `compute_kappa` (line 1820) - *κ = λ_max / λ_min de la covarianza del gradiente.
Parámetro de orden para cristalización (κ≈1 = cristal).
Nota: requiere pasadas backward adicionales. Se ejecuta con protección
para no corromper el estado AMP del trainer principal.*
- `compute_berry_phase` (line 1878) - *Fase de Berry de los kernels espectrales imaginarios.
Surge de los parametros ki_w, ki_x, ki_y, ki_z de QuaternionSpectralLayer.
|berry|>pi/2 con winding!=0 indica estructura topologica.*
- `compute_lc` (line 1891) - *Complejidad local: 1 - similitud coseno promedio entre filas de pesos.*
- `compute_sp` (line 1905) - *Superposicion: correlacion inter-fila promedio (entrelazamiento de features).*
- `classify_phase` (line 1921) - *Clasificacion de fase segun Book.md:

discrete_crystal:       delta<0.05, kappa<1.5
topological_insulator:  |berry|>pi/2, winding!=0
cold_glass:             kappa>>1, delta>0.3
functional_glass:       intermedio (lo mas comun en LM)*
- `compute_all` (line 1940) - *Calcula todas las metricas.
compute_kappa=True hace pasadas backward adicionales (caro, usar cada N epochs).*
- `format_log` (line 1965)
- `__init__` (line 2001)
- `_measure_ratio` (line 2005) - *Mide la coherencia espectral para un ratio dado.
Retorna: varianza del gradiente (menor = mas coherente = mejor).*
- `optimize` (line 2034) - *Retorna el mejor ratio de inicializacion de kernels espectrales.*
- `__init__` (line 2074)
- `prospect` (line 2078) - *Retorna el mejor batch size segun delta y T_eff.*
- `__init__` (line 2157)
- `mine` (line 2161) - *Retorna la semilla con la mejor trayectoria de delta.*
- `__init__` (line 2243)
- `refine` (line 2252) - *Ejecuta refine_epochs epocas de recocido simulado.
Retorna el historial de refinamiento.*
- `__init__` (line 2404)
- `_make_dataloaders` (line 2414)
- `run` (line 2426) - *Ejecuta el pipeline completo.
Retorna el trainer con el modelo entrenado.*
- `ckpt_fn` (line 964)

#### `inference.py`
**Path:** `inference.py`

**Classs:**
- `InferenceConfig` (line 28) - *Parametric configuration container for inference execution.*
- `CheckpointInspector` (line 45) - *Reads safetensors metadata to align architecture configuration.*
- `ModelLoader` (line 90) - *Loads weights from safetensors and binds to the architectural graph.*
- `GenerationEngine` (line 115) - *Handles autoregressive token generation with controlled sampling.*
- `InferenceRunner` (line 140) - *Orchestrates execution flow for prompt processing.*

**Functions:**
- `_load_source_module` (line 19)
- `parse_arguments` (line 178)
- `__init__` (line 47)
- `inspect_kq_head_count` (line 50)
- `patch_config` (line 62)
- `_resolve_preset` (line 81)
- `__init__` (line 92)
- `load_model` (line 96)
- `__init__` (line 117)
- `generate` (line 121)
- `sample_logits` (line 132)
- `__init__` (line 142)
- `_setup_logger` (line 146)
- `run` (line 155)
- `_print_result` (line 170)

#### `inference2.py`
**Path:** `inference2.py`

**Classs:**
- `InferenceConfig` (line 97) - *All tuneable knobs for the inference pipeline.

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
- `BPETokenizer` (line 170) - *Thin wrapper around tiktoken with GPT-2 encoding.*
- `QuaternionOps` (line 196) - *Static quaternion algebra operations.*
- `QuaternionLinear` (line 219) - *Linear layer in the quaternion algebra.

Implements the Hamilton product W ⊗ x using four real weight matrices.
Both in_features and out_features must be divisible by 4.*
- `QuaternionSpectralLayer` (line 252) - *2-D spectral convolution using the quaternion Hamilton product in the
frequency domain.  Each quaternion component (w, x, y, z) has an
independent complex kernel (real + imaginary parts).*
- `SpectralAutoencoder` (line 306) - *Spectral autoencoder: 1-D FFT filtering + quaternion projection for
encoding/decoding, plus stacked QuaternionSpectralLayers for the torus grid.*
- `QuaternionTorusBrain` (line 358) - *Replaces the MLP in each transformer layer.

Fully vectorised pipeline:
    [B, S, D] -> spectral AE -> torus projection -> soft node assignment
    -> 2-D spectral layer on grid -> quaternion message-passing -> readout
    -> [B, S, D]*
- `SwiGLU` (line 462) - *SwiGLU feed-forward block (LLaMA-style).*
- `TopoMoEBrain` (line 481) - *Mixture-of-Experts wrapper: one always-active QuaternionTorusBrain plus
N sparse SwiGLU experts selected by a linear router (top-K per token).
When moe_enabled is False this reduces to a plain QuaternionTorusBrain.*
- `RotaryEmbedding` (line 537) - *Rotary Position Embeddings (RoPE) – Su et al., 2021.*
- `RMSNorm` (line 577) - *Root Mean Square Layer Normalization (no bias).*
- `MultiHeadAttention` (line 589) - *GQA-capable multi-head attention with Flash Attention, RoPE, and KV cache.*
- `TopoGPT2Layer` (line 638) - *Pre-norm transformer layer: attention + TopoMoEBrain.*
- `TopoGPT2` (line 660) - *TopoGPT2: causal language model with quaternion torus topology.
Embedding -> N layers (Attention + QuaternionTorusBrain) -> RMSNorm -> LM head.*
- `ModelConfig` (line 700) - *All architectural hyperparameters required to instantiate TopoGPT2.
Populated entirely from the probed checkpoint shapes.*
- `CheckpointArchProber` (line 735) - *Infers all ModelConfig fields directly from checkpoint tensor shapes,
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
- `CheckpointLoader` (line 890) - *Loads a safetensors or pickle checkpoint into a TopoGPT2 instance.
Restores weight tying after loading.*
- `Sampler` (line 943) - *Stateless token sampling with temperature, top-k, top-p, and
repetition penalty.  All operations are performed on the logit tensor
returned by the model before softmax.*
- `GenerationEngine` (line 1003) - *Autoregressive generation with KV cache and optional token streaming.

First forward pass processes the full prompt and seeds the KV cache.
Subsequent passes process a single token each, giving O(n) complexity.*
- `ResultPrinter` (line 1082) - *Formats and writes generation results to stdout.*
- `InferencePipeline` (line 1116) - *Orchestrates the full inference workflow.

1. Validate config.
2. Probe checkpoint architecture.
3. Instantiate model.
4. Load weights.
5. Run generation in the requested mode.*

**Functions:**
- `build_logger` (line 79) - *Stderr logger with timestamp formatting.*
- `build_arg_parser` (line 1217) - *Construct and return the CLI argument parser.*
- `main` (line 1288) - *CLI entry point.*
- `validate` (line 148) - *Raise ValueError for impossible parameter combinations.*
- `__init__` (line 175)
- `encode` (line 182)
- `decode` (line 185)
- `decode_single` (line 188)
- `hamilton_product` (line 200)
- `normalize` (line 211)
- `conjugate` (line 215)
- `__init__` (line 227)
- `forward` (line 241)
- `__init__` (line 259)
- `_kernel` (line 276)
- `_contract` (line 279)
- `forward` (line 282)
- `__init__` (line 312)
- `_filter1d` (line 334)
- `encode` (line 341)
- `decode` (line 344)
- `forward` (line 347)
- `process_torus_grid` (line 351)
- `__init__` (line 370)
- `_build_torus_graph` (line 395)
- `_torus_soft_assign` (line 411)
- `_message_passing` (line 423)
- `forward` (line 437)
- `__init__` (line 465)
- `forward` (line 475)
- `__init__` (line 488)
- `_route` (line 503)
- `forward` (line 528)
- `__init__` (line 542)
- `_build_cache` (line 550)
- `_rotate_half` (line 557)
- `forward` (line 561)
- `__init__` (line 580)
- `forward` (line 585)
- `__init__` (line 594)
- `forward` (line 609)
- `__init__` (line 641)
- `forward` (line 649)
- `__init__` (line 666)
- `forward` (line 678)
- `d_quat` (line 723)
- `gqa_groups` (line 727)
- `__init__` (line 768)
- `_load_shapes` (line 771)
- `probe` (line 786) - *Return a ModelConfig whose dimensions exactly match the checkpoint.*
- `_fallback_d_head` (line 871)
- `__init__` (line 896)
- `load` (line 899) - *Load weights into model in-place.*
- `__init__` (line 950)
- `__call__` (line 953) - *Sample one token from logits.

Parameters
----------
logits       : [vocab_size] raw logits for the next token position.
generated_ids: token IDs already generated (for repetition penalty).

Returns
-------
Sampled token id.*
- `__init__` (line 1013)
- `generate` (line 1027) - *Generate text from prompt.

Returns
-------
(generated_text, tokens_per_second)
generated_text includes the prompt prefix.*
- `_maybe_stream` (line 1071)
- `print_single` (line 1087)
- `print_benchmark` (line 1100)
- `__init__` (line 1127)
- `_build_model` (line 1131)
- `run` (line 1149)
- `_run_single` (line 1164)
- `_run_interactive` (line 1176)
- `_run_benchmark` (line 1199)

#### `quantize.py`
**Path:** `quantize.py`

**Classs:**
- `InferenceConfig` (line 34) - *Centralized configuration for quantized inference. All parameters are explicitly defined.*
- `CheckpointInspector` (line 105) - *Inspects checkpoint state dict to dynamically resolve architecture parameters.*
- `QuaternionOps` (line 162) - *Pure quaternion operations in PyTorch. Representation: [..., 4] -> [w, x, y, z].*
- `QuaternionLinear` (line 195)
- `QuaternionSpectralLayer` (line 220)
- `SpectralAutoencoder` (line 262)
- `QuaternionTorusBrain` (line 312)
- `RotaryEmbedding` (line 408)
- `RMSNorm` (line 440)
- `SwiGLU` (line 451)
- `TopoMoEBrain` (line 468)
- `MultiHeadAttention` (line 522)
- `TopoGPT2Layer` (line 568)
- `TopoGPT2` (line 590)
- `BPETokenizer` (line 651)
- `QuantizationFormat` (line 668)
- `IQuantizer` (line 678)
- `BitNetQuantizer` (line 692)
- `INT4Quantizer` (line 721)
- `INT8Quantizer` (line 746)
- `Float16Quantizer` (line 760)
- `BFloat16Quantizer` (line 774)
- `Float32Quantizer` (line 788)
- `Float64Quantizer` (line 802)
- `QuantizerFactory` (line 816)
- `ModelLoader` (line 834)
- `InferenceEngine` (line 883)
- `QuantizationInferencePipeline` (line 907)

**Functions:**
- `parse_arguments` (line 939)
- `main` (line 965)
- `resolve_gqa` (line 86)
- `inspect_and_patch` (line 108)
- `hamilton_product` (line 165)
- `normalize` (line 176)
- `conjugate` (line 180)
- `rotate_vector` (line 185)
- `__init__` (line 196)
- `forward` (line 209)
- `__init__` (line 221)
- `_kernel` (line 233)
- `_contract` (line 236)
- `forward` (line 239)
- `__init__` (line 263)
- `_filter1d` (line 286)
- `encode` (line 291)
- `decode` (line 295)
- `forward` (line 299)
- `process_torus_grid` (line 305)
- `__init__` (line 313)
- `_build_torus_graph` (line 338)
- `_torus_soft_assign` (line 354)
- `_message_passing` (line 365)
- `forward` (line 380)
- `__init__` (line 409)
- `_build_cache` (line 415)
- `_rotate_half` (line 422)
- `forward` (line 426)
- `__init__` (line 441)
- `forward` (line 446)
- `__init__` (line 452)
- `forward` (line 464)
- `__init__` (line 469)
- `_route` (line 486)
- `forward` (line 509)
- `__init__` (line 523)
- `forward` (line 539)
- `__init__` (line 569)
- `_forward_impl` (line 579)
- `forward` (line 586)
- `__init__` (line 591)
- `_init_weights` (line 606)
- `forward` (line 613)
- `generate` (line 627)
- `__init__` (line 652)
- `encode` (line 658)
- `decode` (line 661)
- `eot_token` (line 664)
- `quantize` (line 680)
- `get_format_name` (line 684)
- `get_bits_per_weight` (line 688)
- `__init__` (line 693)
- `quantize` (line 696)
- `get_format_name` (line 714)
- `get_bits_per_weight` (line 717)
- `__init__` (line 722)
- `quantize` (line 725)
- `get_format_name` (line 739)
- `get_bits_per_weight` (line 742)
- `__init__` (line 747)
- `quantize` (line 750)
- `get_format_name` (line 753)
- `get_bits_per_weight` (line 756)
- `__init__` (line 761)
- `quantize` (line 764)
- `get_format_name` (line 767)
- `get_bits_per_weight` (line 770)
- `__init__` (line 775)
- `quantize` (line 778)
- `get_format_name` (line 781)
- `get_bits_per_weight` (line 784)
- `__init__` (line 789)
- `quantize` (line 792)
- `get_format_name` (line 795)
- `get_bits_per_weight` (line 798)
- `__init__` (line 803)
- `quantize` (line 806)
- `get_format_name` (line 809)
- `get_bits_per_weight` (line 812)
- `create_quantizer` (line 818)
- `__init__` (line 835)
- `load_checkpoint` (line 839)
- `__init__` (line 884)
- `run_inference` (line 891)
- `__init__` (line 908)
- `execute` (line 919)

#### `reinforce.py`
**Path:** `reinforce.py`

**Classs:**
- `RLConfig` (line 27) - *Parametric configuration for RL alignment of TopoGPT2.*
- `RewardSignalType` (line 72) - *Enumeration of supported reward signal types.*
- `CheckpointPatcher` (line 84) - *Inspects checkpoint weights to align architecture configuration before instantiation.*
- `MechanisticRewardCalculator` (line 120) - *Computes reward signals from mechanistic interpretability metrics.*
- `RewardModel` (line 152) - *Lightweight reward model for scoring generated responses.*
- `ExperienceBuffer` (line 189) - *Stores trajectories for PPO training with advantage computation.*
- `ValueHead` (line 240) - *Scalar value estimation head attached to TopoGPT2 for PPO.*
- `PPOTrainer` (line 262) - *Proximal Policy Optimization trainer for TopoGPT2 alignment.*
- `ChatAgent` (line 519) - *High-level interface for RL-aligned TopoGPT2 as chatbot.*

**Functions:**
- `setup_logger` (line 597)
- `create_rl_agent_from_checkpoint` (line 606)
- `__init__` (line 86)
- `align_config` (line 89)
- `_resolve_preset` (line 111)
- `__init__` (line 122)
- `compute_lc_reward` (line 129)
- `compute_sp_reward` (line 133)
- `compute_delta_reward` (line 137)
- `compute_mechanistic_reward` (line 142)
- `__init__` (line 154)
- `_init_weights` (line 173)
- `forward` (line 180)
- `__init__` (line 191)
- `add` (line 198)
- `compute_advantages` (line 201)
- `sample_minibatches` (line 215)
- `_collate` (line 226)
- `clear` (line 237)
- `__init__` (line 242)
- `_init_weights` (line 251)
- `forward` (line 258)
- `__init__` (line 264)
- `generate_with_policy` (line 294)
- `compute_kl_divergence` (line 306)
- `compute_reward` (line 317)
- `collect_experience` (line 336)
- `_extract_mechanistic_metrics` (line 367)
- `ppo_update` (line 398)
- `train_step` (line 460)
- `_save_checkpoint` (line 482)
- `load_checkpoint` (line 498)
- `__init__` (line 521)
- `attach_trainer` (line 530)
- `respond` (line 533)
- `_format_conversation` (line 553)
- `train_on_feedback` (line 562)
- `reset_conversation` (line 594)

#### `topogpt2_1.py`
**Path:** `topogpt2_1.py`

**Classs:**
- `TopoGPT2Config` (line 55) - *Configuración completa para TopoGPT2.*
- `QuaternionOps` (line 177) - *Operaciones de cuaterniones puras en PyTorch.
Representación: [..., 4]  donde last dim = [w, x, y, z]
q = w + x*i + y*j + z*k*
- `QuaternionLinear` (line 216) - *Capa lineal con pesos cuaterniones.

Implementa la multiplicación W * x en el álgebra de cuaterniones:
- W = Ww + Wx*i + Wy*j + Wz*k  (cuaternión de pesos)
- x = xw + xx*i + xy*j + xz*k  (cuaternión de entrada)
- out = W * x  (producto de Hamilton extendido a vectores)

Parámetros: 4 matrices reales de forma [out_q, in_q]*
- `QuaternionSpectralLayer` (line 261) - *Convolución espectral 2D con cuaterniones y producto de Hamilton completo.

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
- `SpectralAutoencoder` (line 348) - *Autoencoder espectral con cuaterniones.

Opera en dos niveles:
1. Espectral 1D sobre el vector de features (FFT sobre dim D_MODEL):
   captura la espectrografía global del embedding.
2. Espectral 2D sobre el grid del toro (QuaternionSpectralLayer):
   captura correlaciones espaciales en la topología.

Devuelve (latent, recon_loss) para regularización.*
- `QuaternionTorusBrain` (line 431) - *Reemplaza el MLP en cada capa del transformer.

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
- `RotaryEmbedding` (line 648) - *Rotary Position Embeddings (RoPE) - Su et al., 2021.
Codifica la posición como rotaciones del espacio de atención,
naturalmente relativas y sin parámetros extra.*
- `RMSNorm` (line 696) - *Root Mean Square Layer Normalization (sin bias). Más estable que LayerNorm.*
- `SwiGLU` (line 713) - *SwiGLU: SiLU(gate(x)) * up(x) -> down
Usado en LLaMA 2/3, Qwen, Mistral en lugar de GELU-FFN.
Dimension interna: 8/3 * d_model (convención LLaMA, redondeada a múltiplo de 4).*
- `TopoMoEBrain` (line 742) - *Mixture of Experts sobre la capa topologica.

Arquitectura (inspirada en DeepSeek-MoE / Mixtral):
  - 1 experto compartido: QuaternionTorusBrain (siempre activo)
  - N_EXPERTS expertos SwiGLU ligeros (activacion esparsa: Top-K por token)
  - Router: Linear(D, N_EXPERTS) + softmax → top-K

Load-balancing loss (auxiliar): penaliza si un experto acapara todos los tokens.
Activa MOE_TOP_K de N_EXPERTS expertos por token.

Sin MoE (MOE_ENABLED=False): se comporta como QuaternionTorusBrain puro.*
- `MultiHeadAttention` (line 847) - *Multi-head attention con:
- Flash Attention (scaled_dot_product_attention de PyTorch 2.0+)
- Rotary Position Embeddings (RoPE)
- GQA (Grouped Query Attention): N_KV_HEADS < N_HEADS, reduce VRAM de K/V
- KV Cache para inferencia autoregresiva eficiente
- Temperatura termodinámica aprendible*
- `TopoGPT2Layer` (line 929) - *Capa del transformer con TopoMoEBrain (TopoBrain + MoE SwiGLU experts).

Esquema pre-norm (estilo LLaMA):
    x = x + Attention_GQA(RMSNorm(x))
    x = x + TopoMoEBrain(RMSNorm(x))*
- `TopoGPT2` (line 976) - *TopoGPT2: Transformer de lenguaje con TopoBrain cuaternión-espectral.

Arquitectura:
    Embedding de tokens + RoPE (en Attention)
    N_LAYERS × TopoGPT2Layer (Attention + QuaternionTorusBrain)
    RMSNorm final
    Proyección a vocabulario (weight-tied con embeddings)*
- `BPETokenizer` (line 1082) - *Wrapper alrededor de tiktoken (GPT-2 compatible).*
- `CorpusDownloader` (line 1107) - *Descarga corpus de texto para entrenamiento.

Soporta:
- 'tinystories': ~2GB de cuentos cortos (ideal para pruebas)
- 'wikitext103': ~500MB de Wikipedia curada
- 'file': archivo de texto local

Usa HuggingFace 'datasets' para TinyStories y WikiText.*
- `TokenizedDataset` (line 1170) - *Dataset de tokens para language modeling (next-token prediction).

Guarda los tokens tokenizados en disco la primera vez (cache .pt)
para evitar re-tokenizar en cada ejecucion. La clave de cache incluye
un hash del contenido del corpus + tokenizador + max_tokens.*
- `CheckpointManager` (line 1220) - *Gestiona checkpoints de forma acumulativa y segura.

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
- `TopoGPT2Trainer` (line 1453) - *Entrenador acumulativo y resumible.

Caracteristicas:
- Checkpoint automatico en safetensors cada N minutos + cada epoch
- Historial acumulativo entre sesiones (--resume agrega al historial existente)
- Guarda el mejor modelo en checkpoints/best/ automaticamente
- LR schedule: cosine con warmup relativo a los steps de ESTA sesion
- Mixed Precision (AMP) + acumulacion de gradientes*
- `MechanisticMetrics` (line 1746) - *Calcula todas las metricas del diagrama de fases de Book.md.

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
- `Phase0_KernelOptimizer` (line 1983) - *Encuentra el ratio imaginario/real optimo para los kernels espectrales.

Analogia con main.py: evalua la transicion GOE→GUE en el espacio
de kernels. Un ratio optimo promueve estructura topologica (insulador)
vs estructura amorfa (vidrio).

Metodo: calibra con un mini-batch y mide la varianza del gradiente
en funcion del ratio. Ratios que minimizan la varianza de gradiente
(maxima coherencia espectral) son preferibles.

No entrena: solo inicializa los kernels con distintos ratios y mide.
Tiempo tipico: < 30 segundos.*
- `Phase1_BatchProspector` (line 2058) - *Encuentra el batch size optimo testando candidatos con pocos pasos.

De main.py: el batch size regula la temperatura del horno de cristalizacion.
Batch sizes demasiado chicos -> ruido excesivo (vidrio frio).
Batch sizes demasiado grandes -> sin presion annealing (amorfos).
La ventana optima empirica de main.py: [24, 128] para Strassen.

Para LM, testeamos candidatos midiendo:
- delta (δ): velocidad de descenso en prospect_steps pasos
- T_eff: temperatura efectiva del gradiente

Tiempo tipico: < 2 minutos para 3 candidatos × 30 pasos.*
- `Phase2_SeedMiner` (line 2141) - *Encuentra semillas prometedoras midiendo la trayectoria de delta.

De main.py: una semilla "buena" muestra delta descendente en los
primeros N pasos (enfriamiento). Una semilla "mala" se estanca en
el plateau vidrioso (~0.49).

Criterio de seleccion:
1. Semillas con delta_velocity < 0 (enfriando) AND kappa bajo.
2. Si no hay, semillas solo enfriando.
3. Fallback: semilla con menor delta final.

Tiempo tipico: < 3 minutos para 5 semillas × 50 pasos.*
- `Phase4_AnnealingRefiner` (line 2223) - *Refinamiento post-entrenamiento mediante recocido simulado.

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
- `TopoPhasePipeline` (line 2384) - *Orquesta las 5 fases de entrenamiento segun main.py + Book.md.

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

**Functions:**
- `setup_logger` (line 155)
- `set_seed` (line 165)
- `main` (line 2506)
- `__post_init__` (line 124)
- `hamilton_product` (line 185) - *Producto de Hamilton q1 ⊗ q2. Ambos [..., 4].*
- `normalize` (line 197)
- `conjugate` (line 201)
- `rotate_vector` (line 206) - *Rota vector 3D v por cuaternión unitario q. v:[...,3] q:[...,4]*
- `__init__` (line 228)
- `forward` (line 244) - *x: [..., in_features] → [..., out_features]*
- `__init__` (line 281)
- `_kernel` (line 300)
- `_contract` (line 303) - *Suma sobre canales in_q: Y[b,o,h,w] = Σ_i W[i,o,h,w]·X[b,i,h,w]*
- `forward` (line 307) - *x: [B, 4*in_q, H, W]  (4 canales cuaterniones sobre grid espacial)
→ [B, 4*out_q, H, W]*
- `__init__` (line 361)
- `_filter1d` (line 393) - *Filtro espectral 1D: x[..., D] → filtrado[..., D]*
- `encode` (line 399) - *x: [..., D_MODEL] → latent: [..., D_LAT]*
- `decode` (line 404) - *z: [..., D_LAT] → recon: [..., D_MODEL]*
- `forward` (line 409) - *Devuelve (latent, recon_loss)*
- `process_torus_grid` (line 416) - *Procesa el grid del toro con QuaternionSpectralLayer.
grid: [B, 4*D_QUAT, RADIAL, ANGULAR]  →  [B, 4*D_QUAT, RADIAL, ANGULAR]*
- `__init__` (line 449)
- `_build_torus_graph` (line 489) - *Construye las aristas del grafo toro 2×4.

Nodos indexados como: node = r * N_ANGULAR + a
  r ∈ [0, RADIAL-1], a ∈ [0, ANGULAR-1]

Aristas angulares: nodo ↔ nodo a la izquierda/derecha (periódico)
Aristas radiales:  nodo ↔ nodo del anillo interior/exterior*
- `_torus_soft_assign` (line 523) - *Asignación blanda de tokens a los 8 nodos del toro via distancia circular.

phi1: [BS] ángulo angular ∈ [-π, π]
phi2: [BS] ángulo radial ∈ [-π, π]
→ weights: [BS, N_NODES]  (suma a 1, softmax de distancias negativas)*
- `_message_passing` (line 550) - *Message-passing VECTORIZADO con rotaciones cuaterniones.
Sin bucles Python: todas las aristas se procesan en paralelo.

node_feat: [BS, N_NODES, D_MODEL]
→ [BS, N_NODES, D_MODEL]*
- `forward` (line 587) - *x: [B, S, D_MODEL]
→ output: [B, S, D_MODEL], recon_loss: scalar*
- `__init__` (line 655)
- `_build_cache` (line 661)
- `_rotate_half` (line 668)
- `forward` (line 672) - *q, k: [B, n_heads, S_q/S_k, d_head]
offset: posicion inicial (para KV cache: longitud del cache existente)
Aplica posiciones [offset .. offset+S-1] a q y k.*
- `__init__` (line 699)
- `forward` (line 704)
- `__init__` (line 720)
- `forward` (line 734)
- `__init__` (line 757)
- `_route` (line 778) - *x: [N, D] donde N = B*S (tokens aplanados)
Retorna:
expert_out: [N, D]  suma ponderada de top-K expertos
aux_loss:   escalar  load-balancing loss
Routing vectorizado sin boolean indexing ni sincronizacion CUDA.
Usa dispatch por indices agrupados (estilo Mixtral/DeepSeek) para
compatibilidad total con torch.utils.checkpoint.*
- `forward` (line 820) - *x: [B, S, D]
→ output: [B, S, D], aux_loss: escalar*
- `__init__` (line 857)
- `forward` (line 875) - *Args:
    x:        [B, S, D]
    is_causal: usar mascara causal
    past_kv:  (K_cache, V_cache) de pasos anteriores o None
Returns:
    out:      [B, S, D]
    kv_cache: (K, V) completos para cachear en generate()*
- `__init__` (line 938)
- `_forward_impl` (line 947)
- `forward` (line 956) - *Retorna (x_out, aux_loss, kv_cache).
Con gradient checkpointing en training (solo cuando no hay KV cache).*
- `__init__` (line 987)
- `_init_weights` (line 1006)
- `forward` (line 1013) - *token_ids: [B, S]  (enteros)
past_kvs:  lista de (K, V) por capa, o None para entrenamiento
→ logits: [B, S, VOCAB_SIZE], aux_loss: scalar, new_kvs: list[(K,V)]*
- `count_params` (line 1036)
- `generate` (line 1042) - *Generacion autoregresiva con KV cache y muestreo top-k.
En el primer paso procesa el prompt completo y guarda el cache.
En pasos siguientes solo procesa 1 token nuevo (O(n) en lugar de O(n^2)).*
- `__init__` (line 1085)
- `encode` (line 1093)
- `decode` (line 1096)
- `eot_token` (line 1099)
- `__init__` (line 1119)
- `get_text` (line 1125) - *Devuelve el texto del corpus. Descarga si es necesario.*
- `_download_hf` (line 1150)
- `__init__` (line 1179)
- `__len__` (line 1206)
- `__getitem__` (line 1209)
- `__init__` (line 1245)
- `patch_config_for_resume` (line 1255) - *Lee el checkpoint 'latest' y ajusta cfg.N_KV_HEADS / cfg.GQA_GROUPS
para que coincidan con la arquitectura guardada.
Necesario cuando el codigo cambio GQA despues de guardar el checkpoint.*
- `_save_model` (line 1284)
- `_load_model` (line 1297)
- `_save_optimizer` (line 1328)
- `_load_optimizer` (line 1331)
- `_save_state` (line 1340)
- `_load_state` (line 1345)
- `should_save` (line 1356)
- `save` (line 1359) - *Guarda checkpoint completo.

state debe contener al menos: completed_epochs, global_step,
best_val_loss, history, config.*
- `load_latest` (line 1404) - *Carga el ultimo checkpoint guardado.
Devuelve el state dict (vacio si no hay checkpoint).*
- `load_best` (line 1431) - *Carga el mejor modelo guardado (solo pesos, sin optimizador).*
- `has_checkpoint` (line 1443)
- `__init__` (line 1465)
- `resume` (line 1500) - *Carga el ultimo checkpoint disponible.
Restaura: pesos del modelo, estado del optimizador, historial acumulado,
epoch/step completados y mejor val_loss.
Devuelve True si se cargo un checkpoint, False si empieza de cero.*
- `_current_state` (line 1525) - *Construye el dict de estado para persistir en state.json.*
- `_cosine_lr` (line 1536) - *Cosine decay con warmup. El schedule es relativo a la sesion actual.*
- `_set_lr` (line 1544)
- `train` (line 1548) - *Entrena cfg.EPOCHS epocas adicionales a partir de completed_epochs.
El historial se acumula sobre sesiones previas.*
- `_sample_text` (line 1684) - *Genera una muestra de texto al final de cada epoch para monitorear
la calidad cualitativa del modelo (detecta degeneracion, repeticion, etc.).*
- `evaluate` (line 1716)
- `__init__` (line 1766)
- `compute_delta` (line 1774)
- `compute_alpha` (line 1781)
- `update_grad_buffer` (line 1786) - *Captura gradientes de forma segura, ignorando tensores corruptos.*
- `compute_t_eff` (line 1812) - *T_eff = lr/2 * Var(gradiente). Temperatura termodinamica efectiva.*
- `compute_kappa` (line 1820) - *κ = λ_max / λ_min de la covarianza del gradiente.
Parámetro de orden para cristalización (κ≈1 = cristal).
Nota: requiere pasadas backward adicionales. Se ejecuta con protección
para no corromper el estado AMP del trainer principal.*
- `compute_berry_phase` (line 1878) - *Fase de Berry de los kernels espectrales imaginarios.
Surge de los parametros ki_w, ki_x, ki_y, ki_z de QuaternionSpectralLayer.
|berry|>pi/2 con winding!=0 indica estructura topologica.*
- `compute_lc` (line 1891) - *Complejidad local: 1 - similitud coseno promedio entre filas de pesos.*
- `compute_sp` (line 1905) - *Superposicion: correlacion inter-fila promedio (entrelazamiento de features).*
- `classify_phase` (line 1921) - *Clasificacion de fase segun Book.md:

discrete_crystal:       delta<0.05, kappa<1.5
topological_insulator:  |berry|>pi/2, winding!=0
cold_glass:             kappa>>1, delta>0.3
functional_glass:       intermedio (lo mas comun en LM)*
- `compute_all` (line 1940) - *Calcula todas las metricas.
compute_kappa=True hace pasadas backward adicionales (caro, usar cada N epochs).*
- `format_log` (line 1965)
- `__init__` (line 2001)
- `_measure_ratio` (line 2005) - *Mide la coherencia espectral para un ratio dado.
Retorna: varianza del gradiente (menor = mas coherente = mejor).*
- `optimize` (line 2034) - *Retorna el mejor ratio de inicializacion de kernels espectrales.*
- `__init__` (line 2074)
- `prospect` (line 2078) - *Retorna el mejor batch size segun delta y T_eff.*
- `__init__` (line 2157)
- `mine` (line 2161) - *Retorna la semilla con la mejor trayectoria de delta.*
- `__init__` (line 2243)
- `refine` (line 2252) - *Ejecuta refine_epochs epocas de recocido simulado.
Retorna el historial de refinamiento.*
- `__init__` (line 2404)
- `_make_dataloaders` (line 2414)
- `run` (line 2426) - *Ejecuta el pipeline completo.
Retorna el trainer con el modelo entrenado.*
- `ckpt_fn` (line 964)

#### `topogpt2_embeddings_navigator.py`
**Path:** `topogpt2_embeddings_navigator.py`

**Classs:**
- `ThemeTokens` (line 86) - *Palette and CSS tokens for the navigator.*
- `PlotTheme` (line 103) - *Plot-level theme.*
- `SamplingLimits` (line 118) - *Safety caps to keep the UI responsive.*
- `MetricsConfig` (line 132) - *Numerical stability thresholds.*
- `ProjectionConfig` (line 146) - *Projection hyperparameters.*
- `NavigatorConfig` (line 156) - *Top-level configuration.*
- `StyleInjector` (line 189) - *Injects the navigator's CSS once per session.*
- `CheckpointBundle` (line 263) - *Holds a loaded TopoGPT2 model along with its config and tokenizer.*
- `ModelLoader` (line 312) - *Builds a ``CheckpointBundle`` from a checkpoint on disk or in memory.*
- `ActivationCapture` (line 522) - *Extracts per-layer residual-stream activations via forward hooks.*
- `MetricSuite` (line 600) - *Computes the full geometric and topological metric suite.*
- `Projector` (line 1068) - *Projects point clouds into 2D or 3D with multiple algorithms.*
- `FigureStyler` (line 1195) - *Consistent Plotly styling for every figure.*
- `RenderContext` (line 1243) - *Bundle passed to every view during rendering.*
- `BaseEmbeddingView` (line 1255) - *Abstract base for navigator views.*
- `OverviewView` (line 1274) - *Token table, per-layer scalar metric evolution, summary panel.*
- `CloudView` (line 1352) - *Interactive 3D cloud of one layer's residual-stream activations.*
- `MetricsView` (line 1475) - *Detailed per-layer metric card for a selected layer.*
- `PersistenceView` (line 1569) - *Persistence diagram and barcode for H0 and H1.*
- `BerryPhaseView` (line 1666) - *Berry phase and winding number analysis of the token trajectory.*
- `LipschitzView` (line 1758) - *Local Lipschitz profile and trajectory geometry (speed/curvature/torsion).*
- `NeighborhoodView` (line 1834) - *kNN graph and neighborhood statistics.*
- `CrossLayerView` (line 1933) - *Per-token drift across the residual stream.*
- `QuaternionView` (line 1994) - *Quaternion decomposition of activations (w, x, y, z sub-channels).*
- `RawView` (line 2108) - *Raw activation heatmap (tokens x features).*
- `ViewRegistry` (line 2145) - *Collects and instantiates views.*
- `SidebarController` (line 2161) - *Sidebar inputs (checkpoint, text, kNN, model script path).*
- `ModuleImporter` (line 2217) - *Imports ``topogpt2_1.py`` from a user-supplied filesystem path.*
- `NavigatorApp` (line 2255) - *Top-level orchestrator.*

**Functions:**
- `main` (line 2418) - *Streamlit script entry point.*
- `__init__` (line 192)
- `inject` (line 195) - *Render the CSS block in the current Streamlit page.*
- `__init__` (line 266)
- `model` (line 279) - *Return the underlying nn.Module in eval mode.*
- `config` (line 284) - *Return the model config object.*
- `tokenizer` (line 289) - *Return the BPE tokenizer.*
- `source_name` (line 294) - *Return the original file name of the checkpoint.*
- `device` (line 299) - *Return the device the model is currently placed on.*
- `num_layers` (line 303) - *Return the number of transformer layers in the model.*
- `embedding_dim` (line 307) - *Return the model hidden size.*
- `__init__` (line 315)
- `load` (line 318) - *Load a checkpoint and instantiate the corresponding model.

Args:
    source: Either a filesystem path or a Streamlit UploadedFile.
    topogpt2_module: Already-imported ``topogpt2_1`` module providing
        ``TopoGPT2``, ``TopoGPT2Config``, and ``BPETokenizer``.

Returns:
    A :class:`CheckpointBundle` with model, config, and tokenizer.

Raises:
    ValueError: if the checkpoint extension is not supported or if
        the model config cannot be reconstructed.*
- `_read_state_dict` (line 344)
- `_materialize` (line 366)
- `_extract_payload` (line 374)
- `_build_config` (line 391)
- `_infer_config` (line 405)
- `_infer_d_model` (line 433)
- `_infer_num_layers` (line 439)
- `_infer_n_heads` (line 450)
- `_infer_max_seq_len` (line 467)
- `_infer_n_kv_heads` (line 475) - *Infer the number of key/value heads for GQA.

In GQA the ``k_proj`` (and ``v_proj``) output dimension equals
``n_kv_heads * d_head``. When the checkpoint was trained with
standard multi-head attention ``n_kv_heads`` equals ``n_heads``.
Passing the explicit value via ``N_KV_HEADS`` avoids the automatic
``N_HEADS // 4`` heuristic in ``TopoGPT2Config`` which would
otherwise produce a shape mismatch at load time.*
- `_infer_torus_grid` (line 505)
- `_validate_load` (line 514)
- `__init__` (line 525)
- `run` (line 528) - *Run a single forward pass and return activations and tokens.

Args:
    bundle: The loaded :class:`CheckpointBundle`.
    text: The input text to encode.

Returns:
    A dictionary with keys ``tokens`` (list of decoded pieces),
    ``ids`` (list of token ids), ``embedding`` (initial token
    embeddings), ``layers`` (list of per-layer residual-stream
    activations of shape ``[S, D]``), and ``final`` (the post
    final-norm activations).*
- `_decode_pieces` (line 589)
- `__init__` (line 603)
- `compute` (line 606) - *Compute every metric on a point cloud ``[N, D]``.

Args:
    points: Array of shape ``[N, D]`` with ``N >= 4``.
    knn: Number of neighbours for the kNN graph.

Returns:
    Dictionary with scalar and array metrics.*
- `_sanitize` (line 642)
- `_trivial` (line 645)
- `_pairwise` (line 675)
- `_shortest_paths` (line 678)
- `_sp_metrics` (line 698)
- `_kappa` (line 718) - *Local curvature proxy from the chord-vs-arc ratio.

For every point and every nearby pair (a, b) we compare the
Euclidean chord 0.5*(d_E(i,a) + d_E(i,b)) to the geodesic arc
0.5*(d_G(i,a) + d_G(i,b)). When the ratio chord/arc is near 1 the
local neighbourhood is flat; when it is less than 1 the arc bends
outward (spherical-like, positive curvature). The returned scalar
kappa = 1 - (chord/arc)^2, bounded in [0, 1] for positive curvature
and scale-free so it can be compared across layers.*
- `_gromov_delta` (line 759)
- `_persistence` (line 783)
- `_h0_from_mst` (line 810)
- `_h1_from_edges` (line 845) - *Estimate H1 persistence bars from a distance-sorted edge list.

When an edge is added that does not reduce the number of
connected components, it closes a loop. The birth of that H1
feature is the filtration level at which the loop appears. We
estimate the death as the minimum filtration level at which the
loop is filled in by a 2-simplex in the Vietoris-Rips complex
formed from the same edges. When no such filling appears within
the edge budget, the bar is marked as surviving to the maximum
scale.*
- `_berry_phases` (line 905)
- `_winding_numbers` (line 920)
- `_planar_winding` (line 936)
- `_lipschitz` (line 947)
- `_trajectory_geometry` (line 954) - *Frenet-Serret differential geometry of the token trajectory.

Speed is computed in the full ambient space. Curvature and torsion
are well-defined in 3D, so they are evaluated on the top-3 PCA
projection of the sequence; this preserves geometry while giving a
clean, interpretable scalar per position.*
- `_safe_pca3` (line 1017)
- `_spectral_properties` (line 1030)
- `__init__` (line 1071)
- `project` (line 1074) - *Project ``[N, D]`` points to ``n_components`` dims.

Args:
    points: Input point cloud of shape ``[N, D]``.
    method: ``"pca"``, ``"isomap"``, ``"umap"``, ``"random"`` or
        ``"sphere"``.
    n_components: Desired output dimensionality.

Returns:
    Tuple ``(embedding, info)`` where ``info`` contains method
    specific diagnostics (explained variance, etc.).*
- `_pca` (line 1105)
- `_isomap` (line 1123)
- `_umap` (line 1144)
- `_random` (line 1171)
- `_sphere` (line 1181)
- `__init__` (line 1198)
- `style_3d` (line 1201) - *Apply 3D styling.*
- `style_2d` (line 1223) - *Apply 2D styling.*
- `__init__` (line 1261)
- `ctx` (line 1265) - *Return the shared render context.*
- `render` (line 1270) - *Render the view into the current Streamlit container.*
- `render` (line 1280)
- `_render_tokens` (line 1284)
- `_render_layer_evolution` (line 1310)
- `render` (line 1358)
- `_choose` (line 1378)
- `_render_trajectory` (line 1386)
- `_render_residual_streams` (line 1442)
- `render` (line 1481)
- `_get_metrics` (line 1490)
- `_render_card` (line 1496)
- `_render_kappa` (line 1521)
- `_render_path_metrics` (line 1544)
- `render` (line 1575)
- `_stage_metrics` (line 1583)
- `_render_diagram` (line 1591)
- `_render_barcode` (line 1633)
- `render` (line 1672)
- `_stage_metrics` (line 1680)
- `_render_berry` (line 1688)
- `_render_winding` (line 1720)
- `render` (line 1764)
- `_stage_metrics` (line 1772)
- `_render_lc` (line 1780)
- `_render_dynamics` (line 1807)
- `render` (line 1840)
- `_stage_metrics` (line 1849)
- `_stage_points` (line 1857)
- `_render_graph` (line 1864)
- `_render_coherence` (line 1911)
- `render` (line 1939)
- `_cosine_diag` (line 1962)
- `_render_heatmap` (line 1968)
- `render` (line 2000)
- `_points` (line 2021)
- `_render_component_norms` (line 2029)
- `_render_quaternion_norms` (line 2054)
- `_render_sphere` (line 2070)
- `render` (line 2114)
- `_points` (line 2136)
- `__init__` (line 2148)
- `register` (line 2152) - *Register a view factory.*
- `build` (line 2156) - *Instantiate every registered view.*
- `__init__` (line 2164)
- `render` (line 2167) - *Render the sidebar and return user selections.*
- `load` (line 2220) - *Dynamically import the TopoGPT2 module.

Args:
    path: Path to ``topogpt2_1.py``.

Returns:
    The imported module object.

Raises:
    FileNotFoundError: if the path does not exist.
    ImportError: if the module cannot be loaded.*
- `__init__` (line 2258)
- `run` (line 2269) - *Entry point for ``streamlit run``.*
- `_render_header` (line 2307)
- `_render_landing` (line 2324)
- `_try_load_bundle` (line 2335)
- `_compute_all_metrics` (line 2351)
- `_render_meta` (line 2367)
- `_build_registry` (line 2380)
- `_render_tabs` (line 2394)
- `_render_footer` (line 2408)
- `hook` (line 561)
- `find` (line 818)
- `union` (line 824)
- `find` (line 864)
- `union` (line 870)

#### `topogpt2_explorer.py`
**Path:** `topogpt2_explorer.py`

**Classs:**
- `ThemeTokens` (line 59) - *Design tokens for the explorer's dark scientific theme.*
- `PlotTheme` (line 76) - *Plot-level theme constants.*
- `SamplingLimits` (line 91) - *Hard caps to keep the UI responsive regardless of model size.*
- `MetricsConfig` (line 108) - *Numerical stability thresholds for metrics.*
- `GenerationLimits` (line 120) - *Random-projection and synthetic probe parameters.*
- `ExplorerConfig` (line 129) - *Top-level configuration container.*
- `StyleInjector` (line 168) - *Injects the global CSS for the explorer into the Streamlit page.*
- `TensorClassifier` (line 244) - *Classifies tensor keys from a TopoGPT2 checkpoint by semantic role.

The classifier parses the parameter name and extracts:
  * a coarse role ("attention", "moe_router", "spectral_kernel", etc.)
  * the layer index if present
  * the quaternion component (w, x, y, z) if present
  * whether the tensor represents a frequency-domain kernel*
- `CheckpointLoader` (line 337) - *Loads raw tensor dictionaries from disk.

Supports both ``safetensors`` files and plain PyTorch pickles produced
by ``torch.save``. The loader returns CPU float32 tensors exclusively to
guarantee downstream compatibility with NumPy.*
- `TensorInventory` (line 429) - *Holds a checkpoint's tensors along with per-tensor metadata.*
- `TensorProjector` (line 515) - *Projects arbitrary tensors into 2D matrices and 3D point clouds.

Responsibilities:
  * Reduce N-dimensional tensors to a 2D matrix of rows (samples) vs
    columns (features) while preserving interpretability.
  * Subsample rows/columns to respect the configured limits.
  * Compute 3D embeddings (PCA or Gaussian random projection) with
    deterministic seeding.*
- `MetricCalculator` (line 635) - *Computes mechanistic-interpretability metrics for parameter matrices.

Results are memoized by the ``id`` of the input array to guarantee that
repeated requests for the same subsampled matrix (common across tabs) do
not re-run expensive SVDs.*
- `FigureStyler` (line 836) - *Applies consistent styling to Plotly figures.*
- `VisualizationContext` (line 883) - *Context passed to visualizers at render time.*
- `RenderContext` (line 894) - *Concrete visualization context implementation.*
- `BaseVisualizer` (line 904) - *Abstract base class for all visualizers.

Subclasses implement :meth:`render` and :meth:`is_applicable`. The registry
will instantiate them only when :meth:`is_applicable` returns ``True``.*
- `OverviewVisualizer` (line 931) - *Top-level summary of the checkpoint: counts, roles, and inventory table.*
- `TensorExplorerVisualizer` (line 999) - *Deep-dive into a single tensor: 3D cloud, heatmap, histograms, spectrum.*
- `QuaternionDecompositionVisualizer` (line 1227) - *Visualize QuaternionLinear layers by their (Ww, Wx, Wy, Wz) components.*
- `SpectralKernelVisualizer` (line 1385) - *Visualize complex spectral kernels (kr/ki pairs) in the frequency plane.*
- `TorusTopologyVisualizer` (line 1538) - *3D torus graph of the QuaternionTorusBrain node embeddings and edges.*
- `AttentionVisualizer` (line 1773) - *Per-layer attention Q/K/V/O projection analysis with per-head split.*
- `MoEVisualizer` (line 1916) - *Router logit landscape and expert weight geometry.*
- `LayerEvolutionVisualizer` (line 2061) - *Track how metrics evolve across transformer layers for a chosen role.*
- `GlobalGeometryVisualizer` (line 2151) - *Cross-tensor geometry: embed every weight matrix as a 3D point via summary features.*
- `VisualizerRegistry` (line 2291) - *Collects visualizer classes and dispatches to them by label.*
- `SidebarController` (line 2316) - *Renders the sidebar controls and returns user selections.*
- `ExplorerApp` (line 2359) - *Top-level orchestration: composes loader, registry, and layout.*

**Functions:**
- `main` (line 2493) - *Streamlit script entry point.*
- `__init__` (line 171)
- `_build_css` (line 174)
- `inject` (line 239) - *Render the CSS block inside the current Streamlit page.*
- `classify` (line 258) - *Return structured metadata for a checkpoint tensor.

Args:
    name: Full dotted parameter name.
    shape: Tensor shape.

Returns:
    A dictionary with keys ``role``, ``layer``, ``component``,
    ``is_spectral``, ``is_complex_kernel``, ``shape``.*
- `_classify_role` (line 286)
- `_extract_layer` (line 328)
- `_extract_quaternion_component` (line 332)
- `__init__` (line 345)
- `load` (line 348) - *Load a checkpoint from a file path or an uploaded file-like.

Args:
    source: Either a path (``str`` or ``Path``) or a Streamlit
        ``UploadedFile`` object.

Returns:
    Dictionary mapping tensor name to CPU ``torch.Tensor``.

Raises:
    ValueError: If the extension is not supported.
    RuntimeError: If deserialization fails.*
- `_materialize` (line 373)
- `_load_safetensors` (line 382)
- `_load_torch` (line 389)
- `_extract_state_dict` (line 399)
- `_looks_like_state_dict` (line 413)
- `_to_cpu_float32` (line 420)
- `__init__` (line 432)
- `names` (line 443) - *Return all tensor names sorted alphabetically.*
- `tensor` (line 447) - *Retrieve a tensor by name.*
- `meta` (line 451) - *Retrieve structured metadata for a tensor.*
- `layers` (line 455) - *Return all unique layer indices present in the checkpoint.*
- `roles` (line 460) - *Return the distinct roles present in the checkpoint.*
- `filter` (line 464) - *Return tensor names matching the supplied filters.*
- `total_parameters` (line 485) - *Total parameter count across the checkpoint.*
- `summary_rows` (line 489) - *Return a list of per-tensor rows suitable for a Streamlit table.*
- `__init__` (line 526)
- `to_matrix` (line 531) - *Convert a tensor to a 2D ``float64`` matrix.

Complex tensors are stacked as ``[real, imag]`` along the feature axis
before flattening, which preserves their dimensionality information.*
- `subsample` (line 553) - *Return a row/column subsample bounded by the configured caps.*
- `project_3d` (line 575) - *Project a matrix to 3D using PCA or Gaussian random projection.

Args:
    matrix: Row-major 2D matrix ``[N, F]``.
    method: Either ``"pca"`` or ``"random"``.

Returns:
    A pair ``(embedding[N, 3], info)`` where ``info`` contains the
    explained variance ratio (PCA) or the Johnson-Lindenstrauss
    ``eps`` used (random projection).*
- `_pca_3d` (line 606)
- `_random_3d` (line 617)
- `__init__` (line 643)
- `compute_all` (line 649) - *Compute the full metrics dictionary in one pass.

Uses a lightweight cache keyed by ``(id(matrix), shape)`` so that
recomputation across visualizers is avoided when the same subsampled
matrix is analyzed multiple times in one render cycle.*
- `_svd_safe` (line 681) - *Compute singular values once, reused by rank and participation ratio.*
- `_effective_rank_from_svd` (line 690)
- `_participation_from_svd` (line 707)
- `sparsity` (line 720) - *Fraction of entries whose absolute value is below ``threshold``.*
- `entropy` (line 727) - *Shannon entropy (nats) of the discrete value histogram.

Uses probability mass (not density), which guarantees a non-negative
result bounded above by ``log(histogram_bins)``. This is the standard
convention for interpretability dashboards.*
- `effective_rank` (line 748) - *Effective rank via the exponential of the entropy of singular values.*
- `participation_ratio` (line 753) - *Participation ratio of the singular value spectrum.

Defined as ``(sum s)^2 / sum(s^2)`` which equals the effective number
of nonzero singular directions.*
- `fractal_dimension` (line 762) - *Approximate the effective embedding dimension via PCA.

Counts the number of principal components whose explained variance
exceeds ``default_fractal_variance_floor``.*
- `coherence` (line 781) - *Maximum and mean absolute cosine similarity between rows.*
- `spectral_flatness` (line 796) - *Spectral flatness (Wiener entropy) in dB averaged over rows.*
- `dominant_frequency` (line 814) - *Index of the dominant non-zero frequency bin of row 0.*
- `_subsample_for_svd` (line 824)
- `_subsample_for_pca` (line 830)
- `__init__` (line 839)
- `style_3d` (line 842) - *Apply the standard 3D scene styling.*
- `style_2d` (line 864) - *Apply the standard 2D figure styling.*
- `__init__` (line 914)
- `ctx` (line 918) - *Return the render context bound to this visualizer.*
- `is_applicable` (line 922) - *Return ``True`` if there is data in the inventory to render.*
- `render` (line 927) - *Render the visualizer into the current Streamlit container.*
- `render` (line 937)
- `_render_headline` (line 950)
- `_render_role_breakdown` (line 957)
- `_render_inventory_table` (line 984)
- `render` (line 1005)
- `_render_meta` (line 1042)
- `_render_metric_grid` (line 1050)
- `_render_point_cloud` (line 1069)
- `_render_heatmap` (line 1103)
- `_render_distribution` (line 1125)
- `_render_spectrum` (line 1149)
- `_render_singular_spectrum` (line 1180)
- `is_applicable` (line 1233)
- `render` (line 1237)
- `_group_quaternion_bundles` (line 1249)
- `_quaternion_bundle_key` (line 1263)
- `_render_component_stats` (line 1278)
- `_render_component_heatmaps` (line 1290)
- `_render_component_spectra` (line 1315)
- `_render_unit_norm_distribution` (line 1346)
- `is_applicable` (line 1391)
- `render` (line 1397)
- `_pair_kr_ki` (line 1413)
- `_reshape_to_2d` (line 1428)
- `_render_magnitude_phase` (line 1439)
- `_render_complex_scatter` (line 1470)
- `_render_radial_profile` (line 1504)
- `is_applicable` (line 1544)
- `render` (line 1547)
- `_infer_grid` (line 1568)
- `_render_headline_metrics` (line 1578)
- `_render_3d_torus` (line 1591)
- `_torus_positions` (line 1605)
- `_add_edges` (line 1631)
- `_edge_label` (line 1669)
- `_build_segments` (line 1678)
- `_add_nodes` (line 1697)
- `_render_node_correlation` (line 1725)
- `_render_edge_quaternions` (line 1747)
- `is_applicable` (line 1779)
- `render` (line 1785)
- `_infer_head_count` (line 1813)
- `_render_per_head_norms` (line 1822)
- `_render_per_head_spectrum` (line 1849)
- `_render_head_similarity` (line 1881)
- `_render_summary_metrics` (line 1908)
- `is_applicable` (line 1922)
- `render` (line 1927)
- `_render_router_norms` (line 1949)
- `_render_routing_probe` (line 1972)
- `_render_expert_similarity` (line 2015)
- `_softmax` (line 2055)
- `is_applicable` (line 2067)
- `render` (line 2070)
- `_render_metric_grid` (line 2113)
- `render` (line 2157)
- `_render_scatter` (line 2204)
- `_render_feature_correlation` (line 2246)
- `_build_palette` (line 2279)
- `__init__` (line 2294)
- `register` (line 2298) - *Register a visualizer factory.

Args:
    factory: Callable producing a :class:`BaseVisualizer` instance
        given the shared render context.*
- `build` (line 2307) - *Instantiate all registered visualizers.*
- `applicable` (line 2311) - *Return the subset of visualizers whose data is present.*
- `__init__` (line 2319)
- `render` (line 2322) - *Render the sidebar and return the current selections.*
- `__init__` (line 2362)
- `run` (line 2372) - *Entry point used by ``streamlit run``.*
- `_configure_page` (line 2394)
- `_render_header` (line 2401)
- `_render_landing` (line 2416)
- `_resolve_checkpoint` (line 2437)
- `_build_registry` (line 2452)
- `_render_tabs` (line 2465)
- `_render_footer` (line 2483)

#### `topogpt2_grid_scaler.py`
**Path:** `topogpt2_grid_scaler.py`

**Classs:**
- `InterpolationConfig` (line 97) - *Controls the spectral weight interpolation.*
- `ValidationConfig` (line 108) - *What to measure after each scaling step.*
- `ProgressiveConfig` (line 121) - *Multi-hop scaling strategy.*
- `OutputConfig` (line 131) - *Output files.*
- `TopoScalerConfig` (line 141) - *Top-level configuration — mirrors scaler_config_128.toml.*
- `ModuleImporter` (line 181) - *Dynamically imports topogpt2_1.py from any path.*
- `CheckpointReader` (line 205) - *Reads a TopoGPT2 checkpoint and any embedded config.*
- `ConfigReconstructor` (line 242) - *Reconstructs TopoGPT2Config from weights, inferring all dimensions.*
- `TensorRole` (line 328) - *Classifies every state-dict key by its D_MODEL scaling role.*
- `SpectralInterpolator` (line 380) - *Interpolates weight tensors via Fourier-space zero-padding or cropping.

This is the core of the technique — identical in principle to the
Willmore Crystal scaler's Fourier interpolation of spectral kernels,
adapted to weight matrices of arbitrary shape.*
- `StateScaler` (line 483) - *Scales every tensor in a state dict from src_d to tgt_d.

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
- `ScalingValidator` (line 635) - *Measures spectral structure preservation before and after scaling.*
- `ModelAssembler` (line 723) - *Loads scaled weights into a fresh TopoGPT2.*
- `CheckpointSaver` (line 751) - *Saves checkpoint, metrics JSON, and text report.*
- `TopoGPT2DModelScaler` (line 860) - *Main orchestrator.

Mirrors the Willmore Crystal scaler pipeline:

  source_grid_size = D_MODEL_src
  target_grid_sizes = [D1, D2, ...]  (progressive)

The torus topology is the structural invariant: RADIAL, ANGULAR,
N_TORUS_NODES, edges_i/j/type, edge_quat are never modified.*

**Functions:**
- `_setup_logger` (line 169)
- `build_parser` (line 1070)
- `config_from_args` (line 1097)
- `main` (line 1119)
- `__post_init__` (line 159)
- `load` (line 184) - *Import and return the topogpt2 module.*
- `read` (line 208) - *Return (state_dict, optional_embedded_config).*
- `_extract` (line 225)
- `reconstruct` (line 245) - *Return a TopoGPT2Config that matches the loaded weights exactly.*
- `_infer` (line 259)
- `_infer_d_head` (line 291)
- `_infer_n_kv` (line 298)
- `_infer_max_seq` (line 308)
- `_infer_torus` (line 315)
- `classify` (line 340) - *Return a semantic role string.

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
- `__init__` (line 388)
- `interpolate_2d` (line 391) - *Scale a 2D weight matrix [M, N] to [M', N'] via spectral interpolation.

Steps:
  1. FFT2 of W.
  2. Zero-pad or centre-crop frequency spectrum to (M', N').
  3. IFFT2.
  4. Amplitude normalisation: ||W'||_F = ||W||_F.*
- `interpolate_1d` (line 421) - *Scale a 1D vector of length L to length L' via spectral interpolation.*
- `_resize_spectrum_2d` (line 452) - *Zero-pad or centre-crop a 2D complex spectrum.*
- `__init__` (line 499)
- `scale` (line 509) - *Produce a complete scaled state dict.*
- `_dispatch` (line 567) - *Route to the correct interpolation method based on shape and role.*
- `_scale_spectral_2d_to` (line 598) - *Scale [in_q, out_q, R, Af] to [in_q', out_q', R, Af].

R and Af are topo-invariant and must not change.*
- `_bilinear_fallback` (line 626)
- `__init__` (line 638)
- `compute` (line 641) - *Compute all configured validation metrics.*
- `check_degradation` (line 656) - *Return True if any metric dropped beyond its tolerance.*
- `_spectral_concentration` (line 690)
- `_phase_coherence` (line 708)
- `assemble` (line 726) - *Instantiate the target model and load scaled weights.*
- `save` (line 754) - *Persist scaled checkpoint and metadata. Returns checkpoint path.*
- `_write_report` (line 815)
- `__init__` (line 872)
- `run` (line 888) - *Execute the full scaling pipeline. Returns per-step result dicts.*
- `_build_target_config` (line 1001) - *Construct a target config with new D_MODEL, preserving torus topology.*
- `_infer_n_heads` (line 1018) - *Find the largest divisor of tgt_d that keeps D_HEAD >= 8.*
- `_infer_n_kv_heads` (line 1033)
- `_print_summary` (line 1047)
- `_cfg_dict` (line 770)

#### `topogpt2_multi_inference.py`
**Path:** `topogpt2_multi_inference.py`

**Classs:**
- `SamplingConfig` (line 60) - *Generation hyper-parameters.*
- `RunConfig` (line 72) - *Top-level execution configuration.*
- `ModuleImporter` (line 95) - *Imports topogpt2_1.py from any filesystem path (cached per process).*
- `CheckpointDiscovery` (line 122) - *Resolves a mixed list of files and directories to concrete checkpoint paths.*
- `CheckpointLoader` (line 164) - *Loads state dicts and any embedded config from checkpoint files.*
- `ConfigReconstructor` (line 219) - *Reconstructs a TopoGPT2Config from weights, inferring every dimension.*
- `TokenizerFactory` (line 315) - *Builds and caches BPETokenizer instances.*
- `GenerationEngine` (line 327) - *Autoregressive generation with top-k, top-p, and repetition penalty.*
- `ModelResult` (line 433) - *Result from running one checkpoint.*
- `MultiInferenceRunner` (line 450) - *Runs one prompt through every checkpoint and collects results.*
- `ResultRenderer` (line 584) - *Formats and prints inference results.*
- `JsonExporter` (line 677) - *Saves results to a JSON file for later analysis.*

**Functions:**
- `_setup_logger` (line 85)
- `_fmt_params` (line 666) - *Format parameter counts as human-readable strings (25.1M, 147.5M).*
- `build_parser` (line 707) - *Build the CLI argument parser.*
- `config_from_args` (line 780) - *Build a RunConfig from parsed CLI arguments.*
- `main` (line 800) - *CLI entry point.*
- `load` (line 100) - *Return the imported module, reusing the cached copy if available.*
- `resolve` (line 127) - *Expand directories and glob patterns into a sorted list of paths.

Args:
    sources: File paths, directory paths, or glob patterns.

Returns:
    Deduplicated, sorted list of existing checkpoint paths.*
- `load` (line 167) - *Return (state_dict, optional_embedded_config).

Handles:
  - .safetensors (raw state dict)
  - .pt / .pth with {'model_state_dict': ..., 'config': ...}
    (produced by the scaler)
  - .pt / .pth plain state dicts*
- `_load_safetensors` (line 183)
- `_load_torch` (line 191)
- `reconstruct` (line 222) - *Return a TopoGPT2Config matching the loaded weights.

Prefers the embedded config (saved by the scaler) but falls back
to full inference from tensor shapes so that original checkpoints
work without any embedded metadata.*
- `_infer` (line 243)
- `_infer_d_head` (line 278)
- `_infer_n_kv` (line 285)
- `_infer_max_seq` (line 295)
- `_infer_torus` (line 302)
- `get` (line 320) - *Return a shared tokenizer instance (built once per process).*
- `__init__` (line 330)
- `generate` (line 334) - *Run generation and return (full_text, n_new_tokens, elapsed_s).

Uses the model's built-in .generate() when repetition_penalty == 1.0
and top_p == 1.0, otherwise falls back to a manual loop that supports
the full sampling configuration.*
- `_fast_generate` (line 361)
- `_manual_generate` (line 372)
- `_apply_repetition_penalty` (line 412)
- `_apply_top_p` (line 424)
- `__init__` (line 453)
- `run` (line 462) - *Execute the full multi-model inference pipeline.*
- `_run_one` (line 499)
- `_make_label` (line 570) - *Extract a short human-readable label from a checkpoint path.*
- `render` (line 590) - *Print prompt header, per-model outputs, and comparison table.*
- `_print_prompt_header` (line 597)
- `_print_model_output` (line 605)
- `_print_comparison_table` (line 628)
- `export` (line 680) - *Serialize results to JSON.*

#### `zeroshot.py`
**Path:** `zeroshot.py`

**Classs:**
- `ExpansionConfig` (line 87) - *All tuneable knobs for the zero-shot expansion procedure.

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
- `TopoGPT2Config` (line 169) - *Minimal reproduction of the model-architecture fields from the original
TopoGPT2Config.  Only the fields required to instantiate the neural
network are present here.*
- `QuaternionOps` (line 254) - *Static quaternion algebra operations in PyTorch.*
- `QuaternionLinear` (line 287) - *Quaternion-valued linear layer.

Performs the Hamilton product W ⊗ x in the quaternion algebra,
using four real weight matrices (one per quaternion component).
Both in_features and out_features must be divisible by 4.*
- `QuaternionSpectralLayer` (line 321) - *2D spectral convolution with quaternion Hamilton product in frequency domain.

Kernel tensors are registered for each quaternion component (w, x, y, z),
each with separate real and imaginary parts for the complex frequency domain.*
- `SpectralAutoencoder` (line 373) - *Spectral autoencoder operating in both 1D (feature axis) and 2D (torus grid).

Encodes via FFT filtering and quaternion projection to a latent space;
decodes back for reconstruction regularisation.  Also exposes a method
for processing the torus grid through stacked QuaternionSpectralLayers.*
- `QuaternionTorusBrain` (line 427) - *Replaces the MLP in each transformer layer.

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
- `SwiGLU` (line 534) - *SwiGLU feed-forward block (LLaMA-style).
inner dimension = round(d_model * expansion) up to multiple of 4.*
- `TopoMoEBrain` (line 556) - *Mixture-of-Experts wrapper around QuaternionTorusBrain.

One always-active shared expert (QuaternionTorusBrain) plus N_EXPERTS
sparse SwiGLU experts selected by a linear router (top-K per token).
When MOE_ENABLED is False this reduces to a plain QuaternionTorusBrain.*
- `RotaryEmbedding` (line 613) - *Rotary Position Embeddings (RoPE) – Su et al., 2021.*
- `RMSNorm` (line 652) - *Root Mean Square Layer Normalization (no bias).*
- `MultiHeadAttention` (line 665) - *Multi-head attention with Flash Attention, RoPE, and Grouped Query Attention.
Supports an optional KV cache for autoregressive generation.*
- `TopoGPT2Layer` (line 719) - *Single transformer layer: pre-norm attention + pre-norm TopoMoEBrain.
Gradient checkpointing is disabled during inference/expansion.*
- `TopoGPT2` (line 749) - *TopoGPT2: causal language model with quaternion torus topology.

Embedding -> N_LAYERS x (Attention + QuaternionTorusBrain) -> RMSNorm -> LM head.
The embedding and LM head share weights (weight tying).*
- `SpectralKernelInterpolator` (line 828) - *Interpolates QuaternionSpectralLayer kernels to a new (grid_h, grid_w).

The kernels live in frequency space with shape [in_q, out_q, freq_h, freq_w]
where freq_w = grid_w // 2 + 1.  We treat (freq_h, freq_w) as a 2D spatial
grid and apply torch.nn.functional.interpolate.*
- `NodeEmbedInterpolator` (line 876) - *Interpolates the torus node embedding table to a new (n_radial, n_angular).

node_embed has shape [n_nodes, d_model] = [n_radial * n_angular, d_model].
We reshape to a 2D spatial grid [n_radial, n_angular, d_model], transpose
to [d_model, n_radial, n_angular], interpolate per feature dimension, then
reshape back.*
- `TorusBrainExpander` (line 917) - *Transfers weights from a source QuaternionTorusBrain to a target one with
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
- `TopoMoEBrainExpander` (line 1009) - *Transfers weights from a source TopoMoEBrain to a target one.

The shared QuaternionTorusBrain is expanded via TorusBrainExpander.
All SwiGLU expert weights and the router are copied verbatim (they do not
depend on torus resolution – they process flat token embeddings).*
- `TopoGPT2Expander` (line 1052) - *Zero-shot torus expansion of a complete TopoGPT2 model.

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
- `CheckpointIO` (line 1120) - *Loads and saves TopoGPT2 weights using safetensors.
Falls back to torch.save / torch.load when safetensors is unavailable.*
- `CheckpointArch` (line 1216) - *Architecture hyperparameters inferred directly from checkpoint tensor shapes.

All fields that affect tensor dimensions are recovered so that the source
model can be instantiated to exactly match the saved weights, regardless of
what the CLI scale preset would compute.*
- `CheckpointArchProber` (line 1239) - *Infers all architecture hyperparameters from the raw tensor shapes stored
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
- `ExpansionValidator` (line 1463) - *Runs a forward-pass sanity check on the expanded model.

Checks:
- The model produces finite logits for a random token sequence.
- The model produces finite logits for the given text prompt (if tiktoken
  is available).
- The model can generate a short sequence without crashing.*
- `ZeroShotExpansionPipeline` (line 1550) - *Orchestrates the full zero-shot expansion workflow:

1. Read source torus geometry from checkpoint metadata (or config defaults).
2. Build source and target TopoGPT2 configs.
3. Instantiate source and target models.
4. Load source weights into the source model.
5. Expand weights via TopoGPT2Expander.
6. Optionally validate the expanded model.
7. Save the expanded model.

No training is performed at any stage.*

**Functions:**
- `build_logger` (line 69) - *Return a stderr logger with timestamp formatting.*
- `build_arg_parser` (line 1709) - *Construct and return the CLI argument parser.*
- `main` (line 1774) - *CLI entry point.*
- `validate_geometry` (line 140) - *Raise ValueError for impossible torus configurations.*
- `src_nodes` (line 154)
- `tgt_nodes` (line 158)
- `__post_init__` (line 222)
- `hamilton_product` (line 258)
- `normalize` (line 269)
- `conjugate` (line 273)
- `rotate_vector` (line 278)
- `__init__` (line 296)
- `forward` (line 310)
- `__init__` (line 329)
- `_kernel` (line 344)
- `_contract` (line 347)
- `forward` (line 350)
- `__init__` (line 382)
- `_filter1d` (line 404)
- `encode` (line 409)
- `decode` (line 412)
- `forward` (line 415)
- `process_torus_grid` (line 420)
- `__init__` (line 443)
- `_build_torus_graph` (line 468)
- `_torus_soft_assign` (line 484)
- `_message_passing` (line 495)
- `forward` (line 509)
- `__init__` (line 540)
- `forward` (line 552)
- `__init__` (line 565)
- `_route` (line 581)
- `forward` (line 604)
- `__init__` (line 618)
- `_build_cache` (line 626)
- `_rotate_half` (line 633)
- `forward` (line 637)
- `__init__` (line 655)
- `forward` (line 660)
- `__init__` (line 671)
- `forward` (line 686)
- `__init__` (line 725)
- `_forward_impl` (line 734)
- `forward` (line 743)
- `__init__` (line 757)
- `_init_weights` (line 771)
- `forward` (line 778)
- `generate` (line 795) - *Top-k autoregressive generation with KV cache.*
- `__init__` (line 837)
- `_interp2d` (line 840) - *Interpolate a 4D real tensor [in_q, out_q, h, w] to [in_q, out_q, tgt_h, tgt_w].*
- `transfer` (line 856) - *Copy and interpolate all kernel parameters from src_layer to tgt_layer.*
- `__init__` (line 886)
- `transfer` (line 889) - *Interpolate src_embed [src_R*src_A, D] into tgt_embed [tgt_R*tgt_A, D].*
- `__init__` (line 936)
- `expand` (line 946) - *Mutates tgt in-place to carry the expanded weights of src.*
- `__init__` (line 1018)
- `expand` (line 1031) - *Mutates tgt in-place.*
- `__init__` (line 1072)
- `expand` (line 1085) - *Expand src into tgt.  Returns tgt with all weights transferred.
tgt must have already been instantiated with the target config.*
- `__init__` (line 1126)
- `load` (line 1133) - *Load weights into model from path.  Returns the metadata dict.
Supports: .safetensors, .pt, .pth (state_dict or wrapped dict).

Weight tying: checkpoints saved by this script omit lm_head.weight
(it is redundant with token_embed.weight).  After loading, the tie is
restored by pointing lm_head.weight at token_embed.weight.*
- `save` (line 1177) - *Save model weights to path.

Weight tying: token_embed.weight and lm_head.weight share the same
storage tensor.  safetensors rejects aliased tensors with a RuntimeError.
We exclude lm_head.weight from the state dict before saving (it is
redundant) and record the tie in metadata so load() can restore it.*
- `__init__` (line 1286)
- `_load_shapes` (line 1289) - *Return {key: shape} for every tensor in the checkpoint.*
- `_load_metadata` (line 1304) - *Return safetensors string metadata dict (empty when unavailable).*
- `probe` (line 1315) - *Infer CheckpointArch from the checkpoint at path.

Parameters
----------
path            : checkpoint file path
fallback_radial : used only when torus_spectral key is absent
fallback_angular: used only when torus_spectral key is absent*
- `_infer_d_head_fallback` (line 1433) - *Fallback d_head inference when rope.inv_freq is absent.

d_head must divide both q_out and d_model, and n_heads % n_kv_heads == 0.
Returns the largest valid candidate (most heads, smallest d_head is wrong
intuition; we pick the value that makes n_kv_heads a proper divisor of n_heads
and n_heads a standard power-of-2 count).*
- `__init__` (line 1474)
- `validate` (line 1477) - *Return True if all checks pass, False otherwise.
Does not raise; errors are logged as warnings.*
- `__init__` (line 1565)
- `_config_from_arch` (line 1570) - *Build a TopoGPT2Config whose tensor dimensions exactly match arch.

The scale preset is applied first (to get sane defaults for fields not
covered by arch), then every field that affects tensor shapes is
overwritten with the probed value.  This guarantees that the
instantiated model accepts the checkpoint weights without size mismatches.*
- `_build_metadata_for_save` (line 1609)
- `run` (line 1631) - *Execute the full expansion pipeline.  Returns the expanded model.*

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
