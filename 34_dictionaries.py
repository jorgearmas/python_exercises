"""
ENG =>
Write a program that asks the user for his name, age, address and telephone number and stores it in a dictionary. It should then display the message <name> is <age> years old, lives at <address> and his phone number is <phone>.

ESP =>
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
#--Static--
#dictionay declaration
person = {
    "name":[],
    "adress":[],
    "age":[]
}

#input / append
usr_name = input("Enter your name: ")
person["name"].append(usr_name)
usr_adress = input("Enter your adress: ")
person["adress"].append(usr_adress)
usr_age = int(input("Enter your age: "))
person["age"].append(usr_age)

#output
print(person)

#--Dynamic--
#global variables
session = 1

#list declaration
people = []

person_v2 = {}

while session == 1:
    usr_name = input(f"\nEnter your name: ")
    people["name"] = usr_name
    usr_adress = input(f"Enter your adress: ")
    people["address"] = usr_adress
    usr_age = input(f"Enter your age: ")
    people["age"] = usr_age

    session = int(input("Would you like to continue? "))

print(people)

