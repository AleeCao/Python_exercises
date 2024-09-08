import TP1_TAD_auto
from TP1_TAD_auto import *

auto1 = crearAuto()
auto2 = crearAuto()

cargarAuto(auto1, "AA540FR", "150000", "Volkswagen", "Saveiro", "15000")
cargarAuto(auto2, "AB770AI", "154000", "Ford", "Ranger", "32000")

if auto1["kilometraje"] < auto2["kilometraje"]:
    print("El vehiculo con menor kilometraje es: " + auto1["marca"] + " " + auto1["modelo"])
else:
    print("El vehiculo con menor kilometraje es: " + auto2["marca"] + " " + auto2["modelo"])
