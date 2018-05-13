# Проверяет наличие и передает алфавит в программу
def importAlphsbet(Lang):
    if Lang == "eng":
        from Alphabets.English import Alphabet as Alphabet
        return Alphabet
    else:
        if Lang == "rus":
            from Alphabets.Russian import Alphabet as Alphabet
            return Alphabet
        else:
            return 0
    return 0
        # Такого алфавита не существует

# Получение номера символа
def getCodeBySymbol(Symbol, Lang):
    bufAlp = importAlphsbet(Lang)
    if bufAlp != 0:
        try:
            return bufAlp.Alp[Symbol]
        except:
            return -2
            # Такого символа нет в алфавите
    else:
        return -1
        # Алфавита с заданным языком нет

# Получение символа
def getSymbolByCode(Code, Lang):
    bufAlp = importAlphsbet(Lang)
    if bufAlp != 0:
        try:
            return bufAlp.Dic[Code]
        except:
            return -2
            # Такого символа нет в алфавите
    else:
        return -1
        # Алфавита с заданным языком нет
