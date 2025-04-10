print('Ej.1 - funcion random')

# from random import random

# for i in range(15):
#     print(random())

print()

print('Ej.2 - funcion seed')

# from random import random, seed, randrange

# x = randrange(0, 9999999)
# seed(x)

# for i in range(5):
#     print(random())

print()

print('Ej.3 - funciones randrange y randint')

# from random import randrange, randint

# print(randrange(1), end=' ')
# print(randrange(0, 1), end=' ')
# print(randrange(0, 1, 1), end=' ')
# print(randint(0, 1))

print()

print('Ej.4 - generá elementos no únicos')

# from random import randint

# for i in range(10):
#     print(randint(1, 10), end=',')

print()

print('Ej.5 - funciones choice y sample')

# from random import choice, sample

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(choice(my_list))
# print(sample(my_list, 5))
# print(sample(my_list, 10))

print()

print('Ej.6 - implementación')

import random

def elegir_ganador(lista_nombres):
    ganador = random.choice(lista_nombres)
    return ganador

# Lista de nombres de los participantes
participantes = ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis']

# Elegir al ganador de forma aleatoria
ganador = elegir_ganador(participantes)

# Mostrar el nombre del ganador
print('El ganador es:', ganador)
