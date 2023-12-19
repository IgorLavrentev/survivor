def UFO(N, data, octal):
    final_list = [] # список для формирования ответа
    for i in range(N):
        if octal == True: # перевод в восмиричную систему счисления очередного элемента исходного списка
            decimal_number = int(str(data[i]), 8)
            final_list.append(decimal_number)
        if octal == False:  # перевод в шестнадцатиричную систему счисления очередного элемента исходного списка
            decimal_number = int(str(data[i]), 16)
            final_list.append(decimal_number)     
    return final_list

