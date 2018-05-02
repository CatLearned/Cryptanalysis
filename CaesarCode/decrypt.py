from Primitives import modularArithmetic


def DECRYPTION_CEASAR(TEXT, LANGUAGE, KEY):
    if (LANGUAGE == 'eng'):
        from Alphabets.English import Alphabet as ALPHABET
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
        rcode = modularArithmetic.modulardec(scode, keycode, ALPHABET.Length)
        try:
            res = res + ALPHABET.Dic[rcode]
        except:
            return "Ошибка обратной конвертации "
        it = it + 1
    return res
