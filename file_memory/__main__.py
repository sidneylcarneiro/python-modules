# Importa do próprio pacote (o ponto . refere-se ao __init__.py desta pasta)
from . import salvar_interacao, carregar_memoria, limpar_memoria

if __name__ == "__main__":
    arquivo_teste = "teste_memoria.txt"
    
    # print("--- 1. Limpando memória antiga (se existir) ---")
    # limpar_memoria(arquivo_teste)
    
    print("--- 2. Salvando uma interação ---")
    salvar_interacao(
        usuario_texto="Olá, como você está?", 
        ia_texto="Estou bem, obrigado por perguntar!",
        arquivo=arquivo_teste
    )
    print("   (Salvo com sucesso)")

    print("--- 3. Lendo o arquivo ---")
    conteudo = carregar_memoria(arquivo_teste)
    print(conteudo)

