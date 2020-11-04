# Задание 1
# Напишите программу, которая принимает три положительных числа и определяет вид треугольника,
# длины сторон которого равны введенным числам.

a, b, c = int(input()), int(input()), int(input())

if(a == b == c):
    print('Равносторонний')
elif(a == b or a == c or b == c):
    print('Равнобедренный')
else:
    print('Разносторонний')



# Задание 2
# Даны три различных целых числа.
# Напишите программу, которая находит среднее по величине число.

a, b, c = int(input()), int(input()), int(input())

if((a > b and a < c) or (a > c and a < b)):
    print(a)
elif((b > a and b < c) or (b > c and b < a)):
    print(b)
elif((c > a and c < b) or (c > b and c < a)):
    print(c)



# Задание 3
# Дан порядковый номер месяца 1 - 12.
# Напишите программу, которая выводит на экран количество дней в этом месяце. Принять, что год является невисокосным.
# Постарайтесь написать программу, так чтобы в ней было не более трех условий.

m = int(input())

if(m == 2):
    print('28')
elif(m == 4 or m == 6 or m == 9 or m == 11):
    print('30')
else:
    print('31')



# Задание 4
# Известен вес боксера-любителя (целое число). Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых категорий:
# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.
# Напишите программу, определяющую, в какой категории будет выступать данный боксер.

weight = int(input())

if(69 >= weight >= 64):
    print('Полусредний вес')
elif(64 >= weight >= 60):
    print('Первый полусредний вес')
else:
    print('Легкий вес')



# Задание 5
# Напишите программу, которая считывает с клавиатуры два целых числа и строку.
# Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /), то выведите результат применения этой операции к введённым ранее числам,
# в противном случае выведите «Неверная операция».
# Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».

num1 = int(input())
num2 = int(input())
math = input()
if math == '+':
    print(num1 + num2)
elif math == '-':
    print(num1 - num2)
elif math == '*':
    print(num1 * num2)
elif math == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
         print('На ноль делить нельзя!')
else:
    print('Неверная операция')



# Задание 6
# Напишите программу, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке.

# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.

# В противном случае программа должна вывести название вторичного цвета, который получится в результате.

color1 = input()
color2 = input()

if(color1 == 'красный' and color2 == 'красный'):
    print('красный')
elif(color1 == 'синий' and color2 == 'синий'):
    print('синий')
elif(color1 == 'желтый' and color2 == 'желтый'):
    print('желтый')
else:
    if((color1 == 'красный' and color2 == 'желтый') or (color1 == 'желтый' and color2 == 'красный')):
        print('оранжевый')
    elif((color1 == 'красный' and color2 == 'синий') or (color1 == 'синий' and color2 == 'красный')):
        print('фиолетовый')
    elif((color1 == 'синий' and color2 == 'желтый') or (color1 == 'желтый' and color2 == 'синий')):
        print('зеленый')
    else:
        print('ошибка цвета')



# Задание 7
# На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов:

# карман 0 зеленый;
# для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
# для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.

# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным.
# Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.

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



# Задание 8
# На числовой прямой даны два отрезка: a и b.
# Напишите программу, которая находит их пересечение.

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if(a1 < a2 < b2 < b1):
    print(a2, b2)
elif(a1 < a2 < b1 < b2):
    print(a2, b1)
elif(a2 < a1 < b2 < b1):
    print(a1, b2)
elif(a2 < a1 < b1 < b2):
    print(a1, b1)
elif(a1 < b1 == a2 < b2):
    print(b1)
elif(a2 < b2 == a1 < b1):
    print(a1)
elif(a1 == a2 < b1 == b2):
    print(a1, b1)
elif(a1 == a2 < b1 < b2):
    print(a1, b1)
elif(a2 < a1 < b1 == b2):
    print(a1, b1)
elif(a1 < a2 < b1 == b2):
    print(a2, b1)
elif(a1 == a2 < b2 < b1):
    print(a2, b2)
else:
    if(a1 < b1 < a2 < b2):
        print('пустое множество')
    elif(a2 < b2 < a1 < b1):
        print('пустое множество')



# Итоговая работа
# Тест 1
# Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля.
# Если год оканчивается, то выведите «YES», иначе выведите «NO».

num = int(input())

if(num % 100 == 0):
    print('YES')
else:
    print('NO')



# Тест 2
# Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет.
# Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if((x1 + y1 + x2 + y2) % 2 == 0):
    print('YES')
else:
    print('NO')



# Тест 3
# Футбольная команда набирает девочек от 10 до 15 лет включительно.
# Напишите программу, которая запрашивает возраст и пол претендента, используя обозначение пола буквы m (от male – мужчина) и f (от female – женщина)
# и определяет подходит ли претендент для вступления в команду или нет.
# Если претендент подходит, то выведите «YES», иначе выведите «NO».

age = int(input())
gender = input()

if(age in range(10,16,1) and gender == 'f'):
    print('YES')
else:
    print('NO')



# Тест 4
# Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру.
# Если число находится вне диапазона 1-10, то программа должна вывести текст «ошибка».

num = int(input())

if(num > 10 or num < 1):
    print('ошибка')
else:
    if(num == 1):
        print('I')
    elif (num == 2):
        print('II')
    elif (num == 3):
        print('III')
    elif (num == 4):
        print('IV')
    elif (num == 5):
        print('V')
    elif (num == 6):
        print('VI')
    elif (num == 7):
        print('VII')
    elif (num == 8):
        print('VIII')
    elif (num == 9):
        print('IX')
    elif (num == 10):
        print('X')



# Тест 5
# Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».
#
# Условия:
#
# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO».

num = int(input())

if(num % 2 != 0):
    print('YES')
else:
    if(num >= 2 and num <= 5):
        print('NO')
    elif(num >= 6 and num <= 20):
        print('YES')
    elif(num > 20):
        print('NO')



# Тест 6 - Ход слона
# Даны две различные клетки шахматной доски.
# Напишите программу, которая определяет, может ли слон попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести «YES», если из первой клетки ходом слона можно попасть во вторую или «NO» в противном случае.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if((x1 + y1) == (x2 + y2) or (x1 - y1) == (x2 -y2)):
    print('YES')
else:
    print('NO')



# Тест 7 - Ход коня
# Даны две различные клетки шахматной доски.
# Напишите программу, которая определяет, может ли конь попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести «YES», если из первой клетки ходом коня можно попасть во вторую или «NO» в противном случае.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')



# Тест 8 - Ход ферзя
# Даны две различные клетки шахматной доски.
# Напишите программу,  которая определяет, может ли ферзь попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести «YES», если из первой клетки ходом ферзя можно попасть во вторую или «NO» в противном случае.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if(((x1 + y1) == (x2 + y2) or (x1 - y1) == (x2 -y2)) or (x1 == x2 or y1 == y2)):
    print('YES')
else:
    print('NO')