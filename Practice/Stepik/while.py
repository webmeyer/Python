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