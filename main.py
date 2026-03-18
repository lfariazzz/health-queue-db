from src.cli.cli_create import menu
from src.cli.cli_read import menu_read
from src.cli.cli_update import menu_update
from src.cli.cli_delete import menu_delete


def main():
    while True:
        print("\n=============================")
        print("  SISTEMA DE GESTÃO DE FILAS ")
        print("=============================")
        print("1. Inserções")
        print("2. Consultas")
        print("3. Atualizações")
        print("4. Exclusões")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu()
        elif opcao == "2":
            menu_read()
        elif opcao == "3":
            menu_update()
        elif opcao == "4":
            menu_delete()
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()