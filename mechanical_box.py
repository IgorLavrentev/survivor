def SherlockValidString(s):
    # создание словаря и подсчет элементов
    dictionary = {}
    for i in range(len(s)):
        if s[i] not in dictionary:
            dictionary[s[i]] = 0

    for k, v in dictionary.items(): 
        quantity = s.count(k)
        dictionary[k] = quantity

    n = next(iter(dictionary.values())) # количество первых элементов в словаре (берем за эталонное количество)
    key =  list(dictionary.keys())[0] # первый элемент в словаре (берем за эталонный элемент) 

    for j, r in dictionary.items(): # внесение вохможных изменений в словарь
        if n != r and n == 1:
            del dictionary[key[0]]
            break

        if n != r and r == 1:
            del dictionary[j]
            break

        if n != r and r < n:
            dictionary[key[0]] = n - 1
            break

        if n != r and r > n:
            dictionary[j] = r - 1
            break

    n = next(iter(dictionary.values())) # количество первых элементов в словаре (после возможных поправок)

    for t, u in dictionary.items(): # проверка на валидность
        if u != n:
            return False

    return True
