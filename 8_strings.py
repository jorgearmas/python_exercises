"""
ENG =>
Code a program that prompts for the user's full name on the console and then displays the user's full name three times, once with all lowercase letters, once with all uppercase letters, and once with only the first letter of the first name and last name in uppercase. The user can enter his or her name in any combination of upper and lower case letters.

ESP =>
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
print("")
#input
name = input("Enter your name: ")

#functions
lowerCase = name.lower()
upperCase = name.upper()
capitalize = name.title()

print("")
#display
print(f"* Lower case - {lowerCase}")
print(f"* Upper case - {upperCase}")
print(f"* Capitalize - {capitalize}")

