# Manejando archivos de texto write()

# Ej.1
from os import strerror
"""
try:
    file = open('nextext.txt', 'wt', encoding='utf-8')

    for i in range(10):
        s = 'Linea #' + str(i+1) + '\n'
        for char in s:
            file.write(char)
    file.close()
except IOError as e:
    print('Se produjo un error de E/S', strerror(e.errno))
"""

# Ej.2
try:
    file = open('nextext.txt', 'wt', encoding='utf-8')
    for i in range(10):
        file.write('Linea #' + str(i+1) + "\n")
    file.close()
except IOError as e:
    print('Se produjo un error de E/S', strerror(e.errno))