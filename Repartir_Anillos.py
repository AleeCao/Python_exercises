""" /*
 * EJERCICIO:
 * ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
 * ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 * entre las razas de la Tierra Media?
 * Desarrolla un programa que se encargue de distribuirlos.
 * Requisitos:
 * 1. Los Elfos recibirán un número impar.
 * 2. Los Enanos un número primo.
 * 3. Los Hombres un número par.
 * 4. Sauron siempre uno.
 * Acciones:
 * 1. Crea un programa que reciba el número total de anillos
 *    y busque una posible combinación para repartirlos.
 * 2. Muestra el reparto final o el error al realizarlo.
 */ """
import os

# Funcion para repartir los anillos
def repartir_anillos(razas: dict, anillos: int):
    salida: bool = True
    if anillos < 7:
        return False
    else:
        elf: int = 3
        en: int = 2
        hum: int = 2
        sauron: int = 1
        if (elf + en + hum + sauron) == anillos:
                razas['Elfos'] = elf
                razas['Enanos'] = en
                razas['Hombres'] = hum
                razas['Sauron'] = sauron
                return True
        else:
            k: int = 1
            while salida:
                elf += 2
                if (elf + en + hum + sauron) == anillos:
                    razas['Elfos'] = elf
                    razas['Enanos'] = en
                    razas['Hombres'] = hum
                    razas['Sauron'] = sauron
                    return True
                en += 2
                if (elf + en + hum + sauron) == anillos:
                    razas['Elfos'] = elf
                    razas['Enanos'] = en
                    razas['Hombres'] = hum
                    razas['Sauron'] = sauron
                    return True
                hum: int = 4*k - 1
                if (elf + en + hum + sauron) == anillos:
                    razas['Elfos'] = elf
                    razas['Enanos'] = en
                    razas['Hombres'] = hum
                    razas['Sauron'] = sauron
                    return True
                sauron: int = 1
                if (elf + en + hum + sauron) == anillos:
                    razas['Elfos'] = elf
                    razas['Enanos'] = en
                    razas['Hombres'] = hum
                    razas['Sauron'] = sauron
                    return True
                if k > 100:
                    return False
                else:
                    k += 1
                    
reparto = {'Elfos': 0, 'Enanos': 0, 'Hombres': 0, 'Sauron':0}
x = True
while x:
    os.system('cls')
    anillos = input("Ingrese el numero de anillos: ")
    repartir = repartir_anillos(reparto, int(anillos))
    if repartir:
        os.system('cls')
        print('Reparto de anillos:\n')
        print('Los Elfos reciben:', reparto['Elfos'])
        print('Los Enanos reciben:', reparto['Enanos'])
        print('Los Hombres reciben:', reparto['Hombres'])
        print('Sauron recibe:', reparto['Sauron'])
        x = False
    else:
        os.system('cls')
        print('Error al repartir los anillos, intente otra vez')
        input()
        os.system('cls')