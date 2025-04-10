# Variables de instancia

# Ej.1
class ExampleClass:

    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object1 = ExampleClass()

example_object2 = ExampleClass(2)
example_object2.set_second(3)

example_object3 = ExampleClass(4)
example_object3.set_second(5)
example_object3.third = 6

print(example_object1.__dict__)
print(example_object2.__dict__)
print(example_object3.__dict__)