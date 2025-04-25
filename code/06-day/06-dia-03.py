# Lambdas y la función map() y filter()

# Ej.1 - sintaxis
map(function, list)

# Ej.2 
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))

print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

print()

# Ej.2b
def sumar_uno(n):
    return n + 1

numeros = [1, 2, 3, 4, 5]
resultados = map(sumar_uno, numeros)

lista_resultados = list(resultados)
print(lista_resultados)

# map es un iterador de elementos de listas

# Ej.3
from random import seed, randint

seed()
data = [randint(-10, 10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)