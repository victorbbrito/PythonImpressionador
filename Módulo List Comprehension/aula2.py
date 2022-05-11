vendasProdutos = [1500, 150, 2100, 1900]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']

listaAux = list(zip(vendasProdutos, produtos))
listaAux.sort(reverse=True)
print(listaAux)

produtos = [produto for vendas, produto in listaAux]
print(vendasProdutos)
print(produtos)
