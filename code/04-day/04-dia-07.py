# POO: Herencia

# Ej.1
# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#
#
# sun = Star('Sol', 'Vía láctea')
# print(sun)

# Ej.2
# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#
#     def __str__(self):
#         return self.name + ' en ' + self.galaxy
#
#
# # main
# sun = Star('Sol', 'Vía láctea')
# print(sun)

# class Vehicle:
#     pass
#
# class LandVehicle(Vehicle):
#     pass
#
# class TrackedVehicle(LandVehicle):
#     pass

# Ej.4
# print(issubclass(LandVehicle, Vehicle))
# print(issubclass(Vehicle, TrackedVehicle))
# print()
# print(issubclass(TrackedVehicle, LandVehicle))
# print(issubclass(TrackedVehicle, Vehicle))

# Ej.5
# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end="\t")
#     print()

# Ej.6
# obj1 = LandVehicle()
# obj2 = Vehicle()
#
# print(isinstance(obj1, LandVehicle))
# print(isinstance(obj1, Vehicle))
# print()
# print(isinstance(obj2, TrackedVehicle))


# Ej.8
# class SampleClass:
#     def __init__(self, val):
#         self.val = val
#
#
# object_1 = SampleClass(1)
# object_2 = SampleClass(2)
# object_3 = object_1
# object_3.val += 1
#
# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val, object_2.val, object_3.val)
# print()
#
# string1 = 'Mary tenía un '
# string2 = 'Mary tenía un corderito'
# string1 += 'corderito'
#
# print(string1 == string2, string1 is string2)

# Ej.9
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Mi nombre es ' + self.name + '.'


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


# main
obj = Sub('Andy')
print()
print(obj)








