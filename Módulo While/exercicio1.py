vendas = []



while True:
    produto = input('Qual o produto: ')
    if not produto:
        break
    quantidade = int(input('Qual a quantidade: '))
    
    vendas.append([produto, quantidade])

print(vendas)