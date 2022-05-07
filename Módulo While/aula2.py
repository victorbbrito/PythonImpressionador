vendas = [941, 852, 783, 714, 697, 686, 670, 631, 453, 386,
          371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]
vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca',
              'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
meta = 50

indice = 0

while vendas[indice] > meta:
    print('{} bateu a meta. Vendas: {}'.format(vendedores[indice], vendas[indice]))
    indice += 1
