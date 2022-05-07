# criando um registro de hóspedes

# 1. identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio do input)
# 2. de acordo com a quantidade de pessoas dos hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada pessoa, para registra-la no quarto (2 inputs para cada pessoa
#  1 para o nome e 1 para o CPF)
# 3. o seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que  cada item dessa lista é o nome da pessoa e o cpf da pessoa, assim:

# quarto = [
#   ['João', 'CPF:00000000000'],
#   ['Julia','CPF:11111111111'],
#   ['Marcos','CPF:22222222222'],
#   ['Maria','CPF:33333333333']
# ]

quantidade_pessoas = int(input('Quantas pessoas ficarão no quarto ?'))

quarto = []

for i in range(quantidade_pessoas):
    nome = input('Qual o nome da pessoa: ')
    cpf = input('Qual o CPF da pessoa: ')
    hospede = [nome, 'CPF:'+cpf]
    quarto.append(hospede)

print(quarto)
