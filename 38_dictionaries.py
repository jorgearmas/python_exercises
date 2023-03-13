"""
ENG =>
Write a program to manage the customer database of a company. The customers will be stored in a dictionary in which the key of each customer will be its NIF, and the value will be another dictionary with the customer data (name, address, telephone, mail, preferential), where preferential will have the value True if it is a preferential customer. The program must ask the user for an option from the following menu: (1) Add client, (2) Remove client, (3) Show client, (4) List all clients, (5) List preferred clients, (6) Finish. Depending on the option chosen the program will have to do the following:

ESP =>
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
"""
#libs
import os

#dictionaries
prod_dictionary = {}
cx_data_dictionary = {}

#global vars
nif = 0
cx_name = ""
cx_adress = ""
cx_phone = ""
cx_pref = ""


def add_cx():
    print("-"*55)
    print("Add customer")
    print("-"*55)
    add_cx_session = 1
    global prod_dictionary
    global cx_data_dictionary
    global nif
    global cx_name
    global cx_adress
    global cx_phone

    while add_cx_session == 1:
        cx_data_dictionary = {}
        nif = int(input("Enter NIF number: "))
        cx_name = input("Enter customer's name: ")
        cx_data_dictionary['name'] = cx_name
        cx_adress = input("Enter customer's adress: ")
        cx_data_dictionary['adress'] = cx_adress
        cx_phone = input("Enter customer's phone number: ")
        cx_data_dictionary['phone'] = cx_phone
        cx_pref = input("Enter customer's preference: ")
        cx_data_dictionary['preference'] = cx_pref
        #data integration
        prod_dictionary[nif] = cx_data_dictionary
        #continuity of cycle
        print("-"*55) 
        print("***Press 1 to add a new customer***\nor press any key to go back to menu")
        add_cx_session = int(input("-> Option: "))
        if add_cx_session != 1:
            os.system('CLS')
            menu()

def menu():
    menu_session = 1
    while menu_session == 1:
        print(prod_dictionary)
        print("-"*30)
        print("Customer Managment")
        print("-"*30)
        print("1) ... Add customer")
        print("2) ... Delete customer")
        print("3) ... Show customer")
        print("4) ... Show all customers")
        print("5) ... Show preferred customers")
        print("-"*30)
        menu_option = int(input("-> Choose opcion: "))
        if menu_option == 1:
            os.system('CLS')
            add_cx()

if __name__ == "__main__":
    menu()

