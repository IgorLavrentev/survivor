def BigMinus(s1, s2):
    if int(s1) < int(s2): # меняем местами исходные даннные если первое число меньше второго
        s1, s2 = s2, s1

    # ставим нули перед меньшей строкой
    s_temporary = s2[::-1]
    for k in range(len(s1) - len(s2)):
        s_temporary += '0'
    s2 = s_temporary[::-1]

    preliminary_line = ''
    final_line = ''
    flag = False

    # цикл по всей длине большей строки
    for i in range(len(s1) - 1, -1, -1):
        if int(s2[i]) <= int(s1[i]) and flag == False: 
            preliminary_line += str(int(s1[i]) - int(s2[i]))

        elif (int(s2[i]) > int(s1[i])) and (int(s1[i - 1]) == 0) and (flag == False):
            preliminary_line += str(10 + int(s1[i]) - int(s2[i]))
            s1 = s1[: i-1] + "9" + s1[i:]
            flag = True

        # учет флагов
        elif flag == True and (int(s1[i - 1]) == 0):
            preliminary_line += str(9 - int(s2[i]))
            s1 = s1[: i-1] + "9" + s1[i:]
            flag == True

        elif flag == True and (int(s1[i - 1]) != 0):
            preliminary_line += str(9 - int(s2[i]))
            s1 = s1[: i-1] + str(int(s1[i-1])-1) + s1[i:] 
            flag = False

        else:
            preliminary_line += str(10 + int(s1[i]) - int(s2[i]))
            s1 = s1[: i-1] + str(int(s1[i-1])-1) + s1[i:]
    
    # меняем порядок элементов строки, так как цикл шёл с конца строки
    final_line = preliminary_line[::-1].lstrip("0")
    if final_line == '':
        final_line = '0'
    return final_line
