from src.database.update import (
    atualizar_endereco, atualizar_oferece, atualizar_pessoa, 
    atualizar_usuario, atualizar_servico
)

def menu_update():
    while True:
        print("\n--- MENU DE ATUALIZAÇÃO ---")
        print("1. Atualizar Endereço")
        print("2. Atualizar Pessoa")
        print("3. Atualizar Usuário")
        print("4. Atualizar Serviço")
        print("5. Atualizar Associação (Oferece)")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            break

        # --- Lógica para Endereço ---
        if opcao == "1":
            id_end = input("ID do Endereço que deseja alterar: ")
            print("Pressione ENTER para manter o valor atual.")
            cep = input("Novo CEP: ") or None
            rua = input("Nova Rua: ") or None
            num = input("Novo Número: ") or None
            bairro = input("Novo Bairro: ") or None
            
            resultado = atualizar_endereco(id_end, cep, rua, num, bairro)
            exibir_resultado(resultado)

        # --- Lógica para Pessoa ---
        elif opcao == "2":
            cpf = input("CPF da pessoa: ")
            print("Pressione ENTER para manter o valor atual.")
            nome = input("Novo Nome: ") or None
            id_end = input("Novo ID Endereço: ") or None
            
            resultado = atualizar_pessoa(cpf, nome, id_endereco=id_end)
            exibir_resultado(resultado)

        # --- Lógica para Usuário ---
        elif opcao == "3":
            id_p = input("CPF do Usuário: ")
            print("Pressione ENTER para manter o valor atual.")
            email = input("Novo Email: ") or None
            senha = input("Nova Senha: ") or None
            perfil = input("Novo Perfil (SEC, GES, PRO, CID): ") or None
            
            resultado = atualizar_usuario(id_p, email, senha, perfil)
            exibir_resultado(resultado)

        # --- Lógica para Serviço ---
        elif opcao == "4":
            id_s = input("ID do Serviço: ")
            print("Pressione ENTER para manter o valor atual.")
            nome = input("Novo Nome: ") or None
            tempo = input("Novo Tempo Médio: ") or None
            
            resultado = atualizar_servico(id_s, nome, tempo_medio=tempo)
            exibir_resultado(resultado)

        # --- Lógica para Oferece (Chave Composta) ---
        elif opcao == "5":
            id_u = input("ID da Unidade: ")
            id_s = input("ID do Serviço: ")
            print("Pressione ENTER para manter o valor atual.")
            dia = input("Novo Dia (SEG, TER...): ") or None
            h_i = input("Nova Hora Início: ") or None
            h_f = input("Nova Hora Final: ") or None
            vagas = input("Novas Vagas: ") or None
            
            resultado = atualizar_oferece(id_u, id_s, dia, h_i, h_f, vagas)
            exibir_resultado(resultado)

def exibir_resultado(res):
    """Função auxiliar para tratar os retornos das suas funções de update"""
    if res is True:
        print("\n✅ Sucesso: Registro atualizado!")
    elif res is False:
        print("\n⚠️ Aviso: Nenhuma alteração foi feita (campos vazios ou ID não encontrado).")
    else:
        print(f"\n❌ Erro ao atualizar: {res}")