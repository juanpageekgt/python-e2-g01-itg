# Más acerca de excepciones

# Ej.1
""" def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print('Division fallida')
        return None
    else:
        print('Todo salio bien')
        return n
    
print(reciprocal(2))
print(reciprocal(0)) """


# Ej.2
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print('Division fallida')
        return None
    else:
        print('Todo salio bien')
    finally:
        print('Es momento de decir adios')
        return n
    
print(reciprocal(2))
print(reciprocal(0))

# Ej.3
try:
    i = int('!Hola!')
except Exception as e:
    print(e)
    print()
    print(e.__str__())


# Ej.4
def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print('   |' * (nest - 1), end='')
    if nest > 0:
        print('   +---', end='')
    
    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)


# Ej.5
def print_args(args):
    lng = len(args)
    if lng == 0:
        print('')
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))

try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print(e.args)

print()

try:
    raise Exception('Mi excepcion')
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

print()

try:
    raise Exception('mi', 'excepcion')
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)
