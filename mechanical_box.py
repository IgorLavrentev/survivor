def SherlockValidString(s):
    # создание словаря и подсчет элементов
    dictionary = {}
    for i in range(len(s)):
        if s[i] not in dictionary:
            dictionary[s[i]] = 0

    for k, v in dictionary.items(): 
        quantity = s.count(k)
        dictionary[k] = quantity

    # создание эталонного элемента
    quantity_dictionary ={}
    for h in dictionary:
        quantity_dictionary[dictionary.get(h)] = 0

    for g, g_1 in dictionary.items(): 
        for l, l_1 in quantity_dictionary.items(): 
            if g_1 == l:
                quantity_dictionary[l] = l_1 + 1

    # обработка исключений
    if len(dictionary) == 2:
        key_1 = dictionary[list(dictionary.keys())[0]] # первый элемент словаря
        key_2 = dictionary[list(dictionary.keys())[1]] # второй элемент словаря
    if len(dictionary) == 2 and int(key_1) == int(key_2):
        return True
    if len(dictionary) == 2 and int(key_1) == int(key_2) - 1:
        return True
    if len(dictionary) == 2 and int(key_1) - 1 == int(key_2):
        return True

    # находим наиболее часто встречающийся элемент
    maxx = 0
    n = 0
    for d, d_1 in quantity_dictionary.items(): 
        if d_1 >= maxx:
            maxx = d_1
            n = d

    # внесение вохможных изменений в словарь
    for j, r in dictionary.items(): 
        if n != r and r > n:
            dictionary[j] = r - 1
            break

        if n != r and r < n and r == 1:
            del dictionary[j]
            break

    for t, u in dictionary.items(): # проверка на валидность
        if u != n:
            return False

    return True
