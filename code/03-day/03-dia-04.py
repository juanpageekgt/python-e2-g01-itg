# Excepciones integradas

# Ej.1
# from math import tan, radians

# angle = int(input('Ingresa un angulo entero en grados: '))

# # Debemos estar seguros de que angle != 90 + k * 180
# assert angle % 180 != 90
# print(tan(radians(angle)))


# Ej.2
# the_list = [1, 2, 3, 4, 5]
# ix = 0
# do_it = True

# while do_it:
#     try:
#         print(the_list[ix])
#         ix += 1
#     except IndexError:
#         do_it = False

# print('Listo')


# Ej.3
# from time import sleep

# seconds = 0

# while True:
#     try:
#         print(seconds)
#         seconds += 1
#         sleep(1)
#     except KeyboardInterrupt:
#         print('!No hagas esto!')

# Ej.4
# string = 'x'

# try:
#     while True:
#         string = string + string
#         print(len(string))
# except MemoryError:
#     print('Esto no es gracioso!')


# Ej.5
# from math import exp

# ex = 1

# try:
#     while True:
#         print(exp(ex))
#         ex *= 2
# except OverflowError:
#     print('El numero es demasiado grande.')
    

# Ej.6
# try:
#     import math
#     import time
#     import abracadabra
    
# except ImportError:
#     print('Una de tus importaciones ha fallado.')


# Ej.7
dictionary = {'a': 'b', 'b':'c', 'c':'d'}
ch = 'a'

try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No existe tal clave:', ch)
