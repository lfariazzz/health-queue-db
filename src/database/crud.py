from src.database.conexao import conectar

# ---------------- CREATE ----------------

def inserir_endereco(id_endereco, logradouro, cep, rua, numero):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO ENDERECO (ID_ENDERECO, LOGRADOURO, CEP, RUA, NUMERO)
             VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(sql, (id_endereco, logradouro, cep, rua, numero))
    conn.commit()
    print("Endereço inserido com sucesso!")
    conn.close()

def inserir_pessoa_com_endereco(cpf, nome, data_nascimento, logradouro, cep, rua, numero):
    conn = conectar()
    cursor = conn.cursor()

    # Inserir endereço
    sql_endereco = """INSERT INTO ENDERECO (LOGRADOURO, CEP, RUA, NUMERO)
                      VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql_endereco, (logradouro, cep, rua, numero))
    id_endereco = cursor.lastrowid

    # Inserir pessoa vinculada ao endereço
    sql_pessoa = """INSERT INTO PESSOA (CPF, NOME, DATA_NASCIMENTO, ID_ENDERECO)
                    VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql_pessoa, (cpf, nome, data_nascimento, id_endereco))

    conn.commit()
    print("Pessoa e endereço inseridos com sucesso!")
    conn.close()

def inserir_servico(nome, tempo_medio):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Servico (NOME, TEMPO_MEDIO) VALUES (%s, %s)", (nome, tempo_medio))
    conn.commit()
    print("Serviço inserido com sucesso!")
    conn.close()

def inserir_oferece(id_unidade, id_servico, dia_semana, hora_inicio, hora_final, vagas):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO Oferece (ID_UNIDADE, ID_SERVICO, DIA_SEMANA, HORA_INICIO, HORA_FINAL, VAGAS)
             VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (id_unidade, id_servico, dia_semana, hora_inicio, hora_final, vagas))
    conn.commit()
    print("Associação Unidade-Serviço inserida com sucesso!")
    conn.close()

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

