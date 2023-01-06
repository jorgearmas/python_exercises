"""
Code a program that asks the user for his weight (in kg) and height (in meters), then calculate the body mass index and store it in a variable and display the sentence: "Your body mass index is <imc>".
"""

weight = float(input(f"Please enter your weight in KG => "))
height = float(input(f"Please enter your height in Mt => "))

#imc formula
imc = weight/(height**2)
imc = round(imc, 2)

print(f"Your IMC is => {imc}")