# Cadenas breve repaso

print('Ej.1')

word = 'by'
print(len(word))

print()

print('Ej.2')

empty = ''
print(len(empty))

print()

print('Ej.3')

i_am = 'I\'m'
print(len(i_am))

print()

print('Ej.4')

# multiline = 'linea #1
# linea #2'
# print(len(multiline))

print()

print('Ej.5')

multiline = '''Linea #1
Linea #2'''  #Docstring
print(len(multiline))
print(multiline)

print()

print('Ej.6')

multiline = """Linea #1
Linea #2
Linea #3 """  #Docstring
print(len(multiline))
print(multiline)

print()

print('Ej.7')
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('hola' * 3)

print()

print('Ej.8')

char_1 = 'a'
char_2 = 'b'

print(ord(char_1))
print(ord(char_2))

print()

print('Ej.9')

print(chr(97))
# print(chr(945))

print()

print('Ej.10')

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()
print()

print('Ej.11')

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

print('Ej.11')

alpha = 'abdefg'

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:-4])
print(alpha[::2])
print(alpha[1::2])
