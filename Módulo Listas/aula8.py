# alterações incrementais em variáveis

lista =['mac','iphone']
vendas = [100,200]
# adicionar ipad na lista
lista = lista + ['ipad']
print(lista)

soma_vendas = 300
# adicionar na soma a quantidade de ipads
soma_vendas = soma_vendas + 500
print(soma_vendas)

email = 'Esse mês vendemos um total de {} produtos, sendo:\n{} unidades de {}.\n{} unidades de {}.'.format(soma_vendas,vendas[0],lista[0], vendas[1],lista[1])
# adicionando no fim do texto o ipad

email += '\n{} unidades de ipad.'.format(500)
print(email)