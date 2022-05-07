vendas_tecnologia = {'iphone': 15000, 'samsung galay': 12000,
                     'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720}

for chave in vendas_tecnologia:
    print("{}: {} unidades".format(chave,vendas_tecnologia.get(chave)))
