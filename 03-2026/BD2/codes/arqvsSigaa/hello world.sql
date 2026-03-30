-- PALAVRAS RESERVADAS:
CREATE;
SELECT; 
UPDATE; 
DELETE;
FROM;
ON;
DROP;
DATABASE;


-- criar uma nova database
CREATE DATABASE IF NOT EXISTS 
    helloworld;
-- ver todos os bancos
SHOW DATABASES;
-- SELECIONAR BANCO
USE helloworld;
-- criar uma nova tabela no nosso banco

CREATE TABLE aluno (
    -- VARCHAR É MESMA COISA QUE TEXTO
    -- (50) O TAMANHO DOS CARACTERES
    nome_aluno VARCHAR(50),
    -- INT / NUMERO
    matricula INT,
    -- DATAS
    nascimento DATETIME  
);

DESC aluno;

-- alterar a tabela 
-- que ja existe
-- ADICIONANDO UM NOVO ATRIBUTO
ALTER TABLE aluno 
ADD COLUMN turma VARCHAR(10);

-- REMOVENDO UM ATRIBUTO
ALTER TABLE aluno 
DROP COLUMN nascimento;

-- tabela com chave primaria
CREATE TABLE professor(
    -- IDENTIFICADOR 
    -- UNICO DA TABELA
    cpf INT PRIMARY KEY, 
    nome VARCHAR(50),
    -- boolean = verdadeiro 
    -- ou falso
    ferias BOOLEAN
);


CREATE TABLE pessoa(
    rg INT,
    cpf INT,
    -- adicionei uma LIGAÇÃO 
    -- A CHAVE 
    -- CPF DO PROFESSOR 
    -- ESTA LIGADA 
    -- COM ESSA CHAVE
    -- ESTRANGEIRA
    CONSTRAINT 
    fk_cpf FOREIGN KEY (cpf) 
    REFERENCES professor(cpf)
);

-- deletar uma tabela 
-- usar com cuidado
DROP TABLE aluno;


-- mostrar tabelas
SHOW TABLES;    

-- deletar o banco de dados
DROP DATABASE helloworld;

-- COLOCAR INFORMAÇÕES 
-- DENTRO TABELA

-- GRAVAR ESSE COMANDO
-- inserir na tabela aluno
INSERT INTO aluno (
    -- nessas colunas
    nome_aluno,
    matricula 
    ) 
VALUES 
-- esses valores
(
    'Ryan',
    123478127
);

-- ver informações 
-- da nossa tabela
SELECT nome_aluno, matricula
FROM aluno;

-- posso falar quais campos 
-- quero ver da tabela
-- ou posso ver tudo com o * :D
SELECT *
FROM aluno;

-- atualize a tabela aluno
UPDATE aluno 
-- altere o nome_aluno para Ryan Marcos 
SET nome_aluno = 'Ryan Marcos Fragnani';


insert into aluno (nome_aluno) values ('Maria');
insert into aluno (nome_aluno) values ('João');
insert into aluno (nome_aluno) values ('Roberto');
insert into aluno (nome_aluno) values ('José');
insert into aluno (nome_aluno) values ('Ana');

UPDATE aluno 
-- altere o nome_aluno para Ryan Marcos 
SET nome_aluno = 'Ryan' 
-- quando matricula não for nulo
WHERE matricula IS NOT NULL;

-- altere o nome do aluno para RUAN
UPDATE aluno
SET nome_aluno = 'Ruan'
-- onde a matricula é essa aqui:
WHERE matricula = 123478127;

