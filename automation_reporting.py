def ShopOLAP(N, items):
    # группирование продаж по названиям товаров
    count = 0 # счетчик количества совпадений в наименовании товара
    for i in range(N):
        for j in range(N):
            el_1 = items[i]
            el_2 = items[j]
            n_1 = el_1.find(' ')
            n_2 = el_2.find(' ')
            if j == i:
                continue
            if el_1[:n_1] == el_2[:n_2] and el_1 != ' ' and el_2 != ' ':
                items[j] = el_1[:n_1] + ' ' + str(int(el_1[n_1 + 1:]) + int(el_2[n_2 + 1:]))
                items.pop(i) 
                items.append(' ')
                count += 1
    # удаление из писка временных элементов ' '             
    del items[-count:]

    # сортировка по количеству продаж
    list_number = [] # список занчений продаж
    for k in range(len(items)):
        el_11 = items[k]
        n_11 = el_11.find(' ')
        list_number.append(int(el_11[n_11 + 1:]))
    list_number.sort(reverse = True)
    items_new = [] # итоговый список
    for v in list_number:
        for u in range(len(items)):
            el = items[u]
            n = el.find(' ')
            if str(v) == el[n + 1:]:
                items_new.append(el)
                items[u] = ' '
        
    # проверка если количества для каких-то товаров совпали и сортировка в соответствии с лексикографическим возрастанием
    for i in range(5):
        for t in range(len(items_new) - 1):
            e = items_new[t]
            e1 = items_new[t + 1]
            n0 = e.find(' ')
            n01 = e1.find(' ')
            if e[n0 + 1:] == e1[n01 + 1:]:
                list_s = items_new[t:t+2]
                list_s.sort()
                items_new = items_new[:t] + list_s + items_new[t + 2:]
    
    return items_new
