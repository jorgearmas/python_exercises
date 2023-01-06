"""
ESP =>
Code a program that prompts for the user's name on the console and after the user enters it, displays <NAME> has <n> letters, where <NAME> is the user's name in uppercase and <n> is the number of letters in the name.

ESP =>
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca, muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
"""

print("")
#input
name = input("Enter your name: ")

#display
print(f"Your name is {name.upper()} and it has {len(name)} letters")