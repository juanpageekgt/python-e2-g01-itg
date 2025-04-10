#!/usr/bin/env python3
 
def mult(lista):
    mul = 1
    for i in lista:
        mul *= i
    return mul
 
 
def divi(lista):
    div = lista[0]
    del lista[0]
    for i in lista:
        if i != 0:
            div /= i
        else:
            print("No se permite divitir entre cero")
            break
    return div
 
 
if __name__ == "__main__":
    print("probando funciones")
    print(mult([1,2,3]))
    print(divi([4,0]))