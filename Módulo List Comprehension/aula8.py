
preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000,
                    'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}

# fazendo com functions


def calcular_imposto(valor):
    return valor * 1.3


preco_com_imposto = list(map(calcular_imposto, preco_tecnologia.values()))

print(preco_com_imposto)

preco_com_impostoLambda = list(
    map(lambda preco: preco * 1.3, preco_tecnologia.values()))
print(preco_com_impostoLambda)

# fazendo com functions
def maior_que_2000(item):
    return item[1] > 2000

produtos_acima_2000 = list(filter(maior_que_2000, preco_tecnologia.items()))

print(produtos_acima_2000)

# fazendo com lambda
produtos_acima = list(filter(lambda item: item[1]>2000, preco_tecnologia.items()))

print(produtos_acima)
