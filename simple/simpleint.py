print("-> Программа для вычисления простых чисел")
name = input('-> Имя файла для результатов \n-> ')

#import os
#if (os.stat(name).st_size == 0)
    #f = open(name, 'w')
    #f.write('2\n')
    #f.close()
    #current = 3
#else
#    f = open(name, 'r')
#    f.close()

current = int(input('-> Введите последнее число из файла \n-> '))
current = current + 1

while True:
    simp = True
    f = open(name, 'r')
    for line in f:
        if(current % int(line) == 0):
            simp = False
            break

    if (simp == True):
        print('Обнаружено простое число ', current)
        f = open(name, "a")
        f.write(str(current)+'\n')
        f.close()

    current = current + 1
