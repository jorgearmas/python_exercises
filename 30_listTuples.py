"""
ENG =>
Write a program that stores the vectors (1,2,3) and (-1,0,2) in two lists and displays their scalar product.

ESP => Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
"""
#lists
vectorA = [1,2,3]
vectorB = [-1,0,2]

print(f"\nVector A: {vectorA}")
print(f"\nVector B: {vectorB}")

for item in vectorA:
    for element in vectorB:
        if item == vectorA[0] and element == vectorB[0]:
            set1 = item*element
        elif item == vectorA[1] and element == vectorB[1]:
            set2 = item*element
        elif item == vectorA[2] and element == vectorB[2]:
            set3 = item*element

print(f"\nScalar product = {set1+set2+set3}")