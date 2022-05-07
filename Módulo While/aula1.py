venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia.')
vendas = []

# o programa aqui

while(venda != ''):
    vendas.append(venda)
    venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia.')
    

print('Registro finalizado. As vendas cadastradas foram: {}'.format(vendas))