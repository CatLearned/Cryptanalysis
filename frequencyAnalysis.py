from math import log10

def quadAnalysis(mesgArr):
    statsquad = {}
    f = open('../Alphabets/quadEng.txt', 'r')
    for line in f:
        quad, count = line.split(' ')
        statsquad[quad] = int(count)
    itter = 0
    while itter < len(mesgArr):
        mesg = mesgArr[itter].split(":")
        if len(mesg[1]) < 4:
            mesgArr[itter] = mesgArr[itter] + ':Анализ невозможен'
        else:
            res = 0
            counter = 4
            summquad = sum(statsquad.values())
            while counter <= len(mesgArr[itter]):
                buff = mesg[1]
                buff = buff[counter - 4: counter]
                if buff in statsquad:
                    res = res + log10(float(statsquad[buff])/summquad)
                else:
                    res = res + log10(0.01 / summquad)
                counter = counter + 1
            mesgArr[itter] = mesgArr[itter] + ":" + str(int(res))
        itter = itter + 1
    f.close()
    return mesgArr