# ------------------------- #
# Version: Python 3.10.2
# SO: Windows
# version SO: 11
# AMD64
# ------------------------- #


print('Ej.1 - platform')

# platform(aliased = False, terse = False)

print()

print('Ej.2 - ejecución')

# from platform import platform

# print(platform())
# print(platform(1))
# print(platform(0, 1))
# print()

# sistemaOperativo = platform(0, 1)
# requerimientoSO = 'Windows-10'

# if sistemaOperativo == requerimientoSO:
#     print('Su sistema es Windows 11, procedere a instalar')
# else:
#     print('Requiere Windows 11, actulice o cambie de SO.')

print()

print('Ej.3 - función machine')

from platform import machine, processor, system, version

print(machine())

print()

print('Ej.4 - función processor')

print(processor())

print()

print('Ej.5 - función system')

print(system())

print()

print('Ej.6 - función version')

print(version())

print()

# implementación de script
verWin = '10.0.22631'

if verWin == version():
    print('Sistema Operativo complatible')
else:
    print('Actualiza sistema operativo.')

print()

print('Ej.7 - versiones de python')

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
