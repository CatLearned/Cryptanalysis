import modularArithmetic
import alpEng

print("Шифр Цезаря (Расшифрование)")
mesg = input('-> Введите шифротекст: ')
mesg = mesg.upper().replace(' ', '')

slength = len(mesg)
keycode = 0

while not keycode == alpEng.Length:
    it = 0
    res = ''
    while not it == slength:
        scode = alpEng.Alp[mesg[it]]
        rcode = modularArithmetic.modulardec(scode, keycode, alpEng.Length)
        res = res + alpEng.Dic[rcode]
        it = it + 1
    print("Ключ: " + alpEng.Dic[keycode] + " Сообщение: " + res)
    keycode = keycode + 1
