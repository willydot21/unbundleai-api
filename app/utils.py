import json

def try_parse_json(text: str):
    # Intenta localizar JSON en la respuesta del LLM
    # Buscamos la primera llave { y la última } para extraer JSON
    try:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            candidate = text[start:end+1]
            return json.loads(candidate)
    except Exception:
        pass
    return None
