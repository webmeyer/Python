# Example

# объявление функции
def get_factors(num):
    numbers = []
    for i in range(1, num + 1):
        if num % i == 0:
            numbers.append(i)
    return numbers

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))