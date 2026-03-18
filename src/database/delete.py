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
    sql = "DELETE FROM oferece WHERE ID_UNIDADE=%s AND ID_SERVICO=%s"
    cursor.execute(sql, (id_unidade, id_servico))
    conn.commit()
    print("Associação Unidade-Serviço deletada com sucesso!")
    conn.close()


def deletar_pessoa(cpf):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PESSOA WHERE CPF = %s", (cpf,))
    conn.commit()
    print("Pessoa deletada com sucesso!")
    conn.close()


def deletar_unidade(id_unidade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM UNIDADE WHERE ID_UNIDADE = %s", (id_unidade,))
    conn.commit()
    print("Unidade deletada com sucesso!")
    conn.close()


def deletar_servico(id_servico):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM SERVICO WHERE ID_SERVICO = %s", (id_servico,))
    conn.commit()
    print("Serviço deletado com sucesso!")
    conn.close()


def deletar_agendamento(id_agendamento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM AGENDAMENTO WHERE ID_AGENDAMENTO = %s", (id_agendamento,))
    conn.commit()
    print("Agendamento deletado com sucesso!")
    conn.close()