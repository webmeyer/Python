# word1 = input()
# word2 = input()
# count = 0
#
# if len(word1) == len(word2):
#      for i in word1:
#          print(i)
#          for j in word2:
#             if i == j:
#                 count += 1
# if count == len(word1) - 1:
#     print(count)
# else:
#     print('Отличаются больше, чем на 1 символ')
# считываем данные


# объявление функции
def is_one_away(word1, word2):
    count = 0
    if len(word1) == len(word2):
        for i in word1:
            for j in word2:
                if i == j:
                    count += 1
        if count == len(word1) - 1 or count - 1 == len(word1):
            return True
        else:
            return False
    else:
        return False

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))



