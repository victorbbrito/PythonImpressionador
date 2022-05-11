preco_produtos = [100, 150, 300, 5000]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']

# com list comprehension ->

impostos = [preco * 0.3 for preco in preco_produtos]

print(impostos)

def calcular_imposto(preco, imposto):
    return preco * imposto

impostos = [calcular_imposto(preco, 0.5) for preco in preco_produtos]

print(impostos)

