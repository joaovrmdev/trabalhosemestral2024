
# README - Criação do banco, chaves primarias e estrangeiras e inserção de dados

## 0. Database e Schema
```sql
CREATE DATABASE trabalhosemestral2024;

USE DATABASE trabalhosemestral2024;

CREATE SCHEMA projetoparte3;
```


## 1. Criação das Tabelas

### Tabela empresa
```sql
CREATE OR REPLACE TABLE empresa (
    id INTEGER AUTOINCREMENT(1,1) PRIMARY KEY,
    nome STRING NOT NULL,
    endereco STRING NOT NULL
);
```

### Tabela cidade
```sql
CREATE OR REPLACE TABLE cidade (
    nome STRING NOT NULL,
    estado STRING NOT NULL,
    PRIMARY KEY (nome)
);
```

### Tabela cliente
```sql
CREATE OR REPLACE TABLE cliente (
    id INTEGER AUTOINCREMENT(1,1) PRIMARY KEY,
    cpf STRING NOT NULL,
    rg STRING NOT NULL,
    nome_compl STRING NOT NULL,
    endereco_cliente STRING NOT NULL
);
```

### Tabela servico
```sql
CREATE OR REPLACE TABLE servico (
    nome_servico STRING PRIMARY KEY,
    id_guindaste INTEGER,
    id_transporte INTEGER
);
```

### Tabela guindaste
```sql
CREATE OR REPLACE TABLE guindaste (
    id INTEGER AUTOINCREMENT(1,1) PRIMARY KEY,
    tamanho_base FLOAT NOT NULL,
    altura FLOAT NOT NULL
);
```

### Tabela transporte
```sql
CREATE OR REPLACE TABLE transporte (
    id INTEGER AUTOINCREMENT(1,1) PRIMARY KEY
);
```

### Tabela telefone_cliente
```sql
CREATE OR REPLACE TABLE telefone_cliente (
    id INTEGER AUTOINCREMENT(1,1) PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    telefone STRING NOT NULL
);
```

### Tabela telefone_empresa
```sql
CREATE OR REPLACE TABLE telefone_empresa (
    id INTEGER AUTOINCREMENT(1,1) PRIMARY KEY,
    id_empresa INTEGER NOT NULL,
    telefone STRING NOT NULL
);
```

### Tabela pedido
```sql
CREATE OR REPLACE TABLE pedido (
    codigo INTEGER AUTOINCREMENT(1,1) PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    id_empresa INTEGER NOT NULL,
    endereco_part STRING NOT NULL,
    endereco_dest STRING NOT NULL,
    id_solicitacao INTEGER NOT NULL
);
```

### Tabela solicitacao
```sql
CREATE OR REPLACE TABLE solicitacao (
    id INTEGER AUTOINCREMENT(1,1) PRIMARY KEY,
    codigo_pedido INTEGER NOT NULL,
    nome_servico STRING NOT NULL,
    preco FLOAT NOT NULL,
    data_fin STRING NOT NULL,
    tempo_durac INTEGER NOT NULL
);
```

### Tabela func_solicitados
```sql
CREATE OR REPLACE TABLE func_solicitados (
    id INTEGER AUTOINCREMENT(1,1) PRIMARY KEY,
    id_solicitacao INTEGER NOT NULL,
    cpf_func STRING NOT NULL
);
```

### Tabela funcionarios
```sql
CREATE OR REPLACE TABLE funcionarios (
    CPF STRING PRIMARY KEY,
    RG STRING NOT NULL,
    nome STRING NOT NULL,
    endereco STRING NOT NULL,
    telefone STRING NOT NULL,
    tipoFunc STRING NOT NULL,
    salario FLOAT NOT NULL
);
```

### Tabela servico_empresa_cidade
```sql
CREATE OR REPLACE TABLE servico_empresa_cidade (
    id INTEGER AUTOINCREMENT(1,1) PRIMARY KEY,
    id_empresa INTEGER NOT NULL,
    id_cidade STRING NOT NULL,
    id_servico STRING NOT NULL,
    preco_hora FLOAT NOT NULL
);
```

### Tabela acrescimo
```sql
CREATE OR REPLACE TABLE acrescimo (
    id INTEGER AUTOINCREMENT(1,1) PRIMARY KEY,
    id_transporte INTEGER NOT NULL,
    percentual_IT FLOAT NOT NULL,
    limite_carga FLOAT NOT NULL
);
```

### Tabela bonusAumento
```sql
CREATE OR REPLACE TABLE bonusAumento (
    id INTEGER AUTOINCREMENT(1,1) PRIMARY KEY,
    id_guindaste INTEGER NOT NULL,
    percentual FLOAT NOT NULL,
    aumento FLOAT NOT NULL
);
```

---

## 2. Criação das chaves estrangeiras

### Exemplo: Tabela servico
```sql
-- Tabela servico
ALTER TABLE servico
ADD CONSTRAINT fk_guindaste FOREIGN KEY (id_guindaste) REFERENCES guindaste(id) ON DELETE CASCADE;

ALTER TABLE servico
ADD CONSTRAINT fk_transporte FOREIGN KEY (id_transporte) REFERENCES transporte(id) ON DELETE CASCADE;

-- Tabela telefone_cliente
ALTER TABLE telefone_cliente
ADD CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id) ON DELETE CASCADE;

-- Tabela telefone_empresa
ALTER TABLE telefone_empresa
ADD CONSTRAINT fk_empresa FOREIGN KEY (id_empresa) REFERENCES empresa(id) ON DELETE CASCADE;

-- Tabela pedido
ALTER TABLE pedido
ADD CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id) ON DELETE CASCADE;

ALTER TABLE pedido
ADD CONSTRAINT fk_empresa FOREIGN KEY (id_empresa) REFERENCES empresa(id) ON DELETE CASCADE;

ALTER TABLE pedido
ADD CONSTRAINT fk_solicitacao FOREIGN KEY (id_solicitacao) REFERENCES solicitacao(id) ON DELETE CASCADE;

-- Tabela solicitacao
ALTER TABLE solicitacao
ADD CONSTRAINT fk_pedido FOREIGN KEY (codigo_pedido) REFERENCES pedido(codigo) ON DELETE CASCADE;

ALTER TABLE solicitacao
ADD CONSTRAINT fk_servico FOREIGN KEY (nome_servico) REFERENCES servico(nome_servico) ON DELETE CASCADE;

-- Tabela func_solicitados
ALTER TABLE func_solicitados
ADD CONSTRAINT fk_solicitacao FOREIGN KEY (id_solicitacao) REFERENCES solicitacao(id) ON DELETE CASCADE;

ALTER TABLE func_solicitados
ADD CONSTRAINT fk_funcionario FOREIGN KEY (cpf_func) REFERENCES funcionarios(CPF) ON DELETE CASCADE;

-- Tabela servico_empresa_cidade
ALTER TABLE servico_empresa_cidade
ADD CONSTRAINT fk_empresa FOREIGN KEY (id_empresa) REFERENCES empresa(id) ON DELETE CASCADE;

ALTER TABLE servico_empresa_cidade
ADD CONSTRAINT fk_cidade FOREIGN KEY (id_cidade) REFERENCES cidade(nome) ON DELETE CASCADE;

ALTER TABLE servico_empresa_cidade
ADD CONSTRAINT fk_servico FOREIGN KEY (id_servico) REFERENCES servico(nome_servico) ON DELETE CASCADE;

-- Tabela acrescimo
ALTER TABLE acrescimo
ADD CONSTRAINT fk_transporte FOREIGN KEY (id_transporte) REFERENCES transporte(id) ON DELETE CASCADE;

-- Tabela bonusAumento
ALTER TABLE bonusAumento
ADD CONSTRAINT fk_guindaste FOREIGN KEY (id_guindaste) REFERENCES guindaste(id) ON DELETE CASCADE;

```


## 3. Inserção de Dados de Teste

### Tabela cidade
```sql
INSERT INTO cidade (nome, estado) VALUES
('São Paulo', 'SP'),
('Rio de Janeiro', 'RJ'),
('Curitiba', 'PR');
```

### Tabela empresa
```sql
INSERT INTO empresa (nome, endereco) VALUES
('Empresa A', 'Rua 1, 100'),
('Empresa B', 'Rua 2, 200');
```

### Tabela cliente
```sql
INSERT INTO cliente (cpf, rg, nome_compl, endereco_cliente) VALUES
('12345678901', 'MG123456', 'João Silva', 'Rua A, 50'),
('98765432100', 'SP654321', 'Maria Oliveira', 'Rua B, 75');
```

### Tabela guindaste
```sql
INSERT INTO guindaste (tamanho_base, altura) VALUES
(10.5, 20.0),
(12.0, 25.0);
```

### Tabela transporte
```sql
INSERT INTO transporte DEFAULT VALUES;
INSERT INTO transporte DEFAULT VALUES;
```

### Tabela telefone_cliente
```sql
INSERT INTO telefone_cliente (id_cliente, telefone) VALUES
(1, '(11) 98765-4321'),
(2, '(21) 99876-5432');
```

### Tabela telefone_empresa
```sql
INSERT INTO telefone_empresa (id_empresa, telefone) VALUES
(1, '(11) 12345-6789'),
(2, '(21) 98765-4321');
```

### Tabela pedido
```sql
INSERT INTO pedido (id_cliente, id_empresa, endereco_part, endereco_dest, id_solicitacao) VALUES
(1, 1, 'Rua A, 50', 'Rua C, 100', 1),
(2, 2, 'Rua B, 75', 'Rua D, 150', 2);
```

### Tabela solicitacao
```sql
INSERT INTO solicitacao (codigo_pedido, nome_servico, preco, data_fin, tempo_durac) VALUES
(1, 'Guindaste', 0, '2024-12-31', 5),
(2, 'Transporte', 0, '2024-12-30', 3);
```

### Tabela func_solicitados
```sql
INSERT INTO func_solicitados (id_solicitacao, cpf_func) VALUES
(1, '12345678901'),
(2, '98765432100');
```

### Tabela funcionarios
```sql
INSERT INTO funcionarios (cpf, rg, nome, endereco, telefone, tipoFunc, salario) VALUES
('12345678901', 'MG123456', 'João Silva', 'Rua A, 50', '(11) 98765-4321', 'Operador', 3000.00),
('98765432100', 'SP654321', 'Maria Oliveira', 'Rua B, 75', '(21) 99876-5432', 'Motorista', 3500.00);
```

### Tabela servico
```sql
INSERT INTO servico (nome_servico, id_guindaste, id_transporte) VALUES
('Guindaste', 1, NULL),
('Transporte', NULL, 1);
```

### Tabela servico_empresa_cidade
```sql
INSERT INTO servico_empresa_cidade (id_empresa, id_cidade, id_servico, preco_hora) VALUES
(1, 'São Paulo', 'Guindaste', 500.00),
(2, 'Rio de Janeiro', 'Transporte', 200.00);
```

### Tabela acrescimo
```sql
INSERT INTO acrescimo (id_transporte, percentual_it, limite_carga) VALUES
(1, 10.0, 5000.0),
(2, 15.0, 7000.0);
```

### Tabela bonusAumento
```sql
INSERT INTO bonusAumento (id_guindaste, percentual, aumento) VALUES
(1, 5.0, 200.0),
(2, 7.5, 300.0);
```

---

## 4. Criação de Triggers

### Atualizar Preço da Solicitação
A trigger abaixo atualiza o preço das solicitações com base na duração e no preço por hora do serviço correspondente:

```sql
CREATE OR REPLACE PROCEDURE atualizar_preco()
RETURNS STRING
LANGUAGE SQL
AS
$$
BEGIN
    UPDATE solicitacao s
    SET preco = (
        SELECT se.preco_hora * s.tempo_durac
        FROM servico_empresa_cidade se
        JOIN pedido p ON se.id_empresa = p.id_empresa AND se.id_servico = s.nome_servico
        WHERE p.codigo = s.codigo_pedido
    )
    WHERE EXISTS (
        SELECT 1
        FROM servico_empresa_cidade se
        JOIN pedido p ON se.id_empresa = p.id_empresa AND se.id_servico = s.nome_servico
        WHERE p.codigo = s.codigo_pedido
    );
    RETURN 'Preços atualizados com sucesso!';
END;
$$;
```

