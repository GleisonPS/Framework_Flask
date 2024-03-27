from flask import Flask, redirect, render_template, request, template_rendered, url_for
import sqlite3

app = Flask(__name__)


@app.route('/home')
@app.route("/")
def home():
  return render_template('home.html')


#Clientes
#Pagina Inicial do cliente
@app.route("/cliente")
def cliente():
  con = sqlite3.connect("vendas.db")
  cur = con.cursor()
  cur.execute("Select * from cliente")

  dados = cur.fetchall()

  return render_template("cliente/index_Cliente.html", dados=dados)


#Inserindo Novos Cliente
@app.route("/novo_cliente", methods=["GET", "POST"])
def novo_cliente():
  if request.method == 'POST':  #se o metodo for pra inserir
    #Conectando no banco de dados e criando o cursos(cur)
    con = sqlite3.connect('vendas.db')
    cur = con.cursor()

    #Pegando os dados do formulario
    idcliente = request.form['idcliente']
    nome = request.form['nome']
    gmail = request.form['gmail']
    cidade = request.form['cidade']
    tell = request.form['tell']
    data_naci = request.form['data_nasc']

    #Inserindo o noco cliente
    comando_add = 'insert into cliente values(?,?,?,?,?,?)'
    cur.execute(comando_add, (
        idcliente,
        nome,
        gmail,
        cidade,
        tell,
        data_naci,
    ))
    con.commit()

    #Retornar a tela de visualização dos clientes
    return redirect(url_for('cliente'))

  else:  #Se não tiver dados pra inserir
    return render_template("cliente/cad_Cliente.html")


#Exluir um cliente
@app.route('/excluir/<string:id>', methods=["GET"])
def excluir(id):
  #Conectando do banco de dados
  con = sqlite3.connect('vendas.db')
  cur = con.cursor()

  #comando pra excluir
  comando_rem = 'delete from cliente where idcliente = ?'
  cur.execute(comando_rem, (id, ))
  con.commit()
  con.close()

  #Retornar a tela de visualização dos clientes
  return redirect(url_for('cliente'))


#Editar um cliente já inserido
@app.route('/editar_cliente/<string:id>', methods=['GET', 'POST'])
def editar_cliente(id):
  if request.method == 'GET':
    #Conectando no banco de dados e criando o cursos(cur)
    con = sqlite3.connect('vendas.db')
    cur = con.cursor()

    #pegando o cliende com id expecifico
    comando_busc = 'select * from cliente where idcliente = ?'
    cur.execute(comando_busc, (id, ))
    cliente = cur.fetchone()
    cur.close()

    return render_template('cliente/editar_cliente.html', cliente=cliente)

  elif request.method == 'POST':
    #Conectando no banco de dados e criando o cursos(cur)
    con = sqlite3.connect('vendas.db')
    cur = con.cursor()

    #Pegando os valores atualizados
    nome = request.form["nome"]
    gmail = request.form['gmail']
    cidade = request.form['cidade']
    telefone = request.form['tell']
    data_nasc = request.form['data_nasc']

    #Atualizar dados
    cur.execute(
        'update cliente set nome = ?,email = ?,cidade =?,telefone = ?,data_nasc = ? where idcliente = ?',
        (
            nome,
            gmail,
            cidade,
            telefone,
            data_nasc,
            id,
        ))
    con.commit()
    con.close()
    return redirect(url_for('cliente'))


#Produtos
#criando página inicial produto
@app.route('/produto')
def produto():
  con = sqlite3.connect('vendas.db')
  cur = con.cursor()
  cur.execute("Select * from produto")
  dados = cur.fetchall()
  cur.close()

  return render_template('produto/index_produto.html', dados=dados)


#Inserindo novo produto
@app.route('/novo_produto', methods=["GET", "POST"])
def novo_produto():
  if request.method == 'POST':  #se o metodo for pra inserir
    con = sqlite3.connect('vendas.db')
    cur = con.cursor()

    idproduto = request.form['idproduto']
    nome = request.form['nome']
    marca = request.form["marca"]
    categoria = request.form['categoria']
    preco = request.form['preco']
    qtd = request.form['qtd']

    comando_add = 'insert into produto values(?,?,?,?,?,?)'
    cur.execute(comando_add, (idproduto, nome, marca, categoria, preco, qtd))
    con.commit()
    con.close()
    return redirect(url_for('produto'))

  else:
    return render_template('produto/cad_produto.html')


#Excluir produto
@app.route('/excluir_produto/<string:id>', methods=["GET"])
def excluir_produto(id):
  con = sqlite3.connect('vendas.db')
  cur = con.cursor()
  cur.execute('delete from produto where idproduto = ?', (id, ))
  con.commit()
  con.close()
  return redirect(url_for('produto'))


#Editar produto
@app.route('/editar_produto/<string:id>', methods=['GET', 'POST'])
def editar_produto(id):
  con = sqlite3.connect('vendas.db')
  cur = con.cursor()
  if request.method == 'GET':
    comando_busc = 'select * from produto where idproduto = ?'
    cur.execute(comando_busc, (id, ))
    dado = cur.fetchone()
    cur.close()
    return render_template('produto/editar_produto.html', dado=dado)

  elif request.method == 'POST':
    nome = request.form['nome']
    marca = request.form['marca']
    categoria = request.form['categoria']
    preco = request.form['preco']
    qtd = request.form['qtd']
    cur.execute(
        'update produto set nome= ?, marca= ?, categoria = ?,preco = ?, qtd =? where idproduto= ?',
        (nome, marca, categoria, preco, qtd, id))
    con.commit()
    con.close()
    return redirect(url_for('produto'))


#vendas
#criando página inicial vendas
@app.route('/venda')
def venda():
  #conectar ao banco de dados
  con = sqlite3.connect('vendas.db')
  cur = con.cursor()

  comando_select = """
    select v.idvenda, v.data_venda, v.valor_total,
    c.nome, p.nome, v.funcionario from cliente c, produto p, venda v
    where v.idcliente = c.idcliente and v.idproduto = p.idproduto;
  """
  cur.execute(comando_select)
  dadosVenda = cur.fetchall()
  return render_template('venda/index_venda.html', dadosVenda=dadosVenda)

#Nova venda
@app.route('/nova_venda', methods=['GET', 'POST'])
def nova_venda():
  if request.method == 'POST':
    con = sqlite3.connect('vendas.db')
    cur = con.cursor()

    idvenda = request.form['idvenda']
    data_venda = request.form['data_venda']
    valor_total = request.form['valor_total']
    idcliente = request.form['idcliente']
    idproduto = request.form['idproduto']
    funcionario = request.form['funcionario']

    comando_add = 'insert into venda values(?,?,?,?,?,?)'

    cur.execute(comando_add,(idvenda,data_venda,valor_total,idcliente,idproduto,funcionario))
    con.commit()
    con.close()
    return redirect(url_for('venda'))
  else:
    con = sqlite3.connect('vendas.db')
    cur = con.cursor()
    cur.execute("Select * from cliente")

    cliente = cur.fetchall()

    cur.execute('select * from produto')

    produto = cur.fetchall()
    
    return render_template('venda/nova_venda.html', dados =[cliente, produto])

#Excluir Venda
@app.route('/excluir_venda/<string:id>',methods=['GET'])
def excluir_venda(id):
  con = sqlite3.connect('vendas.db')
  cur = con.cursor()

  comando_excluir = 'delete from venda where idvenda = ?'
  cur.execute(comando_excluir,(id,))
  con.commit()
  con.close()
  return redirect(url_for('venda'))

#Editar Venda
@app.route('/editar_venda/<string:id>',methods=['GET','POST'])
def editar_venda(id):
  con = sqlite3.connect('vendas.db')
  cur = con.cursor()
  if request.method == "GET":
    comando_Busca = 'select * from venda where idvenda = ?'
    cur.execute(comando_Busca,(id,))
    dado = cur.fetchone()
    return render_template('venda/editar_venda.html',dado=dado)
  elif request.method == "POST":
    con = sqlite3.connect('vendas.db')
    cur = con.cursor()

    data_venda = request.form['data_venda']
    valor_total = request.form['valor_total']
    idcliente = request.form['idcliente']
    idproduto = request.form['idproduto']
    funcionario = request.form['funcionario']

    cur.execute(
        'update venda set data_venda= ?, valor_total= ?, idcliente = ?,idproduto = ?, funcionario =? where idvenda= ?',
        (data_venda, valor_total, idcliente, idproduto, funcionario, id))

    con.commit()
    con.close()
    return redirect(url_for('venda'))


#Metodo para realizar os testes
@app.route('/teste')
def teste():
  return "TESTE SUCESSO"


if __name__ == '__main__':

  app.secret_key = 'admin123'
  app.run(debug=True)
