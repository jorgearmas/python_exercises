"""
ENG =>
Write a program that stores in a dictionary the prices of the fruits in the table, asks the user for a fruit, a number of kilos and displays the price of that number of kilos of fruit. If the fruit is not in the dictionary it should display a message informing about it.

Banana	1.35
Apple	0.80
Pear	0.85
Orange	0.70

ESP =>
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
"""
#global variables
session = 1
item_option = ""
rslt = ""
item_kilos = 0

#dictionary declaration
prices = {
    "BANANA": 1.35,
    "APPLE": 0.80,
    "PEAR": 0.70,
    "ORANGE": 0.70
}

#functions
def strVerification(strg):
    rslt = strg.upper().strip()
    return(rslt)

while session == 1:
    item_option = strVerification(input("\nEnter the fruit to search: "))
    if item_option in prices.keys():
        item_kilos = float(input("How many kilos would you like to take? "))
        for k, val in prices.items():
            if k == item_option:
                rslt = item_kilos*val
        print("-"*41)
        print(f"You will pay ${rslt} for {item_kilos} kilos of {item_option}")
        print("-"*41)
    else:
        print("Item is not available")

    session = int(input("Would you like to continue? "))
    if session == 0:
        exit()
        
