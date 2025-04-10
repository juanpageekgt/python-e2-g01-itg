print('Ej.12')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print('f' in alphabet)
print('F' in alphabet)
print('1' in alphabet)
print('ghi' in alphabet)
print('Xyz' in alphabet)

print()

print('Ej.13')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print('f' not in alphabet)
print('F' not in alphabet)
print('1' not in alphabet)
print('ghi' not in alphabet)
print('Xyz' not in alphabet)

print()

print('Ej.14')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# inmutabilidad
# alphabet.append('A')

# alphabet.insert(0, 'A')

print()

print('Ej.17')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabet = 'a' + alphabet
alphabet = alphabet + 'z'

print(alphabet)

print()

print('Ej.18')

print(min('aAbByYzZ'))
print(max('aAbByYzZ'))

print('Ej.19')

t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

print()

print('Ej.20')

t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

print()

print('Ej.21')
print('aAbByYzZaA'.index('b'))
print('aAbByYzZaA'.index('Z'))
print('aAbByYzZaA'.index('A'))

print()

print('Ej.22')

print(list('abcabc'))

print()

print('Ej.23')

print('abcabc'.count('b'))
print('abcabc'.count('d'))
