faturamento = input('Qual foi o faturamento da loja nesse mês ?')
custo = input('Qual foi o custo da loja esse mês?')

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print('O lucro da loja foi de {} reais'.format(lucro))
else:
    print('Preencha o faturamento e o lucro cprretamente')