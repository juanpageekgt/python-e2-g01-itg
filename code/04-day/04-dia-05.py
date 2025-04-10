# Variables de clase

# Ej.1 y 2 es volver privada
# class ExampleClass:
#
#     __counter = 0
#
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.__counter += 1
#
#
# example_object_1 = ExampleClass()
# print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
#
# example_object_2 = ExampleClass(2)
# print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
#
# example_object_3 = ExampleClass(4)
# print(example_object_3.__dict__, example_object_3._ExampleClass__counter)


# Ej.3
# class ExampleClass:
#
#     varia = 1
#
#     def __init__(self, val):
#         ExampleClass.varia = val
#
#
# # main
# print(ExampleClass.__dict__)
# print()
#
# example_object = ExampleClass(2)
#
# print(ExampleClass.__dict__)
# print(example_object.__dict__)


# Ej.4
# class ExampleClass:
#
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# example_object = ExampleClass(1)
#
# print(example_object.a)
# print(example_object.b)


# Ej.5
# class ExampleClass:
#
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# example_object = ExampleClass(1)
#
# print(example_object.a)
#
# try:
#     print(example_object.b)
# except AttributeError:
#     pass

# Ej.6
# class ExampleClass:
#
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# example_object = ExampleClass(2)
# # print(example_object.a)
# print()
#
# if hasattr(example_object, 'b'):
#     print(example_object.b)

# Ej.7
# class ExampleClass:
#     attr = 1
#
#
# print(hasattr(ExampleClass, 'attr'))
# print(hasattr(ExampleClass, 'prop'))

# Ej.8
class ExampleClass:

    a = 1

    def __init__(self):
        self.b = 2


# main
example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'a'))
print(hasattr(ExampleClass, 'b'))
