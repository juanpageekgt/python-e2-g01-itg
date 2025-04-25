# bytearray

# Ej.1
"""data = bytearray(10)
print(data)
print(type(data))

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))
"""

# Ej.2
from os import strerror

"""data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print('Se produjo un error de E/S:', strerror(e.errno))
"""

# Ej.3
"""data = bytearray(10)

try:
    binary_file = open('file.bin', 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print('Se produjo un error de E/S:', strerror(e.errno))
"""

# Ej.4
"""try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read())
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print('Se produjo un error de E/S:', strerror(e.errno))
"""

# Ej.5
try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read(5))
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print('Se produjo un error de E/S:', strerror(e.errno))