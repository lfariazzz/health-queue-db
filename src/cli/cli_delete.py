from src.database.delete import (
    deletar_endereco,
    deletar_oferece,
    deletar_pessoa,
    deletar_unidade,
    deletar_servico,
    deletar_agendamento,
)


def menu_delete():
    while True:
        print("\n--- MENU DELETE ---")
        print("1. Deletar endereço")
        print("2. Deletar associação Unidade-Serviço")
        print("3. Deletar pessoa")
        print("4. Deletar unidade")
        print("5. Deletar serviço")
        print("6. Deletar agendamento")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_endereco = input("ID do endereço: ")
            deletar_endereco(id_endereco)
        elif opcao == "2":
            id_unidade = input("ID da unidade: ")
            id_servico = input("ID do serviço: ")
            deletar_oferece(id_unidade, id_servico)
        elif opcao == "3":
            cpf = input("CPF da pessoa: ")
            deletar_pessoa(cpf)
        elif opcao == "4":
            id_unidade = input("ID da unidade: ")
            deletar_unidade(id_unidade)
        elif opcao == "5":
            id_servico = input("ID do serviço: ")
            deletar_servico(id_servico)
        elif opcao == "6":
            id_agendamento = input("ID do agendamento: ")
            deletar_agendamento(id_agendamento)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

menu_delete()