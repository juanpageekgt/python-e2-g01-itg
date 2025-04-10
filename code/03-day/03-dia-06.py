# Programación Orientada a Objetos (POO)

# Clases
# Ej.1
class TheSimpleClass:
    pass

# objetos
# Ej.2
my_first_object = TheSimpleClass()

# Pila
# Ej.3
stack = []

# Ej.4
def push(val):
    stack.append(val)


# Ej.5
def pop():
    val = stack[-1]
    del stack[-1]
    return val

# Ej.6
push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
