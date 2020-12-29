# ФУНКЦИИ (И ВСЁ ЧТО С НИМИ СВЯЗАНО)

# Задача 1
# Напишите функцию draw_box(),
# которая выводит звездный прямоугольник с размерами 10x14 в соответствии с образцом:

def draw_box():
    b = 14
    a = 10
    simvol = '*'
    print(simvol * a)
    for i in range(b - 2):
        print(simvol, ' ' * (a - 2), simvol, sep='')
    print(simvol * a)

draw_box()



# Задача 2
# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10

def draw_triangle():
    n = 10
    for i in range(1, n + 1):
        print('*' * i)

draw_triangle()



# Задача 3
# Напишите функцию c аргументами, которая выводит звездный прямоугольный треугольник с катетами, равными 10
def draw_box(width, height):
    for i in range(width):
        print('*' * height)

draw_box(10, 14)



# Задача 4
# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
# Сменим файл
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.

def draw_triangle(fill, base):
    a = list(range(1, base // 2 + 1 + 1)) + list(range(base // 2, 0, -1))
    for i in a:
        print(fill * i)

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)



# Задача 5
# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
#
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.
#
# Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.

def print_fio(name, surname, patronymic):
    print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name,surname,patronymic)



# Задача 6
# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

# объявление функции
def print_digit_sum(num):
    total = 0
    while num != 0:
        last_digit = num % 10
        if last_digit > 0:
            total += last_digit
        num = num // 10
    print(total)

# считываем данные
num = int(input())

# вызываем функцию
print_digit_sum(num)



# ФУНКЦИИ С ВОЗВРАТОМ ЗНАЧЕНИЙ
# Задача 7
# Напишите функцию, которая принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях.

def convert_to_miles(km):
    miles = km * 0.6214
    return float(miles)

print(convert_to_miles(1))
print(convert_to_miles(5))
print(convert_to_miles(10))

num = int(input())
print(convert_to_miles(num))



# Задача 8
# Напишите функцию, которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.

def get_days(month):
    monthes = [31,28,31,30,31,30,31,31,30,31,30,31]
    return monthes[month - 1]

num = int(input())
print(get_days(num))



# Задача 9
# Напишите функцию, принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.

def get_factors(num):
    numbers = []
    for i in range(1, num + 1):
        if num % i == 0:
            numbers.append(i)
    return numbers

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))