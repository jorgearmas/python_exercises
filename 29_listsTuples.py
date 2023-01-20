"""
ENG =>
Write a program that stores the subjects of a course (e.g. Mathematics, Physics, Chemistry, History and Language) in a list, asks the user the grade he/she has obtained in each subject and removes from the list the subjects passed. At the end the program should display on the screen the subjects that the user has to repeat.

ESP =>
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""
#list
subjets = ["Math", "Physics", "Chemistry", "History", "Literature"]
math = 0
physics = 0
chemistry = 0
history = 0
literature = 0

#input / verification
for element in subjets:
    if element == "Math":
        math = int(input("Grade obtained in math: "))
        if math > 60:
            subjets.remove(element)
    elif element == "Physics":
        physics = int(input("Grade obtained in physics: "))
        if physics > 60:
            subjets.remove(element)
    elif element == "Chemistry":
        chemistry = int(input("Grade obtained in chemistry: "))
        if chemistry > 60:
            subjets.remove(element)
    elif element == "History":
        history = int(input("Grade obtained in history: "))
        if history > 60:
            subjets.remove(element)                 
    elif element == "Literature":
        literature = int(input("Grade obtained in literature: "))
        if literature > 60:
            subjets.remove(element)

for item in subjets:
    print(item)