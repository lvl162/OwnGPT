import os
from dotenv import load_dotenv
from chromadb.config import Settings
import owngptsettings

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
        chroma_db_impl='duckdb+parquet',
        persist_directory=owngptsettings.persist_directory,
        anonymized_telemetry=False
)
