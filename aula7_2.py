import webbrowser
import threading
import time
import random

def comentar(site, comentario):
    # # Simulando um erro para demonstrar a continuidade do programa:
    # if site == 8:
    #     raise Exception('Houve um erro grave!')
    print(f'Entrando no site {site}')
    print(f'Deixando um comentário {comentario}')
    time.sleep(5)
    print(f'Dados processados no site {site}')
# Deixando comentários:
comentarios = ['oi', 'olá', 'gostei', 'curti', 'muito bom']
threads = []
for site in range(100):
    nova_thread = threading.Thread(target=comentar, args=(site, random.choice(comentarios)),)
    threads.append(nova_thread)

for thread in threads:
    thread.start()
    print(f'Iniciando {thread.name}')

# Se for necessária uma sequência de execução (senão serão realizados threads em massa):
# for thread in threads:
#     thread.start()
#     thread.join()
#     # print(f'Iniciando {thread.name}')

for thread in threads:
    thread.join()
    print(f'Finalizando {thread.name}')

