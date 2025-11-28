# Arquivo: modules\file_memory\__init__.py
import os
from datetime import datetime

def salvar_interacao(usuario_texto: str, ia_texto: str, arquivo: str = "memoria_chat.txt"):
    """
    Salva um par de perguntas e respostas no arquivo de texto com timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Formata o bloco de conversa
    conteudo = (
        f"--- [{timestamp}] ---\n"
        f"USUARIO: {usuario_texto}\n"
        f"GEMINI: {ia_texto}\n"
        f"\n" # Linha em branco para separar
    )
    
    # 'a' = append (adiciona ao final sem apagar o que já existe)
    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(conteudo)

def carregar_memoria(arquivo: str = "memoria_chat.txt") -> str:
    """
    Lê todo o conteúdo do arquivo de memória.
    Retorna uma string vazia se o arquivo não existir.
    """
    if not os.path.exists(arquivo):
        return ""
    
    with open(arquivo, "r", encoding="utf-8") as f:
        return f.read()

def limpar_memoria(arquivo: str = "memoria_chat.txt"):
    """
    Apaga o conteúdo do arquivo (opcional).
    """
    if os.path.exists(arquivo):
        os.remove(arquivo)