def crearAuto():
    auto = {
        "patente": "", 
        "kilometraje": "", 
        "marca": "", 
        "modelo": "",
        "precio": ""
    }
    return auto

def cargarAuto(auto, patente, kilometraje, marca, modelo, precio):
    auto["patente"] = patente
    auto["kilometraje"] = kilometraje
    auto["marca"] = marca
    auto["modelo"] = modelo
    auto["precio"] = precio
    
def verPatente(auto):
    return auto["patente"]

def verKm (auto):
    return auto["kilometraje"]

def verMarca (auto):
    return auto["marca"]

def verModelo (auto):
    return auto["modelo"]

def verPrecio (auto):
    return auto["precio"]

    