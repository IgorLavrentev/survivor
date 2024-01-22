def Football(F:list[int], N: int) -> bool:

    # обработка исключений
    summ_el: int = 0 
    for el in range(len(F) - 1):
        if F[el] < F[el+1]:
            summ_el += 1
    if summ_el == N - 1:
        return False

    # вариант 1: поменять местами два произвольных элемента массива
    for i in range(N):
        for j in range(N):
            F[i], F[j] = F[j], F[i] # меняем два очередных элемента местами
            # проверка того, что элементы массива расположены по возрастанию
            summ: int = 0 
            for k in range(len(F) - 1):
                if F[k] < F[k+1]:
                    summ += 1
            if summ == N - 1:
                return True
            F[i], F[j] = F[j], F[i] # возаращаем элементы массива к исходным

    # вариант 2: изменить на обратный порядок произвольной последовательной цепочки элементов в массиве
    for u in range(N):
        for r in range(N):
            reverse: str = F[u:r + 1]
            reverse = reverse[::-1]
            F_1: list = F[:u] + reverse + F[r + 1:]
            if reverse == []:
                continue
            # проверка того, что элементы массива расположены по возрастанию
            summ_1: int = 0 
            for k_1 in range(len(F_1) - 1):
                if F_1[k_1] <= F_1[k_1+1]:
                    summ_1 += 1
            if summ_1 == N - 1:
                return True

    return False
