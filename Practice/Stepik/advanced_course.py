# Задание 1.
# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.

objects = [1, 2, 1, 2, 3]
checker = set()
for obj in objects:
    if id(obj) not in checker:
        checker.add(id(obj))

print(len(checker))



# Задание 2.
# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую самое маленькое целое число y, такое что:
#
# y больше или равно x
# y делится нацело на 5

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        return x + 5 - x % 5
    return "I don't know :("