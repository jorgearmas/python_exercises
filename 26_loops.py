"""
ENG =>
Write a program that asks the user for a phrase and a letter, and displays the number of times the letter appears in the phrase.

ESP =>
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""
#general variables
listSentence = []
letterCounter = 0

#input
sentence = input("\nEnter a sentence: ")
letter = input("Letter to count: ")

#converting string to list
listSentence[:0] = sentence

#loop / count letter
for element in listSentence:
    if element == letter:
        letterCounter += 1

#output
print(f"\nThe sentence contains {letterCounter} times the letter '{letter}'")



