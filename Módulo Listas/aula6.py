# juntar listas, ordenar e cuidados especiais
# lista.extend(lista1)
# listas = lista1 + lista2

produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11',
            'ipad', 'apple watch', 'airpods', 'mac book']
novos_produtos = ['iphone 12', 'iphone 13']

produtos.extend(novos_produtos)
print(produtos)

produtos = ['apple tv', 'mac', 'iphone x',
            'ipad', 'apple watch', 'airpods', 'mac book']
todos_produtos = produtos + novos_produtos
print(todos_produtos)

vendas = [1000, 1500, 15000, 20000, 270, 900, 100, 1200]
vendas_x = [15000]
vendas_11 = [20000]

total_iphones = vendas[2] + vendas[3]
print(total_iphones)

total_iphone_lista = vendas_x + vendas_11
print(total_iphone_lista)

# ordenar a lista
produtos.sort()
print(produtos)

vendas.sort()
print(vendas)

# ordenação invertida
vendas.sort(reverse=True)
print(vendas)
