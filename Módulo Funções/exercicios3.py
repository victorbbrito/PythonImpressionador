meta = 10000

vendas = {
    'João':15000,
    'Júlia':27000,
    'Marcos':9900,
    'Maria':3750,
    'Ana':10300,
    'Alan':7870
}

def bateu_meta(meta,dicionario):
    vendedores_meta_batida = []
    for vendedor in dicionario:
        if dicionario[vendedor] > meta:
            vendedores_meta_batida.append(vendedor)
    
    percentual = len(vendedores_meta_batida) / len(dicionario)
    return percentual, vendedores_meta_batida

print(bateu_meta(meta, vendas))