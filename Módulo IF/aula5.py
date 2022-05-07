meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario =15000
vendas_loja = 280000
nota_funcionario = 9
meta_nota = 9

if nota_funcionario >= meta_nota or (vendas_loja >= meta_loja and vendas_funcionario >= meta_funcionario):
    bonus = 0.03 * vendas_funcionario
    print('O bônus do funcionário foi de {}'.format(bonus))
else:
    print('O funcionário não ganhou bônus')