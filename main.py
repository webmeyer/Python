# EXAMPLE

# объявление функции
def is_valid_password(password):

    # флаги
    flag_1 = True
    flag_2 = False
    flag_3 = False

    # приведение строки к списку и разделение на отдельные элементы
    pass_list = password.split(":")
    palindrome = ''.join(pass_list[0])
    simple_num = ''.join(pass_list[1])
    even_num = ''.join(pass_list[-1])

    # если длина списка больше 3-ёх элементов
    if len(pass_list) > 3:
        return False

    # если один из элементов списка не является числом
    if palindrome.isalpha() or simple_num.isalpha() or even_num.isalpha():
        return False

    # проверка на простое число
    if int(simple_num) == 1:
        flag_1 = False
    for i in range(2, int(simple_num)):
        if int(simple_num) % i == 0:
            flag_1 = False

    # проверка на палиндромность
    if palindrome == palindrome[::-1]:
        flag_2 = True

    # проверка на чётность
    if int(even_num) % 2 == 0:
        flag_3 = True

    # сравниваем значения флагов
    if flag_1 == True and flag_2 == True and flag_3 == True:
        return True
    else:
        return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))




