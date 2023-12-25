import re
def TankRush(H1, W1, S1, H2, W2, S2):
    List_S1 = S1.split() # разбиваем изначальную первую строку на строки массива
    List_S2 = S2.split() # разбиваем изначальную вторую строку на строки массива
    summ = 0 # переменная для подсчета количества совпадений
    count = 0 # переменная для подсчёта строк
    
    # проверка условия, что масив одномерный и в этом случае достаточно проверить входимость одной строки в другую
    if H2 == 1 and S2 in S1: 
        return True

    for i in range(len(List_S1) - 1):
        # обработка исключений
        L1 = List_S1[0]
        res = all(ele == L1[0] for ele in L1) 
        # если все символы строки одинаковые, то проходим по всей длине строки
        if res:        
            indexes = list(range(1, len(List_S1[i])))
            count += 1 
        # если исключений не найдено
        if not res:
            indexes = [match.start() for match in re.finditer((List_S2[0]), List_S1[i])] # находим все индексы вхождения в первую строчку массива 1
            count += 1 

        # проверка в соответствии со всеми найдеными индексами остальных (нижних) строк массива
        for j in indexes:
            n = count
            for k in range(1, H2):          
                srring = List_S1[n]
                if srring[j : j + W2] == List_S2[k]:
                    summ += 1
                if summ == H2 - 1:
                    return True
                n += 1
            summ = 0
    
    return False
