import webbrowser
import threading

# Desafio 1

# def buscar_fotos_do_site(site):
#     webbrowser.open_new(site)
#     print(f'Estamos navegando até o site {site}')    
    
# def baixar_fotos(site):
#     print(f'Estamos baixando fotos no site {site}')
#     print('Fotos baixadas')

# nova_thread = threading.Thread(target=buscar_fotos_do_site, args=('https:www.devaprender.com',), daemon=True)
# nova_thread.start()
# baixar_fotos('https:www.devaprender.com')
# nova_thread.join()

# Desafio 2

# Classe personalizada para estender Thread
class ProdutoThread(threading.Thread):
    def __init__(self, site, produto):
        super().__init__()
        self.site = site
        self.produto = produto           
        print(f'Entrando no site {site} e visualizando o produto {produto}')       
    
# Produtos:
produtos = ['celular', 'monitor', 'fone de ouvido', 'alto-falante', 'computador']

# Site 
site = 'https:www.magazineluiza.com.br'

# Abrir o site
webbrowser.open_new(site) 

# Threads
threads = []
for produto in produtos:
    nova_thread = ProdutoThread(site, produto)
    threads.append(nova_thread)

for thread in threads:
    thread.start()
    print(f'Iniciando {thread.produto}')

for thread in threads:
    thread.join()
    print(f'Finalizando {thread.produto}')




