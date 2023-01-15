"""
ENG =>
Write a program that stores the password string in a variable, prompt the user for the password until the correct password is entered.

default password = bingo123

ESP =>
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

constraseña por defecto = bingo123
"""
#general variables
defaultPassword = "bingo123"

#input
password = input("\nPlease enter your password: ")

#loop / output
while password !=  defaultPassword:
    print("\n---Incorrect password, please try again---")
    password = input("Please enter your password: ")
    if password == defaultPassword:
        print("\n---Logging in---")
        exit()

