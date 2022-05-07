from numpy import indices


produtos = ['iphone', 'galaxy s10', 'ipad', 'tv', 'máquina de café', 'kindle',
            'geladeira', 'adega', 'notebook dell', 'notebook acer', 'ps4', 'ps5']
vendas = [558147, 712350, 573823, 405252, 718654, 751580,
          973139, 892292, 422760, 154753, 887061, 438508]

dicionario = dict.fromkeys(produtos, 0)
print(dicionario)

lista_tuplas = zip(produtos, vendas)
dicionario = dict(lista_tuplas)
print(dicionario)

# quantos iPads vendemos ?

#por listas ->

indice = produtos.index('ipad')

print("Vendemos {} iPads.".format(vendas[indice]))

#com dicionários ->

print("Vendemos {} iPads.".format(dicionario['ipad']))
