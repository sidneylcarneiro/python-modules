# Arquivo: modules/chat/ver_modelos.py
from google import genai
import os

# Use a mesma chave que está no __init__.py ou configure aqui
API_KEY = "AIzaSyCuveq5QUsJSxu3cmp9Zhd8CCJa6K9AP_U" 

client = genai.Client(api_key=API_KEY)

print("--- Listando Modelos ---")
try:
    # Vamos listar tudo sem tentar filtrar propriedades que podem não existir
    for m in client.models.list():
        # Imprime o nome do modelo
        print(f"Nome encontrado: {m.name}")
except Exception as e:
    print(f"Erro crítico: {e}")