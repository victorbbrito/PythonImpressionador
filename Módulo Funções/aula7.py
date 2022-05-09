# retorna um número
from cgitb import text


def minha_soma(num1, num2, num3):
    return num1+num2+num3

# retorna um texto
def padronizar_texto(texto: str):
    texto = texto.casefold()
    texto = texto.replace("  "," ")
    texto = texto.strip()
    return texto

# retorna um boolean
def bateu_meta(vendas, meta):
    if vendas > meta:
        return True
    else:
        return False

# retorna uma lista, tupla ou dicionário
def filtrar_lista_texto(lista, texto):
    lista_filtrada = []
    for item in lista:
        if texto in item:
            lista_filtrada.append(item)
    return lista_filtrada

lista_textos = ['victor@gmail.com','wanner@gmail.com','joao@hotmail.com','ipaam@am.gov.br']
lista = filtrar_lista_texto(lista_textos, 'hotmail')
print(lista)