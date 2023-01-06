"""
A bakery sells loaves of bread at €3.49 each. The non-daily bread is discounted by 60%. Write a program that starts by reading the number of loaves sold that are not of the day. Then the program should display the usual price of a loaf of bread, the discount for non-fresh and the total final cost.
"""
print("")
#number of non-fresh loafs requested
non_fresh_loafs = float(input("Enter the number of non-fresh loafs today => "))
#operation without discount
total = (non_fresh_loafs * 3.49)
total = round(total, 2)
#operation with discount
discount = abs((total*0.6)-total)
discount = round(discount, 2)

#display
print("")
print("-"*80)
print(f"The regular price is €3.49 a unit there are {non_fresh_loafs} in the order. The total price without discount is €{total}")
print("-"*80)
print(f"The price with 60% discount is €{discount}")
print("-"*80)