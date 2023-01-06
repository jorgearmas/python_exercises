"""
ENG =>
Code a program that asks the user for the number of hours worked and the cost per hour. It should then display on the screen the corresponding pay.

Rate per hr: $20

ESP =>
Codifique un programa que pregunte al usuario el número de horas trabajadas y el coste por hora. Luego debe mostrar en pantalla la paga correspondiente.

Tarifa por hora: $20
"""

#input number of worked hours
rateHour = 20
hrsWorked = float(input("Type the numbers of hours worked today => "))
#operation
payment = (hrsWorked * 20)
#display
print(f"Today's payment is: ${payment}")

