# объявление функции
def is_prime(num):
    if num % 2 == 0:
        return num == 2
    if num == 1:
        return False
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))