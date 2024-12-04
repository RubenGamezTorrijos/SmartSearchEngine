from transformers import AutoModel, AutoTokenizer
import torch

class EmbeddingModel:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def get_embedding(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        outputs = self.model(**inputs)
        # Usamos el vector CLS como embedding
        return outputs.last_hidden_state[:, 0, :].detach().numpy()

# Ejemplo de inicialización
model = EmbeddingModel("sentence-transformers/all-MiniLM-L6-v2")
