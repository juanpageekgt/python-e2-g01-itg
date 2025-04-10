# import math

print('Ej.1 - funcion dir()')

# dir(module)

print()

print('Ej.2 - implementando dir()')

# for name in dir(math):
#     print(name, end='\t')


print()
print()

print('Ej.3 - funciones math')

# from math import pi, radians, degrees, sin, cos, tan, asin

# ad = 90
# ar = radians(ad)
# ad = degrees(ar)

# print(ad == 80)
# print(ar == pi / 2)
# print(sin(ar) / cos(ar) == tan(ar))
# print(asin(sin(ar)) == ar)

print()

print('Ej.4 - exponenciacion')

# from math import e, exp, log

# print(pow(e, 1) == exp(log(e)))
# print(pow(2, 2) == exp(2 * log(2)))
# print(log(e, e) == exp(0))

print()

print('Ej.5')

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

print()