meta = 50000
vendas = int(input('Quantidade de vendas de iPhones:'))

if (vendas > meta):
    print('=================================================')
    print(f'Meta batida, vendemos {vendas} unidades de iPhones.')
    print('=================================================')
else:
    print(f'A meta não foi atingida.\nA meta é {meta} e vendemos apenas {vendas}. ')

print('\nFim do programa.')