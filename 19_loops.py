"""
ENG =>
Write a program that prompts the user for a word and displays it on the screen 10 times.

ESP =>
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
#general variables
iterator = 1

#input
word = input("\nEnter any word: ")

#loop / output
while iterator <= 10:
    print(f"{iterator} - {word}")
    iterator += 1