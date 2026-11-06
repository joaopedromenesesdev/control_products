from conexao import Conexao
from modelos import Categoria, Produto

class CategoriaDAO:
    # --- CADASTRO (INSERT) ---
    def inserir(self, categoria):
        conn = Conexao.conectar()
        if conn:
            try:
                cursor = conn.cursor()
                # O %s previne SQL Injection (proteção contra ataques)
                sql = "INSERT INTO categorias (nome) VALUES (%s)"
                valores = (categoria.nome,)
                cursor.execute(sql, valores)
                conn.commit() # Confirma a gravação no banco
                return True
            except Exception as e:
                print(f"Erro ao inserir categoria: {e}")
                return False
            finally:
                cursor.close()
                conn.close()
        return False

    # --- CONSULTA (SELECT) ---
    def listar(self):
        conn = Conexao.conectar()
        categorias = []
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT id, nome FROM categorias")
                resultados = cursor.fetchall()
                # Transforma cada linha do banco em um objeto da classe Categoria (POO)
                for linha in resultados:
                    cat = Categoria(id_categoria=linha[0], nome=linha[1])
                    categorias.append(cat)
            except Exception as e:
                print(f"Erro ao listar categorias: {e}")
            finally:
                cursor.close()
                conn.close()
        return categorias


class ProdutoDAO:
    # --- CADASTRO (INSERT) ---
    def inserir(self, produto):
        conn = Conexao.conectar()
        if conn:
            try:
                cursor = conn.cursor()
                sql = "INSERT INTO produtos (nome, preco, id_categoria) VALUES (%s, %s, %s)"
                valores = (produto.nome, produto.preco, produto.categoria_id)
                cursor.execute(sql, valores)
                conn.commit()
                return True
            except Exception as e:
                print(f"Erro ao inserir produto: {e}")
                return False
            finally:
                cursor.close()
                conn.close()
        return False

    # --- CONSULTA (SELECT) ---
    def listar(self):
        conn = Conexao.conectar()
        produtos = []
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT id, nome, preco, id_categoria FROM produtos")
                resultados = cursor.fetchall()
                for linha in resultados:
                    prod = Produto(id_produto=linha[0], nome=linha[1], preco=linha[2], categoria_id=linha[3])
                    produtos.append(prod)
            except Exception as e:
                print(f"Erro ao listar produtos: {e}")
            finally:
                cursor.close()
                conn.close()
        return produtos