from operator import indexOf

def TreeOfLife(H, W, N, tree):
    # переход от зкаков к цифрам
    next_line = ''
    initial_list = []
    for i in tree: 
        for i_1 in range(len(i)):
            if i[i_1] == '.':
                next_line += '0'
            if i[i_1] == '+':
                next_line += '1'
        initial_list.append(next_line)
        next_line = ''

    # четный год (ветки растут)
    def even_year(initial_list):
        initial_list_1 = initial_list
        h_new = ''
        counter = 0

        for h in initial_list_1: 
            for h_1 in range(len(h)):
                el = str(int(h[h_1]) + 1)
                h_new += el
            initial_list_1[counter] = h_new
            counter += 1
            h_new = ''
        counter = 0

        return initial_list_1
    
    # нечетный год (ветки стареют)
    def odd_year(initial_list):
        initial_list_2 = initial_list
        
        # создание списка индексов для удаления
        indexes_to_delete = []
        string_to_delete = ''
        for q in range(H):
            for q_1 in range(W):
                string_to_delete += '1'
            indexes_to_delete.append(string_to_delete)
            string_to_delete = ''

        # формирование списка индексов для замены с '1' на '0'
        next_line = 0
        for next_str in initial_list_2:
            indexes = [ind for ind, c in enumerate(next_str) if c == '3' or c == '4'] # находим индексы самих значений
            # меняем '1' на '0'
            for x in range(len(indexes)):
                # учет граничных условий и общего случая

                # если индекс это первый элемент первой строки
                if indexes[x] == 0 and next_line == 0:
                    # текущая строка
                    next_l = indexes_to_delete[next_line]
                    next_l =  '0' + next_l[indexes[x] + 1:]
                    next_l = next_l[:indexes[x] + 1]  + '0' + next_l[indexes[x] + 2:]
                    indexes_to_delete[next_line] = next_l
                    # строка ниже
                    next_l = indexes_to_delete[next_line + 1]
                    next_l =  '0' + next_l[indexes[x] + 1:]
                    indexes_to_delete[next_line + 1] = next_l
                    continue

                # если индекс это первый элемент последней строки
                if indexes[x] == 0 and next_line == len(indexes_to_delete) - 1:
                    # текущая строка
                    next_l = indexes_to_delete[next_line]
                    next_l =  '0' + next_l[indexes[x] + 1:]
                    next_l = next_l[:indexes[x] + 1]  + '0' + next_l[indexes[x] + 2:]
                    indexes_to_delete[next_line] = next_l
                    # строка ниже
                    next_l = indexes_to_delete[next_line - 1]
                    next_l =  '0' + next_l[indexes[x] + 1:]
                    indexes_to_delete[next_line - 1] = next_l 
                    continue

                # если индекс это последний элемент первой строки
                if indexes[x] == len(next_str) - 1 and next_line == 0:
                    # текущая строка
                    next_l = indexes_to_delete[next_line]
                    next_l = next_l[:indexes[x]] + '0'
                    next_l = next_l[:indexes[x] - 1]  + '0' + next_l[indexes[x]:]
                    indexes_to_delete[next_line] = next_l
                    # строка ниже
                    next_l = indexes_to_delete[next_line + 1]
                    next_l = next_l[:indexes[x]] + '0'
                    indexes_to_delete[next_line + 1] = next_l  
                    continue

                # если индекс это последний элемент последней строки строки
                if indexes[x] == len(next_str) - 1 and next_line == len(indexes_to_delete) - 1:
                    # текущая строка
                    next_l = indexes_to_delete[next_line]
                    next_l = next_l[:indexes[x]] + '0'
                    next_l = next_l[:indexes[x] - 1]  + '0' + next_l[indexes[x]:]
                    indexes_to_delete[next_line] = next_l
                    # строка выше
                    next_l = indexes_to_delete[next_line - 1]
                    next_l = next_l[:indexes[x]] + '0'
                    indexes_to_delete[next_line - 1] = next_l  
                    continue

                # если индекс на границе строки слева
                if indexes[x] == 0:
                    # текущая строка
                    next_l = indexes_to_delete[next_line]
                    next_l =  '0' + next_l[indexes[x] + 1:]
                    next_l = next_l[:indexes[x] + 1]  + '0' + next_l[indexes[x] + 2:]
                    indexes_to_delete[next_line] = next_l
                    # строка выше
                    next_l = indexes_to_delete[next_line - 1]
                    next_l =  '0' + next_l[indexes[x] + 1:]
                    indexes_to_delete[next_line - 1] = next_l
                    # строка ниже
                    next_l = indexes_to_delete[next_line + 1]
                    next_l =  '0' + next_l[indexes[x] + 1:]
                    indexes_to_delete[next_line + 1] = next_l
                    continue

                # если индекс на границе строки справа
                if indexes[x] == len(next_str) - 1:
                    # текущая строка
                    next_l = indexes_to_delete[next_line]
                    next_l = next_l[:indexes[x]] + '0'
                    next_l = next_l[:indexes[x] - 1]  + '0' + next_l[indexes[x]:]
                    indexes_to_delete[next_line] = next_l
                    # строка выше
                    next_l = indexes_to_delete[next_line - 1]
                    next_l = next_l[:indexes[x]] + '0'
                    indexes_to_delete[next_line - 1] = next_l
                    # строка ниже
                    next_l = indexes_to_delete[next_line + 1]
                    next_l = next_l[:indexes[x]] + '0'
                    indexes_to_delete[next_line + 1] = next_l
                    continue

                # если индекс первой строки
                if (0 < indexes[x] < len(next_str) - 1) and next_line == 0:
                    # текущая строка
                    next_l = indexes_to_delete[next_line]
                    next_l = next_l[:indexes[x] - 1]  + '0' + next_l[indexes[x]:]
                    next_l = next_l[:indexes[x]] + '0' + next_l[indexes[x] + 1:]
                    next_l = next_l[:indexes[x] + 1] + '0' + next_l[indexes[x] + 2:]
                    indexes_to_delete[next_line] = next_l
                    # строка ниже  
                    next_l = indexes_to_delete[next_line + 1]
                    next_l = next_l[:indexes[x]] + '0' + next_l[indexes[x] + 1:]
                    indexes_to_delete[next_line + 1] = next_l 
                    continue

                # если индекс последней строки
                if 0 < indexes[x] < len(next_str) - 1 and next_line == len(indexes_to_delete) - 1:
                    # текущая строка
                    next_l = indexes_to_delete[next_line]
                    next_l = next_l[:indexes[x] - 1]  + '0' + next_l[indexes[x]:]
                    next_l = next_l[:indexes[x]] + '0' + next_l[indexes[x] + 1:]
                    next_l = next_l[:indexes[x] + 1] + '0' + next_l[indexes[x] + 2:]
                    indexes_to_delete[next_line] = next_l
                    # строка выше  
                    next_l = indexes_to_delete[next_line - 1]
                    next_l = next_l[:indexes[x]] + '0' + next_l[indexes[x] + 1:]
                    indexes_to_delete[next_line - 1] = next_l 
                    continue

                # остальное
                if 0 < indexes[x] < len(next_str) - 1:
                    # текцщая строка 
                    next_l = indexes_to_delete[next_line]
                    next_l = next_l[:indexes[x] - 1]  + '0' + next_l[indexes[x]:]
                    next_l = next_l[:indexes[x]] + '0' + next_l[indexes[x] + 1:]
                    next_l = next_l[:indexes[x] + 1] + '0' + next_l[indexes[x] + 2:]
                    indexes_to_delete[next_line] = next_l
                    # строка выше
                    next_l = indexes_to_delete[next_line - 1]
                    next_l = next_l[:indexes[x]] + '0' + next_l[indexes[x] + 1:]
                    indexes_to_delete[next_line - 1] = next_l 
                    # строка ниже 
                    next_l = indexes_to_delete[next_line + 1]
                    next_l = next_l[:indexes[x]] + '0' + next_l[indexes[x] + 1:]
                    indexes_to_delete[next_line + 1] = next_l 
                    continue

            next_line += 1
        
        # приведение в соответствие двух списков (список индексов для удалени и очередной список веток дерева)
        next_l = ''
        initial_list_3 = []
        counter = 0
        for i in indexes_to_delete: 
            for i_1 in range(len(i)):
                if i[i_1] == '0':
                    next_l += '0'
                if i[i_1] != '0':
                    item = initial_list_2[counter]
                    next_l += item[i_1]
            initial_list_3.append(next_l)
            next_l = ''
            counter += 1

        return initial_list_3


    for j in range(N):

        # четный год (ветки растут)
        if j % 2 == 0:
            initial_list = even_year(initial_list)

        # нечетный год (ветки стареют)
        if j % 2 != 0:
            initial_list = even_year(initial_list)
            initial_list = odd_year(initial_list)

    # получение итогового списка в виде символов
    next_m = ''
    list_sivols = []
    for m in initial_list: 

        for m_1 in range(len(m)):
            if m[m_1] == '0':
                next_m += '.'
            if m[m_1] != '0':
                next_m += '+'
        list_sivols.append(next_m)
        next_m = ''

    return list_sivols
