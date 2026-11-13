from flask import Flask, request, jsonify
from flask_cors import CORS
from modelos import Categoria, Produto
from dao import CategoriaDAO, ProdutoDAO

app = Flask(__name__)
CORS(app) # Libera o acesso para o front-end consumir as rotas

# Rota para cadastrar uma categoria (INSERT)
@app.route('/categorias', methods=['POST'])
def cadastrar_categoria():
    dados = request.get_json() # Pega os dados enviados pelo HTML
    nova_categoria = Categoria(id=None, nome=dados['nome'])
    
    dao = CategoriaDAO()
    if dao.inserir(nova_categoria):
        return jsonify({"mensagem": "Categoria cadastrada com sucesso!"}), 201
    return jsonify({"erro": "Falha ao cadastrar"}), 500

# Rota para listar as categorias (SELECT)
@app.route('/categorias', methods=['GET'])
def listar_categorias():
    dao = CategoriaDAO()
    categorias = dao.listar()
    
    # Transforma os objetos Python num formato JSON que o navegador entende
    lista_json = [{"id": c.id, "nome": c.nome} for c in categorias]
    return jsonify(lista_json)

# Rota para cadastrar um produto (INSERT)
@app.route('/produtos', methods=['POST'])
def cadastrar_produto():
    dados = request.get_json() # Pega os dados enviados pelo HTML
    novo_produto = Produto(
        id=None,
        nome=dados['nome'],
        preco=dados['preco'],
        id_categoria=dados['id_categoria']
    )
    
    dao = ProdutoDAO()
    if dao.inserir(novo_produto):
        return jsonify({"mensagem": "Produto cadastrado com sucesso!"}), 201
    return jsonify({"erro": "Falha ao cadastrar"}), 500

# Rota para listar os produtos (SELECT)
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    dao = ProdutoDAO()
    produtos = dao.listar()
    
    # Transforma os objetos Python num formato JSON que o navegador entende
    lista_json = [
        {"id": p.id, "nome": p.nome, "preco": float(p.preco), "id_categoria": p.id_categoria}
        for p in produtos
    ]
    return jsonify(lista_json)

# Inicia o servidor
if __name__ == '__main__':
    app.run(debug=True)