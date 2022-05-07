# comparação com o ano anterior

produtos = ['iphone', 'galaxy s10', 'ipad', 'tv', 'máquina de café', 'kindle',
            'geladeira', 'adega', 'notebook dell', 'notebook acer', 'ps4', 'ps5']
vendas2019 = [558147, 712350, 573823, 405252, 718654,
              751580, 973139, 892292, 422760, 154753, 887061, 438508]
vendas2020 = [951642, 244295, 26964, 787604, 867660,
              78830, 710331, 646016, 694913, 539704, 324831, 667179]

for i, produto in enumerate(produtos):
    if vendas2020[i] > vendas2019[i]:
        porcentagem_crescimento = vendas2020[i] / vendas2019[i] - 1 
        print('{} vendeu R${:,} em 2019, R${:,} em 2020 e teve um crescimento de {:.1%}'.format(
            produto, vendas2019[i], vendas2020[i], porcentagem_crescimento))
