'''
​# Desafio 1

Usando list compreheension, crie a seguinte lista:

[2,4,6,8,10]

# Desafio 2

Use a lista comprheension usando a seguinte lista como base:

cores = ['vermelho','azul','verde','amarelo','rosa','preto']

para criar a lista seguir

['cor - vermelho','cor - azul','cor - verde','cor - amarelo','cor - rosa','cor - preto']

# Desafio 3

Usando a lista seguir como base:

participantes = ['joel','jessica', 'maria','cris','Larissa', 'rafael', 'marcus', 'john']

pagamento_realizado = ['joel','jessica', 'maria','cris']

concatene(adicione) a palavra ' PAGO' aos nomes da lista 'participantes' usando condicionais, somente nos caso onde seu nome esteja na lista 'pagamento_realizado', ou ' DEVENDO' em caso contrário. 

O resultado final deve ser como a lista a seguir:

['joel PAGO', 'jessica PAGO', 'maria PAGO', 'cris PAGO',

    'Larissa DEVENDO', 'rafael DEVENDO', 'marcus DEVENDO', 'john DEVENDO']
'''
from pprint import pprint
# Desafio 1.
def numero_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False
print([numero for numero in range(1, 11) if numero_par(numero)])
print('---')

# Desafio 2.
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa', 'preto']
pprint([str(cores.index(i)+1) + ' - ' + i for i in cores])
print('---')

# Desafio 3.
participantes = ['Joel', 'Jéssica', 'Maria', 'Cris', 'Larissa', 'Rafael', 'Marcus', 'John']
pagamento_realizado = ['Joel', 'Jéssica', 'Maria', 'Cris']
print([nome + ' PAGO' if nome in pagamento_realizado else nome + ' DEVENDO' for nome in participantes])
