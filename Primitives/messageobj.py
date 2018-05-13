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
        er = self.checkStatus(self, other);
        if(er.iserror == 0):
            bufAlp = SymbolsAlg.importAlphsbet(self.lang)
            if bufAlp != 0:
                itter = 0
                lengthControl = 0
                while itter < len(self.mes):
                    if lengthControl >= len(other.Key):
                        lengthControl = 0
                    self.mes[itter] = modularArithmetic.modularsumm(self.mes[itter], other.Key[lengthControl], bufAlp.Length)
                    lengthControl = lengthControl + 1
                    itter = itter + 1
            else:
                return 0
        return 0 # Nothing

    # Вычитание ключа
    def __sub__(self, other):
        er = self.checkStatus(self, other);
        if (er.iserror == 0):
            bufAlp = SymbolsAlg.importAlphsbet(self.lang)
            if bufAlp != 0:
                itter = 0
                lengthControl = 0
                while itter < len(self.mes):
                    if lengthControl >= len(other.key):
                        lengthControl = 0
                    self.mes[itter] = modularArithmetic.modulardec(SymbolsAlg.getCodeBySymbol(self.mes[itter], self.lang), (SymbolsAlg.other.key[lengthControl], other.lang),
                                                                    bufAlp.Length)
                    lengthControl = lengthControl + 1
                    itter = itter + 1
            else:
                return 0
        return 0  # Nothing

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
        return  self.mes