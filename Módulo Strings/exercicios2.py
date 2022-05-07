# cadastro de emails com verificação
nome = input('Informe seu nome: ')
email = input('Informe o email: ')

if nome and email:
    pos_a = email.find('@')
    servidor = email[pos_a:]
    if (pos_a != -1) and '.' in servidor:
        print('Cadastro concluído')
    else:
        print('Digite seu e-mail corretamente')
else:
    print('Digite seu nome e e-mail corretamente')