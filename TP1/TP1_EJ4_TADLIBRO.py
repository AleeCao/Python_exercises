def crearLibro():
    libro = {
        "codigo": "", 
        "nombre": "", 
        "autor": "", 
        "genero": "",
        "editorial": "",
        "precio": ""
    }
    return libro

def cargarLibro(libro, codigo, nombre, autor, genero, editorial, precio):
    libro["codigo"] = codigo
    libro["nombre"] = nombre
    libro["autor"] = autor
    libro["genero"] = genero
    libro["editorial"] = editorial
    libro["precio"] = precio

def verCodigo(libro):
    return libro["codigo"]

def verNombre (libro):
    return libro["nombre"]

def verAutor (libro):
    return libro["autor"]

def verGenero (libro):
    return libro["genero"]

def verEditorial (libro):
    return libro["editorial"]

def verPrecio (libro):
    return libro["precio"]