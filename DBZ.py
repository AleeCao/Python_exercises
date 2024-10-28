""" /*
 * EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud.
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores.
 * - El luchador con más velocidad comienza atacando.
 * - El daño se calcula restando el daño de ataque del
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque.
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque.
 * - Después de cada turno y ataque, el oponente pierde salud.
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2.
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador.
 */ """
 
import os
import random

class Fighter:
    def __init__(self, name: str, power: int, defense: int, speed: int) -> None:
        self.name = name
        self.power = power
        self.life = 100
        self.defense = defense
        self.speed = speed
        
    def attack(self, pj2: "Fighter"):
        if random.random() < 0.2:
            print(f"{pj2.name} dodged the attack!")
        else:
            if self.power <= pj2.defense:
                pj2.life -= self.power * 0.2
            else:
                pj2.life -= self.power - pj2.defense
            
def battle(pj1: Fighter, pj2: Fighter) -> Fighter:
    turn: int
    pj1.life = 100
    pj2.life = 100
    if pj1.speed > pj2.speed:
        turn = 1
    else:
        turn = 2
        
    while pj1.life > 0 and pj2.life > 0:
        if turn == 1:
            print(f"{pj1.name} atack!")
            pj1.attack(pj2)
            print(f"{pj2.name} life: {pj2.life}")
            turn = 2
        elif turn == 2:
            print(f"{pj2.name} atack!")
            pj2.attack(pj1)
            print(f"{pj1.name} life: {pj1.life}")
            turn = 1
    if pj1.life <= 0:
        return pj1
    else:
        return pj2
    
def tournament(figthers: list) -> Fighter:
    while len(figthers) > 1:
        pj1, pj2 = random.sample(figthers, 2)
        eliminated = battle(pj1, pj2)
        figthers.remove(eliminated)
    return figthers[0]
    
            
if __name__ == '__main__': 
    start: bool = True
    figthers: list = [Fighter("Goku", 100, 50, 80), Fighter("Vegeta", 90, 60, 70), Fighter("Piccolo", 80, 70, 60), Fighter("Gohan", 70, 80, 50), Fighter("Trunks", 60, 90, 40), Fighter("Goten", 50, 100, 30), Fighter("Krillin", 40, 110, 20), Fighter("Yamcha", 30, 120, 10), Fighter("Tien", 20, 130, 0), Fighter("Chaoz", 10, 140, 0)]
    op: int = 0
    while start:
        os.system('cls')
        print("====Welcome to the Tournament Of Power=====\n")
        print("1. Add character")
        print("2. Start Tournament")
        print("0. Exit\n")
        op = int(input("Option: "))
        
        if op == 1:
            os.system('cls')
            name = input("Name: ")
            power = int(input("Power: "))
            defense = int(input("Defense: "))
            speed = int(input("Speed: "))
            character = Fighter(name, power, defense, speed)
            figthers.append(character)
        elif op == 2:
            os.system('cls')
            if len(figthers) % 2 == 0:
                print("Tournament Started")
                winner = tournament(figthers)
                print(f"\n\nThe Winner is {winner.name}")
                input("\n\n\nPRESS ENTER TO CONTINUE")
            else:
                print("Invalid number of fighters")
                input("\n\n\nPRESS ENTER TO CONTINUE")
                
        elif op == 0:
            start = False
        else:
            print("Invalid option")