"""
Ejercicio 1:
Escribe una función llamada validar_edad(edad) 
que reciba una edad como argumento. 
Utiliza la instrucción raise para generar una 
excepción ValueError si la edad es negativa. 
Si la edad es válida (mayor o igual a 0), 
la función debe retornar la edad
"""
# def  edadv(edadt):
#     if int(edadt) < 0:
#         raise Exception("Entro negativo")
#     else:
#      return edadt
 
# text=input("Ingresa tu edad: ")
# print (edadv(text))

# def validar_edad(edad):
#     if edad < 0:
#         raise ValueError('La edad no puede ser negativa')
#     return edad


# try:
#     print(validar_edad(25))
#     print(validar_edad(-5))
# except ValueError as e:
#     print(f'Error: {e}')

"""
Escribe una función llamada obtener_elemento(lista, indice)
que intente acceder a un elemento de la lista en
el indice proporcionado. 
Utiliza un bloque try-except para manejar la 
excepción IndexError que ocurre si el índice 
está fuera del rango de la lista. 
Si el índice es inválido, 
la función debe imprimir un mensaje de error y
retornar None.
"""
def obtener_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print("Error con el indice proporcionado")
        return None
 
lista = [1, 2, 3, 4, 5]
indice = int(input("Proporciona un indice para ver cual elemento esta en el mismo: "))
print(f"El elemento es: {obtener_elemento(lista ,indice)}")

