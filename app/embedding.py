from models.bert_model import EmbeddingModel
from app.data_loader import load_data
from app.index import ElasticsearchIndex

def generate_and_index_embeddings(data_file):
    model = EmbeddingModel(settings.embedding_model)
    indexer = ElasticsearchIndex()
    indexer.create_index()

    data = load_data(data_file)
    for doc in data:
        embedding = model.get_embedding(doc["content"])
        indexer.index_document(doc["id"], doc["content"], embedding)
