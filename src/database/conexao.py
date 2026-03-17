import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "sistema_gestao_filas_agendamentos_publicos")
    )

# Teste rápido de conexão
if __name__ == "__main__":
    conn = conectar()
    print("Conexão OK!")
    conn.close()
