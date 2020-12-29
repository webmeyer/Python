# Example

# объявление функции
def find_all(target, symbol):
    target_list = []
    for i in range(len(target)):
        if target[i] == symbol:
            target_list.append(i)
    return target_list

s = input()
char = input()

# вызываем функцию
print(find_all(s, char))