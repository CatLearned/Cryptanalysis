import modularArithmetic
import frequencyAnalysis
from operator import attrgetter



class CryptRes:
    def __init__(self, key, message, frqnc):
        self.key = key
        self.message = message
        self.frqnc = frqnc

def CRACK_CEASAR(TEXT, LANGUAGE, TYPE):
    if (LANGUAGE == 'eng'):
        from Alphabets import alpEng as ALPHABET
    else:
        return "Неверный алфавит!"
    if int(TYPE) < 5 or int(TYPE) >= 0:
        type = int(TYPE)
    else:
        return "Неверный тип частотного анализа!"
    mesg = TEXT.upper().replace(' ', '')
    slength = len(mesg)
    keycode = 0
    decryptmsg = []
    while not keycode == ALPHABET.Length:
        it = 0
        res = ''
        while not it == slength:
            scode = ALPHABET.Alp[mesg[it]]
            rcode = modularArithmetic.modulardec(scode, keycode, ALPHABET.Length)
            res = res + ALPHABET.Dic[rcode]
            it = it + 1
        decryptmsg.append(CryptRes(ALPHABET.Dic[keycode], res, 0))
        keycode = keycode + 1

    frequencyAnalysis.freqAnalysis(decryptmsg, typeAnaliz)




print("Шифр Цезаря (Расшифрование)")
mesg = input('-> Введите шифротекст: ')
typeAnaliz = int(input("Введите тип анализа"))

print("Возможные ключи, сортировка по вероятности: ")
print(CRACK_CEASAR(mesg, 'eng', typeAnaliz))
#for lineRes in decryptmsg:
#    print(lineRes.key + " " + lineRes.message + " " + str(lineRes.frqnc))
