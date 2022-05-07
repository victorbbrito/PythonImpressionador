meta = 10000

vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcos', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alan', 7870]
]

bateu_meta = 0
for item in vendas:
    if item[1] >= meta:
       bateu_meta += 1

porcentagem = bateu_meta/len(vendas)

print('{:.1%} dos vendedores bateram a meta.'.format(porcentagem))
