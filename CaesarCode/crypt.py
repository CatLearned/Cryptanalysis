import modularArithmetic


def CRYPTION_CEASAR(TEXT, LANGUAGE, KEY):
    if (LANGUAGE == 'eng'):
        from Alphabets import alpEng as ALPHABET
    else:
        return "Неверный алфавит!"
    mesg = TEXT.upper().replace(' ', '')
    key = KEY[0].upper()
    try:
        keycode = ALPHABET.Alp[key]
    except:
        return "Ошибка конвертации ключа, ключ отсутствует в словаре"
    slength = len(mesg)
    it = 0
    res = ''
    while not it == slength:
        try:
            scode = ALPHABET.Alp[mesg[it]]
        except:
            return "В строке ошибочный символ: " + "\"" + mesg[it] + "\""
        rcode = modularArithmetic.modularsumm(scode, keycode, ALPHABET.Length)
        res = res + ALPHABET.Dic[rcode]
        it = it + 1
    return res


print("Шифр Цезаря (Шифрование)")
mesg = input('-> Введите сообщение: ')
key = input('-> Ключ символ: ')
print("Зашифрованное сообщение: " + CRYPTION_CEASAR(mesg, 'eng', key))
