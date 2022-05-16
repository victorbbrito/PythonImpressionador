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

# quais os clientes que mais compraram ?
frequencia_cliente = vendas_df['E-mail do Cliente'].value_counts()

print('\n---- Emails dos Clientes ---- Compras')
print(frequencia_cliente[:5])

# quais as lojas que mais venderam ?

vendas_lojas = vendas_df.groupby('Nome da Loja').sum()
vendas_lojas = vendas_lojas[['Quantidade Vendida']]
vendas_lojas = vendas_lojas.sort_values('Quantidade Vendida', ascending=False)
print(vendas_lojas[:5])

maior_valor = vendas_lojas['Quantidade Vendida'].max()
melhor_loja = vendas_lojas['Quantidade Vendida'].idxmax()

print(melhor_loja, maior_valor)

# qual loja menos vendeu ?

print(vendas_lojas[-1:])
