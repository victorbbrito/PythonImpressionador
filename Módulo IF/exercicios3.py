nome = input('Informe o nome do produto:')
categoria = input('Informe a categoria do produto:')
estoque = input('Informe a quantidade do produto no estoque:')

minimo_alimentos = 50
minimo_bebidas = 75
minimo_limpeza = 30

if nome:
    if categoria:
        if estoque:
            if categoria == 'bebidas':
                estoque = int(estoque)
                if estoque > minimo_bebidas:
                    pass
                else:
                    print('Solicitar {} a equipe de compras, temos apenas {} unidades no estoque'.format(
                        nome, estoque))
            elif categoria == 'limpeza':
                if estoque > minimo_limpeza:
                    pass
                else:
                    print('Solicitar {} a equipe de compras, temos apenas {} unidades no estoque'.format(
                        nome, estoque))
            else:
                if estoque > minimo_alimentos:
                    pass
                else:
                    print('Solicitar {} a equipe de compras, temos apenas {} unidades no estoque'.format(
                        nome, estoque))
        else:
            print('Preencha o estoque corretamente')
    else:
        print('Preencha a categoria corretamente')
else:
    print('Preencha o nome corretamente')
