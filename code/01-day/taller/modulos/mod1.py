#!/usr/bin/env python3
 
__suma__ = 0
__resta__ = 0

def __sumar(lista):
    global __suma__
    for i in lista:
        __suma__ += i
    return __suma__
 
def __restar(lista):
    global __resta__
    for i in lista:
        __resta__ -= i
    return __resta__
 
 
if __name__ == "__main__":
    print("probando funciones")
    print(__sumar([1,2,3]))
    print(__restar([1,2,3]))
