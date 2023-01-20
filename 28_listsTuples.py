"""
ENG =>
Write a program that asks the user for the winning numbers of the primitive lottery, stores them in a list and displays them on the screen in order from smallest to largest.

ESP =>
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""
#genral variables
winningNumbers = []
session = 1

#input
while session == 1:
    singleWinningNumber = int(input("Insert winnig number: "))
    session = int(input("Would you like to continue? (1 - Yes / 0 - No): "))
    winningNumbers.append(singleWinningNumber)

#output
winningNumbers.sort()
print(f"\nList of lottery winning numbers: ")
for element in winningNumbers:
    print(element)