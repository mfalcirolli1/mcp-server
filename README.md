# mcp-server
## https://gofastmcp.com/deployment/running-server
## https://pypi.org/project/fastmcp/

python -m venv .venv
source .venv/Scripts/activate

pip install fastmcp==2.14.1

### Para PROMPTS:
#### Os prompts definem modelos de mensagens reutilizáveis para orientar as interações do LLM

"method": "prompts/list"    // Lista todos os prompts
"method": "prompts/get"     // Obtém um prompt específico

### Para TOOLS:
#### As ferramentas permitem que os LLMs executem ações executando suas funções Python. Ideal para cálculos, chamadas de API. As ferramentas podem retornar vários tipos, incluindo texto, objetos serializáveis em JSON e até mesmo imagens ou áudio auxiliados pelas classes auxiliares de mídia FastMCP.

"method": "tools/list"      // Lista todas as ferramentas
"method": "tools/call"      // Chama uma ferramenta

### Para RESOURCES:
#### Os recursos expõem fontes de dados somente leitura

"method": "resources/list"  // Lista recursos
"method": "resources/read"  // Lê um recurso específico