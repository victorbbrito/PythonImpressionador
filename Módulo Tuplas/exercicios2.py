vendas_produtos = [('iphone', 558147, 951642),('galaxy',712350, 244295),('ipad', 573823, 26964),('tv', 405252, 641233)]

for produto, venda2019, venda2020 in vendas_produtos:
    if venda2020 > venda2019:
        crescimento = venda2020/venda2019 - 1
        print('{} teve {} vendas em 2019, {} vendas em 2020. Crescimento de {:.1%}'.format(produto,venda2019,venda2020,crescimento))

