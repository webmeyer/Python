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