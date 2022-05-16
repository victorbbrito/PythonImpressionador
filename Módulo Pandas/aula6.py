from numpy import quantile
import pandas as pd
# importar todos os dados dos arquivos a partir dos arquivos .csv

vendas_df = pd.read_csv(
    r'Módulo Pandas\Contoso - Vendas - 2017.csv', sep=';', encoding='utf-8')
produtos_df = pd.read_csv(
    r'Módulo Pandas\Contoso - Cadastro Produtos.csv', sep=';', encoding='utf-8')
lojas_df = pd.read_csv(
    r'Módulo Pandas\Contoso - Lojas.csv', sep=';', encoding='utf-8')
clientes_df = pd.read_csv(
    r'Módulo Pandas\Contoso - Clientes.csv', sep=';', encoding='utf-8')

clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')

# renomear uma coluna
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})

# calcular a taxa de devolução nas vendas de todas as lojas
quantidade_vendida = vendas_df['Quantidade Vendida'].sum()
quantidade_devolvida = vendas_df['Quantidade Devolvida'].sum()

print('Taxa de Devolução: {:.2%}'.format(
    quantidade_devolvida/quantidade_vendida))

# calcular a taxa de devolução de uma loja especifica

vendas_loja_online = vendas_df[vendas_df['ID Loja'] == 306]

quantidade_vendida = vendas_loja_online['Quantidade Vendida'].sum()
quantidade_devolvida = vendas_loja_online['Quantidade Devolvida'].sum()
print('Taxa de Devolução da Loja com ID 306: {:.2%}'.format(
    quantidade_devolvida/quantidade_vendida))

loja306 = vendas_df['ID Loja'] == 306
semdevolucao = vendas_df['Quantidade Devolvida'] == 0

vendas_sem_devolução_loja306 = vendas_df[loja306 & semdevolucao]
print(vendas_sem_devolução_loja306)
