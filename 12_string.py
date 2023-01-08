"""
ENG =>
Code a program that asks the name of a product, its price and a number of units and displays a string with the name of the product followed by its unit price with 6 integer digits and 2 decimal places, the number of units with three digits and the total cost with 8 integer digits and 2 decimal places.

ESP =>
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""

#input
print("")
product = input(f"Name of the product: ")
price = float(input("Product Price: $"))
units = int(input(f"Number of units: "))
total = (price*units)

#format - price with .zfill()
price = round(price, 2)
priceOutput = str(price).zfill(9)

#format - units
unitsOutput = str(units).zfill(3)

#format
total = round(total, 2)
totalOutput = str(total).zfill(11)

print("")
print(f"Product => {product} / Price => {priceOutput}  / Units => {unitsOutput}")
print("-"*60)
print(f"Total cost => {totalOutput}")
print("")