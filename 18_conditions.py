"""
ENG =>
Pizzeria Bella Napoli offers vegetarian and non-vegetarian pizzas to its customers. The ingredients for each type of pizza are listed below.

 - Vegetarian ingredients: Pepperoni and tofu.
 - Non-vegetarian ingredients: Pepperoni, Ham and Salmon.

Write a program that asks the user if he wants a vegetarian pizza or not, and depending on his answer shows him a menu with the available ingredients to choose from. Only one ingredient can be chosen in addition to the mozzarella and tomato that are in all the pizzas. At the end of the screen it should be shown whether the pizza chosen is vegetarian or not and all the ingredients it contains.

ESP =>
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

 - Ingredientes vegetarianos: Pimiento y tofu.
 - Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""
#General variable
vegetarianChoise = "vegetarian"
nonVegetarianChoise = "nonvegetarian"
#input
choiseOfPizza = input("\nWould you like a vegetarian pizza or a non-vegetarian pizza? ")
#apply format to input
choiseOfPizza = choiseOfPizza.lower()
choiseOfPizza = choiseOfPizza.strip()
choiseOfPizza = choiseOfPizza.replace("-","")
choiseOfPizza = choiseOfPizza.replace(" - ","")
choiseOfPizza = choiseOfPizza.replace(" ","")


if choiseOfPizza == vegetarianChoise:
    print("\nOptions for vegetarian (choose one)")
    print("1 -- Pepper")
    print("2 -- Tofu")
    vegetarianIngredient = int(input("Enter 1 or 2: "))
    if vegetarianIngredient == 1:
        print("\nYour order is a vegetarian pizza with Pepper")
    elif vegetarianIngredient == 2:
        print("\nYour order is a vegetarian pizza with Tofu")
    else:
        print("\nIncorrect option, please choose again")
elif choiseOfPizza == nonVegetarianChoise:
    print("\nOptions for non-vegetarian (choose one)")
    print("1 -- Pepperoni")
    print("2 -- Ham")
    print("3 -- Salmon")
    nonVegetarianIngredient = int(input("Enter 1 or 2 or 3: "))
    if nonVegetarianIngredient == 1:
        print("\nYour order is a non-vegetarian pizza with Pepperoni")
    elif nonVegetarianIngredient == 2:
        print("\nYour order is a non-vegetarian pizza with Ham")
    elif nonVegetarianIngredient == 3:
        print("\nYour order is a non-vegetarian pizza with Salmon")
    else:
        print("\nIncorrect option, please choose again")
else:
    print("\nIncorrect option, please choose again")