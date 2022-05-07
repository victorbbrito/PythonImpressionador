produtos = ['tv', 'celular', 'teclado', 'mouse','tablet','geladeira','forno']
estoque = [100,150,100,120,70,90,80]

i = produtos.index('teclado')
quantidade = estoque[i]

print('A quantidade em estoque do teclado é {}'.format(quantidade))

produto = input('Insira o nome do produto em letra minúscula: ')




if produto in produtos:
    i = produtos.index(produto)
    quantidade = estoque[i]
    print('Temos {} unidades de {} em estoque.'.format(quantidade, produto))
else:
    print('Produto não encontrado no estoque')