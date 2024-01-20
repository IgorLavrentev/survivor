def white_walkers(village: str) -> bool:
    # обработка исключений

    # если цифр меньше одной
    summ_el: int = 0
    for el in village:
        if el in ['0','1','2','3','4','5','6','7','8','9']:
            summ_el += 1
    if summ_el < 2:
        return False
    
    previous: int = 10 # начальное значение предыдущего значения

    for i in range(len(village)):

        if village[i] not in ['0','1','2','3','4','5','6','7','8','9']: # проверка является ли очередной элемент числом
            continue

        # находим очередной элемент
        if village[i] in ['0','1','2','3','4','5','6','7','8','9']:
            current: str = village[i]
            current_ind: int = i

        # если сумма предыдущего и текущего не равна 10, то текущему значению присваиваем предыдущее и переходим к следующему элементу списка
        if int(current) + int(previous) != 10:
            previous: str = current
            previous_ind: int = current_ind
            continue

        # проверяем количество '=' в срезе строки между двумя числами суммаа которых равна 10
        summ: int = 0
        slice = village[previous_ind:current_ind]
        for j in range(len(slice)):
            if slice[j] == '=':
                summ += 1

        if summ != 3: # если количество '=' меньше 3, слодовательно, результат False
            return False
        previous = current
        previous_ind = current_ind

    return True
