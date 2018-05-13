#from Primitives import modularArithmetic, messageobj, keyobj


def CRYPTION_CEASAR(TEXT, KEY):
    #mes = messageobj(TEXT, LANGUAGE)
    #key = keyobj(KEY, LANGUAGE)

    return TEXT + KEY
    #if (LANGUAGE == 'eng'):
    #    from Alphabets.English import Alphabet as ALPHABET
    #else:
    #    return "Неверный алфавит!"
    #mesg = TEXT.upper().replace(' ', '')
    #key = KEY[0].upper()
    #try:
    #    keycode = ALPHABET.Alp[key]
    #except:
    #    return "Ошибка конвертации ключа, ключ отсутствует в словаре"
    #slength = len(mesg)
    #it = 0
    #res = ''
    #while not it == slength:
    #    try:
    #        scode = ALPHABET.Alp[mesg[it]]
    #    except:
    #       return "В строке ошибочный символ: " + "\"" + mesg[it] + "\""
    #    rcode = modularArithmetic.modularsumm(scode, keycode, ALPHABET.Length)
    #    res = res + ALPHABET.Dic[rcode]
    #    it = it + 1
    #return res
