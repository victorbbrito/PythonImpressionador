meta = 100
vendas = [420, 120, 140, 50, 5630, 41, 100]
produtos = ['café', 'coca', 'regente', 'agua', 'suco', 'fanta', 'baré']

produtos_acima_meta = []

for i, produto in enumerate(produtos):
    if vendas[i] >= meta:
        produtos_acima_meta.append(produto)

print(produtos_acima_meta)

produtos_abaixo_meta = [produto for i,
                        produto in enumerate(produtos) if vendas[i] < meta]
print(produtos_abaixo_meta)
