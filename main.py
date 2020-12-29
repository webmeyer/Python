# Example

# объявление функции
def get_days(month):
    monthes = [31,28,31,30,31,30,31,31,30,31,30,31]
    return monthes[month - 1]

print(get_days(9))