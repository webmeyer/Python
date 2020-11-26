# СТРОКОВЫЙ ТИП ДАННЫХ

# Задание 1
# Напишите программу, которая выводит текст:
# "Python is a great language!", said Fred. "I don't ever remember having this much fun before."

s1 = "Python is a great language!"
s2 = ', said Fred. '
s3 = "I don't ever remember having this much fun before."
a = '"'

print(a + s1 + a + s2 + a + s3 + a)



# Задание 2
# Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
# «Hello [введенное имя] [введенная фамилия]! You just delved into Python».
# На вход программе подаётся две строки (имя и фамилия), каждая на отдельной строке.
# Программа должна вывести текст в соответствии с условием задачи.

firstname = input()
lastname = input()

print("Hello " + firstname + " " + lastname + "!" + " You just delved into Python")



# Задание 3
# Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:
# «Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».
# На вход программе подаётся строка – название футбольной команды.
# Программа должна вывести текст в соответствии с условием задачи.

team = input()
print("Футбольная команда " + team + " имеет длину " + str(len(team)) + " символов")



# Задание 4
# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
# На вход программе подаётся названия трех городов, каждое на отдельной строке.
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

city1 = input()
city2 = input()
city3 = input()

print(min(city1, city2, city3, key=len))
print(max(city1, city2, city3, key=len))



# Задание 5
# Вводятся 3 строки в случайном порядке.
# Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
# Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.

a = len(input())
b = len(input())
c = len(input())

if((2 * b - c -a) * (2 * c - b -a) * (2 * a - b - c) == 0):
    print("YES")
else:
    print("NO")



# Задание 6
# Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.
# На вход программе подается одна строка.
# Программа должна вывести текст в соответствии с условием задачи.

str1 = input()

if("синий" in str1):
    print("YES")
else:
    print("NO")



# Задание 7
# Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.
# На вход программе подается одна строка.
# Программа должна вывести текст в соответствии с условием задачи.

str1 = input()

if("суббота" in str1 or "воскресенье" in str1):
    print("YES")
else:
    print("NO")



# Задание 8
# Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки.
# Напишите программу проверяющую корректность email адреса.
# Программа должна вывести строку «YES», если email адрес является корректным и «NO» в ином случае.
# Примечание. Наличие символов @ и . недостаточно для корректности email адреса, однако их отсутствие гарантировано влечёт за собой неверный email.

mail = input()

if("@" in mail and "." in mail):
    print("YES")
else:
    print("NO")

# Задание 9
# На вход программе подается одна строка.
# Напишите программу, которая выводит элементы строки с индексами 0, 2, 4, ... в столбик.

str = input()
for i in range(0, len(str)):
    if(i % 2 == 0):
        print(str[i])


# Задание 10
# Напишите программу, которая выводит в столбик элементы строки в обратном порядке.

str = input()
for i in range(len(str), 0, -1):
    print(str[i - 1])



# Задание 11
# Напишите программу, которая выводит в столбик элементы строки в обратном порядке.

name = input()
lastname = input()
surname = input()

print(len(name[0]) + len(lastname[0]) + len(surname[0]))



# Задание 12
# На вход программе подаются три строки: имя, фамилия и отчество.
# Напишите программу, которая выводит инициалы человека.

name = input()
lastname = input()
surname = input()

print(lastname[0] + name[0] + surname[0])



# Задание 13
# На вход программе подается одна строка состоящая из цифр.
# Напишите программу, которая считает сумму цифр данной строки.

str1 = input()
total = 0

for i in range(0, len(str1)):
    total += int(str1[i])
print(total)



# Задание 14
# На вход программе подается одна строка.
# Напишите программу, которая выводит сообщение «Цифра» (без кавычек), если строка содержит цифру.
# В противном случае вывести сообщение «Цифр нет» (без кавычек).

str1 = input()
flag = False

for i in range(0, len(str1)):
    if(str1[i] in range(0, 9)):
        flag == True
if(flag == True):
    print('Цифра')
else:
    print('Цифр нет')


# Задание 15
# На вход программе подается одна строка.
# Напишите программу, которая определяет сколько раз в строке встречаются символы + и *.

str1 = input()
totalPlus = 0
totalMulti = 0

for i in range(0, len(str1)):
    if(str1[i] in '+'):
        totalPlus += 1
    elif(str1[i] in '*'):
        totalMulti += 1

print('Символ + встречается', totalPlus, 'раз')
print('Символ * встречается', totalMulti, 'раз')



# Задание 16
# На вход программе подается одна строка.
# Напишите программу, которая определяет сколько в ней одинаковых соседних символов.

str1 = input()
total = 0

for i in range(0, len(str1)-1):
    if(str1[i] == str1[i + 1]):
        total += 1
print(total)



# Задание 17
# На вход программе подается одна строка с буквами русского языка.
# Напишите программу, которая определяет количество гласных и согласных букв.

str1 = input()
totaloVovel = 0
totalConsonant = 0

for i in range(0, len(str1)):
    if(str1[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'):
        totaloVovel += 1
    elif(str1[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'):
        totalConsonant += 1
print('Количество гласных букв равно', totaloVovel)
print('Количество согласных букв равно', totalConsonant)



# Задание 18
# На вход программе подается натуральное число, записанное в десятичной системе счисления.
# Напишите программу, которая переводит данное число в двоичную систему счисления.

number = int(input())
countString = ''

while(number != 0):
    ost = number % 2
    countString += str(ost)
    number //= 2
print(countString[::-1])



# Задание 19
# Дополните приведенный код, используя срезы,
# так чтобы он вывел первые 12 символов строки s

str1 = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(str1[:12])



# Задание 20
# Дополните приведенный код, используя срезы,
# так чтобы он вывел последние 9 символов строки s

str1 = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])



# Задание 21
# Дополните приведенный код, используя срезы,
# так чтобы он вывел каждый 7 символ строки s начиная от начала строки

str1 = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])