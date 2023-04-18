with open('Módulo Txt e PDF\Alunos.txt', 'r') as txt:
    lista_por_linha = txt.readlines() # lendo linha por linha do arquivo txt e colocando cada linha em uma lista

del lista_por_linha[:4] #deletando os 3 primeiros indices da lista pois não serão usados

site_org = 0
youtube_org = 0
instagram_org = 0
anuncio = 0
organico = 0

for item in lista_por_linha:
    email, origem = item.split(',') # separando os dados da lista em uma variável email e origem (de onde foi coletado o email)
    if '_org' in origem:
        organico += 1
        if '_yt_' in origem:
            youtube_org += 1
        if '_site_' in origem:
            site_org += 1
        if '_igfb_org' in origem or '_ig_org' in origem:
            instagram_org += 1
    else:
        anuncio += 1

with open('Módulo Txt e PDF\Indicadore.txt', 'w') as arquivo:
    arquivo.write(f'Quantidade por Anuncio: {anuncio}\n')
    arquivo.write(f'Quantidade Organico: {organico}\n')
    arquivo.write(f'Quantidade pelo YouTube: {youtube_org}\n')
    arquivo.write(f'Quantidade pelo Instagram: {instagram_org}\n')
    arquivo.write(f'Quantidade pelo Site: {site_org}\n')
    
print('Executado')