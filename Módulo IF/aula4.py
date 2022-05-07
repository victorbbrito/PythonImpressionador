import email


faturamento_loja_1 = 2500
faturamento_loja_2 = 2200

print('Programa 1')
if faturamento_loja_1 == faturamento_loja_2:
    print('Os faturamentos são iguais')
else:
    print('Os faturamentos são diferentes')

email = "liragmail.com"

print('Programa 2')
if email != 'lira@gmail.com':
    print('Esse não é o email do lira')
else:
    print('Email errado')

print('Programa 3')

if not '@' in email:
    print('Email inválido')
else:
    pass
