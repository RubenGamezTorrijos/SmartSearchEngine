import uvicorn
from app.api import app
from app.embedding import generate_and_index_embeddings

if __name__ == "__main__":
    # Generar embeddings e indexar documentos (solo una vez)
    generate_and_index_embeddings("data/documents.json")

    # Ejecutar el servidor
    uvicorn.run(app, host="127.0.0.1", port=8000)
