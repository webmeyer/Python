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