from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from datetime import datetime
import urllib.parse
import os


os.system('cls')


# Instanciar un cliente de Mongo

  

client = MongoClient('mongodb://localhost:27017/')


db = client['Evidencia3']

col = db['Alumnos']

col2 = db['Carreras']

i = 1

def displayUser():
    os.system('cls')
    for deez in col.find({}):
        print("\n")
        for keys in deez.keys(): 
            print ('{', keys, ":" , deez[keys] , '}' )
    print("\n")


def addAlumno():
    os.system('cls')
    nombre = input("Nombre del alumno ")
    apellido1 = input("Apellido Paterno ")
    apellido2 = input("Apellido Materno ")
    year = int(input("Año de nacimiento "))
    Mes = int(input("Mes de nacimiento "))
    Dia = int(input("Dia de nacimiento "))
    
    Carrera = input("Nombre de carrera ")        
    ins = 0
    while ins == 0:
        Estatus = input("Estatus (Inscrito o No Inscrito) ")
        if Estatus != "Inscrito" and Estatus != "No Inscrito":
            print("Ese no es un valor valido!")
        else:
          newvalues = { "$set": {"Estatus": Estatus}}
          ins = 1
    
    col.insert_one({
        'Nombre': nombre,
        'Apellidos': {'apellido1': apellido1, 'apellido2': apellido2},
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
    for x in col.find({},{ "_id": 0, "Nombre": 1 }):
        print(x) 
    nombre = input("Nombre del alumno del que quieres dar de baja ")
    myquery = { "Nombre": nombre}
    
    

    col.delete_one(myquery)
    input("Presione Enter para continuar ")
    
    
def update():
    os.system('cls')
    for x in col.find({},{ "_id": 0, "Nombre": 1 }):
        print(x) 
    nombre = input("Nombre del alumno del que quieres modificar: ")
    myquery = { "Nombre": nombre}
    
    nombre = input("Nombre del alumno: ")
    apellido1 = input("Apellido Paterno: ")
    apellido2 = input("Apellido Materno: ")
    Carrera = input("Nombre de carrera: ")

    ins = 0
    while ins == 0:
        Estatus = input("Estatus (Inscrito o No Inscrito) ")
        if Estatus != "Inscrito" and Estatus != "No Inscrito" and Estatus != "":
            print("Ese no es un valor valido!")
        else:
          ins = 1
  
    Correo = input("Correo*: ")
    Telefono = input("Telefono*: ")
    Direccion = input("Direccion*: ")
    col.update_one(
    myquery, {"$set": {"Nombre": nombre, 
    "Apellidos": {'apellido1': apellido1, 'apellido2': apellido2}, 
    "Carrera": Carrera, 
    "Estatus": Estatus, 
    "Correo": Correo, 
    "Telefono": Telefono, 
    "Direccion": Direccion}})

    input("Presione Enter para continuar")

            
            
def displayCarrera():
    os.system('cls')
    for deez in col2.find({}):
        for keys in deez.keys(): 
            print ('{', keys, ":" , deez[keys] , '}' )

    


    

while i == 1:
    os.system('cls')
    menu_select = int(input("1- Consulta de informacion de alumnos. \n2- Consulta de informacion de carreras. \n3- Alta un alumno. \n4- Alta una carrera \n5- Baja de un alumno. \n6- Modificacion de un Alumno \n7- Cerrar programa ")) 

    if menu_select == 1:
        displayUser()
        input("Presione Enter para continuar")
    elif menu_select == 2:
        displayCarrera() 
        input("Presione Enter para continuar")
    elif menu_select == 3:
        addAlumno()
        input("Presione Enter para continuar")
    elif menu_select == 4:
        addCarrera()
        input("Presione Enter para continuar")
    elif menu_select == 5:
        delete()    
    elif menu_select == 6:
        update()
    elif menu_select == 7:
        i = 0
    else:
        print("No es una opcion valida")
    
