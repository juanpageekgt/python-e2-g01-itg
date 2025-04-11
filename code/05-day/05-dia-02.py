# Resumen

"""
Herencia
En programación orientada a objetos (POO), 
herencia es un mecanismo mediante el cual una clase 
(llamada clase hija o subclase) puede heredar atributos
y métodos de otra clase (llamada clase padre o superclase). 
Esto permite crear una nueva clase basada en una existente, 
reutilizando y extendiendo su funcionalidad.
"""

"""
Polimorfismo
El polimorfismo es la capacidad de diferentes clases para 
ser tratadas como instancias de la misma clase a través de 
una interfaz común. En otras palabras, diferentes objetos pueden 
responder a la misma acción (método) de diferentes maneras. 
El polimorfismo se logra principalmente mediante la herencia y 
la sobrescritura de métodos.
"""

"""
Encapsulamiento
Es el principio de agrupar datos (atributos) y métodos 
que operan sobre esos datos en una sola unidad o clase, 
y restringir el acceso directo a algunos de los componentes 
del objeto, lo que significa que solo se puede acceder a los 
datos a través de métodos públicos definidos (getters y setters).
"""

"""
Abstracción
Es el proceso de ocultar los detalles de implementación y 
mostrar solo la funcionalidad al usuario. En POO, la abstracción se 
logra mediante el uso de clases abstractas e interfaces.
"""

# Herencia
# Clase base o superclase / Padre
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass


# clase derivada o subclase / hijas
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# uso de la herencia
dog = Dog("Buddy")
cat = Cat('Whiskers')

print(dog.speak()) # utilizando el método
print(cat.speak()) # utilizando el método
print()


# Polimorfismo
# función polimórfica
def animal_sound(animal):
    print(animal.speak())

# Llamada a la función con diferentes tipos de objetos
animal_sound(dog)
animal_sound(cat)
print()


# Encapsulamiento
class Person:
    def __init__(self, name, age):
        self._name = name # Atributo protegido
        self.__age = age # Atributo privado
    
    # Método getter
    def get_age(self):
        return self.__age
    
    # Método setter
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError('La edad debe ser positiva')


# main
person = Person('Alica', 30)

print(person.get_age())
person.set_age(35)
print(person.get_age())


# Abstracción
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


# main
Rectangle = Rectangle(10, 5)
print(Rectangle.area())
