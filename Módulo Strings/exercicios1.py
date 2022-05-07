# insira o seu CPF(apenas números)

cpf = input('Insira seu CPF: (Apenas números)')

if len(cpf) == 11:
    if cpf.isnumeric:
        print(cpf)
    else:
        print('Digite o CPF corretamente.')
else:
    print('Um CPF possui apenas números. ex: 00309807456 (11 números)')

# insira o seu CPF

cpf = input('Insira seu CPF: ')

# tratamentos com a entrada do CPF
# tirar os expaços do inicio e do final
cpf = cpf.strip()

# tirar os ponto(.)
cpf = cpf.replace('.','')

# tirar os traços(-)
cpf = cpf.replace('-','')

if len(cpf) == 11:
    if cpf.isnumeric:
        print(cpf)
    else:
        print('Digite o CPF corretamente.')
else:
    print('Um CPF possui apenas números. ex: 00309807456 (11 números)')