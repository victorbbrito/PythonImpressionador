# Functions em python
# As functions são blocos de código que servem 1 único propósito, fazem uma ação especifica.

# estrutura básica
# def nome_funcao():
#  faça algo
#  faça algo
#  return algo

lista = [150, 2300, 50, 120, 100]

lista.sort()  # uma function que ordena a lista

print(lista)


def cadastrar_produto():
    produto = input('Digite o nome do produto que deseja cadastrar:')
    produto = produto.casefold()
    print("Produto {} cadastrado com sucesso.".format(produto))


for i in range(5):
    cadastrar_produto()
