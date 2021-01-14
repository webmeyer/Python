# EXAMPLE

# объявление функции
from math import factorial
def compute_binom(n, k):
    bino1 = factorial(n)
    bino2 = factorial(k)*factorial(n-k)
    return bino1//bino2

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))





