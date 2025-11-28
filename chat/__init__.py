import os
from google import genai
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega a chave do ambiente seguro
API_KEY = os.getenv("GEMINI_API_KEY")

def perguntar_ao_gemini(modelo: str, texto_usuario: str):
    """
    Função reutilizável para enviar perguntas ao Gemini.
    """
    if not API_KEY:
        return "Erro: Chave de API não configurada no arquivo .env"

    try:
        client = genai.Client(api_key=API_KEY)
        
        response = client.models.generate_content(
            model=modelo,
            contents=texto_usuario
        )
        
        if response.text:
            return response.text
        else:
            return "O modelo respondeu, mas sem texto."
            
    except Exception as e:
        return f"Erro na conexão com a API: {e}"
    