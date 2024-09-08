""" Suponer ya creado y guardado en el ambiente Python el TAD Trámite que permite almacenar
tipo de trámite (reclamo de reparación, alta de servicio, baja de servicio, cambio de titular del
servicio), nro cliente, dni cliente, día y mes de ingreso de un trámite. Las operaciones
admitidas son:
- crearTram()
#retorna un trámite nuevo sin datos
- cargarTram(t,tipo,nroC,dniC,dia,mes)
#asigna los datos al trámite t
- verTipo(t)
#retorna el tipo del trámite t
- verNroC(t)
#retorna nro de cliente del trámite t
- verDniC(t)
#retorna el dni del cliente que hizo el trámite t
- verDia(t)
#retorna el día que se ingresó el trámite t
- verMes(t)
#retorna el mes en el cual se ingresó el trámite t
- modTipo(t, otroT)
#modifica el tipo del trámite t
- modDni(r,otroDni)
#modifica el dni del cliente que inició el trámite t
- modNroC(r, otroNro)
#modifica el nro de cliente del trámite t
- modDia(t,otroD)
#modifica el día del trámite t
- modMes(t,otroM)
#modifica el mes en el cual se ingresó el trámite t
- copiar(t1,t2)
#copia todos los datos del trámite t2 en t1
a) Hacer un programa de aplicación que simule la recepción de varios trámites (usar un while) y
los cargue en una lista. Luego imprima la cantidad de solicitudes de cambio de titularidad recibidas
y un listado con el tipo de trámite y el nro de cliente de todos aquellos trámites que fueron
realizados entre el 10 y el 25 de marzo. Utilizar para manipular las variables de tipo TAD solamente
las operaciones especificadas. Aclaración: la lista no es otro TAD. """

import TAD_tramite 
from TAD_tramite import *

salida = False
tramites = []
while not salida:
    print("Ingrese los datos del trámite:")
    t = crearTram()
    tipo = input("Tipo de trámite: ")
    nroC = int(input("Número de cliente: "))
    dniC = int(input("DNI del cliente: "))
    dia = int(input("Día de ingreso: "))
    mes = int(input("Mes de ingreso: "))
    cargarTram(t, tipo, nroC, dniC, dia, mes)
    tramites.append(t)
    print("¿Desea ingresar otro trámite?")
    if input("Sí/No: ") == "No":
        salida = True