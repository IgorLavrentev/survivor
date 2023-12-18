def MassVote(N, Votes):
    # определяем каличество процентов для каждого кандидата (в виде списка)
    one_percent = 100/sum(Votes)
    list_percentages = [0]
    for i in range(N): 
        list_percentages.append(round(Votes[i] * one_percent, 3))

    # проверяем условие того, что максимальное число одно (выиграл только один кандидат)
    summ = 0
    flag = True
    for j in range(1, N + 1):
        if list_percentages[j] == max(list_percentages):
            summ += 1
    if summ > 1:
        flag = False
    
    # определяем победителя в соответстви с заданными критериями
    for K in range(1, N + 1):
        if list_percentages[K] > 50 and max(list_percentages) == list_percentages[K] and flag == True: # больше 50% и больше всех голосов
            return f'majority winner {K}'
        elif list_percentages[K] <= 50 and max(list_percentages) == list_percentages[K] and flag == True: # меньше 50%, но больше всех голосов
            return f'minority winner {K}'
        elif flag == False: # если количество голосов одинаково
            return 'no winner'

