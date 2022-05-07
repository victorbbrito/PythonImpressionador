# adicionar e remover itens de uma lista

# adicionar -> lista.append(item)
# remover -> lista.remove(item) qual o item a ser removido
# item removido -> item_removido = lista.pop(indice) qual o indice do item a ser removido

produtos = ['apple tv','mac','iphone x','ipad','apple watch','airpods']

print(produtos)

#adicionar o iphone 11
produtos.append('iphone 11')
print(produtos)

#remover o iphone x

produtos.remove('iphone x')
print(produtos)

# ou 

produtos.pop(2) # remove o indice 2 da lista produtos
print(produtos)

produtos = ['apple tv','mac','iphone x','ipad','apple watch','airpods']
produtos.append('iphone 11')
print(produtos)

produto_a_remover = 'iphone x'

if produto_a_remover in produtos:
    produtos.remove(produto_a_remover)
else:
    print('{} não existe na lista de produtos'.format(produto_a_remover))

# ou 

produtos = ['apple tv','mac','iphone x','ipad','apple watch','airpods']

try:
    produtos.remove('iphone x')
    print(produtos)
except:
    print('iphone x não existe na lista de produtos')