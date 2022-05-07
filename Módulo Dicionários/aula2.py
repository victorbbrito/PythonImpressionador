mais_vendidos = {'tecnologia': 'iphone', 'refrigeração': 'ar consul 12000 btu',
                 'livros': 'o alquimista', 'eletrodomesticos': 'cafeteira'}

vendas_tecnologia = {'iphone': 15000, 'samsung galay': 12000,
                     'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720}
# respondendo com chave
print("O livro mais vendido foi {}".format(mais_vendidos['livros']))
# respondendo com o método get
print(vendas_tecnologia.get('tablet'))

# verificar se o item está no dicionário

if vendas_tecnologia.get("copo") == None:
    print("Copo não está dentro da lista de produtos de tecnologia")
else:
    print(vendas_tecnologia.get('copo'))