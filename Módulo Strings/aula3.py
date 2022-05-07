faturamento = 1000
custo = 500
lucro = faturamento - custo

# uso do str() e o concatenar com +
print('O faturamento foi de: '+ str(faturamento) + ' o custo foi de ' + str(custo) + ' e o lucro foi de ' + str(lucro))

# uso do format
print('O faturmanento foi de: {} o custo foi de {} e o lucro foi de {}'.format(faturamento,custo,lucro))

# uso do format com os indices dos parametros passados na função
print('O faturmanento foi de: {0} o custo foi de {1} e o lucro foi de {2}. Lembrando que o faturamento foi de {0}'.format(faturamento,custo,lucro))

# uso do %s para strings e o uso do %d para valores inteiros ou reais
print('O faturamento foi de: %d. O custo foi de %d e o lucro foi de %d' % (faturamento,custo,lucro))

# uso do in em uma string
print('@' in 'victor@gmail.com')
print('@' in 'victorgmail.com')