from src.database.conexao import conectar

# ---------------- READ ----------------

# Consulta sem parâmetro 1
"""Quais são os serviços oferecidos?"""
# CORRIGIDO: LOGRADOURO não existe na tabela endereco, substituído por BAIRRO
def listar_oferece():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
                   SELECT
                   unidade.NOME AS nome_unidade,
                   unidade.TIPO AS tipo_unidade,
                   servico.NOME AS nome_servico,
                   endereco.BAIRRO,
                   endereco.RUA,
                   endereco.NUMERO
                   FROM OFERECE
                   JOIN unidade  ON unidade.ID_UNIDADE   = oferece.ID_UNIDADE
                   JOIN servico  ON servico.id_servico   = oferece.id_servico
                   JOIN endereco ON endereco.id_endereco = unidade.id_endereco""")
    for row in cursor.fetchall():
        print(f"Unidade que oferta: {row['nome_unidade']}")
        print(f"Tipo de unidade: {row['tipo_unidade']}")
        print(f"Bairro: {row['BAIRRO']}")
        print(f"Rua: {row['RUA']}")
        print(f"Número: {row['NUMERO']}")
        print(f"Serviço: {row['nome_servico']}")
        print(f"------------------------------")
    conn.close()


# Consulta sem parâmetro 2
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


# Consulta sem parâmetro 3
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
    if not relatorio:
        print("Nenhum resultado encontrado.")
    else:
        for row in relatorio:
            print(f"Status: {row.get('STATUS_AGENDAMENTO')} - Total: {row.get('total_por_status')}")
            print("------------------------------")
    conn.close()


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
    if not servicos_mais_procurados:
        print("Nenhum serviço encontrado.")
    else:
        for row in servicos_mais_procurados:
            print(f"Serviço: {row.get('NOME')}")
            print(f"Total de agendamentos: {row.get('total')}")
            print("------------------------------")
    conn.close()


# Consulta sem parâmetro 6
"""Listar todas as unidades e seus respectivos endereços"""
# CORRIGIDO: LOGRADOURO não existe na tabela endereco, substituído por BAIRRO
def listar_unidades_com_endereco():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT unidade.NOME, unidade.TIPO, endereco.BAIRRO, endereco.RUA, endereco.NUMERO 
        FROM unidade
        JOIN endereco ON unidade.ID_ENDERECO = endereco.ID_ENDERECO
    """)
    unidades_com_endereco = cursor.fetchall()
    if not unidades_com_endereco:
        print("Nenhuma unidade encontrada.")
    else:
        for row in unidades_com_endereco:
            print(f"Nome: {row.get('NOME')}")
            print(f"Tipo: {row.get('TIPO')}")
            print(f"Endereço: {row.get('BAIRRO')}, {row.get('RUA')}, {row.get('NUMERO')}")
            print("------------------------------")
    conn.close()


# Consulta parametrizável simples 1
"""Quais médicos estão disponíveis na unidade X?"""
def listar_medicos_por_unidade(nome_unidade):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
                   SELECT pessoa.nome AS nome_medico, unidade.nome AS nome_unidade 
                   FROM funcionario
                   JOIN pessoa ON funcionario.id_pessoa = pessoa.cpf
                   JOIN lotacao ON lotacao.id_funcionario = funcionario.id_pessoa
                   JOIN unidade ON unidade.id_unidade = lotacao.id_unidade
                   WHERE funcionario.cargo='Médico' AND unidade.nome=%s
                   """, (nome_unidade,))
    medicos = cursor.fetchall()
    if not medicos:
        print("Nenhum médico encontrado para essa unidade.")
    else:
        for row in medicos:
            print(f"Médico: {row.get('nome_medico')}")
            print(f"Unidade: {row.get('nome_unidade')}")
            print("------------------------------")
    conn.close()


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
    if not dependentes:
        print("Nenhum dependente encontrado para esse responsável.")
    else:
        for row in dependentes:
            print(f"Nome: {row.get('nome_dependente')}")
            print(f"CPF: {row.get('cpf_dependente')}")
            print(f"Cartão SUS: {row.get('CARTAO_SUS')}")
            print(f"Parentesco: {row.get('PARENTESCO')}")
            print(f"Vigência: {row.get('VIGENCIA')}")
            print("------------------------------")
    conn.close()


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
                    ORDER BY agendamento.PRIORIDADE DESC, agendamento.DATA ASC, agendamento.HORA ASC""",
                   (nome_unidade,))
    cidadaos_prioridade = cursor.fetchall()
    if not cidadaos_prioridade:
        print("Nenhum cidadão prioritário encontrado para essa unidade.")
    else:
        for row in cidadaos_prioridade:
            print(f"Nome: {row.get('nome_cidadao')}")
            print(f"Cartão SUS: {row.get('CARTAO_SUS')}")
            print(f"Prioridade: {row.get('PRIORIDADE')} - Hora: {row.get('HORA')}")
            print(f"Status: {row.get('STATUS_AGENDAMENTO')}")
            print("------------------------------")
    conn.close()


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
    if not historico:
        print("Nenhum histórico encontrado para esse cidadão.")
    else:
        for row in historico:
            print(f"Data: {row.get('DATA')} - Hora: {row.get('HORA')}")
            print(f"Serviço: {row.get('nome_servico')} - Unidade: {row.get('nome_unidade')}")
            print(f"Status: {row.get('STATUS_AGENDAMENTO')}")
            print("------------------------------")
    conn.close()


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
    if not horarios_servico:
        print("Nenhum horário encontrado para esse serviço/unidade.")
    else:
        for row in horarios_servico:
            print(f"Dia da semana: {row.get('DIA_SEMANA')}")
            print(f"Início: {row.get('HORA_INICIO')}")
            print(f"Término: {row.get('HORA_FINAL')}")
            print(f"Vagas: {row.get('VAGAS')}")
            print("------------------------------")
    conn.close()


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
    if not agendamentos_filtrados:
        print("Nenhum agendamento encontrado com esses filtros.")
    else:
        for row in agendamentos_filtrados:
            print(f"Nome: {row.get('NOME')}")
            print(f"Data: {row.get('DATA')}")
            print(f"Hora: {row.get('HORA')}")
            print(f"Status: {row.get('STATUS_AGENDAMENTO')}")
            print("------------------------------")
    conn.close()