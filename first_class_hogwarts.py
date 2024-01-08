import itertools 
def BiggerGreater(input):
    # работа с исключениями (если все буквы одинаковые)
    summ = 0
    for e in range(len(input)):
        if input[e] == input[0]:
            summ += 1
    if summ == len(input):
        return ''
    
    # словарь русских букв
    dictionary_ru = {'а' : '01', 'б' : '02', 'в' : '03', 'г' : '04', 'д' : '05', 'е' : '06', 'ё' : '07', 'ж' : '08', 'з' : '09', 'и' : '10', 'й' : '11', 'к' : '12', 
                     'л' : '13', 'м' : '14', 'н' : '15', 'о' : '16', 'п' : '17', 'р' : '18', 'с' : '19', 'т' : '20', 'у' : '21', 'ф' : '22', 'х' : '23', 'ц' : '24',
                     'ч' : '25', 'ш' : '26', 'щ' : '27', 'ъ' : '28', 'ы' : '29', 'ь' : '30', 'э' : '31', 'ю' : '32', 'я' : '33'}
    
    # словарь английских букв
    dictionary_eng = {'a' : '01', 'b' : '02', 'c' : '03', 'd' : '04', 'e' : '05', 'f' : '06', 'g' : '07', 'h' : '08', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 
                      'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 
                      'y' : '25', 'z' : '26'}

    # выбираем словарь
    if input[0] in dictionary_ru:
        dictionary = dictionary_ru
    if input[0] in dictionary_eng:
        dictionary = dictionary_eng

    # рассчитываем значение исходного слова
    original_value = ''
    for i in range(len(input)):
        original_value += str(dictionary.get(input[i]))

    current_value = 999999999999999999999 # максимально большое значение
    final_word = '' # переменная для записи результата
    meaning = '' # переменная для очередного значения
    perm_set = itertools.permutations(input) 

    # присваиваем переменной порядковое значение в соответствии со словарем
    for val in perm_set:
        for j in range(len(val)):
            meaning += str(dictionary.get(val[j])) 
        if  current_value > int(meaning) > int(original_value): # сравниваем с иходным словом
            current_value = int(meaning)
            final_word = val
        meaning = ''

    # если перестановками не получилось получить искомое слово в соответствии с условими
    if final_word == input:
        return ''

    # вывод результата
    string = ''.join(final_word)
    return string
