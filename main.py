#Example

num = int(input())

if num in range(0, 37, 1):
    if(num == 0):
        print('зеленый')
    elif(num in range(1, 11, 1)):
        if(num % 2 == 0):
            print('черный')
        else:
            print('красный')
    elif (num in range(11, 19, 1)):
        if (num % 2 == 0):
            print('красный')
        else:
            print('черный')
    elif (num in range(19, 29, 1)):
        if (num % 2 == 0):
            print('черный')
        else:
            print('красный')
    elif (num in range(29, 37, 1)):
        if (num % 2 == 0):
            print('красный')
        else:
            print('черный')
else:
    print('ошибка ввода')