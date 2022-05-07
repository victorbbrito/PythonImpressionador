
meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)
maior_valor = max(vendas_1sem)
menor_valor = min(vendas_1sem)
print(maior_valor)
print(menor_valor)

indice_maior_valor = vendas_1sem.index(maior_valor)
indice_menor_valor = vendas_1sem.index(menor_valor)

print('O melhor mês do ano foi {} com {} vendas'.format(
    meses[indice_maior_valor], maior_valor))
print('O pior mês do ano foi {} com {} vendas'.format(
    meses[indice_menor_valor], menor_valor))

faturamento = sum(vendas_1sem)
print('Faturamento total: R${:,.2f}'.format(faturamento))

percentual = maior_valor / faturamento
print(
    'O melhor mês representou {:.1%} das vendas do ano todo'.format(percentual))

top3 = []
top3.append(maior_valor)
vendas_1sem.remove(maior_valor)
maior_valor = max(vendas_1sem)
top3.append(maior_valor)
vendas_1sem.remove(maior_valor)
maior_valor = max(vendas_1sem)
top3.append(maior_valor)
print(top3)
