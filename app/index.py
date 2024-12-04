from elasticsearch import Elasticsearch
from app.config import settings

class ElasticsearchIndex:
    def __init__(self):
        self.es = Elasticsearch(settings.elasticsearch_url)

    def create_index(self):
        if not self.es.indices.exists(index=settings.index_name):
            self.es.indices.create(index=settings.index_name)

    def index_document(self, doc_id, content, embedding):
        doc = {
            "content": content,
            "embedding": embedding.tolist()
        }
        self.es.index(index=settings.index_name, id=doc_id, body=doc)

# Ejemplo:
indexer = ElasticsearchIndex()
indexer.create_index()
indexer.index_document(1, "Ejemplo de contenido", [0.1, 0.2, 0.3])
