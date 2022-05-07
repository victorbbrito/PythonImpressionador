
produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11',
            'ipad', 'apple watch', 'airpods', 'mac book']

print(produtos)

print(','.join(produtos))
print('\n'.join(produtos))
print(';'.join(produtos))

produtos = 'apple tv, mac, iphone x, iphone 11, ipad, apple watch, airpods, mac book'
lista = produtos.split(', ')

print(lista)
