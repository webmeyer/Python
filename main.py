# EXAMPLE

import random
print('Сыграем в "Угадай число"?')
user_name = input('Введите Ваше имя..')
num_generate = random.randint(1, 100)
while True:
    user_num = int(input(f'{user_name}, введите число от 1 до 100 \n'))
    if user_num > num_generate:
        print('Слишком много, попробуйте ещё раз')
    elif user_num < num_generate:
        print('Маловато, попробуйте ещё раз')
    else:
        print('Поздравляем! Вы угадали!')
        break





