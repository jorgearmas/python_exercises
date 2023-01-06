"""
Code a program that asks the user for the number of hours worked and the cost per hour. It should then display on the screen the corresponding pay.

Rate per hr: $20 
"""
rateHour = 20
hrsWorked = float(input("Type the numbers of hours worked today => "))
payment = (hrsWorked * 20)
print(f"Today's payment is: ${payment}")

