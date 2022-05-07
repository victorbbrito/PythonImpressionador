for i in range(5):
    # repetir o código n vezes
    print(i)

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]

for i in range(len(produtos)):
    print('{} unidades produzidas de {}'.format(producao[i], produtos[i]))
