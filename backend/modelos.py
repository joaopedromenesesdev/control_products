class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Produto:
    def __init__(self, id, nome, preco, id_categoria):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.id_categoria = id_categoria