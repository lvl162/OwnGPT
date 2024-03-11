# -*- coding: utf-8 -*-
"""
Create ownChat  private gpt
@author: Lawrence P.J.
"""
from dotenv import load_dotenv

load_dotenv()

persist_directory = ".\\chroma_db" #"D:\\gitProjects\\ML\\OwnGPT\\db" #os.environ.get('PERSIST_DIRECTORY')
#persist_directory = ".\\OwnGPT\\db"
source_directory = ".\\source_documents" # os.environ.get('SOURCE_DIRECTORY', 'source_documents')
embeddings_model_name = "sentence-transformers/all-mpnet-base-v2" # os.environ.get('EMBEDDINGS_MODEL_NAME')
collection_name = "collection_name"
#model_path = ".\\Models\\zephyr-7b-beta.gguf" # os.environ.get('MODEL_PATH')
model_path = ".\\Models\\zephyr-7b-beta.Q4_0.gguf"
#model_path = ".\\Models\\starcoder2-15b.gguf"
model_n_ctx = 5000 # os.environ.get('MODEL_N_CTX')
model_type = "LlamaCpp" # os.environ.get('MODEL_TYPE')
#model_type = "GPT4All"
