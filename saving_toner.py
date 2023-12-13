def PrintingCosts(Line):
    # создание словаря
    dictionary = {} 

    dictionary[' '] = 0; dictionary['!'] = 9; dictionary['"'] = 6; dictionary['#'] = 24; dictionary['$'] = 29; dictionary['%'] = 22; 
    dictionary['&'] = 24; dictionary['\''] = 3; dictionary['('] = 12; dictionary[')'] = 12; dictionary['*'] = 17; dictionary['+'] = 13; 
    dictionary[','] = 7; dictionary['-'] = 7; dictionary['.'] = 4; dictionary['/'] = 10; dictionary['0'] = 22; dictionary['1'] = 19; 
    dictionary['2'] = 22; dictionary['3'] = 23; dictionary['4'] = 21; dictionary['5'] = 27; dictionary['6'] = 26; dictionary['7'] = 16; 
    dictionary['8'] = 23; dictionary['9'] = 26; dictionary[':'] = 8; dictionary[';'] = 11; dictionary['<'] = 10; dictionary['='] = 14; 
    dictionary['>'] = 10; dictionary['?'] = 15; dictionary['@'] = 32; dictionary['A'] = 24; dictionary['B'] = 29; dictionary['C'] = 20; 
    dictionary['D'] = 26; dictionary['E'] = 26; dictionary['F'] = 20; dictionary['G'] = 25; dictionary['H'] = 25; dictionary['I'] = 18; 
    dictionary['J'] = 18; dictionary['K'] = 21; dictionary['L'] = 16; dictionary['M'] = 28; dictionary['N'] = 25; dictionary['O'] = 18;  
    dictionary['P'] = 23; dictionary['Q'] = 31; dictionary['R'] = 28; dictionary['S'] = 25; dictionary['T'] = 16; dictionary['U'] = 23; 
    dictionary['V'] = 19; dictionary['W'] = 26; dictionary['X'] = 18; dictionary['Y'] = 14; dictionary['Z'] = 22; dictionary['['] = 18; 
    dictionary['\\'] = 10; dictionary[']'] = 18; dictionary['^'] = 7; dictionary['_'] = 8; dictionary['`'] = 3; dictionary['a'] = 23; 
    dictionary['b'] = 25; dictionary['c'] = 17; dictionary['d'] = 25; dictionary['e'] = 23; dictionary['f'] = 18; dictionary['g'] = 30; 
    dictionary['h'] = 21; dictionary['i'] = 15; dictionary['j'] = 20; dictionary['k'] = 21; dictionary['l'] = 16; dictionary['m'] = 22; 
    dictionary['n'] = 18; dictionary['o'] = 20; dictionary['p'] = 25; dictionary['q'] = 25; dictionary['r'] = 13; dictionary['s'] = 21; 
    dictionary['t'] = 17; dictionary['u'] = 17; dictionary['v'] = 13; dictionary['w'] = 25; dictionary['x'] = 13; dictionary['y'] = 24; 
    dictionary['z'] = 19; dictionary['{'] = 17; dictionary['|'] = 12; dictionary['}'] = 18; dictionary['~'] = 9; 

    counter = len(dictionary) 
    summ = 0 # переменная для суммы расхода тонера
    for i in range(len(Line)):
        for key in dictionary:
            if Line[i] == key:
                summ += dictionary.get(key)
                counter -= 1
        if counter == len(dictionary): # условия для добавления количества тонера для значений вне заданной таблицы
            summ += 23
        counter = len(dictionary)

    return summ