#print("Hola Clouders")

""" name = input("Cómo te llamas?")
saludo = "Hola "
print(saludo + name) """


age = int(input("cuántos años tienes?"))
def mayor_de_edad(age):
    a = 18
    if age >= a:
        return print("Bienvenido")
    else:
        return print("No puedes entrar")

mayor_de_edad(age)