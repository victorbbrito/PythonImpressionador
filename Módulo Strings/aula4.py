# métodos de strings

#capitalize() -> a 1º letra em maiusculo

texto = 'victor'
print(texto.capitalize())

#casefold() -> todas as letras em minuculo, melhor que lower()
print(texto.casefold())

#count() -> quantidade de vezes que um elemento aparece na string
print(texto.count('t'))

#endswith() -> verifica se a string termina com um valor especifico e retorna um boolean
print(texto.endswith('r'))

#find() -> procura um texto dentro de outro texto e da como resposta a posição do texto encontrado
print(texto.find('c'))

#format() -> formata uma string de acordo com os valores passados
print('Meu nome é {}'.format(texto))

#isalnum() -> verifica de um texto é todo feito com caracteres alfanuméricos (letras e numeros) -> letras com acento ou ç são considerados letras nessa função
print(texto.isalnum())
print('vic~tr'.isalnum())

#isalpha() -> verifica se um texto é todo composto por letras
print(texto.isalpha())

#isnumeric() -> verifica se um texto é todo composto por numeros
print(texto.isnumeric())

#replace() -> substitui um texto por um outro texto de uma string
numero = '100.00'
print(numero.replace('.',',')) #substituir o . pela ,

#split() -> separa uma string de acordo com um limitador 
email = 'victor@gmail.com'
print(email.split('@')) #separar o que vem antes do @ e o que vem depois do @

#splitlines() -> separa um texto em vários textos de acordo com os enters do texto
texto = '''Olá.
        Hoje iremos falar sobre
        os numeros naturais'''

print(texto.splitlines())

#startswith() -> verifica se a string começa com determinado caractere
print(texto.startswith('O'))

#strip() -> retira caracteres indesejados dos textos, por padrão retira os espaços no incio e no final
texto = ' o nome '
print(texto.strip())

# title() coloca a 1º letra de cada palavra em maiusculo
print(texto.title())

#upper() -> coloca todo o texto em maiusculo
print(texto.upper())
