def Keymaker(k: int) -> str:
    doors_array = [] # создание массива (первый шаг: открытие дверей)
    for i in range(k):
        doors_array.append(1)

    # второй шаг (закрытие каждой второй двери)
    for j in range(1, k, 2):
        doors_array[j] = 0

    # третий и последующие шаги
    for f in range(k - 2):
        for a in range(2 + f, k, 3 + f):
            if doors_array[a] == 0:
                doors_array[a] = 1
                continue
            if doors_array[a] == 1:
                doors_array[a] = 0
                continue
    
    # для ответа в виде строки
    string = ''
    for el in doors_array:
        string += str(el)
    return string
