from flask import Flask, request, jsonify
from flask_cors import CORS
from modelos import Categoria
from dao import CategoriaDAO

app = Flask(__name__)
CORS(app) # Libera o acesso para o front-end consumir as rotas

# Rota para cadastrar uma categoria (INSERT)
@app.route('/categorias', methods=['POST'])
def cadastrar_categoria():
    dados = request.get_json() # Pega os dados enviados pelo HTML
    nova_categoria = Categoria(id_categoria=None, nome=dados['nome'])
    
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
    lista_json = [{"id": c.id_categoria, "nome": c.nome} for c in categorias]
    return jsonify(lista_json)

# Inicia o servidor
if __name__ == '__main__':
    app.run(debug=True)