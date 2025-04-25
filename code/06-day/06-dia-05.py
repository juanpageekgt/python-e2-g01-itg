# abriendo el flujo (stream) por primera vez

# Ej.1
try:
    stream = open("C:\Users\User\Desktop\file.txt", "rt")
    # stream = open("\\Users\\User\\Destop\\file.txt", "rt") 
    # procesamiento va aquí
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo", exc)

# Ej.2
try:
    # algunas operaciones con strams
except IOError as exc:
    print(exc.errno)


# Ej.3
import errno

try: 
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # procesamiento va aquí
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print('el archivo no existe.')
    elif exc.errno == errno.EMFILE:
        print('Demasiados archivos abiertos')
    else:
        print('El numero del error es:', exc.errno)


# Ej.4
from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # procesamiento va aquí
    s.close()
except Exception as exc:
    print('El archivo no pudo ser abierto:', strerror(exc.errno))