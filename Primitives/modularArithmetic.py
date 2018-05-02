# coding=utf-8

# Модульная сумма
def modularsumm(symcode, keycode, alength):
    return (symcode + keycode) % alength


# Модульная разность
def modulardec(symcode, keycode, alength):
    return ((symcode - keycode) + alength) % alength
