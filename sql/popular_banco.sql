USE sistema_gestao_filas_agendamentos;

# Endereço 
INSERT INTO endereco (id_endereco, cep, rua, numero, bairro) VALUES (1, '63010-000', 'Rua São Pedro', '100', 'Centro');
INSERT INTO endereco (id_endereco, cep, rua, numero, bairro) VALUES (2, '63010-050', 'Rua do Cruzeiro', '45', 'Centro');
INSERT INTO endereco (id_endereco, cep, rua, numero, bairro) VALUES (3, '63040-000', 'Av. Padre Cícero', '2000', 'Triângulo');
INSERT INTO endereco (id_endereco, cep, rua, numero, bairro) VALUES (4, '63050-100', 'Rua Monsenhor Lima', '12', 'Salesianos');
INSERT INTO endereco (id_endereco, cep, rua, numero, bairro) VALUES (5, '63020-000', 'Rua Santa Luzia', '88', 'Pio XII');
INSERT INTO endereco (id_endereco, cep, rua, numero, bairro) VALUES (6, '63030-000', 'Av. Castelo Branco', '1000', 'Novo Juazeiro');

# Serviço
INSERT INTO servico (id_servico, nome, tempo_medio) VALUES (1, 'Emissão de RG', 20);
INSERT INTO servico (id_servico, nome, tempo_medio) VALUES (2, 'Renovação de CNH', 30);
INSERT INTO servico (id_servico, nome, tempo_medio) VALUES (3, 'Vacinação Covid-19', 10);
INSERT INTO servico (id_servico, nome, tempo_medio) VALUES (4, 'Cadastro Único', 40);
INSERT INTO servico (id_servico, nome, tempo_medio) VALUES (5, 'Consulta Clínica', 15);
INSERT INTO servico (id_servico, nome, tempo_medio) VALUES (6, 'Entrega de Título', 5);

# Unidade 
INSERT INTO unidade (id_unidade, nome, id_endereco) VALUES (1, 'Vapt Vupt Juazeiro', 1);
INSERT INTO unidade (id_unidade, nome, id_endereco) VALUES (2, 'Posto de Saúde Central', 2);
INSERT INTO unidade (id_unidade, nome, id_endereco) VALUES (3, 'Detran Unidade Triângulo', 3);
INSERT INTO unidade (id_unidade, nome, id_endereco) VALUES (4, 'Centro de Multiatendimento', 4);
INSERT INTO unidade (id_unidade, nome, id_endereco) VALUES (5, 'Secretaria de Finanças', 5);
INSERT INTO unidade (id_unidade, nome, id_endereco) VALUES (6, 'Câmara Municipal', 6);

# Pessoa 
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('11122233344', 'Ana Beatriz Souza', '1990-05-15', 1);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('22233344455', 'Bruno Oliveira Santos', '1985-10-22', 2);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('33344455566', 'Carla Maria Ferreira', '1998-02-03', 3);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('44455566677', 'Diego Ricardo Lima', '1975-12-30', 4);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('55566677788', 'Elena das Dores Martins', '2000-07-15', 5);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('66677788899', 'Fabio Junior de Alencar', '1992-09-05', 6);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('77788899900', 'Gabriel Rocha', '1988-04-12', 1);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('88899900011', 'Heloisa Mendes', '1995-08-25', 2);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('99900011122', 'Igor Cavalcante', '1982-11-30', 3);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('00011122233', 'Julia Paiva', '1993-01-14', 4);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('12121212121', 'Kauan Silva', '2001-06-20', 5);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('23232323232', 'Larissa Gomes', '1997-03-08', 6);

# Usuário
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('11122233344', 'ana.souza@email.com', 'hash1', 'USER');
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('22233344455', 'bruno.santos@email.com', 'hash2', 'USER');
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('33344455566', 'carla.ferreira@email.com', 'hash3', 'USER');
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('77788899900', 'gabriel.rocha@email.com', 'hash7', 'USER');
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('88899900011', 'heloisa.mendes@email.com', 'hash8', 'USER');
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('99900011122', 'igor.cavalcante@email.com', 'hash9', 'USER');
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('44455566677', 'diego.lima@email.com', 'hash4', 'ADMIN');
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('55566677788', 'elena.martins@email.com', 'hash5', 'ADMIN');
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('66677788899', 'fabio.alencar@email.com', 'hash6', 'ADMIN');
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('00011122233', 'julia.paiva@email.com', 'hash10', 'USER');
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('12121212121', 'kauan.silva@email.com', 'hash11', 'USER');
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('23232323232', 'larissa.gomes@email.com', 'hash12', 'USER');

# Telefone
INSERT INTO telefone (numero, cpf_pessoa) VALUES ('(88) 99911-2233', '11122233344');
INSERT INTO telefone (numero, cpf_pessoa) VALUES ('(88) 99922-3344', '22233344455');
INSERT INTO telefone (numero, cpf_pessoa) VALUES ('(88) 3511-0000', '33344455566');
INSERT INTO telefone (numero, cpf_pessoa) VALUES ('(88) 98877-6655', '44455566677');
INSERT INTO telefone (numero, cpf_pessoa) VALUES ('(88) 99955-4433', '55566677788');
INSERT INTO telefone (numero, cpf_pessoa) VALUES ('(88) 3512-1122', '66677788899');

# Cidadão
INSERT INTO cidadao (id_pessoa, data_cadastro) VALUES ('11122233344', '2024-01-10');
INSERT INTO cidadao (id_pessoa, data_cadastro) VALUES ('22233344455', '2024-02-15');
INSERT INTO cidadao (id_pessoa, data_cadastro) VALUES ('33344455566', '2024-03-20');
INSERT INTO cidadao (id_pessoa, data_cadastro) VALUES ('77788899900', '2024-04-05');
INSERT INTO cidadao (id_pessoa, data_cadastro) VALUES ('88899900011', '2024-04-10');
INSERT INTO cidadao (id_pessoa, data_cadastro) VALUES ('99900011122', '2024-05-01');

# Funcionario
INSERT INTO funcionario (id_pessoa, salario, cargo) VALUES ('44455566677', 2500.00, 'Atendente');
INSERT INTO funcionario (id_pessoa, salario, cargo) VALUES ('55566677788', 4800.00, 'Gerente');
INSERT INTO funcionario (id_pessoa, salario, cargo) VALUES ('66677788899', 3200.00, 'Supervisor');
INSERT INTO funcionario (id_pessoa, salario, cargo) VALUES ('00011122233', 2800.00, 'Atendente');
INSERT INTO funcionario (id_pessoa, salario, cargo) VALUES ('12121212121', 3500.00, 'Analista');
INSERT INTO funcionario (id_pessoa, salario, cargo) VALUES ('23232323232', 4200.00, 'Coordenador');

# Lotação
INSERT INTO lotacao (id_pessoa, id_unidade, data_inicio) VALUES ('44455566677', 1, '2023-01-10');
INSERT INTO lotacao (id_pessoa, id_unidade, data_inicio) VALUES ('55566677788', 2, '2023-02-15');
INSERT INTO lotacao (id_pessoa, id_unidade, data_inicio) VALUES ('66677788899', 3, '2023-03-20');
INSERT INTO lotacao (id_pessoa, id_unidade, data_inicio) VALUES ('00011122233', 4, '2023-04-05');
INSERT INTO lotacao (id_pessoa, id_unidade, data_inicio) VALUES ('12121212121', 5, '2023-05-10');
INSERT INTO lotacao (id_pessoa, id_unidade, data_inicio) VALUES ('23232323232', 6, '2023-06-15');

# Oferece
INSERT INTO oferece (id_unidade, id_servico) VALUES (1, 1);
INSERT INTO oferece (id_unidade, id_servico) VALUES (1, 2);
INSERT INTO oferece (id_unidade, id_servico) VALUES (2, 3);
INSERT INTO oferece (id_unidade, id_servico) VALUES (2, 5);
INSERT INTO oferece (id_unidade, id_servico) VALUES (3, 2);
INSERT INTO oferece (id_unidade, id_servico) VALUES (4, 4);

# Dependendente
INSERT INTO dependente (nome, data_nascimento, id_pessoa_responsavel) VALUES ('Ana Beatriz Jr', '2015-05-15', '11122233344');
INSERT INTO dependente (nome, data_nascimento, id_pessoa_responsavel) VALUES ('Bruno Filho', '2018-10-22', '22233344455');
INSERT INTO dependente (nome, data_nascimento, id_pessoa_responsavel) VALUES ('Carla Maria Jr', '2020-02-03', '33344455566');
INSERT INTO dependente (nome, data_nascimento, id_pessoa_responsavel) VALUES ('Gabriel Jr', '2012-04-12', '77788899900');
INSERT INTO dependente (nome, data_nascimento, id_pessoa_responsavel) VALUES ('Heloisa Jr', '2016-08-25', '88899900011');
INSERT INTO dependente (nome, data_nascimento, id_pessoa_responsavel) VALUES ('Igor Jr', '2014-11-30', '99900011122');

# Agendamento
INSERT INTO agendamento (data_hora, status, id_pessoa, id_servico, id_unidade) VALUES ('2026-04-01 08:00:00', 'Agendado', '11122233344', 1, 1);
INSERT INTO agendamento (data_hora, status, id_pessoa, id_servico, id_unidade) VALUES ('2026-04-01 09:00:00', 'Concluido', '22233344455', 3, 2);
INSERT INTO agendamento (data_hora, status, id_pessoa, id_servico, id_unidade) VALUES ('2026-04-02 10:30:00', 'Agendado', '33344455566', 2, 3);
INSERT INTO agendamento (data_hora, status, id_pessoa, id_servico, id_unidade) VALUES ('2026-04-02 14:00:00', 'Cancelado', '77788899900', 4, 4);
INSERT INTO agendamento (data_hora, status, id_pessoa, id_servico, id_unidade) VALUES ('2026-04-03 08:30:00', 'Agendado', '88899900011', 6, 5);
INSERT INTO agendamento (data_hora, status, id_pessoa, id_servico, id_unidade) VALUES ('2026-04-03 11:00:00', 'Agendado', '99900011122', 5, 6);