
vendas = [('iphone 8',5000,9000),('galaxy s21',5400,10000),('galaxy s22',12000,16400),('iPad',4100, 5400),('MacBook', 19000, 5400)]

lista_vendas2019 = []
for produto, venda2019, venda2020 in vendas:
    lista_vendas2019.append(venda2019)

lista_venda = [(vendas2019, produto) for produto, vendas2019, vendas2020 in vendas]

print(lista_vendas2019)
print(lista_venda)