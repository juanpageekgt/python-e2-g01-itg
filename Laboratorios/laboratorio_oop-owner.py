# Laboratorio de Programación Orientada a Objetos en Python

# Tema 1: Clases y Métodos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        mensaje = "mayor de edad" if self.edad >= 18 else "menor de edad"
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años. Suy {mensaje}"

# Tema 2: Propiedades y Métodos Privados
class CuentaBancaria:
    def __init__(self, titular, saldo, contrasena):
        if saldo < 0:
            raise ValueError('El saldo inicial no puede ser negativo.')
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo  # Atributo privado
        self.__contrasena = contrasena # Atributo privado

    def depositar(self, monto):
        self.__saldo += monto

    def consultar_saldo(self, contrasena):
        if contrasena == self.__contrasena:
            return f"Saldo actual: {self.__saldo}"
        else:
            return f"Password incorrecto. No se puede consultar el saldo."

# Tema 3: Constructores
# Ya manejamos constructores con el método __init__

# Tema 4: Variables de Instancia y de Clase
class Animal:
    especie = "Mamífero"  # Variable de clase

    def __init__(self, nombre):
        self.nombre = nombre  # Variable de instancia

# Tema 5: Introspección y Reflexión
def introspeccion(obj):
    atributos = dir(obj)
    return f"Atributos y métodos: {atributos}"

# Tema 6: Herencia (Simple y Múltiple)
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def especificaciones(self):
        return f"Marca: {self.marca}"

class Motor:
    def tipo_motor(self):
        return "Motor eléctrico"

class Coche(Vehiculo, Motor):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

# Tema 7: Jerarquía de Clases
class Figura:
    def area(self):
        raise NotImplementedError("Este método debe ser implementado en una subclase.")

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# Tema 8: Polimorfismo
class Perro:
    def hacer_sonido(self):
        return "Guau"

class Gato:
    def hacer_sonido(self):
        return "Miau"

def sonido_animal(animal):
    return animal.hacer_sonido()

# Tema 9: Encapsulamiento
# Ya explorado en tema 2

# Tema 10: Abstracción
from abc import ABC, abstractmethod

class Instrumento(ABC):
    @abstractmethod
    def tocar(self):
        pass

class Guitarra(Instrumento):
    def tocar(self):
        return "Tocando la guitarra"

# Uso de try y except
def operacion_segura():
    try:
        numero = int(input("Ingresa un número: "))
        resultado = 10 / numero
        return f"Resultado: {resultado}"
    except ValueError:
        return "Error: Debes ingresar un número válido."
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."

# Programa principal
if __name__ == "__main__":
    # Clases y métodos
    persona = Persona("Juan", 25)
    print(persona.saludar())

    # Propiedades y métodos privados
    cuenta = CuentaBancaria("Ana", 1000)
    cuenta.depositar(500)
    print(cuenta.consultar_saldo())

    # Introspección
    print(introspeccion(persona))

    # Herencia
    coche = Coche("Tesla", "Model S")
    print(coche.especificaciones())
    print(coche.tipo_motor())

    # Jerarquía de clases
    cuadrado = Cuadrado(4)
    print(f"Área del cuadrado: {cuadrado.area()}")

    # Polimorfismo
    perro = Perro()
    gato = Gato()
    print(sonido_animal(perro))
    print(sonido_animal(gato))

    # Abstracción
    guitarra = Guitarra()
    print(guitarra.tocar())

    # Manejo de excepciones
    print(operacion_segura())
    