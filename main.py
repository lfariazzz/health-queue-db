# NAO ESQUECER DE IMPORTAS AS FUNCOES
from src.cli.cli_create import menu
from src.cli.cli_update import menu_update
from src.cli.cli_read import menu_read
from src.cli.cli_delete import menu_delete

def exibir_cabecalho():
    print("\n" + "="*30)
    print("      SISTEMA CRUD     ")
    print("="*30)

def main():
    while True:
        exibir_cabecalho()
        print("1 - Cadastrar (Create)")
        print("2 - Atualizar (Update)")
        print("3 - Ler (Read)")
        print("4 - Deletar (Delete)")
        print("0 - Sair")
        print("-"*30)
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu() 

        elif opcao == '2':
            menu_update() 

        elif opcao == '3':
            menu_read()

        elif opcao == '4':
            menu_delete()

        elif opcao == '0':
            print("Encerrando sistema...")
            break
        else:
            print("⚠️ Opção inválida!")

if __name__ == "__main__":
    main()