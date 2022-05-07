# break -> interrompe e finaliza o for
# continue -> interrompe e vai para o proximo laço do for

vendas = [100, 150, 1500, 2000, 120]

meta = 110
for venda in vendas:
    if venda < meta:
        print('A loja não ganha bônus')
        break
    else:
        print(
            'A loja ganha bônus'
        )

meta = 130
vendedores = ['João', 'Júlia', 'Ana', 'José', 'Maria']

for i, venda in enumerate(vendas):
    if venda < meta:
        continue
    print('{} fez {} vendas.'.format(vendedores[i], venda))
