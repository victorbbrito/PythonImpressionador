vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000)
]
faturamento = 0
for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item

    if produto == 'iphone x' and data == '20/08/2020':
        faturamento += unidades * valor_unitario

print(
    'O faturamento da venda de iphones em 20/08/2020 foi {:,}'.format(faturamento))

produto_mais_vendido = ''
quantidade_mais_vendido = 0
cor_produto_mais_vendido = ''
capacidade_produto_mais_vendido = ''

for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item

    if data == '21/08/2020':
        if unidades > quantidade_mais_vendido:
            produto_mais_vendido = produto
            quantidade_mais_vendido = unidades
            cor_produto_mais_vendido = cor
            capacidade_produto_mais_vendido = capacidade

print('O produto mais vendido em 21/08/2020 foi {} com {} unidades. Cor: {}, Capacidade: {}'.format(
    produto_mais_vendido, quantidade_mais_vendido, cor_produto_mais_vendido, capacidade_produto_mais_vendido))
