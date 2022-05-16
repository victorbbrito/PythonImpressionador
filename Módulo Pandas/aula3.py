from cmath import e
import pandas as pd

vendas_df = pd.read_csv(r'Módulo Pandas\Contoso - Vendas - 2017.csv', sep=';')

lista_de_clientes = vendas_df['ID Cliente']
produtos_quantidade = vendas_df[['ID Produto','Quantidade Vendida','Quantidade Devolvida']]
print(produtos_quantidade)
