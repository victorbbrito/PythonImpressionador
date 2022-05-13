

impostoProduto = 0.1
impostoServico = 0.15
impostoRoialtz = 0.25


def calcular_imposto(imposto):
    return lambda preco: preco*(1+imposto)


calcularPrecoProduto = calcular_imposto(impostoProduto)
calcularPrecoServico = calcular_imposto(impostoServico)
calcularPrecoRoialtz = calcular_imposto(impostoRoialtz)

print(calcularPrecoProduto(100))
print(calcularPrecoServico(100))
print(calcularPrecoRoialtz(100))
