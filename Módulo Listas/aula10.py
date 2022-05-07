# listas de listas

vendedores = ['Lira', 'João', 'Diego', 'Alan']
produtos = ['ipad', 'iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10]
]
vendas_ipad_joao = vendas[1][0]
print(vendas_ipad_joao)

vendas_iphone_diego = vendas[2][1]
print(vendas_iphone_diego)

total_vendas_iphone = vendas[0][1]+vendas[1][1]+vendas[2][1]+vendas[3][1]
print(total_vendas_iphone)

print(vendas)
vendas[0][1] = 150
print(vendas)

vendas[0].append(10)
vendas[1].append(15)
vendas[2].append(60)
vendas[3].append(70)

print(vendas)
