# ЦИКЛЫ WHILE

# Задание 1
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» (без кавычек).
# Напишите программу, которая выводит члены данной последовательности.

text = input()
result = 0

while(text != 'стоп' and text != 'хватит' and text != 'достаточно'):
    text = input()
    result += 1
print(result)




# Задание 2
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек).
# Напишите программу, которая выводит члены данной последовательности.

text = input()

while(text != 'КОНЕЦ' and text != 'конец'):
    print(text)
    text = input()



# Задание 3
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек).
# Напишите программу, которая выводит общее количество членов данной последовательности.

text = input()
result = 0

while(text != 'стоп' and text != 'хватит' and text != 'достаточно'):
    text = input()
    result += 1
print(result)



# Задание 4
# На вход программе подается последовательность целых чисел делящихся на 7, каждое число на отдельной строке.
# Концом последовательности является любое число не делящееся на 7
# Напишите программу, которая выводит члены данной последовательности.

nums = int(input())

while(nums % 7 == 0):
    print(nums)
    nums = int(input())



# Задание 5
# На вход программе подается последовательность целых чисел, каждое число на отдельной строке.
# Концом последовательности является любое отрицательное число.
# Напишите программу, которая выводит сумму всех членов данной последовательности.

nums = int(input())
result = 0

while(nums >= 0):
    result += int(nums)
    nums = int(input())
print(result)



# Задание 6
# На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика, каждое число на отдельной строке.
# Концом последовательности является любое отрицательное число, либо число большее 5.
# Напишите программу, которая выводит количество пятерок.

nums = int(input())
result = 0

while(nums >= 0 and nums <= 5):
    if(nums == 5):
        result += 1
    nums = int(input())
print(result)



# Задание 7
# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево, к тому же ведьмак не принимает купюры, он принимает только чеканные монеты.
# В мире ведьмака существуют монеты с номиналами 1, 5, 10, 25.
# Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.
# На вход программе подается одно натуральное число, цена за услугу ведьмака.
# Программа должна вывести минимально возможное количество чеканных монет для оплаты.

cost = int(input())
count = 0

while(cost > 0):
    if(cost >= 25):
        cost -= 25
        count += 1
    elif(cost >= 10 and cost <= 25):
        cost -= 10
        count += 1
    elif(cost >= 5 and cost <= 10):
        cost -= 5
        count += 1
    elif(cost >= 1 and cost <= 5):
        cost -= 1
        count += 1
print(count)



# Задание 8
# Дано натуральное число.
# Напишите программу, которая выводит его цифры в столбик в обратном порядке.

num1 = int(input())

while(num1 != 0):
    last_digit = num1 % 10
    print(last_digit)
    num1 = num1 // 10



# Задание 9
# Дано натуральное число.
# Напишите программу, которая меняет порядок цифр числа на обратный.

num1 = int(input())
while(num1 != 0):
    last_digit = num1 % 10
    print(last_digit, end='')
    num1 = num1 // 10



# Задание 10
# Дано натуральное число n, (n≥10).
# Напишите программу, которая определяет его максимальную и минимальную цифры.

num1 = int(input())
minimum = num1 % 10
maximum = num1 % 10

while(num1 != 0):
    last_digit = num1 % 10
    if(last_digit > maximum):
        maximum = last_digit
    elif(last_digit < minimum):
        minimum = last_digit
    num1 = num1 // 10
print('Максимальная цифра равна', maximum)
print('Минимальная цифра равна', minimum)



# Задание 11
# Дано натуральное число n, (n≥10).
# Напишите программу, которая вычисляет:
# - сумму его цифр;
# - количество цифр в нем;
# - произведение его цифр;
# - среднее арифметическое его цифр;
# - его первую цифру;
# - сумму его первой и последней цифры.

num1 = int(input())
total = 0
count = 0
proizvedenie = 1
average = 0
first_and_last_digit = 0

last_digit = num1 % 10 # - последняя цифра;

while(num1 != 0):
    first_digit = num1 % 10  # последняя цифра, по завершеню цикла станет первой цифрой числа;
    total += first_digit # - сумма цифр;
    count += 1 # - количество цифр;
    proizvedenie *= first_digit # - произведение цифр;
    num1 = num1 // 10 # убираем последнюю цифру числа

average = total / count # - среднее арифметическое его цифр;
first_and_last_digit = first_digit + last_digit # - сумма его первой и последней цифры.

# Выводим в консоль по условию задачи

print(total)
print(count)
print(proizvedenie)
print(average)
print(first_digit)
print(first_and_last_digit)



# Задание 12
# Дано натуральное число n, (n > 9)
# Напишите программу, которая определяет его вторую (с начала) цифру

num1 = int(input())
while(num1 != 0):
    last_digit = num1 % 10
    print(last_digit, end='')
    num1 = num1 // 10



# Задание 13
# Дано натуральное число
# Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

num1 = int(input())
last_digit = num1 % 10
print(last_digit)
flag = False

while(num1 > 0):
    first_digit = num1 % 10
    if(first_digit < last_digit):
        flag = False
    num1 = num1 // 10
if(flag == False):
    print('YES')
else:
    print('NO')



# Задание 14
# Дано натуральное число.
# Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

num1 = int(input())
flag = 'YES'

while num1 // 10 != 0 :
    first = num1 % 10
    num1 = num1 // 10
    if first > num1 % 10:
        flag = 'NO'
print(flag)



# Задание 15
# На вход программе подается число n > 1.
# Напишите программу, которая выводит его наименьший отличный от 1 делитель.

num1 = int(input())
i = 2

while(num1 % i != 0):
    i += 1
print(i)



# Задание 16
# На вход программе подается число n;
# Напишите программу, которая выводит числа от 1 до n включительно за исключением:
# - чисел от 5 до 9 включительно;
# - чисел от 17 до 37 включительно;
# - чисел от 78 до 87 включительно.

n = int(input())

for i in range(1, n + 1):
    if(5 <= i <= 9):
        continue
    elif(17 <= i <= 37):
        continue
    elif(78 <= i <= 87):
        continue
    print(i)



# ИТОГОВАЯ РАБОТА
# Задание 17
# Ревью кода

n = int(input())
s = 0
while n > 9:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)



# Задание 18
# Ревью кода

n = 8
count = 0
maximum = -10 ** 6 - 1
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')



# Задание 19
# Ревью кода

n = 4
count = 0
maximum = -10 ** 6 - 1
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')



# Задание 20
# Ревью кода

n = int(input())
count = 0

while(count < n):
    print('*' * 19)
    for i in range(n - 2):
        print('*', ' ' * 15, '*')
    count += 1
    print('*' * 19)
    break



# Задание 21
# Дано натуральное число (n > 99).
# Напишите программу, которая определяет его третью (с начала) цифру.

n = int(input())

while(n > 99):
    last_digit = n % 10
    n //= 10
print(last_digit)



# Задание 22
# Дано натуральное число.
# Напишите программу, которая вычисляет:
# - количество цифр 3 в нем;
# - сколько раз в нем встречается последняя цифра;
# - количество четных цифр;
# - сумму его цифр, больших пяти;
# - произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# - сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

n = int(input())
three = 0 # количество цифр 3 в нем;
last = n % 10 # последняя цифра в числе
lastCount = 0 # сколько раз в нем встречается последняя цифра;
even = 0 # количество четных цифр;
amount = 0 # сумму его цифр, больших пяти;
multiSeven = 1 # произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
zeroFive = 0 # сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

while(n != 0):
    last_digit = n % 10
    if(last_digit == 3):
        three += 1
    if(last_digit % 2 == 0):
        even += 1
    if(last_digit > 5):
        amount += last_digit
    if(last_digit > 7):
        multiSeven *= last_digit
    if(last_digit == 0 or last_digit == 5):
        zeroFive += 1
    if(last_digit == last):
        lastCount += 1
    n //= 10

print(three)
print(lastCount)
print(even)
print(amount)
print(multiSeven)
print(zeroFive)

# FINISHED