# Coleção de Módulos Python

Este repositório contém uma coleção de módulos utilitários desenvolvidos em Python.

## 📁 Módulos Disponíveis

### 1. Chat Gemini (`modules/chat`)
Um cliente de chat via terminal que utiliza a API mais recente do Google Gemini (v2.5).
- **Funcionalidade:** Chat interativo via linha de comando.
- **Modelo:** `gemini-2.5-flash` (configurável).

## 🚀 Como Executar

### Pré-requisitos
* Python 3.10 ou superior
* Conta no Google AI Studio (para obter a API Key)

### Instalação

1. Clone o repositório ou baixe a pasta.
2. Crie e ative o ambiente virtual:
   ```powershell
   # Windows
   python -m venv venv
   .\venv\Scripts\Activate
````

3.  Instale as dependências:
    ```powershell
    pip install -r requirements.txt
    ```

### Configuração da API Key

Para segurança, não coloque sua chave diretamente no código se for compartilhar o projeto. Recomenda-se usar variáveis de ambiente.

No arquivo `modules/chat/__init__.py`, configure sua chave `GEMINI_API_KEY`.

### Executando o Chat

Na raiz do projeto (pasta `modules`), execute:

```powershell
python -m chat
```

## 🛠️ Tecnologias

  - Python
  - Google GenAI SDK


````

---
  jbcfjksdhfdksk