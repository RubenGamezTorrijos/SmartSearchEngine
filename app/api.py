from fastapi import FastAPI
from app.search import SearchEngine
from models.bert_model import EmbeddingModel

app = FastAPI()
search_engine = SearchEngine()
model = EmbeddingModel(settings.embedding_model)

@app.get("/search/")
def search(query: str, top_k: int = 5):
    query_embedding = model.get_embedding(query)
    results = search_engine.search(query_embedding, top_k)
    return {"results": results}
