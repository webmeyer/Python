#Университет предоставляет студентам скидки на оплату обучения в зависимости от их успеваемости:
#90-100 => 50%
#80-89   => 30%
#70-79   => 10%
#0-69     => 0%
#Напишите программу, которая берет оценки за первый и второй семестр,
# а затем рассчитывает среднее значение
# и выводит результат в зависимости от оценки.


name = input('Как Вас зовут? - ')
sem1_score = int(input('Введите сумму всех оценок за первый семестр: '))
sem2_score = int(input('Введите сумму всех оценок за второй семестр: '))

mid = (sem1_score + sem2_score) // 2 #Среднее значение оценок за семестры
print('Средний балл Ваших оценок: ', mid)

if(mid >= 90 and mid <= 100):
    print(name, 'Ваша скидка составит: 50%')
elif(mid >= 80 and mid <= 89):
    print(name, 'Ваша скидка составит: 30%')
elif(mid >= 70 and mid <= 79):
    print(name, 'Ваша скидка составит: 10%')
elif(mid >= 0 and mid <= 69):
    print(name, 'Ваша скидка составит: 0%')
else:
    print('Вы точно ввели число?')