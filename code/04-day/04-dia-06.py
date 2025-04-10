# POO: Métodos

# Ej.1 - metodo a detalle
# class Classy:
#     def method(self):
#         print('método')
#
# obj = Classy()
# obj.method()

# Ej.2
# class Classy:
#     def method(self, par):
#         print('método', par)
#
# obj = Classy()
# obj.method(1)
# obj.method(2)
# obj.method(3)

# Ej.3
# class Classy:
#     varia = 2
#     def method(self):
#         print(self.varia, self.var)
#
#
# # main
# obj = Classy()
# obj.var = 3
# obj.method()

# Ej.4
# class Classy:
#     def other(self):
#         print('otro')
#
#     def method(self):
#         print('método')
#         self.other()
#
#
# # main
# obj = Classy()
# obj.method()


# Ej.5
# class Classy:
#     def __init__(self, value):
#         self.var = value
#
# # main
# obj_1 = Classy('objeto')
# print(obj_1.var)

# Ej.6
# class Classy:
#     def __init__(self, value = None):
#         self.var = value
#
# # main
# obj_1 = Classy('objeto')
# obj_2 = Classy()
#
# print(obj_1.var)
# print(obj_2.var)


# Ej.7
# class Classy:
#     def visible(self):
#         print('visible')
#
#     def __hidden(self):
#         print('oculto')
#
# # main
# obj = Classy()
# obj.visible()
#
# try:
#     obj.__hidden()
# except:
#     print('fallido')
#
# print()
# obj._Classy__hidden()

# Ej.8
# class Classy:
#     varia = 1
#     def __init__(self):
#         self.var = 2
#
#     def method(self):
#         pass
#
#     def __hidden(self):
#         pass
#
# # main
# obj = Classy()
#
# print(obj.__dict__)
# print()
# print(Classy.__dict__)


# Ej.9
# class Classy:
#     pass
#
# # main
# print(Classy.__name__)
# print()
# obj = Classy()
# print(type(obj).__name__)
# print()
# obj2 = Classy()
# print(type(obj2).__name__)
# print()
# print(obj.__name__)

# Ej.10
# class Classy:
#     pass
#
# # main
# print(Classy.__module__)
# obj = Classy()
# print(obj.__module__)

# Ej.11
# class SuperOne:
#     pass
#
# class SuperTwo:
#     pass
#
# class Sub(SuperOne, SuperTwo):
#     pass
#
# # main
# def printBases(cls):
#     print('(', end='')
#
#     for x in cls.__bases__:
#         print(x.__name__, end=' ')
#     print(')')
#
#
# printBases(SuperOne)
# printBases(SuperTwo)
# printBases(Sub)

# Ej.12
class MyClass:
    pass


# main
obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incInstI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incInstI(obj)
print(obj.__dict__)
