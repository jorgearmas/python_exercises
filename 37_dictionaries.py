"""
ESP =>
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 

 - Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se  añadirá al diccionario. 
 - Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
 
 Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""
#imports
import os

#global variables
invoice_pile = {}
production_pile = {}
menu_option = 0

#add new item to dictionary
def add_invoice():
    os.system('cls')
    global production_pile
    add_invoice_session = 1
    invoice_number = ""
    invoice_value = 0
    while add_invoice_session == 1:
        invoice_number = input("\nEnter invoice number: ")
        invoice_value = float(input("Enter invoice value : $"))
        invoice_pile[invoice_number] = invoice_value
        add_invoice_session = int(input("--Would you like to add more invoices?-- "))
    production_pile = invoice_pile
    if add_invoice_session != 1:
        os.system('cls')
        menu()

#modify or delete value from item
def pay_invoice(prod_dictionary):
    os.system('cls')
    pay_invoice_session = 1
    invoice_number = ""
    amount_to_pay = 0
    remaining = 0
    to_del = ""
    while pay_invoice_session == 1:
        invoice_number = input("\nEnter invoice code / number: ")
        if invoice_number in prod_dictionary:
            amount_to_pay = float(input("Enter the amount to pay: "))
            for k, v in prod_dictionary.items():
                if k == invoice_number and amount_to_pay < v:
                    remaining = v-amount_to_pay
                    prod_dictionary[k] = remaining
                elif k == invoice_number and amount_to_pay == v:
                    to_del = k
            if to_del != "":
                del prod_dictionary[to_del]
        else:
            print("NOT FLAG")
        pay_invoice_session = int(input("--Would you like to pay another invoice?-- "))
    if pay_invoice_session != 1:
        os.system('cls')
        menu()
        return(prod_dictionary)

#display dictionary contents
def current_status():
    os.system('cls')
    status_session = 1
    global production_pile
    while status_session == 1:
        print(production_pile)
        status_session = int(input("--Would you like to stay?-- "))
    if status_session != 1:
        os.system('cls')
        menu()

#main menu
def menu():
    global production_pile
    print("-"*33)
    print(" Invoice managment program IMP")
    print("-"*33)
    print("1 ..... Add a new invoice")
    print("2 ..... Pay existing invoice")
    print("3 ..... Verify status")
    print("4 ..... Close")
    print("-"*33)
    menu_option = int(input("Enter option => "))
    print("-"*33)
    if menu_option == 1:
        add_invoice()
    elif menu_option == 2:
        production_pile = pay_invoice(invoice_pile)
    elif menu_option == 3:
        current_status()
    elif menu_option == 5:
        exit()

#entry point
if __name__ == "__main__":
    menu()