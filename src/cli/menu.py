from src.database.crud import (
    inserir_pessoa_com_endereco, inserir_servico, inserir_oferece
)

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Inserir Pessoa ")
        print("2. Inserir Serviço")
        print("3. Inserir Associação Unidade-Serviço")
    
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cpf = input("CPF: ")
            nome = input("Nome: ")
            data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
            logradouro = input("LOG: ")
            cep = input("CEP: ")
            rua = input("Rua: ")
            numero = input("Número: ")
            inserir_pessoa_com_endereco(cpf, nome, data_nascimento, logradouro, cep, rua, numero)

        elif  opcao == "2":
            nome = input("Nome do serviço: ")
            tempo = int(input("Tempo médio (minutos): "))
            inserir_servico(nome, tempo)

        elif opcao == "3":
           id_unidade = input("ID da unidade: ")
           id_servico = input("ID do serviço: ")
           dia_semana = input("Dia da semana (SEG, TER, QUA, QUI, SEX, SAB, DOM): ")
           hora_inicio = input("Hora início (HH:MM:SS): ")
           hora_final = input("Hora final (HH:MM:SS): ")
           vagas = input("Número de vagas: ")

           inserir_oferece(id_unidade, id_servico, dia_semana, hora_inicio, hora_final, vagas)

