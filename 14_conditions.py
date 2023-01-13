"""
ENG =>
Write a program that stores the password string in a variable, asks the user for the password and prints on the screen if the password entered by the user matches the password stored in the case insensitive variable.

Pw example: $monday_23

ESP =>
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

Ejemplo de pw: $monday_23
"""
#string in variable
password = "$monday_23"

#input
userPassword = input("\nPassword: ")
#conversion to lowercase
userPassword = userPassword.lower()

#condition / output
if password==userPassword:
    print("\nPassword matches")
else:
    print("\nIncorrect password")
