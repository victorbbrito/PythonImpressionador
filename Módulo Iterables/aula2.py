# Range

produto = ['arroz', 'feijao', 'macarrao', 'atum', 'azeite']
estoque = [50, 100, 20, 5, 80]

# usado comumente no for
for i in range(5):
    print('{} : {}'.format(produto[i], estoque[i]))

# range com inicio e fim
print(range(1, 10))  # termina em 9

for i in range(1, 10):
    print(i)

# Modelo Jack Welch da G&E

# 1. Classe A: 10% melhor
# 2. Classe B: 80% mantém/busca melhorar
# 3. Classe C: 10% pior

funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco',
                'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Thiago',
                'Marcos', 'Francisca', 'Luiza', 'Tatiana', 'Felipe', 'Henrique', 'Belota', 'Wanner']

vendas = [2750, 1900, 1500, 1200, 1111, 1100, 999, 900,
          880, 870, 800, 800, 450, 400, 300, 300, 120, 90, 80, 70]

for i in range(3, 18):
    print('{}: fez {} vendas'.format(funcionarios[i], vendas[i]))

# Range com Passos

for i in range(0, 1000, 10):
    print(i)
