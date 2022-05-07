meta = 0.05
taxa = 0
rendimento = 0.01

if rendimento > meta:
    if rendimento > 0.2:
        taxa = 0.04
        print('A taxa foi de {}'.format(taxa))
    else:
        taxa = 0.02
        print('A taxa foi de {}'.format(taxa))
else:
    taxa = 0
    print('A taxa foi de {}'.format(taxa))
