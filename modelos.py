class Categoria:
    def __init__(self, id_categoria, nome):
        self.id_categoria = id_categoria
        self.nome = nome

class Produto:
    def __init__(self, id_produto, nome, preco, categoria_id):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.categoria_id = categoria_id