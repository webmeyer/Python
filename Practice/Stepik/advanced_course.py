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