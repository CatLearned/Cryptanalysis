# Объявление Алфавита
import array
# Словарь
dict = {'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ж': 7, 'З': 8, 'И': 9, 'Й': 10, 'К': 11, 'Л': 12, 'М': 13, 'Н': 14, 'О': 15, 'П': 16, 'Р': 17, 'С': 18, 'Т': 19, 'У': 20, 'Ф': 21, 'Х':22, 'Ц':23, 'Ч':24, 'Ш':25, 'Щ':26, 'Ъ':27, 'Ы':28, 'Ь':29, 'Э':30, 'Ю':31, 'Я':32} #1-32

# Перевод символьного сообщения в цифровой код
def messageToCode(message):
    xarray = [None]
    length = len(message)
    ctr = 0
    while not ctr == length:
        xarray.append = dict[message.charAt(ctr)]
        ctr = ctr +1
    return xarray

print('-> Программа криптографии')
cmd = input('-> dEscription or enCryption or keY: ')
if (cmd == 'c'):
    mesg = input('-> Введите сообщение: ')
    print('-> Int Code', messageToCode(mesg))
    key = input('-> Введите ключ: ')
elif (cmd == 'e'):
    print('hi')
elif (cmd == 'y'):
    print('hi')
else: print('-> Неверная команда')
