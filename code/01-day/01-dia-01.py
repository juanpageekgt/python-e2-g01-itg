# import math

print('Ej.1 - Importando un modulo')

# print(math.pi)
# print(math.sin(math.pi/2))

# print()

# math.pi
# math.sin

print()

print('Ej.2 - Namespaces')

# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None


# pi = 3.14

# print(sin(pi/2))
# print(math.sin(math.pi/2))

print('Ej.3 - uso de entidades del modulo')

# from math import pi

print()

print('Ej.4 - error de importacion de entidad adicional')

# print(pi)
# print(math.e)

print()

print('Ej.5 - reescribir el codigo')

# from math import sin, pi

# print(sin(pi/2))

print()

print('Ej.6 - nuevo codigo')
# from math import sin, pi

# print(sin(pi/2))

# pi = 3.14

# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None

# print(sin(pi/2))

print()

print('Ej.7 - otra prueba')

# pi = 3.14

# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None

# print(sin(pi/2))

# from math import sin, pi

# print(sin(pi/2))

print()

print('Ej.8 - uso de import *')

# from module import *
# from math import *

print()

print('Ej.9 - alias')

import random as alias

print()

print('Ej.10 - renombrado a mate')

import math as mate

print(mate.sin(mate.pi/2))
# print(math.sin(math.pi/2))

print()

print('Ej.11 - usando variante y cambiar el nombre de la entidad')

# from math import pi as alias

print()

print('Ej.12 - emplear comas para separar las frase')

# from module import n as a, m as b, o as c

print()

print('Ej.13 - implementacion de alias a las entidades')

from math import pi as PI, sin as sine

print(sine(PI/2))

print()

