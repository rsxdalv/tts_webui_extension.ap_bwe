"""Functions for downloading AP-BWE models from HuggingFace Hub."""

import os
from huggingface_hub import hf_hub_download

DEFAULT_MODEL_DIR = "./data/models/ap_bwe"
HUGGINGFACE_REPO = "rsxdalv/AP-BWE"

def ensure_model_downloaded(model_name, model_dir=DEFAULT_MODEL_DIR):
    """Check if model exists locally, download from HuggingFace if not.
    
    Args:
        model_name: The name of the model to download
        model_dir: Directory to store models. Defaults to DEFAULT_MODEL_DIR.
    """
    model_dir_name = os.path.dirname(model_name)
    base_name = os.path.basename(model_name)
    
    full_model_dir = os.path.join(model_dir, "weights", model_dir_name)
    safetensors_path = os.path.join(model_dir, "weights", model_dir_name, base_name)
    config_path = os.path.join(full_model_dir, "config.json")
    
    os.makedirs(full_model_dir, exist_ok=True)
    
    files_to_download = [
        (f"weights/{model_dir_name}/{base_name}", safetensors_path),
        (f"weights/{model_dir_name}/config.json", config_path)
    ]
    
    for remote_path, local_path in files_to_download:
        if not os.path.isfile(local_path):
            try:
                hf_hub_download(
                    repo_id=HUGGINGFACE_REPO,
                    filename=remote_path,
                    local_dir=model_dir,
                    local_dir_use_symlinks=False
                )
                print(f"Downloaded {remote_path} successfully.")
            except Exception as e:
                print(f"Error downloading {remote_path}: {e}")
                return False
    
    return True

def get_default_checkpoint(model_type, model_dir=DEFAULT_MODEL_DIR):
    """Get the default checkpoint path based on model type and ensure it's downloaded.
    
    Args:
        model_type: Type of model to download (e.g., "16kHz (8kHz input)")
        model_dir: Directory to store models. Defaults to DEFAULT_MODEL_DIR.
    """
    model_paths = {
        "16kHz (2kHz input)": "2kto16k/g_2kto16k.safetensors",
        "16kHz (4kHz input)": "4kto16k/g_4kto16k.safetensors",
        "16kHz (8kHz input)": "8kto16k/g_8kto16k.safetensors",
        "48kHz (8kHz input)": "8kto48k/g_8kto48k.safetensors",
        "48kHz (12kHz input)": "12kto48k/g_12kto48k.safetensors",
        "48kHz (16kHz input)": "16kto48k/g_16kto48k.safetensors", 
        "48kHz (24kHz input)": "24kto48k/g_24kto48k.safetensors"
    }
    
    model_path = model_paths.get(model_type, "")
    if not model_path:
        return ""
    
    ensure_model_downloaded(model_path, model_dir)
    
    return os.path.join(model_dir, "weights", model_path)
