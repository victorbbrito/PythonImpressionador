import pyodbc

# Dados utilizados na conexão
dados_conexao = (r"Driver={SQLite3 ODBC Driver};Server=localhost;Database=C:\Users\victor\Desktop\GitHub\PythonImpressionador\Módulo SQL\db\salarios.sqlite")

# Iniciar conexão com o banco de dados
def start_connection(dados_conexao):
    conexao = pyodbc.connect(dados_conexao)
    return conexao.cursor()

cursor = start_connection(dados_conexao)

def execute_comands(command:str,cursor):
    cursor.execute(command)
    return cursor.fetchall()

# Finalizar a conexão
def close_connection(cursor):
    cursor.close()

valores = execute_comands("SELECT * FROM Salaries",cursor)
print(valores[:3])

close_connection(cursor)

