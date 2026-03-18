import hashlib
from src.database.create import (
    inserir_pessoa_com_endereco, inserir_servico, inserir_funcionario,
    inserir_usuario, inserir_unidade, inserir_agendamento, inserir_cidadao, inserir_oferece
)


def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Inserir Pessoa")
        print("2. Inserir Serviço")
        print("3. Inserir Funcionário")
        print("4. Inserir Usuário")
        print("5. Inserir Cidadão")
        print("6. Cadastrar Unidade")
        print("7. Cadastrar Oferta de Serviço")
        print("8. Fazer Agendamento")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cpf = input("CPF: ")
            nome = input("Nome: ")
            data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
            bairro = input("Bairro: ")
            cep = input("CEP: ")
            rua = input("Rua: ")
            numero = input("Número: ")
            try:
                inserir_pessoa_com_endereco(cpf, nome, data_nascimento, cep, rua, numero, bairro)
            except Exception as e:
                print(f"Erro ao inserir pessoa: {e}")

        elif opcao == "2":
            nome = input("Nome do serviço: ")
            tempo = input("Tempo médio (minutos): ")
            try:
                inserir_servico(nome, tempo)
            except Exception as e:
                print(f"Erro ao inserir serviço: {e}")

        elif opcao == "3":
            cpf = input("CPF da Pessoa vinculada: ")
            matricula = input("Matrícula: ")
            cargo = input("Cargo: ")
            admissao = input("Data de Admissão (AAAA-MM-DD): ")
            try:
                inserir_funcionario(cpf, matricula, cargo, admissao)
            except Exception as e:
                print(f"Erro ao inserir funcionário: {e}")

        elif opcao == "4":
            cpf = input("CPF da Pessoa vinculada: ")
            email = input("Email: ")
            senha = input("Senha: ")
            senha_hash = hashlib.sha256(senha.encode()).hexdigest()
            perfil = input("Perfil (SEC, GES, PRO, CID): ")
            try:
                inserir_usuario(cpf, email, senha_hash, perfil)
            except Exception as e:
                print(f"Erro ao inserir usuário: {e}")

        elif opcao == "5":
            cpf = input("CPF da pessoa vinculada: ")
            cartao_sus = input("Cartão SUS: ")
            nis = input("NIS: ")
            try:
                inserir_cidadao(cpf, cartao_sus, nis)
            except Exception as e:
                print(f"Erro ao inserir cidadão: {e}")

        elif opcao == "6":
            nome = input("Nome da unidade: ")
            tipo = input("Tipo da unidade: ")
            cep = input("CEP: ")
            rua = input("Rua: ")
            numero = input("Número: ")
            bairro = input("Bairro: ")
            try:
                inserir_unidade(nome, tipo, cep, rua, numero, bairro)
            except Exception as e:
                print(f"Erro ao inserir unidade: {e}")

        elif opcao == "7":
            id_unidade = input("ID da unidade: ")
            id_servico = input("ID do serviço: ")
            dia_semana = input("Dia da semana (SEG, TER, QUA, QUI, SEX, SAB, DOM): ")
            hora_inicio = input("Hora início (HH:MM:SS): ")
            hora_final = input("Hora final (HH:MM:SS): ")
            vagas = input("Número de vagas: ")
            try:
                inserir_oferece(id_unidade, id_servico, dia_semana, hora_inicio, hora_final, vagas)
            except Exception as e:
                print(f"Erro ao inserir oferta: {e}")

        elif opcao == "8":
            observacao = input("Observação (opcional): ")
            data = input("Data do agendamento (AAAA-MM-DD): ")
            hora = input("Hora do agendamento (HH:MM:SS): ")
            id_unidade = input("ID da unidade sediada: ")
            id_cidadao = input("CPF do cidadão solicitante: ")
            id_servico = input("ID do serviço referente: ")
            status_agendamento = input("Status do agendamento (PENDENTE/CONFIRMADO/CANCELADO/REALIZADO): ")
            prioridade = input("Prioridade (opcional): ")
            notificacao = input("Notificação (0/1): ")
            try:
                inserir_agendamento(
                    observacao or None, data, hora,
                    None, None, None,
                    None,
                    id_unidade, id_cidadao, id_servico,
                    status_agendamento, prioridade or None, notificacao
                )
            except Exception as e:
                print(f"Erro ao inserir agendamento: {e}")

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

