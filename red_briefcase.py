import math
def TheRabbitsFoot(s, encode):
    # зашифровка строки
    if encode == True:
        # подготовка к формированию матрицы
        s_1 = s.replace(' ', '')
        N = len(s_1)
        q = math.sqrt(N)
        max = round(q, 0)
        min = int(q)

        # проверка, что количество элементов достаточно
        if max * min < N:
            min += 1

        list_f = [] # список для разбиения строки

        # формирование матрицы
        while s_1 != '':
            s_parth = s_1[0 : min]
            list_f.append(s_parth)
            s_1 = s_1[min: ]

        list_fin = [] # итоговый список
        str_fin = '' # итоговая строка
        counter = 0 # счетчик для учета разной длины строк матрицы
        # зашифровка
        for i in range(min):
            for k in list_f:
                if counter == len(k):
                    del list_f[list_f.index(k)]
                    continue
                str_fin += k[i]
            counter += 1
            list_fin.append(str_fin)
            str_fin = ""

        # переводим список в строку
        string = ''
        for el in list_fin:
            string += el
            string += ' '
        
        return string.rstrip()

    # расшифровка строки
    if encode == False:
        counter = 0 # счетчик для учета разной длины слов 
        srt_f = '' # итоговая строка
        fruits_list = s.split(" ")
        for i in range(len(fruits_list[0])):
            for j in fruits_list:
                if len(j) < counter + 1:
                    continue
                srt_f += j[counter]
            counter += 1
    
        return srt_f
