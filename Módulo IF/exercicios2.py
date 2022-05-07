vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

if vendas_funcionario1 >= 2000:
    print('O funcionário 1 ganhou {} de bônus'.format(vendas_funcionario1 * 0.15))
elif vendas_funcionario1  >= 1000:
    print('O funcionário 1 ganhou {} de bônus'.format(vendas_funcionario1 * 0.10))
else:
    print('O funcionário 1 ganhou 0 de bônus')

if vendas_funcionario2  >= 2000:
    print('O funcionário 2 ganhou {} de bônus'.format(vendas_funcionario2 * 0.15))
elif vendas_funcionario2  >= 1000:
    print('O funcionário 2 ganhou {} de bônus'.format(vendas_funcionario2 * 0.10))
else:
    print('O funcionário 2 ganhou 0 de bônus')

if vendas_funcionario3 >= 2000:
    print('O funcionário 3 ganhou {} de bônus'.format(vendas_funcionario3 * 0.15))
elif vendas_funcionario3  >= 1000:
    print('O funcionário 3 ganhou {} de bônus'.format(vendas_funcionario3 * 0.10))
else:
    print('O funcionário 3 ganhou 0 de bônus')