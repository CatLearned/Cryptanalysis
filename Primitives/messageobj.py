from Primitives import keyobj, errorobj, modularArithmetic, SymbolsAlg

# Объект сообщение обладает полями:
# 1. Сообщение
# 2. Язык сообщения


class Message:
    def __init__(self, mes, lang):
        self.mes = mes
        self.lang = lang


    # Прибавление ключа
    def __add__(self, other):
        res = Message(self.mes, self.lang)
        er = self.checkStatus(other);
        if(er.iserror == 0):
            bufAlp = SymbolsAlg.importAlphsbet(self.lang)
            if bufAlp != 0:
                itter = 0
                lengthControl = 0
                bufstr = ""
                while itter < len(self.mes):
                    if lengthControl >= len(other.key):
                        lengthControl = 0
                    bufstr = bufstr + SymbolsAlg.getSymbolByCode(modularArithmetic.modularsumm(SymbolsAlg.getCodeBySymbol(self.mes[itter], self.lang), SymbolsAlg.getCodeBySymbol(other.key[lengthControl], self.lang), bufAlp.Length), self.lang)
                    lengthControl = lengthControl + 1
                    itter = itter + 1
                res.mes = bufstr
                return res
            else:
                return res
        return res # Nothing

    # Вычитание ключа
    def __sub__(self, other):
        res = Message(self.mes, self.lang)
        er = self.checkStatus(other);
        if (er.iserror == 0):
            bufAlp = SymbolsAlg.importAlphsbet(self.lang)
            if bufAlp != 0:
                itter = 0
                lengthControl = 0
                bufstr = ""
                while itter < len(self.mes):
                    if lengthControl >= len(other.key):
                        lengthControl = 0
                    bufstr = bufstr + SymbolsAlg.getSymbolByCode(modularArithmetic.modulardec(SymbolsAlg.getCodeBySymbol(self.mes[itter], self.lang), SymbolsAlg.getCodeBySymbol(other.key[lengthControl], other.lang),
                                                                    bufAlp.Length), self.lang)
                    lengthControl = lengthControl + 1
                    itter = itter + 1
                res.mes = bufstr
                return res
            else:
                return res
        return res  # Nothing

    # Проверка возможности применения ключа
    def checkStatus(self, other):
        er = errorobj.error
        if type(other) is keyobj.Key:
            if (self.lang == other.lang):
                er.iserror = 0
                er.description = "Проверка пройдена"
            else:
                er.iserror = 1
                er.description = "Языки не совпадают"
        else:
            er.iserror = 1
            er.description = "Второй операнд не ключ"
        return er  # Ошибка

    def getMessage(self):
        return self.mes