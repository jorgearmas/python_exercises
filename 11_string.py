"""
ENG =>
Code a program that prompts the user to enter a sentence in the console and displays the inverted sentence on the screen.

ESP =>
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
"""
print("")
#input
word = input(f"Enter a word or a phrase: ")
#string gets reversed with step -1
word = word[::-1]
#display
print(f"Iverted word/phrase: {word}")
print("")