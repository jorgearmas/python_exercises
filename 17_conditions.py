"""
ENG =>
In a given company, its employees are evaluated at the end of each year. The points they can obtain in the evaluation start at 0.0 and can increase, resulting in better benefits. The points that employees can achieve can be 0.0, 0.4, 0.6 or more, but not intermediate values between the aforementioned figures. A table with the levels corresponding to each score is shown below. The amount of money earned at each level is €2,400 multiplied by the score of the level.

Unacceptable 0.0
Acceptable 0.4
Meritorious 0.6 or more

Write a program that reads the user's score and indicates the user's performance level, as well as the amount of money the user will receive.

ESP =>
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""
#General variables

unacceptable = 0.0
acceptable = 0.4
meritorious = 0.6

bonusBase = 2400
bonusBase = float(bonusBase)
bonusEarned = 0

#input
performanceLevel = float(input("\nEnter performace level (limit is 1): "))

#condition / output
if performanceLevel == unacceptable:
    bonusEarned = unacceptable * bonusBase
    print(f"\nUnacceptable performance level. Bonus earned: ${bonusEarned}")
elif performanceLevel == acceptable:
    bonusEarned = acceptable * bonusBase
    print(f"\nAcceptable performance level. Bonus earned: ${bonusEarned}")
elif performanceLevel == meritorious or performanceLevel == meritorious+0.2 or performanceLevel == meritorious+0.4:
    bonusEarned = meritorious * bonusBase
    print(f"\nMeritorious performance level. Bonus earned: ${bonusEarned}")
else:
    print(f"\nIncorrect performance level")