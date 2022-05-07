# analise de vendas
# neste exercicio iremos fazer uma analise simples de atingimento de meta
# temos uma lista com os vendedores e os valores de vendas que queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam

from numpy import quantile


meta = 10000

vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcos', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alan', 7870]
]

for item in vendas:
    if item[1] >= meta:
        vendedor = item[0]
        quantidade = item[1]
        print('Vendedor {} bateu a meta. Fez {} vendas'.format(vendedor, quantidade))
