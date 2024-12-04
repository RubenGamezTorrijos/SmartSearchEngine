# Buscador Semántico en Python

Este proyecto es un buscador semántico modular y profesional diseñado para comprender consultas en lenguaje natural y proporcionar resultados relevantes. Utiliza tecnologías modernas como **FastAPI**, **transformers** para embeddings semánticos y **Elasticsearch** como motor de búsqueda.

## Funcionalidades
- Procesamiento de lenguaje natural para consultas en texto libre.
- Generación de embeddings semánticos utilizando modelos preentrenados de Hugging Face.
- Indexación y búsqueda en **Elasticsearch**.
- Arquitectura modular y extensible.
- API REST con FastAPI para interactuar con el buscador.

## Tecnologías utilizadas
- **Python**: Lenguaje principal.
- **FastAPI**: Framework para construir la API.
- **Transformers (Hugging Face)**: Generación de embeddings semánticos.
- **Elasticsearch**: Motor de búsqueda e indexación.
- **Torch**: Backend para el modelo de embeddings.

## Requisitos previos
1. **Python 3.8+**
2. **Elasticsearch** (instalado y corriendo en `http://localhost:9200`)
3. Instalar las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt

## Instalación
1. Clona este repositorio:
```bash
git clone https://github.com/usuario/SmartSearchEngine.git
cd SmartSearchEngine
```

2. Crear el archivo data/documents.json con el siguiente formato:
```bash
[
    {"id": 1, "title": "Ejemplo", "content": "Este es un contenido de ejemplo"},
    {"id": 2, "title": "Otro ejemplo", "content": "Este es otro contenido"}
]
```

