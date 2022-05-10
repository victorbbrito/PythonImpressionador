def descobrir_servidor(email):
    try:
        posicao_a = email.index('@')
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'não determinado'
    except ValueError:
        ('Email digitado não tem @,digite novamente')

texto = 'victorgmail.com'
descobrir_servidor(texto)

