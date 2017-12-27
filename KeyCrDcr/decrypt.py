# Объявление Алфавита
import array
# Словарь (Алфавит) Без буквы Ё
Alp = {'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ж': 7, 'З': 8, 'И': 9, 'Й': 10, 'К': 11, 'Л': 12, 'М': 13, 'Н': 14, 'О': 15, 'П': 16, 'Р': 17, 'С': 18, 'Т': 19, 'У': 20, 'Ф': 21, 'Х':22, 'Ц':23, 'Ч':24, 'Ш':25, 'Щ':26, 'Ъ':27, 'Ы':28, 'Ь':29, 'Э':30, 'Ю':31, 'Я':32} #1-32
Dic = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'] #1-32

# Буквенно-числовой Преобразователь №1
# Вход: буквенное значение слова
# Выход: числовая последовательность
def SymToCode(message):
	xarray = []
	length = len(message)
	ctr = 0
	while not ctr == length:
		xarray.append(Alp[message[ctr]])
		ctr = ctr +1
	return xarray

# Число-буквенный Преобразователь №2
# Вход: числовая последовательность
# Выход: буквенное значение слова
def CodeToSym(imessage):
	Sym = ''
	length = len(imessage)
	itterator = 0
	while not itterator == length:
		Sym = Sym + Dic[imessage[itterator] - 1]
		itterator = itterator + 1
	return Sym

# Числовой Сумматор №3
# Вход: Пара числовых последовательностей
# Выход: Сумма числовых последовательностей с основанием равным длине алфавита
def summator(message, key):
	lengthM = len(message)
	lengthK = len(key)
	itteratorM = 0
	itteratorK = 0	
	while not itteratorM == lengthM:
		if (itteratorK == lengthK):
			itteratorK = 0; 
		message[itteratorM] = message[itteratorM] + key[itteratorK]
                message[itteratotM] = message[itteratotM] % 32
		if(message[itteratorM] == 0):
			message[itteratorM] = 32
		itteratorM = itteratorM + 1
		itteratorK = itteratorK + 1
	return message

# Числовой Вычитатель
# Вход: Сообщение1, сообщение2, является ли сообщение 2 ключом
# Выход: Разница сообщений
def deciminator(message1, message2, bkey):
	lengthM1 = len(message1)
	lengthM2 = len(message2)
	# Увеличить размер сообщения
	# Разделить вычитание с ключом и между двумя сообщениями
	# Вынести алгоритм непосредственно вычитания в другую функцию
	if (bkey == False):
		if(lengthM1 < lengthM2):
			buf = lengthM1
			lengthM1 = lenguhM2
			lengthM2 = 0
		else:
			lengthM2 = 0
	itteratorM1 = 0
	itteratorM2 = 0
	#while not itterator
	return 0

print('-> Программа алгоритм с ключем')
#cmd = input('-> dEscription or enCryption or keY: ')
#if (cmd == 'c'):
mesg = input('-> Введите сообщение: ')
imesg = SymToCode(mesg)
imesg = imesg.upper()
print('-> Числовой вид сообщения: ', imesg)
key = input('-> Введите ключ: ')
ikey = SymToCode(key)
print('-> Числовой вид ключа: ', ikey)
ires = summator(imesg, ikey)
res = CodeToSym(ires)
print('-> Результат шифрования: ', res)
print('-> Числовой Результат Ключевого шифрования: ', ires)
input('-> Конец!')
#elif (cmd == 'e'):
#    print('hi')
#elif (cmd == 'y'):
#    print('hi')
#else: print('-> Неверная команда')
