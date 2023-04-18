import pyodbc

dados_conexao = (
    r"Driver={SQLite3 ODBC Driver};Server=localhost;Database=Módulo SQL\db\chinook.db"
)

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("")
cursor.commit()

cursor.close()
conexao.close()
