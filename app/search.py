from elasticsearch import Elasticsearch
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from app.config import settings

class SearchEngine:
    def __init__(self):
        self.es = Elasticsearch(settings.elasticsearch_url)

    def search(self, query_embedding, top_k=5):
        # Recuperar todos los documentos
        res = self.es.search(index=settings.index_name, body={"query": {"match_all": {}}})
        docs = res["hits"]["hits"]

        # Calcular similitud coseno
        similarities = []
        for doc in docs:
            doc_vector = np.array(doc["_source"]["embedding"])
            similarity = cosine_similarity([query_embedding], [doc_vector])[0][0]
            similarities.append((doc["_source"]["content"], similarity))

        # Ordenar por similitud y devolver los mejores resultados
        similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
        return similarities[:top_k]
