"""
ENG =>
Write a program that stores in a variable the dictionary {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, asks the user for a currency and displays its symbol or a warning message if the currency is not in the dictionary.

ESP =>
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""
#global variables
simbol = ""
new_dict = {}

#dictionary declaration
currency = {
    'Euro': '€',
    'Dollar':'$', 
    'Yen':'¥'
}

#input
currency_user = input("\nEnter a currency: ")

#iterating with a for
for x, y, in currency.items():
    if currency_user == x:
        simbol = y
        break
    else:
        simbol = "Not found"

print(simbol)

#iterating with filter
new_dict = dict(filter(lambda element: element[0] == currency_user, currency.items()))
print(new_dict)