""" /*
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
 */
 """
import random as random
import time as time
import os

class Heroe:
    def __init__(self, nombre:str, vida: int, daño_max: int, evasion: int, ataques: list) -> None:
        self.nombre = nombre
        self.vida = vida
        self.daño = daño_max
        self.regeneracion = 1
        self.evasion = evasion
        self.ataques = ataques
        
    def ataque(self):
        ataque = random.randint(10, self.daño)
        return ataque

    def evadir(self):
        evasion = random.randint(1, self.evasion)
        return evasion
    
class Jugador:
    def __init__(self, nombre: str, personaje: Heroe) -> None:
        self.nombre = nombre
        self.personaje = personaje

def turno_ataque(atacante: Heroe, defensa: Heroe):
    daño = atacante.ataque()
    if defensa.evadir() == 1:
        print(f"{atacante.nombre} ataca pero {defensa.nombre} logra evadir el golpe!")
        return
    elif atacante.daño == daño:
        defensa.vida = defensa.vida - daño
        atacante.regeneracion = 0
        print(f"{atacante.nombre} acerto un golpe critico por {daño} puntos!\n{defensa.nombre} pierde el proximo turno para regenerarse")
        return
    else:
        defensa.vida = defensa.vida - daño
        print(f"{atacante.nombre} {random.choice(atacante.ataques)} generando un daño de {daño} puntos!")
        return
    
def turnos(primero: Jugador, segundo: Jugador):
    aux = 1
    while primero.personaje.vida > 0 and segundo.personaje.vida > 0:
        os.system("cls")
        print(f"{primero.personaje.nombre}: {primero.personaje.vida} ♥♥♥    |   {segundo.personaje.nombre}: {segundo.personaje.vida} ♥♥♥\n\n")
        if aux == 1:
            print(f"{primero.nombre}! es su turno:")
            turno_ataque(primero.personaje, segundo.personaje)
            time.sleep(3)
            if segundo.personaje.regeneracion == 0:
                aux = 1
                segundo.personaje.regeneracion = 1
            else:
                aux = 2
        elif aux == 2:
            print(f"{segundo.nombre}! es su turno:")
            turno_ataque(segundo.personaje, primero.personaje)   
            time.sleep(3)
            if primero.personaje.regeneracion == 0:
                aux = 2
                primero.personaje.regeneracion = 1
            else:
                aux = 1
    os.system("cls")
    if primero.personaje.vida < 0:
        print(f"{segundo.nombre} es el ganador!")
    else:
        print(f"{primero.nombre} es el ganador!")
    
wolverine = Heroe("Wolverine",300, 120, 5, ["le corta la cara", "lo apuñala con sus garras", "lo patea en el estomago", "lo quema con su cigarrillo"])
deadpool = Heroe("Deadpool", 350, 100, 4, ["le corta un pedazo con su espada", "le mete 10 tiros en la cabeza", "acierta una patada voladora", "lo golpea en las bolas"])

seleccion = True
while seleccion == True:
    j1 = int(input("Jugador 1 seleccione su personaje:\n1)Wolverine\n2)Deadpool\n\n"))
    if j1 == 1:
        j1 = Jugador("Jugador 1", wolverine)
        j2 = Jugador("Jugador 2", deadpool)
        seleccion = False
    elif j1 == 2:
        j1 = Jugador("Jugador 2", deadpool)
        j2 = Jugador("Jugador 1", wolverine)
        seleccion = False
    else:
        print("Opcion incorrecta")
primero = random.randint(1,2)
if primero == 1:
    turnos(j1, j2)
else:
    turnos(j2, j1)
