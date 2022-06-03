import pandas as pd
from tqdm import tqdm
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

pbar = tqdm(total = len(vendas_df['ID Loja']), position = 0,leave = True)

for i,id_loja in enumerate(vendas_df):
    pbar.update()
    if id_loja == 222:
        vendas_df.loc[i,'Quantidade Devolvida'] +=1

    
