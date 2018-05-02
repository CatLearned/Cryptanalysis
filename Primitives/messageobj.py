from Primitives import keyobj, errorobj


# Объект сообщение обладает полями:
# 1. Сообщение
# 2. Язык сообщения


class Message:
    def __init__(self, mes, lang):
        self.mes = mes
        self.lang = lang

    def __add__(self, other):
        aer = self.checkStatus(self, other);
        if(aer.iserror == 0):
            itter = 0
            while itter < len(self.mes):
                #self.mes[itter] = modularArithmetic.modularsumm()
                return 0 # Nothing

    def __sub__(self, other):
        if type(other) is keyobj.Key:
            if (self.lang == other.lang):
                return 0 # Nothing
            else:
                return -1 # Ошибка
        else:
            return -1 # Ошибка

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