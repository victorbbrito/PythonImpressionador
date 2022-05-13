
produtos = ['apple tv', 'mac', 'iphone x',
            'iphone 11', 'iphone 12', 'ipad', 'apple watch']
vendas = [100, 522, 1030, 1500, 1500, 400, 600]

lista_vendas = list(zip(produtos, vendas))
def segundo_item(tupla):
    return tupla[1]
lista_vendas.sort(key=segundo_item)
print(lista_vendas)
