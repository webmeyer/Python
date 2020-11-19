# ЦИКЛ FOR

# Задание 1
# Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.
# Программа должна вывести 10 раз текст «Python is awesome!», каждый на отдельной строке.

for i in range(10):
    print('Python is awesome!')



# Задание 2
# Дано предложение и количество раз которое его надо повторить. Напишите программу, которая повторяет данное предложение нужное количество раз.
# В первой строке записано текстовое предложение, во второй — количество повторений.
# Программа должна вывести указанное текстовое предложение нужное количество раз. Каждое повторение должно начинаться с новой строки.

text = input()
count = int(input())

for i in range(count):
    print(text)



# Задание 3
# Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:
# 6AAA, 5BBBB, 1E, 9TTTTT, G

for _ in range(6):
    print('AAA')
for _ in range(5):
    print('BBBB')
print('E')
for _ in range(9):
    print('TTTTT')
print('G')



# Задание 4
# Напишите программу, которая печатает звездный прямоугольник размерами n * 19
# На вход программе подается натуральное число n.
# Программа должна вывести звездный прямоугольник размерами n x 19.

num1 = int(input())

for i in range(num1):
    print('*' * 19)



# Задание 5
# Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9, каждая с указанной строкой текста.
# Программа должна вывести десять строк в соответствии с условием задачи.

name = input()

for i in range(10):
    print(i, name)



# Задание 6
# На вход программе подается натуральное число n.
# Напишите программу, которая для каждого из чисел от 00 до nn (включительно) выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).
# Программа должна вывести текст в соответствии с условием задачи.

num1 = int(input())
print('Квадрат числа 0 равен 0')

for i in range(num1):
    print('Квадрат числа ' + i + 'равен ' + (i ** i))



# Задание 7
# На вход программе подается натуральное число n(n≥2) – катет прямоугольного равнобедренного треугольника.
# Напишите программу, которая выводит звездный треугольник в соответствии с примером.
# Программа должна вывести треугольник в соответствии с условием задачи.

num1 = int(input())

for i in range(num1):
    print('*' * (num1 - i))



# Задание 8
# На вход программе подается три натуральных числа m,p,n:
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.

# Напишите программу, которая предсказывает размер популяции организмов.
# Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-м днем.

m = int(input()) # стартовое количество организмов;
p = int(input()) / 100 # среднесуточное увеличение в %;
n = int(input()) # количество дней для размножения.

print(1, float(m))
for i in range(1, n, 1):
    population = m * p
    m = population + m
    print(i+1, float(m))



# Задание 9
# Даны два целых числа m и n (m ≤ n).
# Напишите программу, которая выводит все числа от m до n включительно.

m = int(input())
n = int(input())

for i in range(m, n+1):
    print(i)



# Задание 9
# Даны два целых числа m и n (m ≤ n).
# Напишите программу, которая выводит все числа от m до n включительно.

m = int(input())
n = int(input())

if(m < n):
    for i in range(m, n+1):
        print(i)
elif(m > n):
    for i in range(m, n-1, -1):
        print(i)
else:
    print("Числа равны:", m)



# Задание 10
# Даны два целых числа m и n (m > n).
# Напишите программу, которая выводит все нечетные числа от m до n включительно в порядке убывания.
# Примечание: Попробуйте решить задачу двумя способами: с использованием условного оператора if и без него.

m = int(input())
n = int(input())

for i in range(m, n - 1, -1):
    if(i % 2 != 0):
        print(i)

# Решение без if

m = int(input())
n = int(input())

m = ((m - 1) // 2) * 2 + 1

for i in range(m, n - 1, -2):
    print(i)



# Задание 11
# Даны два целых числа m и n (m ≤ n):
# число кратно 17;
# число оканчивается на 9;
# число кратно 3 и 5 одновременно.

# Напишите программу, которая выводит все числа от m до n включительно удовлетворяющие хотя бы одному из условий выше.

m = int(input())
n = int(input())

for i in range(m, n + 1):
    if(i % 17 == 0):
        print(i)
    elif(i % 10 == 9):
        print(i)
    elif(i % 3 == 0 and i % 5 == 0):
        print(i)



# Задание 12
# Дано натуральное число n.
# Напишите программу, которая выводит таблицу умножения на n.

n = int(input())

for i in range(1, 11):
    print(n, "x", i, "=", n * i)



# Задание 13
# На вход программе подаются два целых числа a и b (a < b).
# Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно,
# куб которых оканчивается на 4 или 9.

a = int(input())
b = int(input())

count = 0
for i in range(a, b + 1):
    if(i ** 3 % 10 == 4 or i ** 3 % 10 == 9):
        count += 1
print(count)



# Задание 14
# На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке.
# Напишите программу, которая подсчитывает сумму введенных чисел.

n = int(input())
summ = 0

for i in range(n):
    number = int(input())
    summ += number
print(summ)



# Задание 15
# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет значение выражения: (1 + (1 / 2) + (1 / 3) + ... + (1 / n)) -ln(n).

import math

n = int(input())
summ = 0

for i in range(n + 1):
    if i != 0:
        drob = (1 / i)
        summ += drob
result = summ - math.log(n)
print(result)



# Задание 16
# На вход программе подается натуральное число n.
# Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно)
# квадрат которых оканчивается на 2, 5, или 8.

n = int(input())
summ = 0

for i in range(1, n + 1):
    if(i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8):
        summ += i
print(summ)



# Задание 17
# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет n!
# Примечание. Факториалом натурального числа nn, называется произведение всех натуральных чисел от 1 до n

n = int(input())
result = 1

for i in range(n + 1):
    if i != 0:
        result *= i
print(result)



# Задание 18
# На вход программе подаются 10 целых чисел, каждое на отдельной строке.
# Программа должна вывести произведение отличных от нуля чисел.

result = 1

for i in range(1, 11):
    num = int(input())
    if(num != 0):
        result *= num
print(result)



# Задание 19
# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет сумму всех его делителей.

n = int(input())
result = 0

for i in range(1, n + 1, 1):
    if(n % i == 0):
        result += i
print(result)



# Задание 20
# На вход программе подается натуральное число n.
# Напишите программу вычисления знакочередующей суммы 1-2+3-4+5-6 + (-1)^{n+1}n.

n = int(input())
result = 0

for i in range(1, n + 1):
    if(i % 2 == 0):
        result -= i
    else:
        result += i
print(result)