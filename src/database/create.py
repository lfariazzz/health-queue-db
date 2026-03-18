from src.database.conexao import conectar

# ---------------- CREATE ----------------

def inserir_endereco(id_endereco, cep, rua, numero, bairro):
    conn = conectar()
    cursor = conn.cursor()
    sql_endereco = """INSERT INTO endereco (CEP, RUA, NUMERO, BAIRRO)
                  VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql_endereco, (cep, rua, numero, bairro))
    conn.commit()
    print("Endereço inserido com sucesso!")
    conn.close()

def inserir_oferece(id_unidade, id_servico, dia_semana, hora_inicio, hora_final, vagas):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO oferece (ID_UNIDADE, ID_SERVICO, DIA_SEMANA, HORA_INICIO, HORA_FINAL, VAGAS)
             VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (id_unidade, id_servico, dia_semana, hora_inicio, hora_final, vagas))
    conn.commit()
    print("Oferta de serviço inserida com sucesso!")
    conn.close()

def inserir_unidade(nome, tipo, cep, rua, numero, bairro):
    conn = conectar()
    cursor = conn.cursor()

    # Primeiro insere o endereço
    sql_endereco = """INSERT INTO endereco (CEP, RUA, NUMERO, BAIRRO)
                      VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql_endereco, (cep, rua, numero, bairro))
    conn.commit()
    id_endereco = cursor.lastrowid  # pega o ID do endereço recém-criado

    # Depois insere a unidade vinculada ao endereço
    sql_unidade = """INSERT INTO unidade (NOME, TIPO, ID_ENDERECO)
                     VALUES (%s, %s, %s)"""
    cursor.execute(sql_unidade, (nome, tipo, id_endereco))
    conn.commit()

    print("Unidade e endereço inseridos com sucesso!")
    conn.close()

          
def inserir_servico(nome, tempo_medio):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO servico (NOME, TEMPO_MEDIO) VALUES (%s, %s)"
    cursor.execute(sql, (nome, tempo_medio))
    conn.commit()
    print("Serviço inserido com sucesso!")
    conn.close()

def inserir_pessoa_com_endereco(cpf, nome, data_nascimento, cep, rua, numero, bairro):
    conn = conectar()
    cursor = conn.cursor()

    sql_endereco = """INSERT INTO ENDERECO ( CEP, RUA, NUMERO, BAIRRO)
                  VALUES (%s, %s, %s, %s)"""
    
    cursor.execute(sql_endereco, (cep, rua, numero, bairro))

    cursor.execute(sql_endereco, (cep, rua, numero, bairro))
    id_endereco = cursor.lastrowid

    # Inserir pessoa vinculada ao endereço
    sql_pessoa = """INSERT INTO PESSOA (CPF, NOME, DATA_NASCIMENTO, ID_ENDERECO)
                    VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql_pessoa, (cpf, nome, data_nascimento, id_endereco))

    conn.commit()
    print("Pessoa e endereço inseridos com sucesso!")
    conn.close()


def inserir_usuario(id_pessoa, email, senha_hash, perfil):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO usuario (ID_PESSOA, EMAIL, SENHA_HASH, PERFIL)
             VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql, (id_pessoa, email, senha_hash, perfil))
    conn.commit()
    print("Usuário inserido com sucesso!")
    conn.close()

    
def verificar_pessoa_existe(cpf):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM pessoa WHERE CPF = %s", (cpf,))
    existe = cursor.fetchone() is not None
    conn.close()
    return existe

def inserir_funcionario(id_pessoa, matricula, cargo, admissao):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO funcionario (ID_PESSOA, MATRICULA, CARGO, ADMISSAO)
             VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql, (id_pessoa, matricula, cargo, admissao))
    conn.commit()
    print("Funcionário inserido com sucesso!")
    conn.close()

def inserir_cidadao(id_pessoa, cartao_sus, nis):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO cidadao (ID_PESSOA, CARTAO_SUS, NIS)
             VALUES (%s, %s, %s)"""
    cursor.execute(sql, (id_pessoa, cartao_sus, nis))
    conn.commit()
    print("Cidadão inserido com sucesso!")
    conn.close()


def inserir_agendamento(observacao, data, hora,
                        data_inicio_realizado, data_final_realizado, horario_realizado,
                        id_funcionario_realizado,
                        id_unidade_sediada, id_cidadao_solicitado, id_servico_referente,
                        status_agendamento, prioridade, notificacao):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO agendamento (
                OBSERVACAO, DATA, HORA,
                DATA_INICIO_REALIZADO, DATA_FINAL_REALIZADO, HORARIO_REALIZADO,
                ID_FUNCIONARIO_REALIZADO, ID_UNIDADE_SEDIADA, ID_CIDADAO_SOLICITADO,
                ID_SERVICO_REFERENTE, STATUS_AGENDAMENTO, PRIORIDADE, NOTIFICACAO
             )
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (
        observacao, data, hora,
        data_inicio_realizado, data_final_realizado, horario_realizado,
        id_funcionario_realizado, id_unidade_sediada, id_cidadao_solicitado,
        id_servico_referente, status_agendamento, prioridade, notificacao
    ))
    conn.commit()
    print("Agendamento inserido com sucesso!")
    conn.close()