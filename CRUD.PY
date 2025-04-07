# Importar a biblioteca
import mysql.connector

#Conexão com o MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Luanmilagre.123",
    database="teste"
)
cursor = conexao.cursor()

#Criar Crud
nome_produto = "chocolate"
valor = 7

# Comando SQL para inserir dados
comando = "INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)"

dados = (nome_produto, valor)

# Executa o comando
cursor.execute(comando, dados) 
conexao.commit() # Edita o banco de dados

#Fechar a conexão
cursor.close()
conexao.close()