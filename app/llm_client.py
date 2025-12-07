import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
HUGGINGFACE = False
try:
    from huggingface_hub import InferenceClient
    HUGGINGFACE = True if HF_API_KEY else False
except Exception:
    HUGGINGFACE = False

# Provider-agnostic call
def call_llm(prompt: dict[str, str], max_tokens: int = 512, temperature: float = 0.7) -> str:
    """
    Llama al proveedor configurado. Actualmente intenta Hugging Face InferenceClient si HF_API_KEY está presente.
    Cambia esta función si deseas usar OpenRouter, Groq u otro.
    """
    if HUGGINGFACE:
        client = InferenceClient(token=HF_API_KEY)
        # Usa un modelo público ligero; cambia repo_id si lo prefieres
        model = "meta-llama/Llama-3.1-8B-Instruct:novita"
        try:
            completion = client.chat.completions.create(prompt, max_tokens=max_tokens, temperature=temperature, model=model).choices[0].message['content']
            return str(completion)
        except Exception as e:
            raise RuntimeError(f"LLM error: {e}")
    else:
        # Fallback: simple echo (útil para desarrollo offline)
        return f"[Mock LLM] Received prompt length {len(prompt)}. Replace with real provider."
