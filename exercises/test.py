""" import json

texto='{"nombre":"Nhoe", "edad": 35, "mascota": "perro"}'

json_dict=json.loads(texto)
print(type(texto))
print(type(json_dict))
print(json_dict.get("mascota"))
json_dict["mascota"]="gato"
print(json_dict)
texto_json=json.dumps(json_dict)
print(texto_json)
print(type(texto_json)) """

""" import os

def addUsers():
    nameUser= input("Escriba su nombre de ususario:")
    print(f"Su nombre de usuario es {nameUser}?")
    confirm = input("Y/N").upper()

    if confirm == "Y":
        print("Usuario agregado con exito")
    else:
        print("Usuario no agregado")
        
addUsers() """

""" import os


def AnadirUsuario():
    nombreUsuario=input("Introduzca nombre de usuario: ")
    print(f"El nombre de usuario {nombreUsuario} es el correcto")
    confirm=input("Y/N ").upper()
    
    if confirm=="Y":
        os.system("sudo adduser "+ nombreUsuario)
        print("Nuevo usuario añadido con exito")
    
    print("Quiere ver la lista de usuarios actuales? ")
    confirm=input("Y/N").upper()
    if confirm=="Y":
        os.system("cat /etc/passwd")
    

AnadirUsuario() """

def suma(a, b):
    return a + b
assert suma(3, 4)==7, "no funciona bien"