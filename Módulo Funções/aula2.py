def cadastrar_produto():
    produto = input('Digite o nome do produto que deseja cadastrar:')
    produto = produto.casefold()
    produto = produto.strip()
    print("Produto {} cadastrado com sucesso.".format(produto))
    return produto


lista = []

for i in range(0, 3):
    lista.append(cadastrar_produto())

print(lista)
