#Example

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