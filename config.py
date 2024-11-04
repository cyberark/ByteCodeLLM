# Utility executables
PYCDAS_PATH = '/usr/local/bin/pycdas' # 'executables_hidden/pycdas'
PYCDC_PATH = '/usr/local/bin/pycdc' # 'executables_hidden/pycdc'

# Types include 'huggingface', 'local', 'ollama'
MODEL_TYPE = 'huggingface'
# Huggingface model parameters
HF_MODEL_SAVE_DIR = "cache"
HF_REPO_ID = "mradermacher/Gemma-2-Ataraxy-v2-9B-GGUF"
HF_FILENAME = "Gemma-2-Ataraxy-v2-9B.Q8_0.gguf"
HF_MODEL_PARAMS = {"top_p": 0.95, "temperature": 0.5}
HF_MAX_LENGTH = 1024 * 6
# Local model parameters
LOCAL_MODEL_PATH = "path/to/local/model"
LOCAL_MODEL_PARAMS = {"top_p": 0.95, "temperature": 0.5}
LOCAL_MODEL_MAX_LENGTH = 1024 * 6
# Ollama model parameters
OLLAMA_HOST = "localhost"
OLLAMA_PORT = 11434
OLLAMA_API = "/api/generate"
OLLAMA_MODEL = "mistral:latest"
OLLAMA_PARAMS = {"top_p": 0.95, "temperature": 0.5}
OLLAMA_MAX_LENGTH = 1024 * 6
