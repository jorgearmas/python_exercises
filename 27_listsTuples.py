"""
ENG =>
Write a program that stores the subjects of a course (e.g. Mathematics, Physics, Chemistry, History and Language) in a list and displays the message I study <subject>, where <subject> is each of the subjects in the list.

ESP =>
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
"""

#general variables
subjets = ["Math", "Physics", "Chemistry", "History", "Literature"]

#output
for element in subjets:
    print(f"I study {element}")