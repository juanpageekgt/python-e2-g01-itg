#!/usr/bin/env python3

__counter = 0

def sum1(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prod1(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == '__main__':
    print('Prefiero ser un módulo, pero puedo hacer algunas pruebas para usted.')
    my_list = [i+1 for i in range(5)]    
    print(sum1(my_list))
    print(prod1(my_list))
    
