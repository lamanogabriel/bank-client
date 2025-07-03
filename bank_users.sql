
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    agencia TEXT,
    conta TEXT,
    status TEXT
);

INSERT INTO clientes (id, nome, agencia, conta, status) VALUES
(1, 'Ana Lima', '0001', '12345-6', 'ativa'),
(2, 'Bruno Rocha', '0001', '65432-1', 'bloqueada'),
(3, 'Clara Nunes', '0002', '11223-3', 'ativa');
