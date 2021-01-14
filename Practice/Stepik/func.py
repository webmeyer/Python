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



# Задача 10
# Напишите функцию, принимающую в качестве аргумента число и возвращающую количество делителей данного числа.

def get_factors(num):
    numbers = []
    for i in range(1, num + 1):
        if num % i == 0:
            numbers.append(i)
    return numbers

def number_of_factors(num):
    return len(get_factors(num))

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))



# Задача 11
# Напишите функцию, которая принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.

def find_all(target, symbol):
    target_list = []
    for i in range(len(target)):
        if target[i] == symbol:
            target_list.append(i)
    return target_list

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))



# Задача 12
# Напишите функцию, которая принимает в качестве аргументов два отсортированных по возрастанию списка, состоящих из целых чисел,
# и объединяет их в один отсортированный список.

# объявление функции
def merge(list1, list2):
    return sorted(list1 + list2)

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))



# Задача 13
# На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания.
# Из данных строк формируются списки чисел.
# Напишите программу, которая объединяет указанные списки в один отсортированный список с помощью функции, а затем выводит его.

def quick_merge(list1, list2):
    result = []
    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2
    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]
    return result

n = int(input())
numbers1 = [int(c) for c in input().split()]
for _ in range(1, n):
    numbers1 = quick_merge(numbers1, [int(c) for c in input().split()])
print(*numbers1)



# Задача 14
# Напишите функцию, которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в противном случае.

def is_valid_triangle(side1, side2, side3):
    return ((a + b) > c) and ((a + c) > b) and ((b + c) > a)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))



# Задача 15
# Напишите функцию, которая принимает в качестве аргумента натуральное число
# и возвращает значение True если число является простым и False в противном случае.

# объявление функции
def is_prime(num):
    if num % 2 == 0:
        return num == 2
    if num == 1:
        return False
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))



# Задача 16
# Напишите функцию, которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.
# Пароль является надежным если:
#
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

def is_password_good(password):
    if len(password) < 8:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for c in password:
        if c.isupper():
            flag1 = True
        elif c.islower():
            flag2 = True
        elif c.isdigit():
            flag3 = True
    return flag1 and flag2 and flag3

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))



# Задача 17
# Напишите функцию, которая принимает в качестве аргументов два слова word1 и word2
# и возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.

# объявление функции
def is_one_away(word1, word2):
    count = 0
    if len(word1) == len(word2):
        for i in word1:
            for j in word2:
                if i == j:
                    count += 1
        if count == len(word1) - 1 or count - 1 == len(word1):
            return True
        else:
            return False
    else:
        return False

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))



# Задача 18
# Напишите функцию, которая принимает в качестве аргумента строку text и возвращает значение True если указанный текст является палиндромом и False в противном случае.
#
# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы ",", ".", "!", "?", "-"

# объявление функции
def is_palindrome(text):
    txt_list = []
    for char in text:
        if char.isalpha():
            txt_list.append(char.lower())
    if txt_list[:] == txt_list[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))



# Задача 19
# Напишите функцию, которая принимает в качестве аргумента строковое значение пароля и возвращает значение True если пароль является действительным, и False в противном случае.
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.

# объявление функции
def is_valid_password(password):
    # флаги
    flag_1 = True
    flag_2 = False
    flag_3 = False

    # приведение строки к списку и разделение на отдельные элементы
    pass_list = password.split(":")
    palindrome = ''.join(pass_list[0])
    simple_num = ''.join(pass_list[1])
    even_num = ''.join(pass_list[-1])

    # если длина списка больше 3-ёх элементов
    if len(pass_list) > 3:
        return False

    # если один из элементов списка не является числом
    if palindrome.isalpha() or simple_num.isalpha() or even_num.isalpha():
        return False

    # проверка на простое число
    if int(simple_num) == 1:
        flag_1 = False
    for i in range(2, int(simple_num)):
        if int(simple_num) % i == 0:
            flag_1 = False

    # проверка на палиндромность
    if palindrome == palindrome[::-1]:
        flag_2 = True

    # проверка на чётность
    if int(even_num) % 2 == 0:
        flag_3 = True

    # сравниваем значения флагов
    if flag_1 == True and flag_2 == True and flag_3 == True:
        return True
    else:
        return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))



# Задача 20
# Напишите функцию, которая принимает в качестве аргумента непустую строку text, состоящую из символов '(', ')' и возвращает значение True
# если поступившая на вход строка является правильной скобочной последовательностью и False в противном случае.
#
# Примечание 1. Правильной скобочной последовательностью называется строка,
# состоящая только из символов ( и ), где каждой открывающей скобке найдется парная закрывающая скобка.

# объявление функции
def is_correct_bracket(text):
    meetings = 0
    for c in text:
        if c == '(':
            meetings += 1
        elif c == ')':
            meetings -= 1
            if meetings < 0:
                return False

    return meetings == 0

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))



# Задача 21
# Напишите функцию, которая выводит звездный равнобедренный треугольник с основанием и высотой равными 15 и 8 соответственно:

# объявление функции
def draw_triangle():
    for i in range(8):
        k1 = 7 - i
        k2 = 7 + i
        for j in range(k2 + 1):
            print('*' if j >= k1 else ' ', end='')
        print()


# основная программа
draw_triangle()  # вызов функции



# Задача 22
# Напишите функцию которая принимает в качестве аргумента натуральное число quantity – количество товаров в заказе и возвращает стоимость доставки.

# объявление функции
def get_shipping_cost(quantity):
    cost = 0
    while quantity > 0:
        if quantity == 1:
            cost += 1000
            quantity -= 1
        else:
            cost += 120
            quantity -= 1
    return cost


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))



# Задача 23

# объявление функции
from math import factorial
def compute_binom(n, k):
    bino1 = factorial(n)
    bino2 = factorial(k)*factorial(n-k)
    return bino1//bino2

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))



# Задача 24
# Напишите функцию, которая принимает в качестве аргумента натуральное число num и возвращает его словесное описание на русском языке.

def number_to_words(num):
    zero_to_ninety_nine = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять',
                           'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
                           'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'двадцать один',
                           'двадцать два', 'двадцать три', 'двадцать четыре', 'двадцать пять', 'двадцать шесть',
                           'двадцать семь', 'двадцать восемь', 'двадцать девять', 'тридцать', 'тридцать один',
                           'тридцать два', 'тридцать три', 'тридцать четыре', 'тридцать пять', 'тридцать шесть',
                           'тридцать семь', 'тридцать восемь', 'тридцать девять', 'сорок', 'сорок один', 'сорок два',
                           'сорок три', 'сорок четыре', 'сорок пять', 'сорок шесть', 'сорок семь', 'сорок восемь',
                           'сорок девять', 'пятьдесят', 'пятьдесят один', 'пятьдесят два', 'пятьдесят три',
                           'пятьдесят четыре', 'пятьдесят пять', 'пятьдесят шесть', 'пятьдесят семь',
                           'пятьдесят восемь', 'пятьдесят девять', 'шестьдесят', 'шестьдесят один', 'шестьдесят два',
                           'шестьдесят три', 'шестьдесят четыре', 'шестьдесят пять', 'шестьдесят шесть',
                           'шестьдесят семь', 'шестьдесят восемь', 'шестьдесят девять', 'семьдесят', 'семьдесят один',
                           'семьдесят два', 'семьдесят три', 'семьдесят четыре', 'семьдесят пять', 'семьдесят шесть',
                           'семьдесят семь', 'семьдесят восемь', 'семьдесят девять', 'восемьдесят', 'восемьдесят один',
                           'восемьдесят два', 'восемьдесят три', 'восемьдесят четыре', 'восемьдесят пять',
                           'восемьдесят шесть', 'восемьдесят семь', 'восемьдесят восемь', 'восемьдесят девять',
                           'девяносто', 'девяносто один', 'девяносто два', 'девяносто три', 'девяносто четыре',
                           'девяносто пять', 'девяносто шесть', 'девяносто семь', 'девяносто восемь',
                           'девяносто девять']
    return zero_to_ninety_nine[num]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))



# Задача 25
# Напишите функцию, которая принимает на вход два аргумента language – язык ru или en и number – номер месяца (от 1 до 12)
# и возвращает название месяца на русском или английском языке.

# объявление функции
def get_month(language, number):
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
              'декабрь']
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december']

    if language == 'ru':
        return lng_ru[number - 1]
    else:
        return lng_en[number - 1]

# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))



# Задача 26
# Магическая дата – это дата, когда день, умноженный на месяц, равен числу образованному последними двумя цифрами года.
#
# Напишите функцию, которая принимает в качестве аргумента строковое представление корректой даты и возвращает значение True если дата является магической и False в противном случае.

# объявление функции
def is_magic(date):
    date_list = date.split('.')
    magic_number = int(date_list[0]) * int(date_list[1])
    last_num = date_list[-1]
    last_num = last_num[2:]
    if magic_number == int(last_num):
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))



# Задача 27
# Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.
# Напишите функцию, которая принимает в качестве аргумента строку текста на английском языке и возвращает значение True если текст является панграммой и False в противном случае.

# объявление функции
# объявление функции
def is_pangram(text):
    text = text.replace(' ', '').lower()
    return len(set(text)) == 26

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))