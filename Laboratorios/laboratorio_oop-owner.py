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

    def __calcular_cargo(self):
        return self.__saldo * 0.01
    
    def depositar(self, monto):
        self.__saldo += monto

    def consultar_saldo(self, contrasena):
        if contrasena == self.__contrasena:
            cargo = self.__calcular_cargo()
            saldo_final = self.__saldo + cargo
            return f"Saldo actual: {saldo_final}"
        else:
            return f"Password incorrecto. No se puede consultar el saldo."

# Tema 3: Constructores
# Ya manejamos constructores con el método __init__

# Tema 4: Variables de Instancia y de Clase
class Animal:
    especie = "Mamífero"  # Variable de clase

    def __init__(self, nombre, color):
        self.nombre = nombre  # Variable de instancia
        self.color = color  # Variable de instancia
    
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        return f"El color del animal ha sido cambiado a {self.color}"

# Tema 5: Introspección y Reflexión
def introspeccion(obj):
    atributos = dir(obj)
    detalles = {atributo: type(getattr(obj, atributo)).__name__ for atributo in atributos if hasattr(obj, atributo)}
    return f"Atributos y métodos: {detalles}"

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

class Moto(Vehiculo):
    def __init__(self, marca, tiene_sidecar):
        super().__init__(marca)
        self.tiene_sidecar = tiene_sidecar
    
    def especificaciones(self):
        sidecar = "con sidecar" if self.tiene_sidecar else "sin sidecar"
        return f"Marca: {self.marca}, {sidecar}"

# Tema 7: Jerarquía de Clases
class Figura:
    def area(self):
        raise NotImplementedError("Este método debe ser implementado en una subclase.")

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        import math
        return math.pi * (self.radio ** 2)

# Tema 8: Polimorfismo
class Perro:
    def hacer_sonido(self):
        return "Guau"

class Gato:
    def hacer_sonido(self):
        return "Miau"

class Vaca:
    def hacer_sonido(self):
        return "Muu"

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

class Trompeta(Instrumento):
    def tocar(self):
        return "Tocando la trompeta"

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
    cuenta = CuentaBancaria("Ana", 1000, "contrasena123")
    cuenta.depositar(500)
    print(cuenta.consultar_saldo("contrasena123"))

    # Introspección
    print(introspeccion(persona))

    # Herencia
    coche = Coche("Tesla", "Model S")
    print(coche.especificaciones())
    print(coche.tipo_motor())
    moto = Moto("Harley", True)
    print(moto.especificaciones())

    # Jerarquía de clases
    cuadrado = Cuadrado(4)
    print(f"Área del cuadrado: {cuadrado.area()}")
    circulo = Circulo(3)
    print(f"Area del circulo: {circulo.area()}")

    # Polimorfismo
    perro = Perro()
    gato = Gato()
    vaca = Vaca()
    print(sonido_animal(perro))
    print(sonido_animal(gato))
    print(sonido_animal(vaca))

    # Abstracción
    guitarra = Guitarra()
    print(guitarra.tocar())
    trompeta = Trompeta()
    print(trompeta.tocar())

    # Manejo de excepciones
    print(operacion_segura())