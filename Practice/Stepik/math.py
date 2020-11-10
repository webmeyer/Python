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