
# o que é um Iterable?
# Um iterable é uma estrutura que armazena dados que pode ser "iterada" ou seja, que você pode fazer um loop como um for dentro dela e ir passando de item a item.
# É como se fosse um tipo de lista de coisas que você pode ir olhando cada um dos elementos dentro dela.

# Listas

produtos = ['iphone', 'galaxy s10', 'ipad', 'tv', 'máquina de café', 'kindle',
            'geladeira', 'adega', 'notebook dell', 'notebook acer', 'ps4', 'ps5']

for produto in produtos:
    print(produto)

# Strings

texto = 'victor@gmail.com'

for char in texto:
    print(char)

# Tuplas

tupla = ('iphone', 'galaxy s10', 'ipad', 'tv', 'máquina de café', 'kindle',
         'geladeira', 'adega', 'notebook dell', 'notebook acer', 'ps4', 'ps5')

for produto in tupla:
    print(produto)

# Dicionário
produtos = {'iphone': (558147, 951642), 'galaxy s10': (712350, 244295), 'ipad': (573823, 26964), 'tv': (405252, 787604), 'máquina de café': (718654, 867660), 'kindle': (
    751580, 78830), 'geladeira': (973139, 710331), 'adega': (892292, 646016), 'notebook dell': (422760, 694913), 'notebook acer': (154753, 539704), 'ps4': (887061, 324831), 'ps5': (438508, 667179)}

for chave in produtos:
    print('{}:{}'.format(chave, produtos[chave]))
