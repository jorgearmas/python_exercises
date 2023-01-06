"""

ENG =>
Imagine you have just opened a new savings account that offers you 4% interest per year. These savings due to interest, which are not collected until the end of the year, are added to your final savings account balance. Write a program that starts by reading the amount of money deposited in the savings account, entered by the user. Then the program should calculate and display the amount of savings after the first, second and third years. Round each amount to two decimal places.

ESP =>
Imagine que acaba de abrir una nueva cuenta de ahorro que le ofrece un interés del 4% anual. Estos ahorros debidos a los intereses, que no se cobran hasta final de año, se añaden al saldo final de su cuenta de ahorro. Escriba un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorro, introducida por el usuario. A continuación, el programa debe calcular y mostrar la cantidad de ahorro después del primer, segundo y tercer año. Redondea cada cantidad a dos decimales.
"""

#input
intial_balance = float(input("Enter the amount initially deposited: $"))
i = 0

print("")
print(f"SAVINGS per year with an investment of ${intial_balance}")

#loop that calculates balance per year / output
while i < 5:
    if i == 0:
        amount = (intial_balance * 0.04) + intial_balance
        amount = round(amount, 2)
    else:
        amount = (amount * 0.04) + amount
        amount = round(amount, 2)
    i += 1
    print(f"- Year {i} .......... {amount}")
print("")