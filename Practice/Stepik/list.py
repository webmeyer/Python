# СПИСКИ
# Задача 1
# На вход программе подается одно число n.
# Напишите программу, которая выводит список [1, 2, 3, ..., n].

num1 = int(input())
listNumbers = list(range(1, num1 + 1))
print(listNumbers)



# Задача 2
# На вход программе подается одно число n.
# Напишите программу, которая выводит список, состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.

num1 = int(input())
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listABC = []

for i in range(num1):
    listABC.append(abc[i])
print(listABC)



# Задача 3
# Дополните приведенный код
# Чтобы элемент списка имеющий значение Green заменился на значений Зеленый, а элемент Violet на Фиолетовый.
# Далее необходимо вывести полученный список.

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3], rainbow[-1]  = 'Зеленый', 'Фиолетовый'
print(rainbow)



# Задача 4
# Дополните приведенный код, чтобы он:
# Вывел длину списка;
# Вывел последний элемент списка;
# Вывел список в обратном порядке (вспоминаем срезы);
# Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
# Вывел список с удаленным первым и последним элементами.
# Примечание. Каждый вывод осуществлять с новой строки.

numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')
print(numbers[1:-1:1])



# Задача 5
# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает из указанных строк список и выводит его.

n = int(input())
new_list = []

for i in range(n):
    string = str(input())
    new_list.append(string)
print(new_list)



# Задача 6
# Напишите программу, выводящую следующий список:
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# Примечание. Последний элемент списка состоит из 26 символов z.

abc = 'abcdefghijklmnopqrstuvwxyz'
abc_list = []
count = 1

for i in range(len(abc)):
    abc_list.append(abc[i] * count)
    count += 1
print(abc_list)



# Задача 7
# Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
sum = 0
for i in range(len(numbers)):
    quatro = (numbers[i] * numbers[i])
    sum += quatro
print(sum)



# Задача 8
# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая для каждого введенного числа x выводит значение функции f(x) = x^2 + 2x + 1f(x) = x + 2x + 1, каждое на отдельной строке.

n = int(input())
numbers = []
total = []

for i in range(n):
    number = int(input())
    numbers.append(number)
    quatro = (number + 1) ** 2
    total.append(quatro)
print(*numbers, sep='\n')
print()
print(*total, sep='\n')



# Задача 9
# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список их кубов.

n = int(input())
numbers = []
quatro = []

for i in range(n):
    num1 = int(input())
    quat = num1 ** 3
    quatro.append(quat)
print(quatro)



# Задача 10
# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.

n = int(input())
numbers = []

for i in range(n - 1):
    num1 = int(input())
    numbers.append(num1)

del numbers[::2]
print(numbers)



# Задача 11
# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.
# Напишите программу, которая выводит инициалы человека.

name = input().split()
first = []

for i in name:
    first.append(i[0])
    '.'.join(first)
print('.'.join(first) + '.')



# Задача 12
# В операционной системе Windows полное имя файла состоит из буквы диска,
# после которого ставится двоеточие и символ  "\",
# затем через такой же символ перечисляются подкаталоги (папки), в которых находится файл,
# в конце пишется имя файла (C:\Windows\System32\calc.exe).
#
# На вход программе подается одна строка с корректным именем файла в операционной системе Windows.
# Напишите программу, которая разбирает строку на части, разделенные символом "\". Каждую часть вывести в отдельной строке.

print('\n'.join(input().split('\\')))



# Задача 13
# На вход программе подается строка текста, содержащая целые числа.
# Напишите программу, которая по заданным числам строит столбчатую диаграмму.

numbers = (int(c) for c in input().split())
for num in numbers:
    print('+' * num)



# Задача 14
# На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.
# Напишите программу, которая определяет является ли введенная строка текста корректным ip-адресом.

ip = input().split('.')
adress_valid_list = []

for addr in ip:
    if 0 <= int(addr) <= 255:
        adress_valid_list.append(addr)
if len(adress_valid_list) == 4:
    print('ДА')
else:
    print('НЕТ')



# Задача 15
# На вход программе подается строка текста и строка разделитель.
# Напишите программу, которая вставляет указанный разделитель между каждым символом введенной строки текста.

str1 = input()
dash = input()

print(dash.join(str1))



# Задача 16
# На вход программе подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел.
# Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

n = int(input())
num_list = []

for i in len(str1):
    numb = input()



# Задача 17
# На вход программе подается натуральное число n.
# Напишите программу, которая создает список состоящий из делителей введенного числа.

number = int(input())
numbers = []

for i in range(1, number + 1):
    if number % i == 0:
        numbers.append(i)
print(numbers)



# Задача 18
# На вход программе подается натуральное число n ≥ 2, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).

n = int(input())
numbers_list = []
total_list = []

for i in range(n):
    numb = int(input())
    numbers_list.append(numb)

while len(numbers_list) > 1:
    total = numbers_list[0] + numbers_list[1]
    del numbers_list[0]
    total_list.append(total)
print(total_list)



# Задача 19
# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.

n = int(input())
numbers_list = []

for i in range(n):
    numb = int(input())
    numbers_list.append(numb)

del numbers_list[1::2]
print(numbers_list)



# Задача 20
# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает список из символов всех строк, а затем выводит его.

n = int(input())
numbers_list = []

for i in range(n):
    numb = int(input())
    numbers_list.extend(numb)
print(numbers_list)



# Задача 21
# На вход программе подается натуральное число n, а затем n различных натуральных чисел.
# Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.

n = int(input())
numbers_list = []

for i in range(n):
    number = int(input())
    numbers_list.append(number)
min_num = min(numbers_list)
max_num = max(numbers_list)

numbers_list.remove(max_num)
numbers_list.remove(min_num)

print(*numbers_list, sep='\n')



# Задача 22
# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.

n = int(input())
words_list = []

for i in range(n):
    str1 = input()
    if str1 not in words_list:
        words_list.append(str1)
    else:
        continue
print(*words_list, sep='\n')



# Задача 23
# На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

n = int(input())
strings_list = []
filtration_list = []

for i in range(n):
    strings = input()
    strings_list.append(strings)

keyword = input().lower()

for string in strings_list:
    if keyword in string.lower():
        filtration_list.append(string)

print(*filtration_list, sep='\n')



# Задача 23 (not_full)
# На вход программе подается натуральное число n, затем n строк,  затем число k — количество поисковых запросов, затем k строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.

n = int(input())
strings_list = []
keywords_list = []
result_list = []

for i in range(n):
    strings = input('Input search string: ')
    strings_list.append(strings)

k = int(input())

for j in range(k):
    keyword = input().lower()
    keywords_list.append(keyword)

print(keywords_list)
#
# flag = False
#
# for string in strings_list:
#     for key in keywords_list:
#         if key in string.lower():
#             result_list.append(string)
#             flag == True
#         else:
#             continue
#
# print(result_list)



# Задача 24
# Дополните приведенный код, чтобы он:
#
# Заменил второй элемент списка на 17;
# Добавил числа 4, 5 и 6 в конец списка;
# Удалил первый элемент списка;
# Удвоил список;
# Вставил число 25 по индексу 3;
# Вывел список, с помощью функции print().

numbers = [8, 9, 10, 11]

numbers[1] = 17
numbers.extend([4, 5, 6])
del numbers[0]
numbers *= 2
numbers.insert(3, 25)
print(numbers)



# Задача 25
# На вход программе подается строка текста, содержащая различные натуральные числа. Из данной строки формируется список чисел.
# Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

numbers = input().split()

minimum  =  numbers.index(min(numbers))
maximum  =  numbers.index(max(numbers))
numbers[minimum],  numbers[maximum]  =  max(numbers),  min(numbers)

print(*numbers)



# Задача 26
# На вход программе подается строка, содержащая английский текст.
# Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'

abc = input().lower().split(' ')
cnt1 = abc.count('a')
cnt2 = abc.count('an')
cnt3 = abc.count('the')

total_cnt = cnt1 + cnt2 + cnt3
print('Общее количество артиклей:', total_cnt)



# Задача 27
# На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел.
# Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию.

numbers = input().split()
int_numbers = [int(num) for num in numbers]
numbers = sorted(int_numbers)
numbers_r = sorted(int_numbers, reverse=True)

print(' '.join(map(str, numbers)))
print(' '.join(map(str, numbers_r)))



# Задача 28
# Дополните приведенный код, используя списочное выражение, так чтобы получить новый список, содержащий строки исходного списка с удаленным первым символом.

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [m[1:] for m in keywords]
print(new_keywords)



# Задача 29
# Дополните приведенный код, используя списочное выражение, так чтобы получить новый список, содержащий длины строк исходного списка.

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

lengths = [len(word) for word in keywords]
print(lengths)



# Задача 30
# Дополните приведенный код списочным выражением, чтобы получить новый список, содержащий только слова длиной не менее пяти символов (включительно).

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [word for word in keywords if len(word) >= 5]
print(new_keywords)



# Задача 31
# Дополните приведенный код, используя списочное выражение, так чтобы получить список всех чисел палиндромов от 100 до 1000.

palindromes = [i for i in range(1000) if i > 100 and i % 10 == i // 100]
print(palindromes)



# Задача 32
# Проверить валидность ввода номера телефона (с 7 и без неё), чтобы не было букв и длина полей совпадала

n = input().split("-")
c = [len(i) for i in n]
if c == [3, 3, 4] and ''.join(n).isdigit():
    print("YES")
elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7':
    print("YES")
else:
    print("NO")