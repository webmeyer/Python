# Задание 1
# Найти ошибки в коде

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



# Задание 2
# Найти ошибки в коде

mx = -10**6 - 1
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
    if x < 0 and x > mx:
        mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print('NO')


# Задание 3
# Найти ошибки в коде

s = 0

for i in range(1, 8):
    n = int(input())
    if n % 2 == 0:
        s += n
print(s)



# Задание 4
# Найти ошибки в коде

n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)



# Задание 5
# Найти ошибки в коде

n = int(input())
while n > 9:
    n //= 10
print(n)

