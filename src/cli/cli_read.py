from src.database.read import (
    listar_medicos_por_unidade, listar_oferece, listar_unidades, listar_cidadaos
)

def menu_read():
    while True:
        print("\n--- MENU ---")
        print("1. Listar serviços oferecidos")
        print("2. Listar unidades disponíveis")
        print("3. Listar possíveis clientes registrados")
        print("4. listas médicos por unidade")

        print("0. Voltar")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            listar_oferece()
        elif opcao == 2:
            listar_unidades()
        elif opcao == 3:
            listar_cidadaos()
        elif opcao == 4:
            nome_unidade = input("Digite o nome da unidade que deseja ver a disponibilidade de médicos: ")
            print(listar_medicos_por_unidade(nome_unidade))
        
        elif opcao == 0:
            break

menu_read()
