# МЕТОДЫ СТРОК
# Задание 1
# На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним пробелом.
# Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.

str1 = input()

if(str1 == str1.title()):
    print('YES')
else:
    print('NO')



# Задание 2
# На вход программе подается строка.
#  Напишите программу, которая меняет регистр символов, другими словами замените все строчные символы заглавными и наоборот.

str1 = input()
print(str1.swapcase())

