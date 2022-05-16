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

# modificar o tipo dos dados da coluna

vendas_df['Data da Venda'] = pd.to_datetime(
    vendas_df['Data da Venda'], format='%d/%m/%Y')
'''
vendas_df['Ano da Venda'] = vendas_df['Ano da Venda'].dt.year
vendas_df['Mes da Venda'] = vendas_df['Mes da Venda'].dt.month
vendas_df['Dia da Venda'] = vendas_df['Dia da Venda'].dt.day
'''
vendas_df.info()

# pegar o preço do produto Contoso Optical Wheel OEM PS/2 Mouse E60 Black
# por loc

novoproduto_df = pd.read_csv(
    r'Módulo Pandas\Contoso - Cadastro Produtos.csv', sep=';', encoding='utf-8')
novoproduto_df = novoproduto_df.set_index('Nome do Produto')
print(novoproduto_df.loc['Contoso Optical Wheel OEM PS/2 Mouse E60 Black'])

# por iloc novoproduto_df.iloc[linha,coluna]
print(novoproduto_df.iloc[2, 5])

# atualizar o valor de um indice na nossa base de dados

print(
    novoproduto_df.loc['Contoso Wireless Laser Mouse E50 Grey', 'Preco Unitario'])
novoproduto_df.loc['Contoso Wireless Laser Mouse E50 Grey',
                   'Preco Unitario'] = 25
print(
    novoproduto_df.loc['Contoso Wireless Laser Mouse E50 Grey', 'Preco Unitario'])

