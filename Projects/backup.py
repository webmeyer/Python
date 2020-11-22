#Скрипт для создания бэкапов с диска

import os
import time

#1 - Собираем нужные каталоги в список
source = ['C:\\Zenno\\test']

#2 - Выбираем место для хранения рез.копий
target_dir = 'C:\\VMs'

#3 - Все файлы будут в zip - архиве
#4 - Именем для зипа будет текущая дата и время
target = target_dir + os.sep + time.strftime('%Y%m%d') + '.zip'

#5 Используем ZIP для архивирования файлов (os.system)
zip_command = '"C:\\Program Files (x86)\\GnuWin32\\bin\\zip.exe" -qr {0} {1}'.format(target, ' '.join(source))


#Запускаем создание резервной копии
print('Читай:', zip_command)
if os.system(zip_command) == 0:
    print('Резеврная копия успешно создана в', target)
else:
    print('Создать НЕ УДАЛОСЬ!')