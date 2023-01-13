"""
ENG =>
To pay a certain tax, the user must be over 16 years old and have an income equal to or greater than 1000 € per month. Write a program that asks the user his age and monthly income and displays on the screen whether the user has to pay tax or not.

ESP =>
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""

#condition variables
minAge = 16
monthlyIncome = 1000

#input
ageUser = int(input("\nWhat is your age? "))
incomeUser = int(input("What is your monthly income? "))

#condition / output
if ageUser > minAge and incomeUser >= monthlyIncome:
    print("\nRequired to pay tax")
else:
    print("\nNot required to pay pax")