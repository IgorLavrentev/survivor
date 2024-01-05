def BastShoe(command):
    global n, list_changes, position, inp_previous # глобальные переменные

    # если команда задана некорректно возвращаем текцщую строку
    if len(command) == 1 and (command[0] != '4' and command[0] != '5'):
        list_changes.append(n)
        position += 1
        return n

    if command == '' or (command[0] != '1' and command[0] != '2' and command[0] != '3' and command[0] != '4' and command[0] != '5') :
        list_changes.append(n)
        position += 1
        return n
    
    if (int(command[0]) == 1 or int(command[0]) == 2 or int(command[0]) == 3) and command[1] != ' ':
        list_changes.append(n)
        position += 1
        return n

    if inp_previous == 4 and (int(command[0]) == 1 or int(command[0]) == 2 or int(command[0]) == 3): # редактирование списка изменений при выполнении операции 1 или 2
        lis = list_changes[position]
        list_changes.clear()
        list_changes.append(lis)
        position = 0
    
    inp_previous = int(command[0]) # присвоение переменной 'inp_previous' номера предыдущей команды

    # 1. Добавить в конец текущей строки
    if command[0] == '1':
        n += command[2:]
        list_changes.append(n)
        position += 1
        return n

    # 2. Удалить N символов из конца текущей строки, если N больше длины текущей строки, удаляем из неё все символы
    if command[0] == '2':  
        N = int(command[2:])
    if command[0] == '2' and N > len(n) :
        n = ''
        list_changes.append(n)
        position += 1
        return n
    if command[0] == '2':
        n = n[:-N]
        list_changes.append(n)
        position += 1
        return n

    # 3. Выдать i-й символ текущей строки
    if command[0] == '3' and int(command[2:]) >= len(n):
        n = ''
        list_changes.append(n)
        position += 1
        return n
    if command[0] == '3':
        i = int(command[2:])
        n = n[i]
        list_changes.append(n)
        position += 1

    # 4. Undo отмена последней операции 1 или 2
    if command[0] == '4' and position <= 1:
        n = list_changes[0]
        position = 1
        return n
    if command[0] == '4':
        n = list_changes[position - 1]
        position -= 1
    
    # 5. Redo выполнить заново последнюю отменённую с помощью Undo операцию
    if command[0] == '5' and position >= len(list_changes) - 1:
        n = list_changes[len(list_changes) - 1]
        position = len(list_changes) - 1
        return n
    if command[0] == '5':
        n = list_changes[position + 1]
        position += 1

    return n

n = '' # текущая строка
list_changes = [] # список всех её изменений
position = 0 #  переменная-позиция в списке list_changes
inp_previous = 0 # номер предыдущей команды
