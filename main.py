# EXAMPLE

# объявление функции
def get_shipping_cost(quantity):
    cost = 0
    while quantity > 0:
        if quantity == 1:
            cost += 1000
            quantity -= 1
        else:
            cost += 120
            quantity -= 1
    return cost


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))




