produtos = ['computador', 'livro', 'tablet', 'celular', 'tv',
            'ar condicionado', 'alexa', 'máquina de café', 'kindle']

produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

qtdade = 5000


if 'livro' in produtos:
    i_livro = produtos.index('livro')
    total_antes = produtos_ecommerce[i_livro][1] * produtos_ecommerce[i_livro][0]
    produtos_ecommerce[i_livro][1] = produtos_ecommerce[i_livro][1] * 1.1
    total_agora = produtos_ecommerce[i_livro][1] * produtos_ecommerce[i_livro][0]
    print(produtos_ecommerce[i_livro])

    valor_imposto = total_agora - total_antes
    print('Vamos pagar de imposto a mais: R${:,}'.format(valor_imposto))
