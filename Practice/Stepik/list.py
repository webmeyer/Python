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