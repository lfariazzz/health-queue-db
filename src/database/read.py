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

# Consulta sem parâmetro 4
"""Qual o volume de atendimentos e faltas por status em todo o sistema?"""
def relatorio_estatistico_geral():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            STATUS_AGENDAMENTO, 
            COUNT(*) AS total_por_status
        FROM agendamento
        GROUP BY STATUS_AGENDAMENTO
    """)
    relatorio = cursor.fetchall()
    conn.close()
    return relatorio

# Consulta sem parâmetro 5
"""Quais os serviços mais procurados no sistema?"""
def listar_servicos_mais_procurados():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT servico.NOME, COUNT(agendamento.ID_AGENDAMENTO) AS total 
        FROM agendamento
        JOIN servico ON agendamento.ID_SERVICO_REFERENTE = servico.ID_SERVICO
        GROUP BY servico.NOME ORDER BY total DESC
    """)
    servicos_mais_procurados = cursor.fetchall()
    conn.close()
    return servicos_mais_procurados

# Consulta sem parâmetro 6
"""Listar todas as unidades e seus respectivos endereços"""
def listar_unidades_com_endereco():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT unidade.NOME, unidade.TIPO, endereco.LOGRADOURO, endereco.RUA, endereco.NUMERO 
        FROM unidade
        JOIN endereco ON unidade.ID_ENDERECO = endereco.ID_ENDERECO
    """)
    unidades_com_endereco = cursor.fetchall()
    conn.close()
    return unidades_com_endereco

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

# Consulta parametrizável simples 2
"""Quais são os dependentes do cidadão X?"""
def listar_dependentes_por_cidadao(cpf_responsavel):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""SELECT 
                        pessoa.NOME AS nome_dependente,
                        pessoa.CPF AS cpf_dependente,
                        cidadao.CARTAO_SUS,
                        dependente.PARENTESCO,
                        dependente.VIGENCIA
                    FROM dependente
                    JOIN pessoa ON dependente.ID_PESSOA = pessoa.CPF
                    JOIN cidadao ON pessoa.CPF = cidadao.ID_PESSOA
                    WHERE dependente.ID_RESPONSAVEL = %s""", (cpf_responsavel,))
    dependentes = cursor.fetchall()
    conn.close()
    return dependentes

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
    cidadaos_prioridade = cursor.fetchall()
    conn.close()
    return cidadaos_prioridade

# Consulta parametrizável simples 4
"""Qual o histórico de agendamentos do cidadão X?"""
def listar_historico_cidadao(cpf_cidadao):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            agendamento.DATA, 
            agendamento.HORA, 
            servico.NOME AS nome_servico, 
            unidade.NOME AS nome_unidade,
            agendamento.STATUS_AGENDAMENTO
        FROM agendamento
        JOIN servico ON agendamento.ID_SERVICO_REFERENTE = servico.ID_SERVICO
        JOIN unidade ON agendamento.ID_UNIDADE_SEDIADA = unidade.ID_UNIDADE
        WHERE agendamento.ID_CIDADAO_SOLICITADO = %s
        ORDER BY agendamento.DATA DESC, agendamento.HORA DESC
    """, (cpf_cidadao,))
    
    historico = cursor.fetchall()
    conn.close()
    return historico
    
# Consulta com 2 parâmetros
"""Quais são os horários de um serviço X na unidade Y?"""
def listar_horarios_servico_unidade(nome_servico, nome_unidade):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT oferece.DIA_SEMANA, oferece.HORA_INICIO, oferece.HORA_FINAL, oferece.VAGAS
        FROM oferece
        JOIN servico ON oferece.ID_SERVICO = servico.ID_SERVICO
        JOIN unidade ON oferece.ID_UNIDADE = unidade.ID_UNIDADE
        WHERE servico.NOME = %s AND unidade.NOME = %s
    """, (nome_servico, nome_unidade))
    horarios_servico = cursor.fetchall()
    conn.close()
    return horarios_servico

# Consulta com 3 parâmetros
"""Busca avançada: Filtrar agendamentos por Unidade, Serviço e Status"""
def filtrar_agendamentos_avancado(unidade, servico, status):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT pessoa.NOME, agendamento.DATA, agendamento.HORA, agendamento.STATUS_AGENDAMENTO
        FROM agendamento
        JOIN unidade ON agendamento.ID_UNIDADE_SEDIADA = unidade.ID_UNIDADE
        JOIN servico ON agendamento.ID_SERVICO_REFERENTE = servico.ID_SERVICO
        JOIN pessoa ON agendamento.ID_CIDADAO_SOLICITADO = pessoa.CPF
        WHERE unidade.NOME = %s AND servico.NOME = %s AND agendamento.STATUS_AGENDAMENTO = %s
    """, (unidade, servico, status))
    agendamentos_filtrados = cursor.fetchall()
    conn.close()
    return agendamentos_filtrados