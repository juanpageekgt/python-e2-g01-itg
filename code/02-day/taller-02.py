# Ej.1 - Contar vocales
"""
Escribe una función que tome una cadena como entrada y
devuelva el número total de vocales (a, e, i, o, u) 
presentes en la cadena.
"""
# Calcula cuantas vocales tiene la frase recibida
# def cuantas_vocales(cadena):
#     vocales = 0
#     for vocal in cadena:
#         if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal == 'o' or vocal == 'u':
#             vocales += 1  
#     return vocales
 
# # User input, se convierte la frase en minuscula todo
# cadena = input("Ingrese una oracion: ").lower()
# #Llamar función para saber cuantas vocales tiene
# vocales = cuantas_vocales(cadena)
       
# print("La cantidad de vocales en la frase ingresada es:", vocales)
 
 # Ej.2 - Palíndromo
"""
Escribe una función que tome una cadena como entrada y 
determine si es un palíndromo 
(se lee igual de izquierda a derecha y
de derecha a izquierda). Ej. oso, tenet
"""
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "") #Convertir a minusculas y eliminar espacios
    return cadena == cadena[::-1]

texto1 = "Anita lava la tina"
texto2 = "Hola mundo"
print(f"'{texto1}' es palindromo: {es_palindromo(texto1)}")
print(f"'{texto2}' es palindromo: {es_palindromo(texto2)}")

