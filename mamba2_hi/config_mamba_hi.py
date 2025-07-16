from dataclasses import dataclass, field
from transformers.configuration_utils import PretrainedConfig

@dataclass
class MambaHiConfig(PretrainedConfig):

    d_model: int = 2048
    d_intermediate: int = 0
    n_layer: int = 48
    vocab_size: int = 50277
    ssm_cfg: dict = field(default_factory=lambda: {'layer': 'Mamba2'})
    attn_layer_idx: list = field(default_factory=list)
    attn_cfg: dict = field(default_factory=dict)
    rms_norm: bool = True
    residual_in_fp32: bool = True
    fused_add_norm: bool = True
    pad_vocab_size_multiple: int = 16
    tie_embeddings: bool = True
    tie_word_embeddings: bool = True
    max_position_embeddings: int = 2048
    kernel_size: int = 3
    strength: float = 1.0
    sigma: float = 3
    n_layers: int = 4
