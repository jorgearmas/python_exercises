"""
ENG =>
Write a program that prompts the user for a word and then displays on the screen one by one the letters of the word entered starting with the last letter.

ENG =>
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""
#general variables
listLetters = []

#input 
word = input("Enter any word: ")

#converting string into a list
listLetters[:0] = word

#reversing list
listLetters.reverse()

#loop / output
for element in listLetters:
    print(element)