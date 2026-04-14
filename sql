CRIAR BANCO + TABELA

CREATE DATABASE IF NOT EXISTS escola;
USE escola;

CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    curso VARCHAR(100) NOT NULL
);

INSERIR DADOS

INSERT INTO alunos (nome, idade, curso) VALUES
('João', 16, 'Informática'),
('Maria', 17, 'Administração'),
('Carlos', 18, 'Enfermagem');

PESQUISAR

SELECT * FROM alunos;

PESQUISAR POR NOME

SELECT * FROM alunos
WHERE nome LIKE '%João%';

ATUALIZAR

UPDATE alunos
SET nome = 'João Silva', idade = 17, curso = 'TI'
WHERE id = 1;

EXCLUIR

DELETE FROM alunos
WHERE id = 1;
