def LineAnalysis(line):
    # обработка исключений
    if line == '*.*':
        return True

    # если все элементы строки '*'
    summ_1 = 0
    for el in line:
        if el == '*':
            summ_1 += 1
    if summ_1 == len(line):
        return True
    
    # если все элементы строки между звездочками '.'
    summ_2 = 0
    for elem in line:
        if elem == '.':
            summ_2 += 1
    if summ_2 == len(line) - 2:
        return True
    
    # сравниваем первую часть строки (шаблон) с остальными частями строки
    i = 1
    while line[i] != '.':
        i += 1
    start = i

    # еще одно исключение если количество '*' в начале строки и в конце строки не совпадает
    u = len(line) - 1
    while line[u] != '.':
        u -= 1
    if start != len(line) - 1 - u:
        return False

    # создание шаблона для проверки корректности строки
    new_line = ''
    while line[i] != '*':
        new_line += line[i]
        i += 1

    while line[i] != '.':
        new_line += line[i]
        i += 1
    
    # проверка всей строки с шагом длины шаблона
    for k in range(start, len(line), len(new_line)):
        if line[k: k + len(new_line)] != new_line:
            return False

    return True
