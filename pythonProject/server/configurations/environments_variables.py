import os

HOST = os.getenv("HOST") or "localhost"
PORT = os.getenv("PORT") or 8080
PROJETO_DBCONN = os.getenv("PROJETO_DBCONN")

# Variaveis opcionais
PER_PAGE = int(os.getenv("PER_PAGE")) if os.getenv("PER_PAGE") else 50
MAX_PER_PAGE = int(os.getenv("MAX_PER_PAGE")) if os.getenv("MAX_PER_PAGE") else 50
