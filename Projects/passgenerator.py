# Password generator

import random as rnd
def generate_passwords(long, chars):

    '''генерируем пасс'''

    password = ''

    for _ in range(long):
        password += rnd.choice(chars)

    print(password)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

count_pass = int(input('Сколько паролей сгенерировать? '))
long_pass = int(input('Длинна пароля: '))

if input('Нажми 1, чтобы разрешить прописные буквы ') == '1':
    chars += lowercase_letters

if input('Нажми 1, чтобы разрешить заглавные буквы ') == '1':
    chars += uppercase_letters

if input('Нажми 1, чтобы разрешить цифры ') == '1':
    chars += digits

if input('Нажми 1, чтобы разрешить символы ') == '1':
    chars += punctuation

if input('Нажми 1, чтобы разрешить неоднозначные символы "il1Lo0O" ') != '1':
    for _ in 'il1Lo0O':
        chars = chars.replace(_,'')

for _ in range(count_pass):
    generate_passwords(long_pass, chars)