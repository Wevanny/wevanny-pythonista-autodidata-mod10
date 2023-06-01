import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluído na pasta final:
arquivos = ['pythonpy.ico'] # Se acrescentar uma pasta usar barra para que seja acessado o conteúdo dela. Ex:
#arquivos = ['web.ico', 'musicas/'].
configuracao = Executable(
    script = 'aula9.py',
    icon = 'pythonpy.ico'
)
# Configurar o cx-freeze(detalhes do programa)
setup(
    name = 'Automatizador de Login',
    version = '1.0',
    description = 'Este programa automatiza o login',
    author = 'Jonathan de Souza',
    options = {'build_exe': {'include_files': arquivos}},
    executables = [configuracao]
)

#1. No cmd rodar pip install cx-freeze caso ainda não o tenha instalado;
#2. No terminal rodar cxfreeze nome_do_arquivo (colocar \antes do nome se estiver dentro de uma pasta);
#3. Se adicionar um ícone e algum outro arquivo(uma pasta por exemplo) rodar no terminal o comando 
# python setup.py build.