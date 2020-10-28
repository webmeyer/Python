#Методы объектов типа str

name = 'Whatsapp' # Это объект строки
if name.startswith('Wha'):
    print('Да, строка начинается на "Wha"')
if 'a' in name:
    print('Да, она содержит строку "a"')
if name.find('what') != -1:
    print('Да, она содержит строку "what"')
delimiter = '_*_'

mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))