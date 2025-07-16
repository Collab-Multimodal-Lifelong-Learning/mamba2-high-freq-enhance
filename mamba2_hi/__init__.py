from .modeling_mamba_hi import MambaHiLMHeadModel
from .config_mamba_hi import MambaHiConfig

MODEL_DICT = {
    "mamba2_hi": MambaHiLMHeadModel,
    }


CONFIG_DICT = {
    "mamba2_hi": MambaHiConfig,
}
