CREATE TABLE tb_clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente TEXT NOT NULL
);

CREATE TABLE tb_vendas (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    quantidade INTEGER,
    preco_unitario REAL,
    categoria TEXT,
    id_cliente INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES tb_clientes(id_cliente)
);
