#Не тестировано!!!
import modularArithmetic
import alpEng

print("Шифр Цезаря")
mesg = input('-> Введите сообщение: ')
mesg = mesg.ToUpper().replace(' ', '')
key = input('-> Ключ символ: ')
key = key[0].ToUpper()

slength = len(mesg)
keycode = alpEng.Alp(key[0])
it = 0
res = ''

while not it == slength:
    scode = alpEng.Alp(mesg[it])
    rcode = modularArithmetic.modularsumm(scode, keycode, alpEng.Length)
    res = res + alpEng.Dic[rcode]

print ("Зашифрованное сообщение: " + res)