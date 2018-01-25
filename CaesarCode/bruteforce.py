import modularArithmetic
import frequencyAnalysis
from Alphabets import alpEng


print("Шифр Цезаря (Расшифрование)")
mesg = input('-> Введите шифротекст: ')
mesg = mesg.upper().replace(' ', '')

slength = len(mesg)
keycode = 0
resaultMass = []
while not keycode == alpEng.Length:
    it = 0
    res = ''
    while not it == slength:
        scode = alpEng.Alp[mesg[it]]
        rcode = modularArithmetic.modulardec(scode, keycode, alpEng.Length)
        res = res + alpEng.Dic[rcode]
        it = it + 1
    resaultMass.append(alpEng.Dic[keycode] + ':' + res)
    # print(alpEng.Dic[keycode] + " : " + res + " : " + str(int(frequencyAnalysis.quadAnalysis(res))))
    keycode = keycode + 1
frequencyAnalysis.quadAnalysis(resaultMass)
for lineRes in resaultMass:
    print(lineRes)
