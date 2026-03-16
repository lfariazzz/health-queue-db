import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Malaquias2005",  
        database="sistema_gestao_filas_agendamentos_publicos"
    )

# Teste rápido de conexão
if __name__ == "__main__":
    conn = conectar()
    print("Conexão OK!")
    conn.close()
