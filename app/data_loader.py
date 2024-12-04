import json

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Formato esperado del archivo JSON:
[{"id": 1, "title": "Título", "content": "Contenido del documento"}]
