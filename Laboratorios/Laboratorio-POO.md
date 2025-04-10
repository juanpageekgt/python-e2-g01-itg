# Guía del Laboratorio: Programación Orientada a Objetos en Python

## Introducción
Bienvenido al laboratorio de Programación Orientada a Objetos (POO). En este laboratorio, aprenderás los conceptos fundamentales de POO en Python mediante el análisis, modificación y mejora del código proporcionado. A lo largo de esta guía, explorarás temas como clases, métodos, encapsulamiento, herencia, polimorfismo, excepciones y más.

### Objetivos
- Comprender los conceptos básicos de POO.
- Analizar y modificar código existente para reforzar los conceptos.
- Aplicar conceptos avanzados como introspección, reflexión, abstracción y jerarquías de clases.
- Manejar errores utilizando `try` y `except`.

---

## Requisitos Previos
1. Conocimientos básicos de Python (variables, funciones y estructuras de control).
2. Instalación de Python >= 3.6 en tu computadora.
3. Un editor de texto o entorno de desarrollo (recomendado: Visual Studio Code, PyCharm o Jupyter Notebook).

---

## Guía Paso a Paso

### Tema 1: Clases y Métodos
1. Abre el archivo `laboratorio_oop.py` y revisa la clase `Persona` y su método `saludar`.
2. **Tarea**: Modifica el método `saludar` para incluir un mensaje adicional que indique si la persona es mayor o menor de edad según su atributo `edad`.

---

### Tema 2: Propiedades y Métodos Privados
1. Revisa la clase `CuentaBancaria` y observa cómo se utilizan los atributos privados (`__titular` y `__saldo`).
2. **Tarea**: Modifica el método `consultar_saldo` para que solo permita consultar el saldo si una contraseña proporcionada como argumento coincide con una contraseña almacenada en la cuenta (puedes agregar un atributo privado `__contraseña`).

---

### Tema 3: Constructores
1. Observa cómo el método `__init__` se utiliza para inicializar las instancias en las clases `Persona` y `CuentaBancaria`.
2. **Tarea**: Agrega validaciones al constructor `__init__` de la clase `CuentaBancaria` para asegurarte de que el saldo inicial no pueda ser negativo.

---

### Tema 4: Variables de Instancia y de Clase
1. Examina la clase `Animal` y nota cómo se utilizan las variables de instancia y de clase.
2. **Tarea**: Modifica la clase `Animal` para incluir un atributo de instancia que registre el color del animal y un método que permita modificar ese color.

---

### Tema 5: Introspección y Reflexión
1. Revisa la función `introspeccion` y observa cómo utiliza `dir` para analizar un objeto.
2. **Tarea**: Amplía la función `introspeccion` para que también muestre los tipos de cada atributo o método del objeto inspeccionado.

---

### Tema 6: Herencia (Simple y Múltiple)
1. Revisa cómo la clase `Coche` implementa herencia múltiple al combinar las clases `Vehiculo` y `Motor`.
2. **Tarea**: Agrega una nueva clase `Moto` que herede de `Vehiculo` y que implemente un método que indique si tiene o no tiene sidecar.

---

### Tema 7: Jerarquía de Clases
1. Observa la jerarquía en la que `Figura` es una clase base y `Cuadrado` hereda de ella.
2. **Tarea**: Agrega una nueva subclase `Circulo` que implemente el método `area` utilizando el radio como atributo.

---

### Tema 8: Polimorfismo
1. Revisa cómo la función `sonido_animal` utiliza el polimorfismo para trabajar con objetos de distintas clases (`Perro` y `Gato`).
2. **Tarea**: Agrega una nueva clase `Vaca` con el método `hacer_sonido`. Luego, prueba el polimorfismo con una lista que contenga objetos de las clases `Perro`, `Gato` y `Vaca`.

---

### Tema 9: Encapsulamiento
1. Observa cómo los atributos privados se utilizan para encapsular datos en la clase `CuentaBancaria`.
2. **Tarea**: Agrega un método privado que calcule un cargo por uso (por ejemplo, 1% del saldo) y utilízalo en el método `consultar_saldo`.

---

### Tema 10: Abstracción
1. Revisa cómo la clase abstracta `Instrumento` utiliza el módulo `abc` para definir métodos obligatorios.
2. **Tarea**: Agrega una nueva clase `Trompeta` que herede de `Instrumento` y que implemente el método `tocar`.

---

### Manejo de Excepciones
1. Revisa la función `operacion_segura` y observa cómo se manejan las excepciones con `try` y `except`.
2. **Tarea**: Amplía la función para que vuelva a solicitar un número al usuario si se produce un error, en lugar de terminar con un mensaje de error.

---

## Entregables
1. El archivo `laboratorio_oop.py` con todas las modificaciones realizadas.
2. Agrega comentarios en tu código explicando cada cambio realizado.
3. Proporciona ejemplos de entrada y salida para cada tarea que realices.

---

## Evaluación
- **Análisis del Código (30%)**: Se evaluará si el estudiante comprende el código proporcionado.
- **Modificaciones Realizadas (40%)**: Se evaluará si los cambios son correctos y funcionales.
- **Documentación y Comentarios (30%)**: Se evaluará que el código esté bien documentado y sea fácil de entender.

---

¡Buena suerte y disfruta aprendiendo POO en Python!