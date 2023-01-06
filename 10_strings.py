"""
ENG =>
The telephones of a company have the following format prefix-number-extension where the prefix is the country code +34, and the extension has two digits (for example +34-913724710-56). Write a program that asks for a phone number in this format and displays the phone number without the prefix and extension.

ESP =>
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""
#input
number = input("Enter a number with the following format (xx-xxxxxxxxx-xx) => ")
#convertion from list to string
lst = list(number)
#slicing of numbers in middle
lst2 = lst[3:12]

#string that will contain middle numbers
str1 = ""

#conversion from list to string
for ele in lst2:
    str1 += ele

#output
print(f"Middle numbers are => {str1}")


