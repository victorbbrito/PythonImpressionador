from pathlib import Path
import shutil

caminho = Path('Arquivos e pastas do computador/Arquivos_Lojas') # current directory , onde está rorando o programa em si

# rastrear os arquivos que tem dentro de uma pasta
arquivos = Path.iterdir(caminho)

print(caminho)

# Verificar se um arquivo está dentro de um diretório
if (caminho / Path('202004_Shopping Tijuca_RJ.csv')).exists():
    print('Existe')

# printando cada arquivo dentro do diretório
for arquivo in arquivos:
    print(arquivo)

# criando uma pasta
# Path('Arquivos e pastas do computador/Pasta Auxiliar').mkdir()

# copiando um arquivo
arquivo_para_copiar = Path('Arquivos e pastas do computador/Arquivos_Lojas/202004_Shopping Tijuca_RJ.csv')
onde_colar = Path('Arquivos e pastas do computador/Pasta Auxiliar/202004_Shopping Tijuca_RJ_cópia.csv')

shutil.copy2(arquivo_para_copiar,onde_colar)

# mover um arquivo
arquivo_para_mover = Path('Arquivos e pastas do computador/Pasta Auxiliar/202004_Shopping Tijuca_RJ_cópia.csv')
onde_mover = Path('Arquivos e pastas do computador/Arquivos_Lojas/202004_Shopping Tijuca_RJ_cópia.csv')
shutil.move(arquivo_para_mover, onde_mover)


