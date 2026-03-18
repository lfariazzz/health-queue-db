USE sistema_gestao_filas_agendamentos_publicos;

-- 1. ENDEREÇO
INSERT INTO endereco (cep, rua, numero, bairro) VALUES ('63010-000', 'Rua das Flores', '100', 'Centro');
INSERT INTO endereco (cep, rua, numero, bairro) VALUES ('63020-000', 'Av. Brasil', '500', 'São José');
INSERT INTO endereco (cep, rua, numero, bairro) VALUES ('63030-000', 'Rua do Horto', 's/n', 'Horto');
INSERT INTO endereco (cep, rua, numero, bairro) VALUES ('63040-000', 'Rua Padre Cícero', '25', 'Salesianos');
INSERT INTO endereco (cep, rua, numero, bairro) VALUES ('63050-000', 'Av. Castelo Branco', '1200', 'Pirajá');
INSERT INTO endereco (cep, rua, numero, bairro) VALUES ('63010-010', 'Rua São Pedro', '88', 'Centro');

-- 2. SERVIÇO
INSERT INTO servico (nome, tempo_medio) VALUES ('Emissão de RG', 20);
INSERT INTO servico (nome, tempo_medio) VALUES ('Renovação de CNH', 30);
INSERT INTO servico (nome, tempo_medio) VALUES ('Vacinação Covid-19', 10);
INSERT INTO servico (nome, tempo_medio) VALUES ('Cadastro Único', 40);
INSERT INTO servico (nome, tempo_medio) VALUES ('Consulta Clínica', 15);
INSERT INTO servico (nome, tempo_medio) VALUES ('Entrega de Título', 5);

-- 3. UNIDADE
INSERT INTO unidade (nome, tipo, id_endereco) VALUES ('Vapt Vupt Juazeiro', 'Central de Atendimento', 1);
INSERT INTO unidade (nome, tipo, id_endereco) VALUES ('Posto de Saúde Central', 'Saúde', 2);
INSERT INTO unidade (nome, tipo, id_endereco) VALUES ('Detran Unidade Triângulo', 'Trânsito', 3);
INSERT INTO unidade (nome, tipo, id_endereco) VALUES ('Centro de Multiatendimento', 'Serviços Públicos', 4);
INSERT INTO unidade (nome, tipo, id_endereco) VALUES ('Secretaria de Finanças', 'Administrativo', 5);
INSERT INTO unidade (nome, tipo, id_endereco) VALUES ('Câmara Municipal', 'Legislativo', 6);

-- 4. PESSOA
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
-- CORRIGIDO: adicionado médico
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('34343434343', 'Dr. Marcos Vinicius', '1980-03-10', 1);
-- Dependentes
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('00011100011', 'Ana Beatriz Jr', '2015-05-15', 1);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('00022200022', 'Bruno Filho', '2018-10-22', 2);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('00033300033', 'Carla Maria Jr', '2020-02-03', 3);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('00044400044', 'Gabriel Jr', '2012-04-12', 1);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('00055500055', 'Heloisa Jr', '2016-08-25', 2);
INSERT INTO pessoa (cpf, nome, data_nascimento, id_endereco) VALUES ('00066600066', 'Igor Jr', '2014-11-30', 3);

-- 5. USUARIO
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('11122233344', 'ana.souza@email.com', 'hash1', 'CID');
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('44455566677', 'diego.lima@email.com', 'hash4', 'GES');
INSERT INTO usuario (id_pessoa, email, senha_hash, perfil) VALUES ('00011122233', 'julia.paiva@email.com', 'hash10', 'CID');

-- 6. TELEFONE
INSERT INTO telefone (id_pessoa, cod_telefone, numero_telefone) VALUES ('11122233344', 1, '(88) 99911-2233');
INSERT INTO telefone (id_pessoa, cod_telefone, numero_telefone) VALUES ('44455566677', 1, '(88) 98877-6655');

-- 7. CIDADÃO
INSERT INTO cidadao (id_pessoa, cartao_sus, nis) VALUES ('11122233344', '700111222333441', '11122233344');
INSERT INTO cidadao (id_pessoa, cartao_sus, nis) VALUES ('22233344455', '700222333444552', '22233344455');
INSERT INTO cidadao (id_pessoa, cartao_sus, nis) VALUES ('33344455566', '700333444555663', '33344455566');
INSERT INTO cidadao (id_pessoa, cartao_sus, nis) VALUES ('77788899900', '700777888999007', '77788899900');
INSERT INTO cidadao (id_pessoa, cartao_sus, nis) VALUES ('88899900011', '700888999000118', '88899900011');
INSERT INTO cidadao (id_pessoa, cartao_sus, nis) VALUES ('99900011122', '700999000111229', '99900011122');
-- CORRIGIDO: dependentes precisam estar em cidadao para a query listar_dependentes funcionar
INSERT INTO cidadao (id_pessoa, cartao_sus, nis) VALUES ('00011100011', '700000111000111', '00011100011');
INSERT INTO cidadao (id_pessoa, cartao_sus, nis) VALUES ('00022200022', '700000222000222', '00022200022');

-- 8. DEPENDENTE
INSERT INTO dependente (id_pessoa, id_responsavel, vigencia, parentesco) VALUES ('00011100011', '11122233344', '2024-01-01', 'Filho(a)');
INSERT INTO dependente (id_pessoa, id_responsavel, vigencia, parentesco) VALUES ('00022200022', '22233344455', '2024-01-01', 'Filho(a)');

-- 9. FUNCIONÁRIO
INSERT INTO funcionario (id_pessoa, matricula, cargo, admissao) VALUES ('44455566677', 'MAT001', 'Atendente', '2024-01-10');
INSERT INTO funcionario (id_pessoa, matricula, cargo, admissao) VALUES ('55566677788', 'MAT002', 'Gerente', '2023-05-15');
INSERT INTO funcionario (id_pessoa, matricula, cargo, admissao) VALUES ('66677788899', 'MAT003', 'Supervisor', '2024-02-20');
INSERT INTO funcionario (id_pessoa, matricula, cargo, admissao) VALUES ('00011122233', 'MAT004', 'Atendente', '2024-03-01');
INSERT INTO funcionario (id_pessoa, matricula, cargo, admissao) VALUES ('12121212121', 'MAT005', 'Analista', '2023-12-12');
INSERT INTO funcionario (id_pessoa, matricula, cargo, admissao) VALUES ('23232323232', 'MAT006', 'Coordenador', '2024-01-05');
-- CORRIGIDO: médico adicionado para a query listar_medicos_por_unidade funcionar
INSERT INTO funcionario (id_pessoa, matricula, cargo, admissao) VALUES ('34343434343', 'MAT007', 'Médico', '2022-06-01');

-- 10. LOTAÇÃO
INSERT INTO lotacao (id_funcionario, id_unidade, data_inicio, data_final, horarios) VALUES ('44455566677', 1, '2024-01-10', '2026-12-31', '08:00 - 14:00');
INSERT INTO lotacao (id_funcionario, id_unidade, data_inicio, data_final, horarios) VALUES ('55566677788', 2, '2023-05-15', '2026-12-31', '09:00 - 15:00');
-- CORRIGIDO: lotação do médico adicionada
INSERT INTO lotacao (id_funcionario, id_unidade, data_inicio, data_final, horarios) VALUES ('34343434343', 2, '2022-06-01', '2026-12-31', '07:00 - 13:00');

-- 11. OFERECE
INSERT INTO oferece (id_unidade, id_servico, dia_semana, hora_inicio, hora_final, vagas) VALUES (1, 1, 'SEG', '08:00:00', '12:00:00', 20);
INSERT INTO oferece (id_unidade, id_servico, dia_semana, hora_inicio, hora_final, vagas) VALUES (1, 2, 'TER', '13:00:00', '17:00:00', 15);
INSERT INTO oferece (id_unidade, id_servico, dia_semana, hora_inicio, hora_final, vagas) VALUES (2, 3, 'QUA', '07:00:00', '11:00:00', 10);

-- 12. AGENDAMENTO
INSERT INTO agendamento (data, hora, id_unidade_sediada, id_cidadao_solicitado, id_servico_referente, status_agendamento, prioridade)
VALUES ('2026-04-01', '08:00:00', 1, '11122233344', 1, 'PENDENTE', 0);

INSERT INTO agendamento (data, hora, id_unidade_sediada, id_cidadao_solicitado, id_servico_referente, status_agendamento, prioridade)
VALUES ('2026-04-01', '09:30:00', 2, '22233344455', 3, 'CONFIRMADO', 1);

INSERT INTO agendamento (data, hora, id_unidade_sediada, id_cidadao_solicitado, id_servico_referente, status_agendamento, prioridade)
VALUES ('2026-04-02', '10:00:00', 3, '33344455566', 2, 'PENDENTE', 0);