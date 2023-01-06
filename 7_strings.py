"""
ENG =>
Code a program that prompts for the user's name on the console and an integer and prints the user's name on separate lines as many times as the number entered.

ESP=>
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

#input
name = input("Enter you name: ")
name = name + " "
repetitions = int(input("Enter the number of times that you would like to see your name repeated: "))

#operation
sentence = name * repetitions

#display
print(f"Result: {sentence}")