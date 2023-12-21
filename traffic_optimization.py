def Unmanned(L, N, track):
    # создаем словарь с точками остановки на светофоре
    dictionary = {}
    for k in range(len(track)):
        el = track[k]
        dictionary[el[0]] = el[1:]

    time = 1 # переменная времени
    for j in range(1, L + 1): # цикл по всей длине пути
        # вычисление сигнала светофора
        if j in dictionary and (dictionary.get(j)[0] + dictionary.get(j)[1]) < time:
            b = dictionary.get(j)
            n = time - (time // (b[0] + b[1])) * (b[0] + b[1])
        elif j in dictionary and (dictionary.get(j)[0] + dictionary.get(j)[1]) > time:
            b = dictionary.get(j)
            n = time
        else:
            time += 1
            continue
        # подсчет количества времени, которое автомобиль будет стоять на светофоре
        if n == b[0]:
            time += b[0] - n
            time += 1   
        if n < b[0]: 
            time += b[0] - n
        if n > b[0]:
            time += 1  

    return time

