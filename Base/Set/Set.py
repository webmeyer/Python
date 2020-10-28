#Множества

bri = set(['Бразилия', 'Россия', 'Индия'])

bric = bri.copy()
bric.add('Китай')
bric.issuperset(bri)

bri.remove('Россия')