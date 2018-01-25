import modularArithmetic
import random
import frequencyAnalysis
from Alphabets import alpEng
from operator import attrgetter

class CryptRes:
    def __init__(self, key, message, frqnc):
        self.key = key
        self.message = message
        self.frqnc = frqnc

print("Шифр Цезаря (Шифрование-тест)")
mesg = input('-> Введите сообщение: ')
mesg = mesg.upper().replace(' ', '')
key = random.randint(1, alpEng.Length)
print(alpEng.Dic[key])
it = 0
codedMsg = ''
while not it == len(mesg):
    scode = alpEng.Alp[mesg[it]]
    rcode = modularArithmetic.modularsumm(scode, key, alpEng.Length)
    codedMsg = codedMsg + alpEng.Dic[rcode]
    it = it + 1
keycode = 0
decryptmsg = []
while not keycode == alpEng.Length:
    it = 0
    res = ''
    while not it == len(codedMsg):
        scode = alpEng.Alp[codedMsg[it]]
        rcode = modularArithmetic.modulardec(scode, keycode, alpEng.Length)
        res = res + alpEng.Dic[rcode]
        it = it + 1
    decryptmsg.append(CryptRes(alpEng.Dic[keycode], res, 0))
    keycode = keycode + 1

frequencyAnalysis.quadAnalysis(decryptmsg)
print("Возможные ключи, сортировка по вероятности: ")
decryptmsg = sorted(decryptmsg, key=attrgetter('frqnc'), reverse=True)
for lineRes in decryptmsg:
    print(lineRes.key + " " + lineRes.message + " " + str(lineRes.frqnc))
