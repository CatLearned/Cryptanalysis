# Объявление Алфавита
import array
# Словарь (Алфавит) Без буквы Ё
Alp = {'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ж': 7, 'З': 8, 'И': 9, 'Й': 10, 'К': 11, 'Л': 12, 'М': 13, 'Н': 14, 'О': 15, 'П': 16, 'Р': 17, 'С': 18, 'Т': 19, 'У': 20, 'Ф': 21, 'Х':22, 'Ц':23, 'Ч':24, 'Ш':25, 'Щ':26, 'Ъ':27, 'Ы':28, 'Ь':29, 'Э':30, 'Ю':31, 'Я':32} #1-32
Dic = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
# Перевод символьного сообщения в цифровой код
def SymToCode(message): # Буквенно-числовой Преобразователь №1
	xarray = []
	length = len(message)
	ctr = 0
	while not ctr == length:
		xarray.append(Alp[message[ctr]])
		ctr = ctr +1
	return xarray

# Число-буквенный Преобразователь №2
def CodeToSym(imessage):
	Sym = ''
	length = len(imessage)
	itterator = 0
	while not itterator == length:
		Sym = Sym + Dic[imessage[itterator] - 1]
		itterator = itterator + 1
	return Sym

def summator(message, key): # Числовой Сумматор №3
	lengthM = len(message)
	lengthK = len(key)
	itteratorM = 0
	itteratorK = 0	
	while not itteratorM == lengthM:
		if (itteratorK == lengthK):
			itteratorK = 0; 
		message[itteratorM] = message[itteratorM] + key[itteratorK]
		if(message[itteratorM] > 32):
			message[itteratorM] = message[itteratorM] - 32
		itteratorM = itteratorM + 1
		itteratorK = itteratorK + 1
	return message

print('-> Программа алгоритм с ключем')
#cmd = input('-> dEscription or enCryption or keY: ')
#if (cmd == 'c'):
mesg = input('-> Введите сообщение: ')
imesg = SymToCode(mesg)
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
