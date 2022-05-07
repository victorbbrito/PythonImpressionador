
vendas_coca = 150
vendas_pepsi = 130

preco_coca = 1.50
preco_pepsi = 1.50

custo_loja = 2500

faturamento_coca = vendas_coca * preco_coca
faturamento_pepsi = vendas_pepsi * preco_pepsi

print(f'Faturamento coca-cola: {faturamento_coca}')
print(f'Faturamento pepsi: {faturamento_pepsi}')

lucro = (faturamento_coca + faturamento_pepsi) - custo_loja

print(f'Lucro da loja: {lucro}')

margem = lucro/(faturamento_coca + faturamento_pepsi)
print(f'Margem da loja: {margem}')

