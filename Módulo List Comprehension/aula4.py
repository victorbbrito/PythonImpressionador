vendedores_dic = {'Maria': 1200, 'José': 300, 'Antônio': 800,
                  'João': 1500, 'Francisco': 1900, 'Ana': 2750, 'Luiz': 400}

meta = 1000

lista = [(item, vendedores_dic[item]*0.1) if vendedores_dic[item]
         > meta else (item, 0) for item in vendedores_dic]

print(lista)
