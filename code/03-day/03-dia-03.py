# Excepciones, continuación

# Ej.1
# try:
#     y = 1 / 0
# except ZeroDivisionError:
#     print('uuupsss...')

# print('FIN')

# Ej.2
# try:
#     y = 1 / 0
# except ArithmeticError:
#     print('uuupsss...')

# print('FIN')

# Ej.3
# try:
#     y = 1 / 0
# except ZeroDivisionError:
#     print('!Division entre cero!')
# except ArithmeticError:
#     print('!Problema Aritmetico!')

# print('FIN')

# Ej.4
# try:
#     y = 1 / 0
# except ArithmeticError:
#     print('!Problema Aritmetico!')
# except ZeroDivisionError:
#     print('!Division entre cero!')

# print('FIN')

# Ej.5
# def bad_fun(n):
#     try:
#         return 1 / n
#     except ArithmeticError:
#         print('!Problema Aritmetico.')
#     return None


# bad_fun(0)

# print('FIN')

# Ej.6
# def bad_fun(n):
#     return 1 / n


# try:
#     bad_fun(0)
# except ArithmeticError:
#     print('¿que ocurrio?, !Se genero una excepcion!')

# print('FIN')

# Ej.7
# def bad_fun(n):
#     raise ZeroDivisionError


# try:
#     bad_fun(0)
# except ArithmeticError:
#     print('¿Que paso?, ¿Un error?')

# print('FIN')

# Ej.8
# def bad_fun(n):
#     try:
#         return n / 0
#     except:
#         print('!Lo hice otra vez!')
#         raise


# try:
#     bad_fun(0)
# except ArithmeticError:
#     print('!Ya veo!')

# print('FIN')

# Ej.9
import math

x = float(input('Ingrese un numero: '))
assert x >= 0.0

x = math.sqrt(x)

print(x)
