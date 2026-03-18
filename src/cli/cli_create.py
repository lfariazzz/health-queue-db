from datetime import datetime, date
from datetime import datetime
import re
import hashlib
from src.database.crud import (
    inserir_pessoa_com_endereco, inserir_servico, inserir_funcionario, 
    inserir_usuario, verificar_pessoa_existe, inserir_unidade, inserir_agendamento, inserir_cidadao, inserir_oferece
)

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Inserir Pessoa ")
        print("2. Inserir Serviço")
        print("3. inserir profissional")
        print("4. Inserir Usuário")
        print("5. Inserir funcionario")
        print("6  cadrastar nova unidade")
        print("7. cadrastar oferta de servico")
        print("8. fazer agendamento")
    
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cpf = input("CPF: ")
            if not cpf.isdigit() or len(cpf) != 11:
                print("CPF inválido! Deve conter 11 caracteres numéricos.")
                continue

            nome = input("Nome: ")
            data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
            try:
                datetime.strptime(data_nascimento, "%Y-%m-%d")
            except ValueError:
                print("Data inválida! Use o formato AAAA-MM-DD.")
                continue

            bairro = input("bairro: ")
            cep = input("CEP: ")
            if not (cep.isdigit() and len(cep) == 8):
                print("CEP inválido! Deve conter 8 dígitos numéricos.")
                continue

            rua = input("Rua: ")
            numero = input("Número: ")

            inserir_pessoa_com_endereco(cpf, nome, data_nascimento, cep, rua, numero, bairro)

        elif opcao == "2":
            nome = input("Nome do serviço: ")
            tempo = input("Tempo médio (minutos): ")
            if not tempo.isdigit() or int(tempo) <= 0:
                print("Tempo inválido! Deve ser um número positivo.")
                continue
            inserir_servico(nome, int(tempo))
        
        if opcao == "4":
            print("\n--- Cadastro de Novo Usuário ---")
            cpf = input("CPF da Pessoa vinculada: ")
            if not verificar_pessoa_existe(cpf):
                print("Erro: Pessoa não encontrada. Cadastre primeiro na opção 1.")
                continue


            email = input("Email: ").strip()
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("Erro: Email inválido.")
                continue

            senha = input("Senha: ").strip()
            if not senha:
                print("Erro: Senha obrigatória.")
                continue

            # Gera hash da senha (SHA256 como exemplo)
            senha_hash = hashlib.sha256(senha.encode()).hexdigest()

            perfil = input("Perfil (SEC, GES, PRO, CID): ").strip().upper()
            if perfil not in ["SEC", "GES", "PRO", "CID"]:
                print("Erro: Perfil inválido. Use SEC, GES, PRO ou CID.")
                continue

            try:
                inserir_usuario(cpf, email, senha_hash, perfil)
                print("Usuário inserido com sucesso!")
            except Exception as e:
                print(f"Erro ao inserir usuário: {e}")

        if opcao == "5":
            print("\n--- Cadastro de Novo Funcionário ---")

            cpf = input("CPF da Pessoa vinculada: ").strip()
            if not cpf.isdigit() or len(cpf) != 11:
                 print("Erro: CPF inválido! Deve conter 11 dígitos numéricos.")
                 continue
            if not verificar_pessoa_existe(cpf):
                 print("Erro: Pessoa não encontrada. Cadastre primeiro na opção 1.")
                 continue

            matricula = input("Matrícula: ").strip()
            if not matricula:
                  print("Erro: Matrícula obrigatória.")
                  continue
            if len(matricula) > 20:
                  print("Erro: Matrícula muito longa (máx. 20 caracteres).")
                  continue
            print("Escolha o cargo:")
            print("1 - Médico")
            print("2 - Secretário")
            cargo_opcao = input("Digite o número da opção: ").strip()
            if cargo_opcao == "1":
                cargo = "Médico"
            elif cargo_opcao == "2":
                cargo = "Secretário"
            else:
                print("Erro: Opção inválida. Escolha 1 ou 2.")
                continue
            
            admissao_str = input("Data de Admissão (AAAA-MM-DD) [Enter para hoje]: ").strip()
            if not admissao_str:
                admissao = date.today()
            else:
               try:
                   admissao = datetime.strptime(admissao_str, "%Y-%m-%d").date()
               except ValueError:
                    print("Erro: Data inválida! Use o formato AAAA-MM-DD.")
                    continue

            try:
                inserir_funcionario(cpf, matricula, cargo, admissao)
                print(f"Funcionário {matricula} inserido com sucesso!")
            except Exception as e:
                print(f"Erro ao inserir funcionário: {e}")

                
        elif opcao == "9":
          print("\n--- Cadastro de Novo Cidadão ---")

          cpf = input("CPF da pessoa vinculada: ").strip()
          if not cpf.isdigit() or len(cpf) != 11:
             print("Erro: CPF inválido! Deve conter 11 dígitos numéricos.")
             continue

          cartao_sus = input("Cartão SUS: ").strip()
          if not cartao_sus:
            print("Erro: Cartão SUS obrigatório.")
            continue

          nis = input("NIS: ").strip()
          if not nis:
            print("Erro: NIS obrigatório.")
            continue

          try:
            inserir_cidadao(cpf, cartao_sus, nis)
            print("Cidadão inserido com sucesso!")
          except Exception as e:
            print(f"Erro ao inserir cidadão: {e}")
    
        elif opcao == "6":
               print("\n--- Cadastro de Nova Unidade ---")

               nome = input("Nome da unidade: ").strip()
               if not nome or len(nome) < 3:
                   print("Erro: Nome inválido (mínimo 3 caracteres).")
                   continue

                # Escolha restrita para tipo
               print("Escolha o tipo da unidade:")
               print("1 - Hospital")
               print("2 - Clínica")
               print("3 - Posto de Saúde")
               tipo_opcao = input("Digite o número da opção: ").strip()

               if tipo_opcao == "1":
                  tipo = "Hospital"
               elif tipo_opcao == "2":
                  tipo = "Clínica"
               elif tipo_opcao == "3":
                  tipo = "Posto de Saúde"
               else:
                  print("Erro: Opção inválida. Escolha 1, 2 ou 3.")
                  continue

                # Cadastro do endereço vinculado
               cep = input("CEP: ").strip()
               if not (cep.isdigit() and len(cep) == 8):
                    print("Erro: CEP inválido! Deve conter 8 dígitos numéricos.")
                    continue

               rua = input("Rua: ").strip()
               numero = input("Número: ").strip()
               bairro = input("Bairro: ").strip()

               try:
                  inserir_unidade(nome, tipo, cep, rua, numero, bairro)
                  print(f"Unidade '{nome}' inserida com sucesso!")
               except Exception as e:
                  print(f"Erro ao inserir unidade: {e}")

        
        elif opcao == "7":
             print("\n--- Cadastro de Oferta de Serviço ---")

             id_unidade = input("ID da unidade: ").strip()
             if not id_unidade.isdigit():
                 print("Erro: ID da unidade deve ser numérico.")
                 continue

             id_servico = input("ID do serviço: ").strip()
             if not id_servico.isdigit():
                print("Erro: ID do serviço deve ser numérico.")
                continue

             # Restrição para dia da semana
             print("Escolha o dia da semana:")
    
             dia_opcao = input("Digite o número da opção: ").strip()

             dias_semana = {
             "1": "SEG",
             "2": "TER",
             "3": "QUA",
             "4": "QUI",
             "5": "SEX",
             "6": "SAB",
             "7": "DOM"
            }

             if dia_opcao not in dias_semana:
                print("Erro: Opção inválida para dia da semana.")
                continue
             dia_semana = dias_semana[dia_opcao]

             hora_inicio = input("Hora início (HH:MM:SS): ").strip()
             hora_final = input("Hora final (HH:MM:SS): ").strip()

             vagas = input("Número de vagas: ").strip()
             if not vagas.isdigit() or int(vagas) <= 0:
                 print("Erro: Número de vagas inválido! Deve ser positivo.")
                 continue

             try:
               inserir_oferece(int(id_unidade), int(id_servico), dia_semana, hora_inicio, hora_final, int(vagas))
               print("Oferta de serviço inserida com sucesso!")
             except Exception as e:
                print(f"Erro ao inserir oferta: {e}")
        


        elif opcao == "8":
            print("\n--- Cadastro de Novo Agendamento ---")

            # Observação opcional
            observacao = input("Observação (opcional): ").strip()
            if observacao == "":
                 observacao = None

            # Data e hora obrigatórias
            data_str = input("Data do agendamento (AAAA-MM-DD): ").strip()
            try:
               data = datetime.strptime(data_str, "%Y-%m-%d").date()
            except ValueError:
               print("Erro: Data inválida! Use o formato AAAA-MM-DD.")
               continue

            hora_str = input("Hora do agendamento (HH:MM:SS): ").strip()
            try:
               hora = datetime.strptime(hora_str, "%H:%M:%S").time()
            except ValueError:
              print("Erro: Hora inválida! Use o formato HH:MM:SS.")
              continue

             # Unidade vinculada
            id_unidade = input("ID da unidade sediada: ").strip()
            if not id_unidade.isdigit():
               print("Erro: ID da unidade deve ser numérico.")
               continue

            # Cidadão solicitante
            id_cidadao = input("CPF do cidadão solicitante: ").strip()
            if not id_cidadao.isdigit() or len(id_cidadao) != 11:
                print("Erro: CPF inválido! Deve conter 11 dígitos numéricos.")
                continue

            # Serviço referente
            id_servico = input("ID do serviço referente: ").strip()
            if not id_servico.isdigit():
               print("Erro: ID do serviço deve ser numérico.")
               continue

            # Status do agendamento com restrição
            print("Escolha o status do agendamento:")
            print("1 - PENDENTE")
            print("2 - CONFIRMADO")
            print("3 - CANCELADO")
            print("4 - REALIZADO")
            status_opcao = input("Digite o número da opção: ").strip()

            status_map = {
              "1": "PENDENTE",
              "2": "CONFIRMADO",
              "3": "CANCELADO",
              "4": "REALIZADO"
            }

            if status_opcao not in status_map:
               print("Erro: Status inválido. Escolha 1, 2, 3 ou 4.")
               continue
            status_agendamento = status_map[status_opcao]

            # Prioridade opcional
            prioridade = input("Prioridade (número, opcional): ").strip()
            if prioridade == "":
                  prioridade = None
            elif not prioridade.isdigit():
                 print("Erro: Prioridade deve ser numérica.")
                 continue
            else:
                prioridade = int(prioridade)

            # Notificação (0 ou 1)
            notificacao = input("Notificação (0 - não, 1 - sim): ").strip()
            if notificacao not in ["0", "1"]:
                print("Erro: Notificação deve ser 0 ou 1.")
                continue
            notificacao = int(notificacao)

            try:
               inserir_agendamento(
                   observacao, data, hora,
                    None, None, None,  # datas/hora de realizado (opcionais)
                    None,              # funcionário realizado (opcional)
                    int(id_unidade), id_cidadao, int(id_servico),
                    status_agendamento, prioridade, notificacao
                )
               print("Agendamento inserido com sucesso!")
            except Exception as e:
               print(f"Erro ao inserir agendamento: {e}")

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

