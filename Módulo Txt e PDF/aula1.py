
arquivo = open(r'Módulo Txt e PDF\Alunos.txt', 'r')

print(arquivo.readlines())

novo_arquivo = open('Módulo Txt e PDF\Resumo.txt', 'w')
novo_arquivo.write('OLA ESTAMOS TESTANDO')

novo_arquivo.close()

with open(r'Módulo Txt e PDF\Resumo.txt', 'a') as arquivo2:
    arquivo2.write('\nTESTANDO')
    print('executado')
