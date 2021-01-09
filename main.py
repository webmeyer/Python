# EXAMPLE

# объявление функции
def is_palindrome(text):
    txt_list = []
    for char in text:
        if char.isalpha():
            txt_list.append(char.lower())
    if txt_list[:] == txt_list[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))



