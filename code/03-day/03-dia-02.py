# Errores, fallas y otras plagas

# Ej.1
# import math

# x = float(input("Ingresa x: "))
# y = math.sqrt(x)

# print('la raiz cuadrada de', x, 'es igual a', y)

# print()

# Ej.2
# value = 1
# value /= 0

# print()

# Ej.3
# my_list = []
# x = my_list[0]

# print()

# Ej.4
# first_number = int(input('Ingresa el primer numero: '))
# second_number = int(input('Ingresa el segundo numero: '))

# if second_number != 0:
#     print(first_number / second_number)
# else:
#     print('Esta operacion no puede ser realizada.')

# print('FIN')

# print()

# Ej.5
# first_number = int(input('Ingresa el primer numero: '))
# second_number = int(input('Ingresa el segundo numero: '))

# try:
#     print(first_number / second_number)
# except:
#     print('Esta operacion no puede ser realizada.')

# print('FIN')

# print()

# Ej.6
# try:
#     print('1')
#     x = 1 / 0
#     print('2')
# except:
#     print('Oh cielos, algo salio mal...')

# print('3')

# print()

# Ej.7
# try:
#     x = int(input('Ingresa un numero: '))
#     y = 1 / x
# except:
#     print('oh cielos, algo salio mal...')
    
# print('Fin.')

# print()

# Ej.8
# try:
#     x = int(input('Ingresa un numero: '))
#     y = 1 / x
#     print(y)
# except ZeroDivisionError:
#     print('No puedes dividir entre cero, lo siento.')
# except ValueError:
#     print('Debes ingresar un valor entero.')
# except KeyboardInterrupt:
#     print()
#     print('Se interrumpio por comando de teclado.')
# except:
#     print('Oh cielos, algo salio mal...')

# print('FIN.')

# Ej.9
# try:
#     x = int(input('Ingresa un numero: '))
#     y = 1 / x
#     print(y)
# except ValueError:
#     print('Debes ingresar un valor entero.')
# except:
#     print('Oh cielos, algo salio mal...')

# print('FIN.')

# Ej.10
try:
    x = int(input('Ingresa un numero: '))
    y = 1 / x
    print(y)
except ValueError:
    print('Debes ingresar un valor entero.')

print('FIN.')