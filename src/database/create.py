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