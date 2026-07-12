# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 12 | **Total Symbols Extracted:** 1020 | **Total Imports:** 211

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

**Classes:**
- `TopoGPT2Config` (line 55) `class TopoGPT2Config` - *Configuración completa para TopoGPT2.*
- `QuaternionOps` (line 177) `class QuaternionOps` - *Operaciones de cuaterniones puras en PyTorch.
Representación: [..., 4]  donde last dim = [w, x, y, z]
q = w + x*i + y*j + z*k*
- `QuaternionLinear` (line 216) `class QuaternionLinear` - *Capa lineal con pesos cuaterniones.

Implementa la multiplicación W * x en el álgebra de cuaterniones:
- W = Ww + Wx*i + Wy*j + Wz*k  (cuaternión de pesos)
- x = xw + xx*i + xy*j + xz*k  (cuaternión de entrada)
- out = W * x  (producto de Hamilton extendido a vectores)

Parámetros: 4 matrices reales de forma [out_q, in_q]*
- `QuaternionSpectralLayer` (line 261) `class QuaternionSpectralLayer` - *Convolución espectral 2D con cuaterniones y producto de Hamilton completo.

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
- `SpectralAutoencoder` (line 348) `class SpectralAutoencoder` - *Autoencoder espectral con cuaterniones.

Opera en dos niveles:
1. Espectral 1D sobre el vector de features (FFT sobre dim D_MODEL):
   captura la espectrografía global del embedding.
2. Espectral 2D sobre el grid del toro (QuaternionSpectralLayer):
   captura correlaciones espaciales en la topología.

Devuelve (latent, recon_loss) para regularización.*
- `QuaternionTorusBrain` (line 431) `class QuaternionTorusBrain` - *Reemplaza el MLP en cada capa del transformer.

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
- `RotaryEmbedding` (line 648) `class RotaryEmbedding` - *Rotary Position Embeddings (RoPE) - Su et al., 2021.
Codifica la posición como rotaciones del espacio de atención,
naturalmente relativas y sin parámetros extra.*
- `RMSNorm` (line 696) `class RMSNorm` - *Root Mean Square Layer Normalization (sin bias). Más estable que LayerNorm.*
- `SwiGLU` (line 713) `class SwiGLU` - *SwiGLU: SiLU(gate(x)) * up(x) -> down
Usado en LLaMA 2/3, Qwen, Mistral en lugar de GELU-FFN.
Dimension interna: 8/3 * d_model (convención LLaMA, redondeada a múltiplo de 4).*
- `TopoMoEBrain` (line 742) `class TopoMoEBrain` - *Mixture of Experts sobre la capa topologica.

Arquitectura (inspirada en DeepSeek-MoE / Mixtral):
  - 1 experto compartido: QuaternionTorusBrain (siempre activo)
  - N_EXPERTS expertos SwiGLU ligeros (activacion esparsa: Top-K por token)
  - Router: Linear(D, N_EXPERTS) + softmax → top-K

Load-balancing loss (auxiliar): penaliza si un experto acapara todos los tokens.
Activa MOE_TOP_K de N_EXPERTS expertos por token.

Sin MoE (MOE_ENABLED=False): se comporta como QuaternionTorusBrain puro.*
- `MultiHeadAttention` (line 847) `class MultiHeadAttention` - *Multi-head attention con:
- Flash Attention (scaled_dot_product_attention de PyTorch 2.0+)
- Rotary Position Embeddings (RoPE)
- GQA (Grouped Query Attention): N_KV_HEADS < N_HEADS, reduce VRAM de K/V
- KV Cache para inferencia autoregresiva eficiente
- Temperatura termodinámica aprendible*
- `TopoGPT2Layer` (line 929) `class TopoGPT2Layer` - *Capa del transformer con TopoMoEBrain (TopoBrain + MoE SwiGLU experts).

Esquema pre-norm (estilo LLaMA):
    x = x + Attention_GQA(RMSNorm(x))
    x = x + TopoMoEBrain(RMSNorm(x))*
- `TopoGPT2` (line 976) `class TopoGPT2` - *TopoGPT2: Transformer de lenguaje con TopoBrain cuaternión-espectral.

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
- `TokenizedDataset` (line 1170) `class TokenizedDataset` - *Dataset de tokens para language modeling (next-token prediction).

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

**Functions:**
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
- `QuaternionLinear` (line 219) `class QuaternionLinear` - *Linear layer in the quaternion algebra.

Implements the Hamilton product W ⊗ x using four real weight matrices.
Both in_features and out_features must be divisible by 4.*
- `QuaternionSpectralLayer` (line 252) `class QuaternionSpectralLayer` - *2-D spectral convolution using the quaternion Hamilton product in the
frequency domain.  Each quaternion component (w, x, y, z) has an
independent complex kernel (real + imaginary parts).*
- `SpectralAutoencoder` (line 306) `class SpectralAutoencoder` - *Spectral autoencoder: 1-D FFT filtering + quaternion projection for
encoding/decoding, plus stacked QuaternionSpectralLayers for the torus grid.*
- `QuaternionTorusBrain` (line 358) `class QuaternionTorusBrain` - *Replaces the MLP in each transformer layer.

Fully vectorised pipeline:
    [B, S, D] -> spectral AE -> torus projection -> soft node assignment
    -> 2-D spectral layer on grid -> quaternion message-passing -> readout
    -> [B, S, D]*
- `SwiGLU` (line 462) `class SwiGLU` - *SwiGLU feed-forward block (LLaMA-style).*
- `TopoMoEBrain` (line 481) `class TopoMoEBrain` - *Mixture-of-Experts wrapper: one always-active QuaternionTorusBrain plus
N sparse SwiGLU experts selected by a linear router (top-K per token).
When moe_enabled is False this reduces to a plain QuaternionTorusBrain.*
- `RotaryEmbedding` (line 537) `class RotaryEmbedding` - *Rotary Position Embeddings (RoPE) – Su et al., 2021.*
- `RMSNorm` (line 577) `class RMSNorm` - *Root Mean Square Layer Normalization (no bias).*
- `MultiHeadAttention` (line 589) `class MultiHeadAttention` - *GQA-capable multi-head attention with Flash Attention, RoPE, and KV cache.*
- `TopoGPT2Layer` (line 638) `class TopoGPT2Layer` - *Pre-norm transformer layer: attention + TopoMoEBrain.*
- `TopoGPT2` (line 660) `class TopoGPT2` - *TopoGPT2: causal language model with quaternion torus topology.
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
- `QuaternionLinear` (line 195) `class QuaternionLinear`
- `QuaternionSpectralLayer` (line 220) `class QuaternionSpectralLayer`
- `SpectralAutoencoder` (line 262) `class SpectralAutoencoder`
- `QuaternionTorusBrain` (line 312) `class QuaternionTorusBrain`
- `RotaryEmbedding` (line 408) `class RotaryEmbedding`
- `RMSNorm` (line 440) `class RMSNorm`
- `SwiGLU` (line 451) `class SwiGLU`
- `TopoMoEBrain` (line 468) `class TopoMoEBrain`
- `MultiHeadAttention` (line 522) `class MultiHeadAttention`
- `TopoGPT2Layer` (line 568) `class TopoGPT2Layer`
- `TopoGPT2` (line 590) `class TopoGPT2`
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

**Functions:**
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
- `RewardModel` (line 152) `class RewardModel` - *Lightweight reward model for scoring generated responses.*
- `ExperienceBuffer` (line 189) `class ExperienceBuffer` - *Stores trajectories for PPO training with advantage computation.*
- `ValueHead` (line 240) `class ValueHead` - *Scalar value estimation head attached to TopoGPT2 for PPO.*
- `PPOTrainer` (line 262) `class PPOTrainer` - *Proximal Policy Optimization trainer for TopoGPT2 alignment.*
- `ChatAgent` (line 519) `class ChatAgent` - *High-level interface for RL-aligned TopoGPT2 as chatbot.*

**Functions:**
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
- `QuaternionLinear` (line 216) `class QuaternionLinear` - *Capa lineal con pesos cuaterniones.

Implementa la multiplicación W * x en el álgebra de cuaterniones:
- W = Ww + Wx*i + Wy*j + Wz*k  (cuaternión de pesos)
- x = xw + xx*i + xy*j + xz*k  (cuaternión de entrada)
- out = W * x  (producto de Hamilton extendido a vectores)

Parámetros: 4 matrices reales de forma [out_q, in_q]*
- `QuaternionSpectralLayer` (line 261) `class QuaternionSpectralLayer` - *Convolución espectral 2D con cuaterniones y producto de Hamilton completo.

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
- `SpectralAutoencoder` (line 348) `class SpectralAutoencoder` - *Autoencoder espectral con cuaterniones.

Opera en dos niveles:
1. Espectral 1D sobre el vector de features (FFT sobre dim D_MODEL):
   captura la espectrografía global del embedding.
2. Espectral 2D sobre el grid del toro (QuaternionSpectralLayer):
   captura correlaciones espaciales en la topología.

Devuelve (latent, recon_loss) para regularización.*
- `QuaternionTorusBrain` (line 431) `class QuaternionTorusBrain` - *Reemplaza el MLP en cada capa del transformer.

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
- `RotaryEmbedding` (line 648) `class RotaryEmbedding` - *Rotary Position Embeddings (RoPE) - Su et al., 2021.
Codifica la posición como rotaciones del espacio de atención,
naturalmente relativas y sin parámetros extra.*
- `RMSNorm` (line 696) `class RMSNorm` - *Root Mean Square Layer Normalization (sin bias). Más estable que LayerNorm.*
- `SwiGLU` (line 713) `class SwiGLU` - *SwiGLU: SiLU(gate(x)) * up(x) -> down
Usado en LLaMA 2/3, Qwen, Mistral en lugar de GELU-FFN.
Dimension interna: 8/3 * d_model (convención LLaMA, redondeada a múltiplo de 4).*
- `TopoMoEBrain` (line 742) `class TopoMoEBrain` - *Mixture of Experts sobre la capa topologica.

Arquitectura (inspirada en DeepSeek-MoE / Mixtral):
  - 1 experto compartido: QuaternionTorusBrain (siempre activo)
  - N_EXPERTS expertos SwiGLU ligeros (activacion esparsa: Top-K por token)
  - Router: Linear(D, N_EXPERTS) + softmax → top-K

Load-balancing loss (auxiliar): penaliza si un experto acapara todos los tokens.
Activa MOE_TOP_K de N_EXPERTS expertos por token.

Sin MoE (MOE_ENABLED=False): se comporta como QuaternionTorusBrain puro.*
- `MultiHeadAttention` (line 847) `class MultiHeadAttention` - *Multi-head attention con:
- Flash Attention (scaled_dot_product_attention de PyTorch 2.0+)
- Rotary Position Embeddings (RoPE)
- GQA (Grouped Query Attention): N_KV_HEADS < N_HEADS, reduce VRAM de K/V
- KV Cache para inferencia autoregresiva eficiente
- Temperatura termodinámica aprendible*
- `TopoGPT2Layer` (line 929) `class TopoGPT2Layer` - *Capa del transformer con TopoMoEBrain (TopoBrain + MoE SwiGLU experts).

Esquema pre-norm (estilo LLaMA):
    x = x + Attention_GQA(RMSNorm(x))
    x = x + TopoMoEBrain(RMSNorm(x))*
- `TopoGPT2` (line 976) `class TopoGPT2` - *TopoGPT2: Transformer de lenguaje con TopoBrain cuaternión-espectral.

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
- `TokenizedDataset` (line 1170) `class TokenizedDataset` - *Dataset de tokens para language modeling (next-token prediction).

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

**Functions:**
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

**Functions:**
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

**Functions:**
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

**Functions:**
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

**Functions:**
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
- `QuaternionLinear` (line 287) `class QuaternionLinear` - *Quaternion-valued linear layer.

Performs the Hamilton product W ⊗ x in the quaternion algebra,
using four real weight matrices (one per quaternion component).
Both in_features and out_features must be divisible by 4.*
- `QuaternionSpectralLayer` (line 321) `class QuaternionSpectralLayer` - *2D spectral convolution with quaternion Hamilton product in frequency domain.

Kernel tensors are registered for each quaternion component (w, x, y, z),
each with separate real and imaginary parts for the complex frequency domain.*
- `SpectralAutoencoder` (line 373) `class SpectralAutoencoder` - *Spectral autoencoder operating in both 1D (feature axis) and 2D (torus grid).

Encodes via FFT filtering and quaternion projection to a latent space;
decodes back for reconstruction regularisation.  Also exposes a method
for processing the torus grid through stacked QuaternionSpectralLayers.*
- `QuaternionTorusBrain` (line 427) `class QuaternionTorusBrain` - *Replaces the MLP in each transformer layer.

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
- `SwiGLU` (line 534) `class SwiGLU` - *SwiGLU feed-forward block (LLaMA-style).
inner dimension = round(d_model * expansion) up to multiple of 4.*
- `TopoMoEBrain` (line 556) `class TopoMoEBrain` - *Mixture-of-Experts wrapper around QuaternionTorusBrain.

One always-active shared expert (QuaternionTorusBrain) plus N_EXPERTS
sparse SwiGLU experts selected by a linear router (top-K per token).
When MOE_ENABLED is False this reduces to a plain QuaternionTorusBrain.*
- `RotaryEmbedding` (line 613) `class RotaryEmbedding` - *Rotary Position Embeddings (RoPE) – Su et al., 2021.*
- `RMSNorm` (line 652) `class RMSNorm` - *Root Mean Square Layer Normalization (no bias).*
- `MultiHeadAttention` (line 665) `class MultiHeadAttention` - *Multi-head attention with Flash Attention, RoPE, and Grouped Query Attention.
Supports an optional KV cache for autoregressive generation.*
- `TopoGPT2Layer` (line 719) `class TopoGPT2Layer` - *Single transformer layer: pre-norm attention + pre-norm TopoMoEBrain.
Gradient checkpointing is disabled during inference/expansion.*
- `TopoGPT2` (line 749) `class TopoGPT2` - *TopoGPT2: causal language model with quaternion torus topology.

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
