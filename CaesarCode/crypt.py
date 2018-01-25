import modularArithmetic
from Alphabets import alpEng

print("Шифр Цезаря (Шифрование)")
mesg = input('-> Введите сообщение: ')
mesg = mesg.upper().replace(' ', '')
key = input('-> Ключ символ: ')
key = key[0].upper()

slength = len(mesg)
keycode = alpEng.Alp[key]
it = 0
res = ''

while not it == slength:
    scode = alpEng.Alp[mesg[it]]
    rcode = modularArithmetic.modularsumm(scode, keycode, alpEng.Length)
    res = res + alpEng.Dic[rcode]
    it = it + 1

print("Зашифрованное сообщение: " + res)
