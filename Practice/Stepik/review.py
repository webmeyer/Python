# Найти ошибки в коде
# Задание 1

count = 0
p = 1

for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')