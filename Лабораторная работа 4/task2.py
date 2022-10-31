main_grade = {}

def get_count_char(str_):
    str_ = str_.lower()
    for letter in str_:
        if letter.isalpha() is True:
            if letter in main_grade:
                main_grade[letter] += 1
            else:
                main_grade[letter] = 1
    return main_grade
 # TODO посчитать количество каждой буквы в строке в аргументе str_
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
