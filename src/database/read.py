from src.database.conexao import conectar

# ---------------- READ ----------------
def listar_enderecos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ENDERECO")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def listar_oferece():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Oferece")
    for row in cursor.fetchall():
        print(row)
    conn.close()