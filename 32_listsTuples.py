"""
ENG =>
Write a program that stores the following prices in a list, 50, 75, 46, 22, 80, 65, 8, and displays the lowest and highest price on the screen.

ESP =>
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
"""
#list
pricesList = [50, 75, 46, 22, 80, 65, 8]
#order min to max
pricesList.sort()

#output
print(f"Lowest price: {pricesList[0]}")
print(f"Highest price: {pricesList[len(pricesList)-1]}")
