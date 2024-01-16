def MatrixTurn(Matrix, M, N, T):
    # количество поворотов в одной матрице (количество 'рамок')
    if M % 2 == 0 and M <= N:
            repeat = M // 2
    if N % 2 == 0 and N < M:
            repeat = N // 2

    for t_1 in range(T): # цикл по количеству шагов
        for step in range(repeat):

            # создание 4-х строк для поворота 

            # верхняя строка
            str_next_1 = Matrix[step]
            str_1 = str_next_1[0 + step : len(str_next_1) - 1 - step]

            # правая строка
            str_2 = ''
            for i in range(0 + step, len(Matrix) - 1 - step):
                str_next_2 = Matrix[i]
                str_2 += str_next_2[len(str_next_2) - 1 - step]

            # нижняя строка
            str_next_3 = Matrix[len(Matrix) - 1 - step]
            str_3 = str_next_3[1 + step: len(str_next_3) - step]

            # левая строка
            str_4 = ''
            for j in range(1 + step, len(Matrix) - step):
                str_next_4 = Matrix[j]
                str_4 += str_next_4[0 + step]

            # внесение изменений в матрицу

            # верхняя редактируемая строка
            str_01 = Matrix[0 + step]
            if step > 0:
                Matrix[0 + step] = str_01[:step] + str_4[0] + str_1 + str_01[len(str_01) - step:]
            if step == 0:
                Matrix[0] = str_4[0] + str_1


            # редактируемые строки посередине
            counter = 0 
            counter_str_4 = 1
            for k in range(1 + step, len(Matrix) - 1 - step):
                str_02 = Matrix[k]
                Matrix[k] = str_02[:step] + str_4[counter_str_4] + str_02[1 + step : len(str_02) - 1 - step] + str_2[counter] + str_02[len(str_02) - step:]
                counter += 1
                counter_str_4 += 1

            # нижняя редактируемая строка
            str_04 = Matrix[len(Matrix) - 1 - step]
            if step > 0:
                Matrix[len(Matrix) - 1 - step] = str_04[:step] + str_3 + str_2[len(str_2) - 1] + str_04[len(str_04) - step:]
            if step == 0:    
                Matrix[len(Matrix) - 1] = str_3 + str_2[len(str_2) - 1]

