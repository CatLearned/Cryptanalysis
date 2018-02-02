import modularArithmetic
import random
import frequencyAnalysis
from operator import attrgetter
from CaesarCode import crypt
from CaesarCode import bruteforce

class CryptRes:
    def __init__(self, key, message, frqnc):
        self.key = key
        self.message = message
        self.frqnc = frqnc

def TEST_CRACK_CEASAR(TEXT, LANGUAGE, TYPE):
    if (LANGUAGE == 'eng'):
        from Alphabets import alpEng as ALPHABET
    else:
        return "Неверный алфавит!"
    if int(TYPE) < 5 or int(TYPE) >= 0:
        type = int(TYPE)
    else:
        return "Неверный тип частотного анализа!"
    mesg = TEXT.upper().replace(' ', '')
    key = random.randint(1, ALPHABET.Length)
    try:
        keycode = ALPHABET.Dic[key]
    except:
        return "Ошибка генерации ключа "
    # Обязательно переделать!!!
    print("Случайный ключ: " + keycode)
    newmesg = crypt.CRYPTION_CEASAR(mesg, LANGUAGE, key)
    print("Зашифрованое сообщение: " + newmesg)
    return bruteforce.CRACK_CEASAR(newmesg, LANGUAGE, type)

print("Шифр Цезаря (Шифрование-тест)")
mesg = input('-> Введите сообщение: ')
typeAnaliz = int(input("-> Введите тип анализа: "))
print(TEST_CRACK_CEASAR(mesg, 'eng', typeAnaliz))
#for lineRes in decryptmsg:
#    print(lineRes.key + " " + lineRes.message + " " + str(lineRes.frqnc))
