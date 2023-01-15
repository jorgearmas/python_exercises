"""
ENG =>
Write a program that prompts the user for a positive integer and displays all the odd numbers from 1 to that number separated by commas.

ESP =>
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
#general variables
numbersList = []
numbersString = ""

#input
number = float(input("\nEnter a positive integer number: "))
displayNumber = int(number)

#verification of input
if number > 0 and number%1 == 0 :
    #loop
    while number >= 0:
        if number%2 != 0:
            numbersList.append(number)
        number -= 1
    #reversing list
    numbersList.reverse()

    #converting list to integer items
    numbersList = [int(x) for x in numbersList]

    #converting list to string
    numbersString = ', '.join([str(elem) for elem in numbersList])

    #output
    print(f"\n{numbersString} - Original number: {displayNumber}")
else:
    print("\nEnter a positive integer number")
