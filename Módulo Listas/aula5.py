
# tamanho da lista
produtos = ['apple tv','mac','iphone x','ipad','apple watch','airpods', 'mac book']

tamanho = len(produtos)
print('Temos {} produtos'.format(tamanho))

vendas = [1000,1500,15000,270,900,100,1200]

mais_vendido = max(vendas)
menos_vendido = min(vendas)

indice_mais_vendido = vendas.index(mais_vendido)
indice_menos_vendido =  vendas.index(menos_vendido)

print('O produto mais vendido foi {} e vendeu {} unidades.'.format(produtos[indice_mais_vendido], mais_vendido))
print('O produto menos vendido foi {} e vendeu {} unidades.'.format(produtos[indice_menos_vendido], menos_vendido))