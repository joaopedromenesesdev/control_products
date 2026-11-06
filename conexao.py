import mysql.connector
from mysql.connector import Error

class Conexao:
    @staticmethod
    def conectar():
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",          # Altere para a senha do seu MySQL local, se houver
                password="",
                database="db_estoque" # Nome do banco que criamos no script.sql
            )
            return conn
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

# Bloco de teste para verificar se a conexão está funcionando
if __name__ == "__main__":
    conexao = Conexao.conectar()
    if conexao and conexao.is_connected():
        print("✅ Conexão ao MySQL bem-sucedida!")
        conexao.close()
    else:
        print("❌ Falha na conexão.")