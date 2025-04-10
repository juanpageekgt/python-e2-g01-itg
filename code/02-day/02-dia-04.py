print('Ej.1')

print('aBcD'.capitalize())
print('ALPHA'.capitalize())
print(' ALPHA'.capitalize())
print('123'.capitalize())
print('αβγδ'.capitalize())

print()

print('Ej.2')

print('[' + 'alpha'.center(10) + ']')

print()

print('Ej.3')

print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

print()

print('Ej.4')

print('[' + 'gamma'.center(20, '*') + ']')

print()

print('Ej.5')

if 'epsilon'.endswith('on'):
    print('si')
else:
    print('no')

print()

print('Ej.7')

t = 'zeta'
print(t.endswith('a'))
print(t.endswith('A'))
print(t.endswith('et'))
print(t.endswith('eta'))

print()

print('Ej.8')

print('Eta'.find('ta'))
print('Eta'.find('mma'))

print('Ej.9')

print('kappa'.find('a', 2))

print()

print('Ej.10')

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')

while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

print()

print('Ej.12')

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

print()

print('Ej.13')

print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

print()

print('Ej.14')
t = 'Six lambdas'
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

print()

print('Ej.15')

print('Moooo'.isalpha())
print('Mu40'.isalpha())

print()

print('Ej.16')

print('2018'.isdigit())
print('Year2025'.isdigit())

print()

print('Ej.17')

print('Moooo'.islower())
print('moooo'.islower())

print()

print('Ej.18')

print(' \n'.isspace())
print(' '.isspace())
print('mooo mooo mooo'.isspace())

print()

print('Ej.19')

print('Moooo'.isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

print()

print('Ej.20')

print(','.join(['omicron', 'pi', 'rho']))

print()

print('Ej.21')

print('SiGmA=60'.lower())

print()

print('Ej.22')

print('[' + ' tau '.lstrip() + ']')

print()

print('Ej.23')

print('www.cisco.com'.lstrip('w.'))

print()

print('Ej.24')

print('pythoninstitute.org'.lstrip('.org'))

print()

print('Ej.25')

print('www.netacad.com'.replace('netacad.com', 'pythoninstitute.org'))
print('this is it!'.replace('is', 'are'))

print()

print('Ej.26')

print('This is it!'.replace('is', 'are', 1))
print('This is it!'.replace('is', 'are', 2))

print()

print('Ej.27')

print('tau tau tau'.rfind('ta'))
print('tau tau tau'.rfind('ta', 9))
print('tau tau tau'.rfind('ta', 3, 9))

print()

print('Ej.28')

print('[' + 'upsilon '.rstrip() + ']')
print('cisco.com'.rstrip('.com'))

print()

print('Ej.29')

print('phi       chi\npsi'.split())

print()

print('Ej.30')

print('omega'.startswith('meg'))
print('omega'.startswith('om'))

print()

print('Ej.31')

print('[' + '   aleph    '.strip() + ']')

print()

print('Ej.32')

print('Yo solo se que no se nada'.swapcase())

print()

print('Ej.33')

print('Yo solo se que no se nada. Parte 1.'.title())

print()

print('Ej.34')

print('Yo solo se que no se nada. Parte 2.'.upper())

print()