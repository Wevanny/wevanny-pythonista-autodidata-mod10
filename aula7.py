import webbrowser
import threading
import time

def extrair_dados_do_site(site):
    print(f'estamos navegando até o site {site}')
    webbrowser.open_new(site)
    for i in range(1, 20):
        print(f'Processando dados - {i}/19')
        time.sleep(1)
        print('Finalizando extração de dados do site')

def baixar_arquivos():
    for i in range(1, 10):
        print(f'Baixando arquivos - {i}/10')
        time.sleep(1)
        print('Arquivos baixados')

nova_thread = threading.Thread(target=extrair_dados_do_site, args=('https:www.devaprender.com',), daemon=True )
nova_thread.start()
baixar_arquivos()
nova_thread.join()

# Caso seja preciso concluir a thread principal antes de continuar a execução do programa setar como abaixo:
# nova_thread = threading.Thread(target=extrair_dados_do_site, args=('https:www.devaprender.com',), daemon=True )
# nova_thread.start()
# nova_thread.join()
# baixar_arquivos()
