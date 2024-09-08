import TP_1_TADMED
from TP_1_TADMED import *

# Test
rem1 = crearMed()
rem2 = crearMed()
rem3 = crearMed()
rem4 = crearMed()
rem5 = crearMed()
rem6 = crearMed()
remedios = [rem1, rem2, rem3, rem4, rem5, rem6]

cargarMed(rem1, "Paracetamol", "Panadol", "Bayer", 1000)
cargarMed(rem2, "Ibuprofeno", "Ibupirac", "Bayer", 150)
cargarMed(rem3, "Amoxicilina", "Amoxidal", "Roemmers", 200)
cargarMed(rem4, "Diclofenac", "Voltaren", "Novartis", 250)
cargarMed(rem5, "Aspirina", "Bayaspirina", "Bayer", 300)
cargarMed(rem6, "Omeprazol", "Omeprazol", "Roemmers", 350)

aux = 0
for i in remedios:
    if (verPrecio(i) > aux):
        aux = verPrecio(i)
        aux2 = i

print(verNomGen(aux2))
    