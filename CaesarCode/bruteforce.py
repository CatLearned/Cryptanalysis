import modularArithmetic
import frequencyAnalysis
from Alphabets import alpEng
from operator import attrgetter



class CryptRes:
    def __init__(self, key, message, frqnc):
        self.key = key
        self.message = message
        self.frqnc = frqnc


print("Шифр Цезаря (Расшифрование)")
mesg = input('-> Введите шифротекст: ')
mesg = mesg.upper().replace(' ', '')
typeAnaliz = int(input("Введите тип анализа"))

slength = len(mesg)
keycode = 0
decryptmsg = []
while not keycode == alpEng.Length:
    it = 0
    res = ''
    while not it == slength:
        scode = alpEng.Alp[mesg[it]]
        rcode = modularArithmetic.modulardec(scode, keycode, alpEng.Length)
        res = res + alpEng.Dic[rcode]
        it = it + 1
    decryptmsg.append(CryptRes(alpEng.Dic[keycode], res, 0))
    keycode = keycode + 1

frequencyAnalysis.freqAnalysis(decryptmsg, typeAnaliz)
print("Возможные ключи, сортировка по вероятности: ")
decryptmsg = sorted(decryptmsg, key=attrgetter('frqnc'), reverse=True)
for lineRes in decryptmsg:
    print(lineRes.key + " " + lineRes.message + " " + str(lineRes.frqnc))
