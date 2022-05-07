vendas = ('Lira', '25/08/2020','15/02/2000',2000, 'Estagiário')

print(vendas)

nome, data_contratacao, data_nascimento, salario, cargo = vendas

print(nome)
print(salario)

vendas = [1000,2000,300,300,150]
funcionarios = ['João', 'Lira', 'Ana', 'Maria', 'Paula']

for i, venda in enumerate(vendas):
    print('{} vendeu {} unidades'.format(funcionarios[i], venda))
