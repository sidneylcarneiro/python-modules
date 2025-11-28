# Arquivo: modules/chat/__init__.py
from google import genai
import os

# Configuração da Chave (Idealmente use variáveis de ambiente)
# Se não funcionar, verifique se a chave está correta
API_KEY = "AIzaSyCuveq5QUsJSxu3cmp9Zhd8CCJa6K9AP_U" 

def perguntar_ao_gemini(modelo: str, texto_usuario: str):
    """
    Função reutilizável para enviar perguntas ao Gemini.
    """
    try:
        # Instancia o cliente da nova biblioteca google-genai
        client = genai.Client(api_key=API_KEY)
        
        # Envia a mensagem
        response = client.models.generate_content(
            model=modelo,
            contents=texto_usuario
        )
        
        # Retorna o texto da resposta
        if response.text:
            return response.text
        else:
            return "O modelo respondeu, mas sem texto (pode ter sido bloqueado)."
            
    except Exception as e:
        return f"Erro na conexão com a API: {e}"
    
