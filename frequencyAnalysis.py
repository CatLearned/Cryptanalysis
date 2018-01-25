from math import log10

def quadAnalysis(mesgArr):
    statsquad = {}
    f = open('../Alphabets/quadEng.txt', 'r')
    for line in f:
        quad, count = line.split(' ')
        statsquad[quad] = int(count)
    itter = 0
    while itter < len(mesgArr):
        mesg = mesgArr[itter].message
        if len(mesg) < 4:
            mesgArr[itter].frqnc = ':Анализ невозможен'
        else:
            res = 0
            counter = 4
            summquad = sum(statsquad.values())
            while counter <= len(mesg):
                buff = mesg
                buff = buff[counter - 4: counter]
                if buff in statsquad:
                    res = res + log10(float(statsquad[buff])/summquad)
                else:
                    res = res + log10(0.01 / summquad)
                counter = counter + 1
            mesgArr[itter].frqnc = res
        itter = itter + 1
    f.close()
    return mesgArr