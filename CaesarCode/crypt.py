import modularArithmetic


# from Alphabets import alpEng as ALPHABET

# { "Eng" : from Alphabets import alpEng as ALPHABET}

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
mesg = mesg.upper().replace(' ', '')
key = input('-> Ключ символ: ')
key = key[0].upper()
print("Зашифрованное сообщение: " + CRYPTION_CEASAR(mesg, key, 'eng'))
