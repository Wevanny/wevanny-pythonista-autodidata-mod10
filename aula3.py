# Dictionary comprehension.
# List comprehension -> [expressão for membro iterável]
# Dictionary comprehension -> {chave:expressão for membro iterável}
from pprint import pprint
print({i: i for i in range(20)})
pprint({i: i for i in range(20)})
print('---')
# Popular um dicionário com valores usando uma lista como base.
produtos = ['produto1', 'produto2', 'produto3', 'produto4', 'produto5',]
pprint({produto: 1 for produto in produtos})
print('---')
# Gerar uma matriz de valores de teste.
pprint({produto: [0 for i in range(5)] for produto in produtos})
print('---')
pprint({produto: [i * 2 for i in range(5)] for produto in produtos})
print('---')
# Gerar valores de teste usando o random.
import random
pprint({produto: [random.randint(1000, 15000) for i in range(5)] for produto in produtos})
