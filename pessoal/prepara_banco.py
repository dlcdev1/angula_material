import sqlite3

connection = sqlite3.connect('banco_pessoal.db')
cursor = connection.cursor()

cria_tabela_mes = """
CREATE TABLE IF NOT EXISTS meses (
    id_mes INTEGER PRIMARY KEY,
    name  VARCHAR(12),
    ano INTEGER(4) NOT NULL 
);
"""

cria_tabela_contas = """
CREATE TABLE IF NOT EXISTS contas (
    id_contas INTEGER PRIMARY KEY AUTOINCREMENT,
    id_mes INTEGER NOT NULL,
    name_conta TEXT NOT NULL,
    vencimento VARCHAR(6) NOT NULL,
    valor REAL NOT NULL,
    data_pagamento VARCHAR,
    codigo_b INTEGER,
    pago BOOLEAN,
    FOREIGN KEY(id_mes) REFERENCES meses(id_mes)
);
"""


cria_meses = """
INSERT INTO meses (id_mes, name, ano)
    VALUES
    (1, "Janeiro", strftime('%Y')), 
    (2, "Fevereiro", strftime('%Y')),
    (3, "Março", strftime('%Y')),
    (4, "Abril", strftime('%Y')),
    (5, "Maio", strftime('%Y')),
    (6, "Junho", strftime('%Y')),
    (7, "Julho", strftime('%Y')),
    (8, "Agosto", strftime('%Y')),
    (9, "Setembro", strftime('%Y')),
    (10, "Outubro", strftime('%Y')),
    (11, "Novembro", strftime('%Y')),
    (12, "Dezembro", strftime('%Y'));
"""

cursor.execute(cria_tabela_mes)
cursor.execute(cria_tabela_contas)
cursor.execute(cria_meses)
connection.commit()
connection.close()

