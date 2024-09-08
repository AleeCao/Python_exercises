def crearMed(): #retorna un remedio sin datos
    medicamento = {"nombre_genérico": "", "nombre_comercial": "", "laboratorio": "", "precio": 0}
    return medicamento

def cargarMed(r,nomg,nomcom,lab,prec): #asigna nombre genérico, nombre comercial, laboratorio y precio al remedio r
    r["nombre_genérico"] = nomg
    r["nombre_comercial"] = nomcom
    r["laboratorio"] = lab
    r["precio"] = prec

def verNomGen(r): #retorna el nombre genérico del remedio r
    return r["nombre_genérico"]

def verNomCom(r): #retorna el nombre comercial de r
    return r["nombre_comercial"]

def verLab(r): #retorna el laboratorio de r
    return r["laboratorio"]

def verPrecio(r): #retorna el precio de r
    return r["precio"]

def modNomGen(r, otroNG): #modifica el nombre genérico de r
    r["nombre_genérico"] = otroNG

def modNomCom(r, otroNC): #modifica el nombre comercial de r
    r["nombre_comercial"] = otroNC

def modLab(r, otroL): #modifica el laboratorio de r
    r["laboratorio"] = otroL

def modPrecio(r,otroP): #modifica el precio de r
    r["precio"] = otroP

def copiar(r1,r2): #copia todos los datos del remedio r2 en r1
    r1["nombre_genérico"] = r2["nombre_genérico"]
    r1["nombre_comercial"] = r2["nombre_comercial"]
    r1["laboratorio"] = r2["laboratorio"]
    r1["precio"] = r2["precio"]