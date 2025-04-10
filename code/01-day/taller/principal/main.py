from sys import path
path.append("..\\modulos")
 
 
from mod1 import sumar as sum, restar as res
from mod2 import divi as div, mult as mul
 
 
control = 1
while control == 1:
    print("\n\nPor favor escoja la operación matématica:")
    print("  1 - sumar")
    print("  2 - restar")
    print("  3 - multiplicar")
    print("  4 - dividir")
    print("  5 - salir")
    op = input("")
    li = []
 
    if (op == "1"):
        con = 1
        while con == 1:
            txt = input("escriba entero o fin para salir: ")
            if (txt == "fin"):
                break
            else:
                li.append(int(txt))
        print("La suma es:",sum(li))
    elif(op == "2"):
        con = 1
        while con == 1:
            txt = input("escriba entero o fin para salir: ")
            if (txt == "fin"):
                break
            else:
                li.append(int(txt))
        print("La resta es:",res(li))
    elif(op == "3"):
        con = 1
        while con == 1:
            txt = input("escriba entero o fin para salir: ")
            if (txt == "fin"):
                break
            else:
                li.append(int(txt))
        print("La multiplicación es:",mul(li))
    elif(op == "4"):
        con = 1
        while con == 1:
            txt = input("escriba entero o fin para salir: ")
            if (txt == "fin"):
                break
            else:
                li.append(int(txt))
        print("La division es:",div(li))
    elif(op == "5"):
        print("Gracias por utilizar la aplicación.")
        break