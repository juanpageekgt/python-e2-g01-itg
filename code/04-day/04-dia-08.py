# Ej.10
# class Super:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Mi nombre es ' + self.name + '.'
#
#
# class Sub(Super):
#     def __init__(self, name):
#         super().__init__(name)
#
#
# # main
# obj = Sub('Andy')
# print(obj)

# Ej.11
# class Super:
#     supVar = 1
#
#
# class Sub(Super):
#     subVar = 2
#
#
# # main
# obj = Sub()
#
# print(obj.supVar)
# print(obj.subVar)


# Ej.12
# class Super:
#     def __init__(self):
#         self.supVar = 11
#
#
# class Sub(Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar = 12
#
# # main
# obj = Sub()
#
# print(obj.subVar)
# print(obj.supVar)

# Ej.13
# class Level1:
#     variable_1 = 100
#     def __init__(self):
#         self.var_1 = 101
#
#     def fun_1(self):
#         return 102
#
#
# class Level2(Level1):
#     variable_2 = 200
#     def __init__(self):
#         super().__init__()
#         self.var_2 = 201
#
#     def fun_2(self):
#         return 202
#
#
# class Level3(Level2):
#     variable_3 = 300
#     def __init__(self):
#         super().__init__()
#         self.var_3 = 301
#
#     def fun_3(self):
#         return 302
#
# # main
# obj = Level3()
#
# print(obj.variable_1, obj.var_1, obj.fun_1())
# print(obj.variable_2, obj.var_2, obj.fun_2())
# print(obj.variable_3, obj.var_3, obj.fun_3())

# Ej.14
# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11
#
# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21
#
#
# class Sub(SuperA, SuperB):
#     pass
#
# obj = Sub()
#
# print(obj.var_a, obj.fun_a())
# print(obj.var_b, obj.fun_b())

# Ej.15
# class Level1:
#     var = 100
#     def fun(self):
#         return 101
#
# class Level2(Level1):
#     var = 200
#     def fun(self):
#         return 201
#
# class Level3(Level2):
#     pass
#
# # main
# obj = Level3()
# print(obj.var, obj.fun())  # 200 201


# Ej.16
# class Left:
#     var = 'L'
#     var_left = 'LL'
#     def fun(self):
#         return 'Left'
#
# class Right:
#     var = 'R'
#     var_right = 'RR'
#     def fun(self):
#         return 'Right'
#
#
# class Sub(Right, Left):
#     pass
#
# # main
# obj = Sub()
# print(obj.var, obj.var_left, obj.var_right, obj.fun())












