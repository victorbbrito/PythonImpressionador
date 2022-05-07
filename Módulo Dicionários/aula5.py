vendas_tecnologia = {'iphone': 15000, 'samsung galay': 12000,
                     'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720}

itens_dicionario = vendas_tecnologia.items()
print(itens_dicionario)

for produto, qntdade in vendas_tecnologia.items():
    print('{}:{}'.format(produto, qntdade))

for chave in vendas_tecnologia:
    if vendas_tecnologia[chave] > 5000:
        print('{}:{}'.format(chave, vendas_tecnologia[chave]))

for produto, qntdade in vendas_tecnologia.items():
    if qntdade > 5000:
        print('{}:{}'.format(produto, qntdade))

chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()

print("---------------COMO DICT------------------")
print(chaves)
print(valores)
print("-----------------COMO LISTAS-------------------")
print(list(chaves))
print(list(valores))

lista_chaves = list(chaves)
lista_valores = list(valores)
lista_chaves.sort()

for chave in lista_chaves:
    print('{}:{}'.format(chave, vendas_tecnologia[chave]))
print('-'*20)
