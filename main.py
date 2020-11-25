#Example

num1 = int(input())
while(num1 != 0):
    last_digit = num1 % 10
    print(last_digit, end='')
    num1 = num1 // 10