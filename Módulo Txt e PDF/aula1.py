
arquivo = open(r'PythonImpressionador\Módulo Txt e PDF\Alunos.txt', 'r')

print(arquivo.readlines())

novo_arquivo = open('PythonImpressionador\Módulo Txt e PDF\Resumo.txt', 'w')
novo_arquivo.write('OLA ESTAMOS TESTANDO')

novo_arquivo.close()
