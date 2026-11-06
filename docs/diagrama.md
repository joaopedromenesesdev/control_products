classDiagram
  class Categoria {
    -int id
    -String nome
    +getId()
    +getNome()
  }
  class Produto {
    -int id
    -String nome
    -float preco
    -int id_categoria
    +getId()
    +getNome()
    +getPreco()
  }
  class CategoriaDAO {
    +inserir(Categoria)
    +listar()
  }
  class ProdutoDAO {
    +inserir(Produto)
    +listar()
  }
  Produto "*" --> "1" Categoria : pertence a