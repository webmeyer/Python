#Example

name = input()
sem1_score = int(input())
sem2_score = int(input())

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

