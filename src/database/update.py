from src.database.conexao import conectar

# ---------------- UPDATE ----------------
def atualizar_endereco(id_endereco, novo_logradouro, novo_cep, nova_rua, novo_numero):
    conn = conectar()
    cursor = conn.cursor()
    sql = """UPDATE ENDERECO 
             SET LOGRADOURO = %s, CEP=%s, RUA=%s, NUMERO=%s
             WHERE ID_ENDERECO=%s"""
    cursor.execute(sql, (novo_logradouro, novo_cep, nova_rua, novo_numero, id_endereco))
    conn.commit()
    print("Endereço atualizado com sucesso!")
    conn.close()

def atualizar_oferece(id_unidade, id_servico, novo_dia_semana, nova_hora_inicio, nova_hora_final, novas_vagas):
    conn = conectar()
    cursor = conn.cursor()
    sql = """UPDATE Oferece
             SET DIA_SEMANA=%s, HORA_INICIO=%s, HORA_FINAL=%s, VAGAS=%s
             WHERE ID_UNIDADE=%s AND ID_SERVICO=%s"""
    cursor.execute(sql, (novo_dia_semana, nova_hora_inicio, nova_hora_final, novas_vagas, id_unidade, id_servico))
    conn.commit()
    print("Associação Unidade-Serviço atualizada com sucesso!")
    conn.close()