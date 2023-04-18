import pyodbc
import pandas as pd

dados_conexao = (r"Driver={SQLite3 ODBC Driver};Server=localhost;Database=Módulo SQL\db\chinook.db")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("SELECT * FROM customers")
descricao = cursor.description

# List compreretions (extrair cada informação de cada item da tupla na lista descricao)
colunas = [tupla[0] for tupla in descricao]
print(colunas)

valores = cursor.fetchall()

tabela_clientes = pd.DataFrame.from_records(valores, columns=["ID","Nome","Sobrenome","Empresa","Endereço","Cidade","Estado","Pais","CEP","Tel","Fax","Email","SupportRepId"])
tabela_clientes.info()

#cursor.commit()

cursor.close()
conexao.close()