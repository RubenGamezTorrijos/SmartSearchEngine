from pydantic import BaseSettings

class Settings(BaseSettings):
    elasticsearch_url: str = "http://localhost:9200"
    index_name: str = "documents"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

settings = Settings()
