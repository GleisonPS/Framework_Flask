import sqlite3

# Conectar ao banco de dados ou criar um novo se não existir
conn = sqlite3.connect('vendas.db')

# Criar o cursor
c = conn.cursor()

comando_Cliente = """
    INSERT INTO cliente (idcliente, nome, email, cidade, telefone, data_nasc) VALUES
    (5, 'John Doe', 'john.doe@example.com', 'New York', 123456789, '1990-01-15'),
    (6, 'Jane Smith', 'jane.smith@example.com', 'Los Angeles', 987654321, '1985-05-20'),
    (7, 'Alice Johnson', 'alice.johnson@example.com', 'Chicago', 555444333, '1978-12-10'),
    (8, 'Michael Brown', 'michael.brown@example.com', 'Houston', 111222333, '1982-08-25'),
    (9, 'Emily Wilson', 'emily.wilson@example.com', 'San Francisco', 777888999, '1995-03-12');
"""
comando_Produto = """
    INSERT INTO produto (idproduto, nome, marca, categoria, preco, qtd) VALUES
    (5,'Smartphone', 'Samsung', 'Eletrônicos', 999.99, 50),
    (6, 'Laptop', 'Apple', 'Eletrônicos', 1499.99, 30),
    (7, 'Headphones', 'Sony', 'Eletrônicos', 199.99, 100),
    (8, 'Sneakers', 'Nike', 'Calçados', 129.99, 200),
    (9, 'T-Shirt', 'Adidas', 'Roupas', 29.99, 300);    
"""
comando_Vendas = """
    INSERT INTO venda (idvenda, data_venda, valor_total, idcliente, idproduto, funcionario) VALUES 
    (6, '2024-03-10', 2500.00, 1, 1,'Mario'),
    (7, '2024-03-11', 1500.00, 2, 2, 'Luide'),
    (8, '2024-03-12', 1800.00, 3, 3, 'Brozer'),
    (9, '2024-03-13', 300.00, 4, 4, 'Pit'),
    (10, '2024-03-14', 240.00, 5, 5,'Yochi');
"""
c.execute(comando_Cliente)
c.execute(comando_Produto)
c.execute(comando_Vendas)

conn.commit()