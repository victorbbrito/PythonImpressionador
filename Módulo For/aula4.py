# enumerate -> permite que você percorra uma lista e ao mesmo tempo tenha em uma variável o indice daquele item

funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco',
                'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Thiago',
                'Marcos', 'Francisca', 'Luiza', 'Tatiana', 'Felipe', 'Henrique']

for i, funcionario in enumerate(funcionarios):
    print('{} é o funcionário {}'.format(i, funcionario))

############################################################################################################################
estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90,
           80, 1100, 999, 900, 800, 870, 50, 1111, 120, 300, 450, 800]
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'dolly',
            'del valle', 'red bull', 'cachaça', 'vinho', 'fanta', 'baré', 'tuchaua']
estoque_minimo = 50

for i, quantidade in enumerate(estoque):
    if quantidade < estoque_minimo:
        print('{} está abaixo do estoque minimo. Temos apenas {} unidades'.format(produtos[i],quantidade))


