""" /*
 * EJERCICIO:
 * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
 * ¿Alguien se entera de todas las relaciones de parentesco
 * entre personajes que aparecen en la saga?
 * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 * Requisitos:
 * 1. Estará formado por personas con las siguientes propiedades:
 *    - Identificador único (obligatorio)
 *    - Nombre (obligatorio)
 *    - Pareja (opcional)
 *    - Hijos (opcional)
 * 2. Una persona sólo puede tener una pareja (para simplificarlo).
 * 3. Las relaciones deben validarse dentro de lo posible.
 *    Ejemplo: Un hijo no puede tener tres padres.
 * Acciones:
 * 1. Crea un programa que permita crear y modificar el árbol.
 *    - Añadir y eliminar personas
 *    - Modificar pareja e hijo
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 * 
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
 */ """
 
import os
 
class Character:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.partner = []
        self.children = []
        self.parents = []
        
    def get_married(self, partner: 'Character') -> None:
        self.partner.append(partner)
    
    def have_children(self, children: 'Character') -> None:
        self.children.append(children)
        
    def born(self, parent1: 'Character', parent2: 'Character') -> None:
        self.parents.append(parent1)
        self.parents.append(parent2)
        
class Relations:
    characters: list = []
    
    def print_tree(self):
        for character in self.characters:
            print(f'ID: {character.id}')
            print(f'Name: {character.name}')
            print(f'Partner: {[partner.name for partner in character.partner]}')
            print(f'Children: {[child.name for child in character.children]}')
            print(f'Parents: {[parent.name for parent in character.parents]}\n')
        x = input("PRESS ENTER TO CONTINUE")
    
    def original(self, p1: Character):
        self.characters.append(p1)
    
    def marriage(self, id1: int, id2: int) -> None:
        p1 = next((pid for pid in self.characters if pid.id == id1), False)
        p2 = next((pid for pid in self.characters if pid.id == id2), False)
        if p1 and p2:
            p1.get_married(p2)
            p2.get_married(p1)
        else:
            os.system('cls')
            print("Ops, seems like somebody doesn't want to get married!\n\n")
            x = input("PRESS ENTER TO CONTINUE")
        
    def get_pregnant(self, id1: int, id2: int, bid: int, bname: str) -> None:
        p1 = next((pid for pid in self.characters if pid.id == id1), False)
        p2 = next((pid for pid in self.characters if pid.id == id2), False)
        if p1 and p2:
            b = Character(bid, bname)
            p1.have_children(b)
            p2.have_children(b)
            b.born(p1, p2)
            self.characters.append(b)
        else:
            os.system('cls')
            print("Ops, we need 2 persons to make a baby!\n\n")
            x = input("PRESS ENTER TO CONTINUE")
        
      
if __name__ == '__main__':  
    start: bool = True
    op: int = 0
    characters = Relations()
    while start:
        os.system('cls')
        print("Welcome to the House of the Dragon Genealogical Tree\n")
        print("1. Add character")
        print("2. Add marriage")
        print("3. Add children")
        print("4. Print tree")
        print("5. Exit\n")
        op = int(input("Option: "))

        if op == 1:
            os.system('cls')
            if characters.characters.__len__() == 0:
                print('Character ID: 1')
                name = input("Name: ")
                character = Character(1, name)
                characters.original(character)
            else:
                print(f'Character ID: {(characters.characters[-1].id + 1)}')
                name = input("Name: ")
                character = Character((characters.characters[-1].id + 1), name)
                characters.original(character)
        elif op == 2:
            os.system('cls')
            id1 = int(input("ID 1: "))
            id2 = int(input("ID 2: "))
            characters.marriage(id1, id2)
        elif op == 3:
            os.system('cls')
            id1 = int(input("ID 1: "))
            id2 = int(input("ID 2: "))
            bname = input("Name: ")
            characters.get_pregnant(id1, id2, (characters.characters[-1].id + 1), bname)
        elif op == 4:
            os.system('cls')
            characters.print_tree()
        elif op == 5:
            start = False
        else:
            print("Invalid option")