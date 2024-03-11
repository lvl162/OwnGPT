# -*- coding: utf-8 -*-
"""
Create ownChat  private gpt
@author: Lawrence P.J.
"""
persist_directory = ".\\chroma_db"
source_directory = ".\\source_documents"
embeddings_model_name = "sentence-transformers/all-mpnet-base-v2"
collection_name = "collection_name"
model_path = ".\\Models\\zephyr-7b-beta.Q4_0.gguf"
model_n_ctx = 5000
model_type = "LlamaCpp"
