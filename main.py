# объявление функции
def is_valid_triangle(side1, side2, side3):
    return ((a + b) > c) and ((a + c) > b) and ((b + c) > a)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))