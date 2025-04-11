# Generadores

# Ej.2
class Fib:
    def __init__(self, nn):
        print('__init__')
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1
    
    def __iter__(self):
        print('__iter__')
        return self
    
    def __next__(self):
        print('__next__')
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)


# Ej.3
class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print('Fib iter')
        return self
    
    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret
    

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)
    
    def __iter__(self):
        print("Class iter")
        return self.__iter


object = Class(8)

for i in object:
    print(i)

print()

object2 = Fib(8)

for i in object2:
    print(i)


" Ej.4"
def fun(n):
    for i in range(n):
        return i

" Ej.5"
def fun(n):
    for i in range(n):
        yield i

" Ej.6"
def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)