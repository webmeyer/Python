# Словари - объекты класса dict
# ab - сокращение от address book

ab = { 'name' : 'Dmitri',
       'country' : 'Russia',
       'email' : 'dimka@yahoo.com',
       'phone' : '+79995550022'
       }
print('Пользователь с именем:', ab['name'], 'проживает в стране:', ab['country'])
print('Чтобы связаться с ним, напишите на почту:', ab['email'], 'или позвоните на', ab['phone'])


# Удаляем пару ключ:значение
del ab['phone']

print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакт с {0} с адресом {1}'.format(name, address))

# Добавляем пару ключ:значение
ab['skype'] = 'dimka@skype.ru'

if 'skype' in ab:
    print('\nАдрес Скайпа:', ab['skype'])


