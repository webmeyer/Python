import math

num1 = math.sqrt(2)    # вычисление корня квадратного из двух
num2 = math.ceil(3.8)  # округление числа вверх
num3 = math.floor(3.8) # округление числа вниз

print(num1)
print(num2)
print(num3)


# Задание 1
# Напишите программу определяющую Eвклидово расстояние между двумя точками, координаты которых заданы.

from math import *

x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

result = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(result)



# Задание 2
# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.

from math import *

radius = float(input())

square = pi * radius ** 2
length = 2 * pi * radius

print(square)
print(length)



# Задание 3
# На вход программе подается два вещественных числа a и b, каждое на отдельной строке.
# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

from math import *

a = float(input())
b = float(input())

medAriphmetic = (a + b) / 2
medGeometry = sqrt(a * b)
medGarmonic = (2 * a * b) / (a + b)
medQuadratic = sqrt((a ** 2 + b ** 2) / 2)

print(medAriphmetic)
print(medGeometry)
print(medGarmonic)
print(medQuadratic)



# Задание 4
# Напишите программу, вычисляющую значение тригонометрического выражения sin(x)+cos(x)+tan^2(x)
# по заданному числу градусов x.
# На вход программе подается одно вещественное число xx измеряемое в градусах.

from math import *

x = float(input())

trigonometry = sin(radians(x)) + cos(radians(x)) + (tan(radians(x))) ** 2
print(trigonometry)



# Задание 5
# Напишите программу, вычисляющее значение ⌈x⌉ + ⌊x⌋ по заданному вещественному числу x.
# На вход программе подается одно вещественное число x.
# Программа должна вывести одно число – значение указанного выражения.

from math import ceil, floor

x = float(input())

result = ceil(x) + floor(x)
print(result)



# Задание 6
# Даны три вещественных числа aa, bb, cc. Напишите программу, которая находит вещественные корни квадратного уравнения ax^2 + bx + c = 0.
# На вход программе подается три вещественных числа a!=0, b, c каждое на отдельной строке.
# Программа должна вывести вещественные корни уравнения если они существуют или текст «Нет корней» в противном случае.

from math import *

a = float(input())
b = float(input())
c = float(input())

discr = (b ** 2) - 4 * a * c

if (discr > 0):
    x1 = (-b + sqrt(discr)) / (2 * a)
    x2 = (-b - sqrt(discr)) / (2 * a)

    print(min(x1, x2))
    print(max(x1, x2))

elif (discr == 0):
    x = -b / (2 * a)
    print(x)

else:
    print('Нет корней')



# Задание 7
# Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами.
# Даны два числа: натуральное число n и вещественное число a.
# Напишите программу, которая находит площадь указанного правильного многоугольника.

from math import *

n = int(input())
a = float(input())

S = n * (a ** 2) / 4 * tan(pi / n)

print(float(S))


# Завершено