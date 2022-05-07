

def padronizar_codigos(lista_codigos, padrao='m'):
    nova_lista = []
    for item in lista_codigos:
        item = item.replace('  ', '')
        item = item.strip()
        if padrao == 'M':
            item = item.upper()
        else:
            item = item.casefold()
        nova_lista.append(item)
    return nova_lista


cod_produtos = ['ABC12', 'abc37', 'AbC34']
print(padronizar_codigos(cod_produtos, 'm'))
