""" /*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */ """
 
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
        
    def sound(self):
        pass
    
class Perro(Animal):
    def sound(self):
        print(f"{self.name}: Guau!")
        
class Gato(Animal):
    def sound(self):
        print(f"{self.name}: Miau!")
        
gato1 = Gato("Áster")
gato2 = Gato("Júpiter")
perro1 = Perro("Simba")

gato1.sound()
gato2.sound()
perro1.sound()


class Empleados:
    def __init__(self, name: str, id: int) -> None:
        self.name = name
        self.id = id
        
class Manager(Empleados):
    
    
class ProjectManager(Empleados):
    
    
class Programmer(Empleados):