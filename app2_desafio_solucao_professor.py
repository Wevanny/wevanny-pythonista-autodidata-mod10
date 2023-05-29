import random
from pprint import pprint
# Desafio 1
pprint([i * 2 for i in range(1, 6)])

# Desafio 2
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa', 'preto']
pprint([str(cores.index(cor)+1) + ' - ' + cor for cor in cores])

# Desafio 3
participantes = ['Joel', 'Jéssica', 'Maria', 'Cris', 'Larissa', 'Rafael', 'Marcus', 'John']
pagamento_realizado = ['Joel', 'Jéssica', 'Maria', 'Cris']
pprint([i + ' PAGO' if i in pagamento_realizado else i + ' DEVENDO' for i in participantes])




