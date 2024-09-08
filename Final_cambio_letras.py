#Por razones de seguridad una empresa decide que sus comunicaciones internas se harán con un vocabulario limitado 
# a 1500 palabras de no más de diez caracteres que se hallan en un archivo sin ningún orden prestablecido. 
# Los mensajes tendrán un espacio blanco entre palabras a excepción de la última que será seguida de un punto. 
# El algoritmo que Ud. desarrollará, deberá tomar cada texto del que se conoce previamente su longitud y transformar
# cada palabra según las siguientes reglas: las letras en posición impares se reemplazan por la siguiente en el abecedario,
# las pares por la anterior y los blancos por la letra “z” a excepción que la anterior sea una “z” en cuyo caso se reemplaza 
# por “y”.
# Finalmente, deberá imprimir un reporte donde conste la distribución de palabras usadas ordenadas decrecientemente
# según cantidad de letras, cantidad de palabras que luego de haber sido encriptadas siguen manteniendo significado dentro 
# del vocabulario establecido, listado de las mismas y cantidad de blancos reemplazados con“z” y con “y”.

def cambio_letra(letra, letra_ant, paridad):
    abcd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(abcd)):
        if (abcd[i] == letra):
            if ((lambda es_par:paridad%2 == 0) == True):
                return  abcd[i-1]
            else:
                if  (letra == 'z'):
                    return abcd[0]
                else:
                    return abcd[i+1]
        if (letra == ' '):
            if (letra_ant == 'z'):
                return 'y'
            else:
                return 'z'
        if (letra == '\n'):
            return "\n"
        if (letra == '.'):
            return "."
        if (letra == ','):
            return ","

with open('Ejercicios\\Miguel_Torres_Granados.txt',encoding= "UTF-8") as arch:
    with open('Ejercicios\\Miguel_Torres_Granados_codificado.txt','w',encoding= "UTF-8") as archcod:
        archivo = arch.readlines() #Variable que toma la linea
        for frase in archivo:
            tamanio = frase #Variable que toma la linea como oracion
            ant = "a"
            for num in enumerate(tamanio):
                nueva_letra = cambio_letra(num[1].lower(), ant.lower(), num[0] + 1)
                ant = num[1]
                archcod.write(nueva_letra)