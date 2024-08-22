""" /*
 * EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
 */ """
 
import random
import os

class Player:
    def __init__(self, name, country) -> None:
        self.name = name
        self.country = country

class Event:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players = []
    
    def event_register(self, players_amount: int):
        for i in range(players_amount):
            os.system('cls')
            nm = input(f'Enter player\'s {i+1} name: ')
            cnty = input(f'Enter player\'s {i+1} country: ')
            player = Player(nm, cnty)
            self.players.append(player)
            
class Simulations:
    def __init__(self) -> None:
        self.sports = []
        self.statistics_gold = {}
        self.statistics_silver = {}
        self.statistics_bronze = {}
        self.gold = []  
        self.silver = []  
        self.bronze = []
        
    def event_sim(self, event: Event):
        self.sports.append(event.name)
        gold_win = random.choice(event.players)
        event.players.remove(gold_win)
        silver_win = random.choice(event.players)
        event.players.remove(silver_win)
        bronze_win = random.choice(event.players)
        self.gold.append(gold_win.country)
        self.silver.append(silver_win.country)
        self.bronze.append(bronze_win.country)
        os.system('cls')
        print(f'\t\t  GOLD: {gold_win.name} from {gold_win.country}')
        print(f'SILVER: {silver_win.name} from {silver_win.country}')
        print(f'\t\t\t\tBRONZE: {bronze_win.name} from {bronze_win.country}\n\n')
        input('PRESS ENTER TO CONTINUE')
        
    def games_statistics(self):
        for winner in self.gold:
            self.statistics_gold[winner] = self.gold.count(winner)
        self.statistics_gold = dict(sorted(self.statistics_gold.items(), key=lambda item: item[1], reverse=True))
        for winner in self.silver:
            self.statistics_silver[winner] = self.silver.count(winner)
        self.statistics_silver = dict(sorted(self.statistics_silver.items(), key=lambda item: item[1], reverse=True))
        for winner in self.bronze:
            self.statistics_bronze[winner] = self.bronze.count(winner)
        self.statistics_bronze = dict(sorted(self.statistics_bronze.items(), key=lambda item: item[1], reverse=True))
        os.system('cls')
        print(f'GOLD RANKING: {self.statistics_gold}')
        print(f'SILVER RANKING: {self.statistics_silver}')
        print(f'BRONZE RANKING: {self.statistics_bronze}\n\n')
        input('PRESS ENTER TO CONTINUE')
        
if __name__ == '__main__':
    op = True
    sim = Simulations()
    while op:
        os.system('cls')
        print('WELCOME TO PARIS 2024 OLYMPIC GAMES')
        print('1. Register events')
        print('2. Generate reports')
        print('3. Exit')
        option = int(input('Enter an option: '))
        
        if option == 1:
            os.system('cls')
            event = Event(input('Enter the name of the event: '))
            num_players =int(input('Enter the number of players: '))
            event.event_register(num_players)
            sim.event_sim(event)
        elif option == 2:
            sim.games_statistics()
        elif option == 3:
            op = False
        else:
            print('Invalid option')
        