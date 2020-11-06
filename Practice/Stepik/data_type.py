# Задание 1
# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.

num1 = float(input())
num2 = float(input())

square = 0.5 * num1 * num2

print(square)



# Задание 2
# Два автомобиля едут навстречу друг другу с постоянными скоростями V1 и V2 км/ч.
# Определите, через какое время автомобили встретятся, если расстояние между ними равно S км.

s = float(input())
v1 = float(input())
v2 = float(input())

result = s / (v1 + v2)

print(float(result))



# Задание 3
# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
# Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).

num1 = float(input())

if(num1 != 0):
    print(1 / num1)
else:
    print('Обратного числа не существует')




# Задание 4
# У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту».
# Напишите программу, которая определяет, какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.

cels = float(input())
far = 5 / 9 * (cels - 32)

print(far)



# Задание 5
# На вход программе подается число – количество собачьих лет.
# В течение первых двух лет собачий год равен 10.510.5 человеческим годам. После этого каждый год собаки равен 4 человеческим годам.
# Напишите программу, которая вычисляет возраст собаки в человеческих годах.

age = int(input())

if 0 < age <= 2:
    print(age * 10.5)
else:
    print((age - 2) * 4 + 21)



# Задание 6
# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

num1 = float(input())

res = num1 * 10
res = res % 10

print(int(res))



# Задание 7
# Дано положительное действительное число. Выведите его дробную часть.

num1 = float(input())
res = num1 - int(num1)
print(round(res, 4))

