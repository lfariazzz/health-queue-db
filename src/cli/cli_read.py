from src.database.read import (
    listar_medicos_por_unidade,
    listar_oferece,
    listar_unidades,
    listar_cidadaos,
    relatorio_estatistico_geral,
    listar_servicos_mais_procurados,
    listar_unidades_com_endereco,
    listar_dependentes_por_cidadao,
    listar_prioridade_de_cidadao_por_unidade,
    listar_historico_cidadao,
    listar_horarios_servico_unidade,
    filtrar_agendamentos_avancado,
)


# As funções de `src.database.read` já imprimem seus resultados.
# Aqui apenas chamamos os métodos diretamente.


def menu_read():
    while True:
        print("\n--- MENU ---")
        print("1. Listar serviços oferecidos")
        print("2. Listar unidades disponíveis")
        print("3. Listar possíveis clientes registrados")
        print("4. Listar médicos por unidade")
        print("5. Relatório estatístico geral (status)")
        print("6. Serviços mais procurados")
        print("7. Unidades com endereço")
        print("8. Dependentes de um cidadão")
        print("9. Ordem de prioridade por unidade")
        print("10. Histórico de agendamentos de um cidadão")
        print("11. Horários de um serviço em uma unidade")
        print("12. Filtrar agendamentos (unidade, serviço, status)")
        print("0. Voltar")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            continue

        if opcao == 1:
            listar_oferece()
        elif opcao == 2:
            listar_unidades()
        elif opcao == 3:
            listar_cidadaos()
        elif opcao == 4:
            nome_unidade = input("Nome da unidade: ")
            listar_medicos_por_unidade(nome_unidade)
        elif opcao == 5:
            relatorio_estatistico_geral()
        elif opcao == 6:
            listar_servicos_mais_procurados()
        elif opcao == 7:
            listar_unidades_com_endereco()
        elif opcao == 8:
            cpf = input("CPF do responsável: ")
            listar_dependentes_por_cidadao(cpf)
        elif opcao == 9:
            nome_unidade = input("Nome da unidade: ")
            listar_prioridade_de_cidadao_por_unidade(nome_unidade)
        elif opcao == 10:
            cpf = input("CPF do cidadão: ")
            listar_historico_cidadao(cpf)
        elif opcao == 11:
            servico = input("Nome do serviço: ")
            unidade = input("Nome da unidade: ")
            listar_horarios_servico_unidade(servico, unidade)
        elif opcao == 12:
            unidade = input("Nome da unidade: ")
            servico = input("Nome do serviço: ")
            status = input("Status do agendamento: ")
            filtrar_agendamentos_avancado(unidade, servico, status)
        elif opcao == 0:
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_read()
