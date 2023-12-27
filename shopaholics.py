def MaximumDiscount(N, price):
    price.sort(reverse=True) # сортировка списка по убыванию
    # учитываем, что количество цен может быть меньше трех
    if N < 3:
        return 0
    
    samm = 0 # переменная для подсчета суммы максимальной скидки
    for i in range(2, N, 3): # цикл для суммирования каждого третьего числа
        samm += price[i]

    return samm

