# EXAMPLE

# объявление функции
def draw_triangle():
    for i in range(8):
        k1 = 7 - i
        k2 = 7 + i
        for j in range(k2 + 1):
            print('*' if j >= k1 else ' ', end='')
        print()


# основная программа
draw_triangle()  # вызов функции




