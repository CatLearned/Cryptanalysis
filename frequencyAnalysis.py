from math import log10

Types = {1: "../Alphabets/monoEng.txt", 2: "../Alphabets/biEng.txt", 
         3: "../Alphabets/triEng.txt", 4: "../Alphabets/quadEng.txt"}

def freqAnalysis(mesgArr, type):
    '''
    Описание функции, неинтерпретируемый код
    '''
    freqStats = {}
    f = open(Types[type], 'r')
    for line in f:
        textValue, count = line.split(' ')
        freqStats[textValue] = int(count)
    itter = 0
    while itter < len(mesgArr):
        mesg = mesgArr[itter].message
        if len(mesg) < type or type == 0:
            mesgArr[itter].frqnc = ':Анализ невозможен'
        else:
            res = 0
            counter = type
            summquad = sum(freqStats.values())
            while counter <= len(mesg):
                buff = mesg
                buff = buff[counter - type: counter]
                if buff in freqStats:
                    res = res + log10(float(freqStats[buff])/summquad)
                else:
                    res = res + log10(0.01 / summquad)
                counter = counter + 1
            mesgArr[itter].frqnc = res
        itter = itter + 1
    f.close()
    return mesgArr