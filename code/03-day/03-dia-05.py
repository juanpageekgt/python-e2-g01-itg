# literales de cadena formateados "f-string"
# f {}  (la f puede ser mayúscula o minúscula)

# Ej.1
nombre = 'Carlos'
edad = 30
print(f'Mi nombre es {nombre} y tengo {edad}')

# Ej.2
precio_producto = 25.50
cantidad = 3
print(f'El precio total es: {precio_producto * cantidad}.')

# Ej.3
def obtener_saludo(nombre):
    return f"Hola, {nombre}"

nombre_usuario = "Sofia"
print(f'{obtener_saludo(nombre_usuario)}')

# Ej.4
pi = 3.14159
print(f'El valor de pi con dos decimales es: {pi:.2f}')

numero = 10
print(f'El numero en formato binario es: {numero:b}')
