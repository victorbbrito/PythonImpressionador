# for + if

vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70,
          90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]

funcionario_bateu_meta = 0
for venda in vendas:
    if venda >= 1000:
        print(venda)
        funcionario_bateu_meta += 1

# quantos bateram a meta divido pelo total de funcionários que é o tamanho da lista de vendas
percentual = funcionario_bateu_meta / len(vendas)

print('{} funcionários bateram a meta, isso representa {:.1%} dos funcionários'.format(
    funcionario_bateu_meta, percentual))
