"""
ENG =>
Code a program that asks the user for his weight (in kg) and height (in meters), then calculate the body mass index and store it in a variable and display the sentence: "Your body mass index is <imc>".

ESP =>
Codifique un programa que pida al usuario su peso (en kg) y su altura (en metros), luego calcule el índice de masa corporal y lo almacene en una variable y muestre la frase: "Su índice de masa corporal es <imc>".

"""

#input
weight = float(input(f"Please enter your weight in KG => "))
height = float(input(f"Please enter your height in Mt => "))

#imc formula
imc = weight/(height**2)
imc = round(imc, 2)

#display
print(f"Your IMC is => {imc}")