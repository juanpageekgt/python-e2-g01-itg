# Cifrado César
# text = input("Ingresa tu mensaje: ")  # Ingresa tu Criptograma
# cipher = ''

# for char in text:
#     if not char.isalpha(): # verifica si el caracter es alfabetico
#         continue
#     char = char.upper() # convierte a mayúsculas
#     code = ord(char) + 1
#     if code > ord('Z'):
#         code = ord('A')
#     cipher += chr(code)

# print(cipher)

# print()

# text = input("Ingresa mensaje a decifrar: ")
# cipher = ''
 
# for char in text:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) - 1
#     if code > ord('Z'):
#         code = ord('A')
#     cipher += chr(code)
   
# print(cipher)

print()

# Procesador de Números
# line = input('Ingresa una linea de numeros, separalos con espacio: ')
# strings = line.split()  # separa la cadena en una lista
# total = 0

# try:
#     for substr in strings:
#         total += float(substr)
#     print('El total es:', total)
# except:
#     print(substr, 'No es un numero.')


print()

# Validador IBAN.
iban = input('Ingresa un IBAN, por favor: ')
iban = iban.replace(' ','')

if not iban.isalnum(): # verifica todos los caracteres sean alfanumericos
    print('Has introducido caracteres no validos.')
elif len(iban) < 15:
    print('El IBAN ingresado es demasiado corto.')
elif len(iban) > 31:
    print('El IBAN ingresado es demasiado largo.')
else:
    iban = (iban[4:] + iban[0:4].upper())
    iban2 = ''
    for ch in iban:
        if ch.isdigit(): # verifica si el caracter es un digito
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    
    if iban % 97 == 1:
        print('El IBAN ingresado es valido.')
    else:
        print('El IBAN ingresado no es valido.')
