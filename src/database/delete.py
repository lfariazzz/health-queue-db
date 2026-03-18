from src.database.conexao import conectar

# ---------------- DELETE ----------------
def deletar_endereco(id_endereco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ENDERECO WHERE ID_ENDERECO = %s", (id_endereco,))
    conn.commit()
    print("Endereço deletado com sucesso!")
    conn.close()

def deletar_oferece(id_unidade, id_servico):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM Oferece WHERE ID_UNIDADE=%s AND ID_SERVICO=%s"
    cursor.execute(sql, (id_unidade, id_servico))
    conn.commit()
    print("Associação Unidade-Serviço deletada com sucesso!")
    conn.close()