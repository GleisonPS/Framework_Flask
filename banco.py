import sqlite3

# Conectar ao banco de dados ou criar um novo se não existir
conn = sqlite3.connect('vendas.db')

# Criar o cursor
c = conn.cursor()

# Criar a tabela cliente
c.execute('''CREATE TABLE IF NOT EXISTS cliente (
                idcliente INTEGER PRIMARY KEY,
                nome TEXT,
                email TEXT,
                cidade TEXT,
                telefone INTERGER,
                data_nasc DATE
            )''')

# Criar a tabela produto
c.execute('''CREATE TABLE IF NOT EXISTS produto (
                idproduto INTEGER PRIMARY KEY,
                nome TEXT,
                marca TEXT,
                categoria TEXT,
                preco REAL,
                qtd INTEGER
            )''')

# Criar a tabela venda
c.execute('''CREATE TABLE IF NOT EXISTS venda (
                idvenda INTEGER PRIMARY KEY,
                data_venda DATE,
                valor_total REAL,
                idcliente INTEGER,
                idproduto INTEGER,
                funcionario TEXT,
                FOREIGN KEY (idcliente) REFERENCES cliente(idcliente),
                FOREIGN KEY (idproduto) REFERENCES produto(idproduto)
            )''')

# Commit para salvar as alterações
conn.commit()

# Fechar a conexão
conn.close()
