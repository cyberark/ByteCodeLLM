# Class to create and handle model access, initialization, and context
import requests
import json
from huggingface_hub import hf_hub_download
from c import Llama
import os
import config
 



class Model:

    def __init__(self, model, model_args={"top_p": 0.95, "temperature": 0.5}):
        save_dir = os.path.dirname(os.path.realpath(__file__))
        self.mode = model
        self.model_args = model_args
        if config.REPO_ID and config.FILENAME:
            try:
                self.model = hf_hub_download(\
                    repo_id=config.REPO_ID, filename=config.FILENAME \
                    ,cache_dir = save_dir,local_dir = save_dir\
                         ,token="***REMOVED***"\
                            )
            except Exception as e:
                print(e)
        return



    def load_model(self):
        pass

    def generate_ollama(self, prompt):
        data = {
            "prompt": prompt,
            "model": self.model,
            "options": self.model_args
        }
        response = requests.post(f'http://localhost:11434/api/generate', json=data)

        # load jsonlines from response
        all_jsons = response.text.split('\n')

        jsons = []
        for j in all_jsons:
            try:
                jsons.append(json.loads(j))
            except:
                pass

        # collect responses into one string
        responses = ""
        for j in jsons:
            responses += j['response']

        
        return responses

    def generate_local(self, prompt):
        llm = Llama(
            model_path=self.model,
            n_ctx=4096,  # Adjust context size as needed
            n_threads=2,  # Adjust threads based on your CPU
            # ... other parameters you want to set
        )
        # Generate text
        responses = llm(prompt)#, stop=["\n"])  # Adjust parameters as needed
        return responses

    def generate(self, prompt):
        self.generate_local(self, prompt)

