produtos = ['iphone', 'galaxy s10', 'ipad', 'tv', 'máquina de café', 'kindle',
            'geladeira', 'adega', 'notebook dell', 'notebook acer', 'ps4', 'ps5']
vendas2019 = [558147, 712350, 573823, 405252, 718654,
              751580, 973139, 892292, 422760, 154753, 887061, 438508]
vendas2020 = [951642, 244295, 26964, 787604, 867660,
              78830, 710331, 646016, 694913, 539704, 324831, 667179]

tuplas_vendas = zip(vendas2019,vendas2020)
lista = zip(produtos, tuplas_vendas)
dicionario = dict(lista)

print(dicionario)