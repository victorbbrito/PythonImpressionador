precos_imoveis = [2.17,1.54,1.45,1.94,2.37,2.3,1.79,1.8,2.25,1.37]
tamanho_imoveis = [207,148,130,203,257,228,160,194,232,147]

def separar_listas(precos, tamanhos, fator=0.1):
    if len(precos) == len(tamanhos):
        i = int((1 - fator) * len(precos_imoveis))
        precos_imoveis_treino = precos[:i]
        precos_imoveis_teste = precos[i:]
        tamanho_imoveis_treino = tamanhos[:i]
        tamanho_imoveis_teste = tamanhos[i:]
        return precos_imoveis_treino,precos_imoveis_teste,tamanho_imoveis_treino, tamanho_imoveis_teste
    else:
        print("As listas de preços e tamanhos dos imóveis não tem a mesma quantidade de itens")
        return

pTreino, pTeste, tTreino, tTeste = separar_listas(precos_imoveis,tamanho_imoveis)

print(pTreino)
print(pTeste)
print(tTreino)
print(tTeste)