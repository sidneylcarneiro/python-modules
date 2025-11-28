from . import perguntar_ao_gemini

if __name__ == "__main__":
    print("\n" + "="*40)
    print("🤖 CHAT GEMINI 2.5 (Digite 'sair' para encerrar)")
    print("="*40)
    
    modelo = "gemini-2.5-flash"
    
    while True:
        # Pega a entrada do usuário
        texto_usuario = input("\n👤 Você: ")
        
        # Verifica se é para sair
        if texto_usuario.lower() in ["sair", "exit", "quit"]:
            print("👋 Encerrando chat...")
            break
            
        if not texto_usuario.strip():
            continue
            
        print("⏳ Pensando...")
        
        # Chama a função do seu módulo
        resposta = perguntar_ao_gemini(modelo, texto_usuario)
        
        print(f"🤖 Gemini: {resposta}")
        