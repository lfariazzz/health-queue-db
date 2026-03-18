# Sistema de Gestão de Filas e Agendamentos Públicos

## 📌 Descrição e Objetivos
Este projeto consiste no desenvolvimento de um Banco de Dados passando pelo ciclo completo de projeto, da modelagem conceitual à implementação lógica, para apoiar a gestão pública, norteado pela questão de pesquisa do **Tema 7**, proposto na disciplina de Banco de Dados (UFCA).

**Questão de Pesquisa:**
> "Como um sistema para gestão de filas e agendamentos públicos (CRAS, postos de saúde, CREAS) pode reduzir tempo de espera e faltas com regras de prioridade?"

**Objetivos Principais:**
* Modelar um banco de dados capaz de gerenciar agendamentos em múltiplas unidades (Saúde e Assistência Social).
* Implementar regras de negócio para **prioridades legais** (idosos, PCDs, gestantes).
* Criar mecanismos para registro e monitoramento de **faltas**.
* Extrair requisitos de informação de um contexto;
* Construir um MER explícito (entidades, atributos, chaves, relacionamentos, cardinalidades, regras);
* Elaborar um DER claro na notação escolhida (notação Chen ou Crow’s Foot).;
* Mapear ER → relacional (tabelas, PK/FK, associativas, especializações, entidades fracas);
* Identificar Dependências Funcionais (DFs) e normalizar (1FN, 2FN, 3FN), reconhecendo e prevenindo anomalias.
* Desenvolver habilidades de projeto em equipe e resolução de problemas reais.

## 📂 Estrutura do Projeto e Instruções

A documentação deste projeto está organizada na **Wiki** deste repositório, com uma página para cada um dos artefatos entregues:

* **[Acesse a WIKI Oficial aqui](https://github.com/lfariazzz/health-queue-db/wiki)**
    * Consulte a seção *01. Discussão, Requisitos e Modelo Conceitual* para entender as Regras de Negócio e Histórias de Usuário.
    * Consulte a seção *02. MER* e *03. DER* para ver a modelagem dos dados.
    * Consulte a seção *04. Esquema Relacional* para ver a estrutura das tabelas mapeadas.
    * Consulte a seção *05. Normalização* para ver a análise de dependências funcionais e formas normais (1FN, 2FN, 3FN).
    * Consulte a seção *06. Amostra Mínima de Dados* para ver os dados de teste utilizados.
    * Consulte a seção *07. Consultas em Linguagem Natural* para ver as perguntas de negócio respondidas pelo sistema.
    * Consulte a seção *08. Implementação do Modelo Físico* para ver os ajustes estruturais realizados no modelo e as decisões técnicas tomadas nesta etapa.

---

## ⚙️ Como Executar

### Pré-requisitos
- Python 3.8+
- MySQL 8.0+

### Passo a passo

1. Clone o repositório:
```bash
## Configuração do banco

1. Instale o MySQL localmente
2. Rode o script `banco.sql` para criar o banco
3. Copie `.env.example` para `.env`:
   cp .env.example .env
4. Edite o `.env` com sua senha do MySQL
5. pip install mysql-connector-python python-dotenv
6. python main.py
```

## 👥 Equipe do Projeto
| Desenvolvedor | Perfil
| :--- | :--- |
| **Levi Farias** | [@lfariazzz](https://github.com/lfariazzz)
| **Henrique Coimbra** | [@HenriqueCoimbra12](https://github.com/HenriqueCoimbra12)
| **Malaquias** | [@malaquiaso841-cyber](https://github.com/malaquiaso841-cyber)
| **André** | [@awesleyy](https://github.com/awesleyy)

**Orientador:** Prof. Willianson Silva & Prof. Raphael Will

---
*Projeto desenvolvido como requisito parcial da disciplina de Banco de Dados.*
