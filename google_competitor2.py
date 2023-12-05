def WordSearch(len, s,  subs):

    # вычисляем длину строки
    counter = 0
    for i in s:
        counter += 1

    str_1 = '' # часть строки для каждой итерации
    list_f = [] # список для записи итоговых строк

    # строка разбивается на набор строк через выравнивание по заданной ширине
    while s != '':
        s_parth = s[0 : len]
        if ' ' not in s_parth:
            list_f.append(s_parth)
            s = s[len:].lstrip()
        else:
            last = s_parth.rfind(' ')
            s_parth_two = s[0:last].lstrip()
            list_f.append(s_parth_two)
            s = s[last + 1:]

    # каждая строка проверяется на наличие в ней заданного целого слова

    list_ret = [] # итоговый список

    # вычисляем длину искомой строки
    subs_counter = 0
    for k in subs:
        subs_counter += 1

# проверяем есть ли в каждой из строк искомое слово
    for i in list_f:
        if subs in i:
            ind = i.find(subs)
            ind_last = ind + subs_counter - 1
            if ind != 0:
                if i[ind - 1] in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
                    list_ret.append(0)
                    continue
            if i[ind:] == subs:
                list_ret.append(1)
            else:
                if i[ind_last + 1] in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
                    list_ret.append(0) 
                else:
                    list_ret.append(1) 
        else:
            list_ret.append(0)

    return list_ret