#Example

num1 = int(input())

a = num1 % 10
b = num1 % 100
b = b // 10
c = num1 / 100
c = c % 10

minValue = min(a, b, c)
maxValue = max(a, b, c)
middle = (a + b + c) - (maxValue + minValue)

print(int(minValue))
print(int(maxValue))
print(int(middle))

if(int(middle) == int(maxValue) - int(minValue)):
    print('Число интересное')
else:
    print('Число неинтересное')