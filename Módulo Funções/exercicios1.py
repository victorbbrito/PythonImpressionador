
def carga_tributaria(preco, custo, lucro):
    imposto = preco - custo - lucro
    return imposto/preco

preco = 1500
custo = 400
lucro = 615

print("A carga tributaia foi de {:.1%}".format(carga_tributaria(preco, custo, lucro)))
