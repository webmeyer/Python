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