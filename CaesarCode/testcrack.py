import random
from CaesarCode import crypt
from CaesarCode import bruteforce


class CryptRes:
    def __init__(self, key, message, frqnc):
        self.key = key
        self.message = message
        self.frqnc = frqnc


def TEST_CRACK_CEASAR(TEXT, LANGUAGE, TYPE):
    if (LANGUAGE == 'eng'):
        from Alphabets.English import Alphabet as ALPHABET
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
    resString = "Случайный ключ: " + keycode + "\n"
    newmesg = crypt.CRYPTION_CEASAR(mesg, LANGUAGE, keycode)
    resString += "Зашифрованое сообщение: " + newmesg + "\n"
    resString += bruteforce.CRACK_CEASAR(newmesg, LANGUAGE, type)
    return resString
