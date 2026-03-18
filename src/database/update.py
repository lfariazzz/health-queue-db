from src.database.conexao import conectar


def atualizar_endereco(id_endereco, cep=None, rua=None, numero=None, bairro=None):
    campos_para_atualizar = []
    valores = []

    if cep is not None:
        campos_para_atualizar.append("CEP = %s")
        valores.append(cep)

    if rua is not None:
        campos_para_atualizar.append("RUA = %s")
        valores.append(rua)

    if numero is not None:
        campos_para_atualizar.append("NUMERO = %s")
        valores.append(numero)

    if bairro is not None:
        campos_para_atualizar.append("BAIRRO = %s")
        valores.append(bairro)

    if not campos_para_atualizar:
        return False

    valores.append(id_endereco)
    sql = f"UPDATE ENDERECO SET {', '.join(campos_para_atualizar)} WHERE ID_ENDERECO = %s"

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(sql, tuple(valores))
        conn.commit()
        sucesso = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return sucesso
    except Exception as e:
        return e


def atualizar_oferece(id_unidade, id_servico, dia=None, h_inicio=None, h_fim=None, vagas=None):
    campos_para_atualizar = []
    valores = []

    if dia is not None:
        campos_para_atualizar.append("DIA_SEMANA = %s")
        valores.append(dia)

    if h_inicio is not None:
        campos_para_atualizar.append("HORA_INICIO = %s")
        valores.append(h_inicio)

    if h_fim is not None:
        campos_para_atualizar.append("HORA_FINAL = %s")
        valores.append(h_fim)

    if vagas is not None:
        campos_para_atualizar.append("VAGAS = %s")
        valores.append(vagas)

    if not campos_para_atualizar:
        return False

    # Chave composta
    valores.append(id_unidade)
    valores.append(id_servico)
    sql = f"UPDATE OFERECE SET {', '.join(campos_para_atualizar)} WHERE ID_UNIDADE = %s AND ID_SERVICO = %s"

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(sql, tuple(valores))
        conn.commit()
        sucesso = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return sucesso
    except Exception as e:
        return e


def atualizar_pessoa(cpf, nome=None, data_nascimento=None, id_endereco=None):
    campos_para_atualizar = []
    valores = []

    if nome is not None:
        campos_para_atualizar.append("NOME = %s")
        valores.append(nome)

    if id_endereco is not None:
        campos_para_atualizar.append("ID_ENDERECO = %s")
        valores.append(id_endereco)

    if not campos_para_atualizar:
        return False

    valores.append(cpf)
    sql = f"UPDATE PESSOA SET {','.join(campos_para_atualizar)} WHERE CPF = %s"

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(sql, tuple(valores))
        conn.commit()
        sucesso = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return sucesso
    except Exception as e:
        return e


def atualizar_usuario(id_pessoa, email=None, senha_hash=None, perfil=None):
    campos_para_atualizar = []
    valores = []

    if email is not None:
        campos_para_atualizar.append("EMAIL = %s")
        valores.append(email)

    if senha_hash is not None:
        campos_para_atualizar.append("SENHA_HASH = %s")
        valores.append(senha_hash)

    if perfil is not None:
        campos_para_atualizar.append("PERFIL = %s")
        valores.append(perfil)

    if not campos_para_atualizar:
        return False

    valores.append(id_pessoa)
    sql = f"UPDATE USUARIO SET {', '.join(campos_para_atualizar)} WHERE ID_PESSOA = %s"

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(sql, tuple(valores))
        conn.commit()
        sucesso = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return sucesso
    except Exception as e:
        return e


def atualizar_servico(id_servico, nome=None, tempo_medio=None):
    campos_para_atualizar = []
    valores = []

    if nome is not None:
        campos_para_atualizar.append("NOME = %s")
        valores.append(nome)

    if tempo_medio is not None:
        campos_para_atualizar.append("TEMPO_MEDIO = %s")
        valores.append(tempo_medio)

    if not campos_para_atualizar:
        return False

    valores.append(id_servico)
    sql = f"UPDATE SERVICO SET {', '.join(campos_para_atualizar)} WHERE ID_SERVICO = %s"

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(sql, tuple(valores))
        conn.commit()
        sucesso = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return sucesso
    except Exception as e:
        return e