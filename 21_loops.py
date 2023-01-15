"""
ENG =>
Write a program that prompts the user for an integer and displays a right triangle like the one below, with the height of the number entered.
*
**
***
****
*****

ESP =>
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****
"""
#general variables
iterator = 1
session = 1

while session == 1:
    #input
    number = float(input("\nEnter a positive integer number: "))

    #number verification
    if number > 0 and number%1 == 0:
        if number == 1:
            print("*")
        else:
            while iterator <= number:
                print("*"*iterator)
                iterator += 1
    else:
        print("\nIncorrect number")
    
    #session validation - active/inactive
    session = int(input("Would you like to continue (1 = yes | 2 = no) => "))
    if session == 2:
        exit()