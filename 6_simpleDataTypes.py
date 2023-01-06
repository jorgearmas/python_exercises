"""
ENG =>
A bakery sells loaves of bread at €3.49 each. The non-daily bread is discounted by 60%. Write a program that starts by reading the number of loaves sold that are not of the day. Then the program should display the usual price of a loaf of bread, the discount for non-fresh and the total final cost.

ESP =>
Una panadería vende barras de pan a 3,49 euros cada una. El pan que no es del día tiene un descuento del 60%. Escribe un programa que empiece leyendo el número de barras de pan vendidas que no son del día. A continuación, el programa debe mostrar el precio habitual de una barra de pan, el descuento por no ser del día y el coste final total.
"""
print("")
#number of non-fresh loafs requested
non_fresh_loafs = float(input("Enter the number of non-fresh loafs today => "))
#operation without discount
total = (non_fresh_loafs * 3.49)
total = round(total, 2)
#operation with discount
discount = abs((total*0.6)-total)
discount = round(discount, 2)

#display
print("")
print("-"*80)
print(f"The regular price is €3.49 a unit there are {non_fresh_loafs} in the order. The total price without discount is €{total}")
print("-"*80)
print(f"The price with 60% discount is €{discount}")
print("-"*80)