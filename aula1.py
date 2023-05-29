# Como podemos criar listas?
# Usando loops e range().
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

# Usando a função map().
nomes = ['Larissa', 'Rafael', 'Marcos', 'John']
def aprovar_pessoa(nome):
    return nome + ' APROVADO'

print(map(aprovar_pessoa, nomes))
print(list(map(aprovar_pessoa, nomes)))
