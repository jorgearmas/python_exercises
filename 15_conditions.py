"""
ENG =>
Write a program that prompts the user for an integer and displays on the screen whether it is odd or even.

ESP =>
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""
#input
number = int(input("\nEnter a number: "))
#condition / output
if (number%2==0):
    print(f"\n{number} is an even number")
else:
    print(f"\n{number} is an odd number")