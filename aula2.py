# Como podemos criar listas?
# Usando loops e range().
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)
print('---')

# Usando a função map().
nomes = ['Larissa', 'Rafael', 'Marcos', 'John']
def aprovar_pessoa(nome):
    return nome + ' APROVADO'

print(map(aprovar_pessoa, nomes))
print(list(map(aprovar_pessoa, nomes)))
print('---')

# Como usar uma list comprehension.

nova_lista = [2 * i for i in range(10)]
# [expressão for membro in iterável]
print(nova_lista)
print('---')
print([nome + ' APROVADO' for nome in nomes])
print('---')
print([aprovar_pessoa(nome) for nome in nomes])
print('---')
'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
from pprint import pprint
pprint([[i for i in range(1, 6)] for x in range(5)])
print('---')
# Usar condicionais em list comprehension.
# [expressão for membro in iterável (condicional if)]
print([aprovar_pessoa(nome) for nome in nomes if nome != 'Rafael'])
print('---')
# Valores numéricos.
print([i for i in range(20) if i not in (1, 5, 15, 19)])
print('---')

def e_numero_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False

print([i for i in range(20) if e_numero_par(i)])
print('---')
# A condicional é flexível.
# [expressão (condicional if) for membro in iterável]
participantes = ['Larissa', 'Rafael', 'Marcus', 'John']
ganhadores = ['Marcus', 'John']
print([i + ' GANHADOR' if i in ganhadores else i + ' NÃO SELECIONADO' for i in participantes])
