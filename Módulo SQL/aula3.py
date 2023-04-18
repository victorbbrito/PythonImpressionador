import pandas as pd
import sqlite3

conexao = sqlite3.connect(r"Módulo SQL\db\chinook.db")

tabela_clientes = pd.read_sql("SELECT * FROM customers", conexao)
tabela_clientes.info()

conexao.close()
