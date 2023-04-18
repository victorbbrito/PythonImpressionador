import pandas as pd

# Lê as informações da tabela e aramazena na variável tabela
tabela = pd.read_csv(r"C:\Users\victor\Desktop\GitHub\PythonImpressionador\Módulo Pandas\Mentoria\exportacoes_franca.csv")

def info(tabela):
    # Exibe as informações gerais da tabela
    print(tabela.info())

def describe(tabela):
    # Exibe estatisticas a partir dos dados
    print(tabela.describe())

def formatar(valor):
    # Formatar os dados da coluna
    return f"${valor:,.2f}"

def evolucao_dos_anos(tabela):
    # Agrupar os dados e somar na coluna ano "YEAR" para resultar em valores formatados em USD $ e exibilos
    exportacao_ano = tabela.loc[tabela["Economic Block"]=="Europe",:]
    exportacao_ano = exportacao_ano.groupby("Year").sum()
    exportacao_ano = exportacao_ano[["US$ FOB"]]
    exportacao_ano["US$ FOB"] = exportacao_ano["US$ FOB"].map(formatar)
    print(exportacao_ano)

def evolucao_por_mes(tabela):
    # Agrupar os dados e somar na coluna ano "YEAR" e mes "MONTH" para resultar em valores formatados em USD $ e exibilos
    exportacao_mes = tabela.loc[tabela["Economic Block"]=="Europe",:]
    exportacao_mes = exportacao_mes.groupby(["Year","Month"]).sum()
    exportacao_mes = exportacao_mes[["US$ FOB"]]
    exportacao_mes["US$ FOB"] = exportacao_mes["US$ FOB"].map(formatar)
    print(exportacao_mes)

def produtos_mais_exportados(tabela):
    # Agrupar os dados da tabela conforme a descrição dos produtos e somar os valores de exportação
    exportacao_produto = tabela.loc[tabela["Economic Block"] == "Europe",:]
    exportacao_produto = exportacao_produto.groupby("SH4 Description").sum()
    exportacao_produto = exportacao_produto[["US$ FOB"]]
    exportacao_produto = exportacao_produto.sort_values("US$ FOB", ascending=False)
    exportacao_produto["US$ FOB"] = exportacao_produto["US$ FOB"].map(formatar)
    print(exportacao_produto)

def cidade_mais_exportou_no_ano(tabela, ano:int):
    exportacao_produto = tabela.loc[tabela["Economic Block"]=="Europe",:]
    exportacao_produto = exportacao_produto.loc[exportacao_produto["Year"] == ano,:]
    exportacao_produto = exportacao_produto.groupby(["City"]).sum()[["US$ FOB"]]
    exportacao_produto = exportacao_produto.sort_values("US$ FOB", ascending=False)
    exportacao_produto["US$ FOB"] = exportacao_produto["US$ FOB"].map(formatar)
    print(exportacao_produto)
    return exportacao_produto.index[0]

def localizar_cidade_ano(tabela, cidade, ano):
    tabela_cidade = tabela.loc[tabela["Economic Block"]=="Europe",:]
    tabela_cidade = tabela_cidade.loc[tabela_cidade["City"] == cidade, :]
    tabela_cidade = tabela_cidade.loc[tabela_cidade["Year"] == ano, :]
    tabela_cidade = tabela_cidade.groupby("SH4 Description").sum()[["US$ FOB"]]
    tabela_cidade = tabela_cidade.sort_values("US$ FOB", ascending=False)
    tabela_cidade["US$ FOB"] = tabela_cidade["US$ FOB"].map(formatar)
    print(tabela_cidade)

describe(tabela)
cidade_mais_exportou_no_ano(tabela,2020)
localizar_cidade_ano(tabela,cidade_mais_exportou_no_ano(tabela,2020) , 2020)
#produtos_mais_exportados(tabela)
#evolucao_dos_anos(tabela)
#evolucao_por_mes(tabela)




