import TP1_EJ4_TADLIBRO
from TP1_EJ4_TADLIBRO import *

libro1 = crearLibro()
libro2 = crearLibro()
libro3 = crearLibro()
libro4 = crearLibro()

cargarLibro(libro1, "03", "El principito", "Antoine de Saint-Exupéry", "Cuento", "Santillana", 500)
cargarLibro(libro2, "04", "El señor de los anillos", "J.R.R. Tolkien", "Fantasía", "Santillana", 800)
cargarLibro(libro3, "05", "El código Da Vinci", "Dan Brown", "Novela", "Planeta", 600)
cargarLibro(libro4, "06", "Harry Potter", "J.K. Rowling", "Fantasía", "Puerto de Palos", 700)

libros = [libro1, libro2, libro3, libro4]

for libro in libros:
    if libro["editorial"] == "Santillana":
        print("Precio viejo: " + str(libro["precio"]))
        libro["precio"] = libro["precio"] * 1.08
        print("Precio nuevo: " + str(libro["precio"]))