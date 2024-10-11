#print("Hola Clouders")

""" name = input("Cómo te llamas? ")
saludo = "Hola"
print(saludo + ' ' +name)

age = int(input("cuántos años tienes? "))
def mayor_de_edad(age, name):
    a = 18
    if age >= a:
        return print(f"Bienvenido {name}")
    else:
        return print("No puedes entrar")

mayor_de_edad(age, name) """




""" banana = 10
manzana = 20
banana = manzana

print(banana) """

""" list1 = ["banana", "pinneaple", "orange"]
ingresar = input("añade tu frutra favorita")
def sumFruit(list1, ingresar):
    return print(list1 + [ingresar])

sumFruit(list1, ingresar) """

users = {
   "Ada": {"apellido":"perez", "age":25},
   "Juan": {"apellido": "Góez0", "age":30}
}
for user in users:
    print(users[user]["apellido"])