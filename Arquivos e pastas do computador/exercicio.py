from pathlib import Path
import shutil

caminho = Path('Arquivos e pastas do computador/Arquivos_Lojas')

estados = ['RJ','SP','MG','GO','AM']
Path(f'Arquivos e pastas do computador/Aux').mkdir()

for estado in estados:
    arquivos = caminho.iterdir()
    Path(f'Arquivos e pastas do computador/Aux/{estado}').mkdir()
    
    for arquivo in arquivos:
        if f'{estado}.csv' in arquivo.name:
            pasta = Path('Arquivos e pastas do computador/Aux/'+f'{estado}/{arquivo.name}')
            shutil.move(arquivo,pasta)
    

    
