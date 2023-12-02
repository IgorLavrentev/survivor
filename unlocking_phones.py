def PatternUnlock(N, hits):
    # calculating distances between points
    summ = 0
    for i in range(N - 1):
        if hits[i] == 1 and hits[i + 1] == 8 or hits[i] == 8 and hits[i + 1] == 1 or hits[i] == 6 and hits[i + 1] == 2 or hits[i] == 2 and hits[i + 1] == 6 or hits[i] == 2 and hits[i + 1] == 7 or hits[i] == 7 and hits[i + 1] == 2 or hits[i] == 5 and hits[i + 1] == 3 or hits[i] == 3 and hits[i + 1] == 5 or hits[i] == 1 and hits[i + 1] == 5 or hits[i] == 5 and hits[i + 1] == 1 or hits[i] == 9 and hits[i + 1] == 2 or hits[i] == 2 and hits[i + 1] == 9 or hits[i] == 2 and hits[i + 1] == 4 or hits[i] == 4 and hits[i + 1] == 2 or hits[i] == 8 and hits[i + 1] == 3 or hits[i] == 3 and hits[i + 1] == 8:
            summ += 1.41421356237
        else:
            summ += 1
    
    # removing zeros and dots, if any
    txt = str(round(summ, 5))
    result = ''
    for j in range(len(txt)):
        if txt[j] == '.' or txt[j] == '0':
            continue
        else:
            result += txt[j]

    return result
