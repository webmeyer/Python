# EXAMPLE

# объявление функции
def is_correct_bracket(text):
    meetings = 0
    for c in text:
        if c == '(':
            meetings += 1
        elif c == ')':
            meetings -= 1
            if meetings < 0:
                return False

    return meetings == 0

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))




