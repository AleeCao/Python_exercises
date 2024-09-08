""" /*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */ """
 
def contador_inverso (max: int):
   if max >= 0:
       print(max)
       contador_inverso(max - 1)
   else:
       return
   
def factorial (n: int):
    if n > 0:
        n = n * factorial (n - 1)
        return n
    elif n == 0:
        n = 1
        return n
    
def fibonacci (index: int):
    if index > 1:
        n = fibonacci(index-1) + fibonacci(index-2)
        return n
    elif index == 1:
        return 1
    elif index == 0:
        return 0
        
    
    
contador_inverso(100)

print(factorial(7))

print(fibonacci(10))