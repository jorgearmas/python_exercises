"""
ENG =>
Write a program that prompts the user for an integer and displays on the screen whether it is an prime number or not.

ESP =>
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""
#general variables
iterator = 1
remainder = 0
remainderCount = 0

#input
number = int(input("\nEnter an positive integer number: "))

#loop
while iterator <= number:
    #exeption for 1
    if number == 1:
        print(f"{number} is an non-prime number")
        break
    else:
        remainder = number%iterator
        if remainder == 0:
            remainderCount += 1
        iterator += 1

#output
if number != 1:
    if remainderCount > 2:
        print(f"{number} is an non-prime number")
    else:
        print(f"{number} is an prime number")
