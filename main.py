# EXAMPLE

# объявление функции
def is_magic(date):
    date_list = date.split('.')
    magic_number = int(date_list[0]) * int(date_list[1])
    last_num = date_list[-1]
    last_num = last_num[2:]
    if magic_number == int(last_num):
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))




