# Procesamiento de archivos de texto

# Ej.1
# stream = open('file.txt', 'rt', encoding='utf-8')

# Ej.2
"""
from os import strerror

try:
    counter = 0
    stream = open('text.txt', "rt", encoding='utf-8')
    char = stream.read(1)

    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print('Se produjo un error de E/S:', strerror(e.errno))
"""
    
# Ej.3
"""
from os import strerror

try:
    counter = 0
    stream = open('text.txt', 'rt', encoding='utf-8')
    content = stream.read()

    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print('se produjo un error de E/S:', strerror(e.errno))
"""

# Ej.4
"""
from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('text.txt', 'rt', encoding='utf-8')
    line = stream.readline()

    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()

    print("\n\nCaracteres en el archivo:", character_counter)
    print('Lineas en el archivo:', line_counter)
except IOError as e:
    print('Se produjo un error de E/S:', strerror(e.errno))

print()

# Ej.5
stream = open('text.txt', 'rt', encoding='utf-8')
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
stream.close()
"""

# Ej.6
"""
from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt', encoding='utf-8')
    lines = s.readlines(20)

    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()

    print('\n\nCaracteres en el archivo:', ccnt)
    print('Lineas en el archivo:', lcnt)
except IOError as e:
    print('Se produjoo un error de E/S:', strerror(e.errno))
"""

# Ej.7
from os import strerror

try:
    ccnt = lcnt = 0
    for line in open('text.txt', 'rt', encoding='utf-8'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    
    print('\n\nCaracteres en el archivo:', ccnt)
    print('Lineas en el archivo:', lcnt)
except IOError as e:
    print('Se produjoo un error de E/S:', strerror(e.errno))