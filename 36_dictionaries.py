"""
ENG =>
Write a program that asks for a date in dd/mm/yyyy format and displays the same date in dd format of <month> of yyyy where <month> is the name of the month.

ESP =>
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""
#global variables
dict_date = {}
day = ""
month = ""
year = ""
order_day = ""

#input
usr_date = input("Enter date with the following format (dd/mm/yyyy): ")

#split by "/" will return a list
lst_usr_date = usr_date.split("/")

# number of month conversion
def month_name(month):
    if month == "01":
        month = "January"
    elif month == "02":
        month = "February"
    elif month == "03":
        month = "March"
    elif month == "04":
        month = "April"
    elif month == "05":
        month = "May"
    elif month == "06":
        month = "June"
    elif month == "07":
        month = "July"
    elif month == "08":
        month = "August"
    elif month == "09":
        month = "September"
    elif month == "10":
        month = "October"
    elif month == "11":
        month = "November"
    elif month == "12":
        month = "December"
    
    return(month)

# assigning order to number of day
def day_order(day):
    if day == "01":
        day = "st"
    elif day == "02":
        day = "nd"
    elif day == "03":
        day = "trd"
    else:
        day = "th"
    
    return(day)

#inserting elements of list into a dictionay
for item in lst_usr_date:
    dict_date["day"] = lst_usr_date[0]
    dict_date["month"] = lst_usr_date[1]
    dict_date["year"] = lst_usr_date[2]

#assigning elements of dictionary to variables
for k, v in dict_date.items():
    day = dict_date.get("day")
    month = dict_date.get("month")
    year = dict_date.get("year")

#invoking functions and storing in variables
month = month_name(month)
order_day = day_order(day)

#output
print(f"{month} the {day}{order_day}, {year}")

