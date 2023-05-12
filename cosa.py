from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from datetime import datetime
import os


os.system('cls')


# Instanciar un cliente de Mongo
client = MongoClient('localhost',
                     port=27017,
                     )


db = client['Evidencia3']

col = db['Alumnos']

col2 = db['Carreras']

i = 1


def addAlumno():
    os.system('cls')
    nombre = input("Nombre del alumno ")
    apellido1 = input("Primer Apellido ")
    apellido2 = input("Segundo Apellido ")
    year = int(input("Año de nacimiento "))
    Mes = int(input("Mes de nacimiento "))
    Dia = int(input("Dia de nacimiento "))
    Carrera = input("Nombre de carrera ")        
    Estatus = input("Estatus (Inscrito o No Inscrito) ")
    
    col.insert_one({
        'Nombre': nombre,
        'Apellido': {'apellido1': apellido1, 'apellido2': apellido2},
        'Nacimiento': datetime(year, Mes, Dia, 0, 0),
        'Carrera': Carrera,
        'Estatus': Estatus, 'Correo': '', 'Telefono': '', 'Direccion': ''
    })   
    
def addCarrera():
    os.system('cls')
    Carrera = input("Nombre de carrera ")
    Descripcion = input("Descripcion de la carrera ")
    Departamento = input("Departamento de la carrera ")
    
    col2.insert_one({
        'Carrera': Carrera,
        'Descripcion': Descripcion,
        'Departamento': Departamento
    })  
    
def delete():
    os.system('cls')
    nombre = input("Nombre del alumno del que quieres dar de baja ")
    myquery = { "Nombre": nombre}

    col.delete_one(myquery)
    input("Presione cualquier cosa para continuar ")
    
    
def update():
    os.system('cls')
    nombre = input("Nombre del alumno del que quieres modificar ")
    myquery = { "Nombre": nombre}
    nombre = input("Nombre del alumno ")
    newvalues = { "$set": {"Nombre": nombre}}
    col.update_one(myquery, newvalues)
    apellido1 = input("Primer Apellido ")
    newvalues = { "$set": {"apellido1": apellido1}}
    col.update_one(myquery, newvalues)
    apellido2 = input("Segundo Apellido ")
    newvalues = { "$set": {"apellido2": apellido2}}
    col.update_one(myquery, newvalues)
    Carrera = input("Nombre de carrera ")
    newvalues = { "$set": {"Carrera": Carrera}}
    col.update_one(myquery, newvalues)
    Estatus = input("Estatus (Inscrito o No Inscrito) ")
    newvalues = { "$set": {"Estatus": Estatus}}
    col.update_one(myquery, newvalues)
    Correo = input("Correo: ")
    newvalues = { "$set": {"Correo": Correo}}
    col.update_one(myquery, newvalues)
    Telefono = input("Telefono: ")
    newvalues = { "$set": {"Telefono": Telefono}}
    col.update_one(myquery, newvalues)
    Direccion = input("Direccion: ")
    newvalues = { "$set": {"Direccion": Direccion}}
    col.update_one(myquery, newvalues)
    input("Presione cualquier cosa para continuar")



    
    


    

while i == 1:
    os.system('cls')
    menu_select = int(input("1- Consulta de informacion de alumnos. \n2- Consulta de informacion de carreras. \n3- Alta un alumno. \n4- Alta una carrera \n5- Baja de un alumno. \n6- Modificacion de un Alumno \n7- Cerrar programa ")) 

    if menu_select == 1:
        for documento in col.find({}): 
            print(documento) 
        input("Presione cualquier cosa para continuar")
    elif menu_select == 2:
        for documento in col2.find({}): 
            print(documento)    
        input("Presione cualquier cosa para continuar")
         
    elif menu_select == 3:
        addAlumno()   
    elif menu_select == 4:
        addCarrera()  
    elif menu_select == 5:
        delete()    
    elif menu_select == 6:
        update()
    elif menu_select == 7:
        i = 0
    else:
        print("No es una opcion valida")
    