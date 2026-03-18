from src.database.conexao import conectar

# ---------------- READ ----------------

#Consulta sem parâmetro 1
"""Quais são os serviços oferecidos?"""
def listar_oferece():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
                   SELECT
                   unidade.NOME AS nome_unidade,
                   unidade.TIPO AS tipo_unidade,
                   servico.NOME AS nome_servico,
                   endereco.LOGRADOURO,
                   endereco.RUA,
                   endereco.NUMERO
                   FROM OFERECE
                   JOIN unidade  ON unidade.ID_UNIDADE   = oferece.ID_UNIDADE
                   JOIN servico ON servico.id_servico = oferece.id_servico
                   JOIN endereco ON endereco.id_endereco = unidade.id_endereco""")
    for row in cursor.fetchall():
        print(f"Unidade que oferta: {row['nome_unidade']}")
        print(f"Tipo de unidade: {row['tipo_unidade']}")
        print(f"Endereço unidade: {row['LOGRADOURO'], row['RUA'], row['NUMERO']}")
        print(f"Serviço: {row['nome_servico']}")
        print(f"------------------------------")
    conn.close()

#Consulta sem parâmetro 2
"""Quais são as unidades disponíveis?"""
def listar_unidades():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM unidade")
    for row in cursor.fetchall():
        print(f"ID: {row['ID_UNIDADE']}")
        print(f"Nome: {row['NOME']}")
        print(f"Tipo: {row['TIPO']}")
        print(f"Endereço: {row['ID_ENDERECO']}")
        print(f"------------------------------")
    conn.close()

#Consulta sem parâmetro 3
"""Quais são os possíveis pacientes registrados no sistema?"""
def listar_cidadaos():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""SELECT
                   PESSOA.NOME AS nome_pessoa,
                   pessoa.CPF,
                   pessoa.DATA_NASCIMENTO,
                   cidadao.CARTAO_SUS,
                   cidadao.NIS
                   FROM cidadao
                   JOIN pessoa ON cidadao.id_pessoa = pessoa.cpf""")
    for row in cursor.fetchall():
        print(f"Pessoa: {row['nome_pessoa']}")
        print(f"CPF: {row['CPF']}")
        print(f"Data de nascimento: {row['DATA_NASCIMENTO']}")
        print(f"Cartão SUS: {row['CARTAO_SUS']}")
        print(f"NIS: {row['NIS']}")
        print(f"------------------------------")
    conn.close()

#Consulta parametrizável simples 1
"""Quais médicos estão disponível na unidade X?"""
def listar_medicos_por_unidade(nome_unidade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT pessoa.nome AS nome_medico, unidade.nome AS nome_unidade 
                   FROM funcionario
                   JOIN pessoa ON funcionario.id_pessoa = pessoa.cpf
                   JOIN lotacao ON lotacao.id_funcionario = funcionario.id_pessoa
                   JOIN unidade ON unidade.id_unidade = lotacao.id_unidade
                   WHERE funcionario.cargo='Médico' AND unidade.nome=%s
                   """, (nome_unidade,))
    medicos = cursor.fetchall()
    conn.close()
    return medicos

#Consulta parametrizável simples 2
"""Quais são os dependentes do cidadão X"""

# Consulta parametrizável simples 3
"""Qual é a ordem de prioridade na unidade X?"""
def listar_prioridade_de_cidadao_por_unidade(nome_unidade):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""SELECT 
                        pessoa.NOME AS nome_cidadao,
                        cidadao.CARTAO_SUS,
                        agendamento.PRIORIDADE,
                        agendamento.HORA,
                        agendamento.STATUS_AGENDAMENTO
                    FROM agendamento
                    JOIN cidadao ON agendamento.ID_CIDADAO_SOLICITADO = cidadao.ID_PESSOA
                    JOIN pessoa ON cidadao.ID_PESSOA = pessoa.CPF
                    JOIN unidade ON agendamento.ID_UNIDADE_SEDIADA = unidade.ID_UNIDADE
                    WHERE unidade.NOME = %s AND agendamento.STATUS_AGENDAMENTO = 'PENDENTE'
                    ORDER BY agendamento.PRIORIDADE DESC, agendamento.DATA ASC, agendamento.HORA ASC""", (nome_unidade,))
    
    # Armazena os resultados na variável em vez de imprimir aqui
    cidadaos_prioridade = cursor.fetchall()
    
    conn.close()
    return cidadaos_prioridade

