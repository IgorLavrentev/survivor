def TankRush(H1, W1, S1, H2, W2, S2):
    List_S1 = S1.split() # разбиваем изначальную первую строку на строки массива
    List_S2 = S2.split() # разбиваем изначальную вторую строку на строки массива
    summ = 0 # переменная для подсчета количества совпадений

    # проверяем есть ли все элементы вторго массива в первом массиве
    for i in List_S2:
        for j in List_S1:
            if i in j:
                summ += 1
                break
        if summ == len(List_S2):
            return True
