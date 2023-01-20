"""
ENG =>
Write a program that stores the matrices in a list and displays their product on the screen.

A = (1, 2, 3
     4, 5, 6) 2*3

B = (-1, 0,
      0, 1
      1, 1) 3*2

ESP =>
Escribir un programa que almacene las matrices en una lista y muestre por pantalla su producto

A = (1, 2, 3
     4, 5, 6) - 2*3

B = (-1, 0,
      0, 1
      1, 1) - 3*2
"""

#matrices
matrixA = [[1, 2, 3],
           [4, 5, 6]]

matrixB = [[-1, 0],
           [0, 1],
           [1, 1]]

product = [[0, 0],
           [0, 0]]

for i in range(len(matrixA)): #Iteration through rows in matrixA
    for j in range(len(matrixB[0])): #Iteration through columns in matrixB
        for k in range(len(matrixB)): #Iteration through rows in matrixB
            product[i][j] += matrixA[i][k] * matrixB[k][j]

print(f"\nProduct Matrix:")
for item in product:
    print(item)