meta = 20000
vendas = 15000

if vendas < meta:
    print('Não ganhou bônus')
elif vendas >= 2*meta:
    bonus = 0.07 * vendas
    print(f'Ganhou {bonus} de bônus')
else:
    bonus = 0.03 * vendas
    print(f'Ganhou {bonus} de bônus')