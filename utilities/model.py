# Class to create and handle model access, initialization, and context
import requests
import json
from huggingface_hub import hf_hub_download
from llama_cpp import Llama
import os
import logging

import sys
import importlib.util

def load_config():
    # Determine the directory of the running executable or script
    if getattr(sys, 'frozen', False):  # Check if running in a PyInstaller bundle
        base_path = sys._MEIPASS  # Temporary folder where PyInstaller extracts files
        # Look for `config.py` in the same directory as the executable
        config_path = os.path.join(os.path.dirname(sys.executable), 'config.py')
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        # Look for `config.py` relative to the source structure
        config_path = os.path.join(base_path, '..', 'config.py')

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")

    spec = importlib.util.spec_from_file_location("config", config_path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    return config

config = load_config()

logger = logging.getLogger(__name__)

class Model:
    def __init__(self):
        save_dir = os.path.abspath(config.HF_MODEL_SAVE_DIR)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        logger.info(f"Model type: {config.MODEL_TYPE}")
        if config.MODEL_TYPE == 'huggingface':
            local_model_path = os.path.join(save_dir, config.HF_FILENAME)
            if os.path.exists(local_model_path):
                self.model = local_model_path
                logger.info(f"Using local model at {local_model_path}")
            else:
                try:
                    logger.info(f"Downloading model {config.HF_REPO_ID} from huggingface")
                    logger.info(f"Saving model to {save_dir}")
                    self.model = hf_hub_download(
                        repo_id=config.HF_REPO_ID,
                        filename=config.HF_FILENAME,
                        cache_dir=save_dir,
                        local_dir=save_dir
                    )
                except Exception as e:
                    logger.error(f"Error downloading model: {e}")
                    raise e
            
            self.llm = Llama(
                model_path=self.model,
                n_ctx= config.HF_MAX_LENGTH,  # Adjust context size as needed
                n_threads=4,  # Adjust threads based on your CPU
                # ... other parameters you want to set
                verbose=False
            )
            
        elif config.MODEL_TYPE == 'local':
            logger.info(f"Using local model at {config.LOCAL_MODEL_PATH}")
            # TODO fix, maybe use huggingface api for local models instead as we are currently using llama only
            self.llm = Llama(
                model_path=self.model,
                n_ctx= config.LOCAL_MODEL_MAX_LENGTH,  # Adjust context size as needed
                n_threads=12,  # Adjust threads based on your CPU
                # ... other parameters you want to set
                verbose=False
            )
        elif config.MODEL_TYPE == 'ollama':
            logger.info(f"Using ollama model {config.OLLAMA_MODEL}")
            pass

    def generate_ollama(self, prompt):
        data = {
            "prompt": prompt,
            "model": config.OLLAMA_MODEL,
            "options": config.OLLAMA_PARAMS
        }
        response = requests.post(
            f'http://{config.OLLAMA_HOST}:{config.OLLAMA_PORT}/{config.OLLAMA_API.strip('/')}', json=data)

        # load jsonlines from response
        all_responses = [json.loads(x)['response']
                         for x in response.text.split('\n') if x]
        return ''.join(all_responses)

    def generate_local(self, prompt):
        if config.MODEL_TYPE == 'huggingface':
            return self.llm(prompt, max_tokens=config.HF_MAX_LENGTH)["choices"][0]["text"]
        if config.MODEL_TYPE == 'local':
            return self.llm(prompt, max_tokens=config.LOCAL_MODEL_MAX_LENGTH)["choices"][0]["text"]

    def generate(self, prompt):
        if config.MODEL_TYPE == 'huggingface':
            return self.generate_local(prompt)
        elif config.MODEL_TYPE == 'local':
            return self.generate_local(prompt)
        elif config.MODEL_TYPE == 'ollama':
            return self.generate_ollama(prompt)
