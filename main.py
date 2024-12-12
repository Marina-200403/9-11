import funcs

def menu_first():
    caption_start = "ЗАДАЧА 1\n1. Создать матрицы\n2. Выполнить алгоритм\n3. Вывести результат \n0. Выход\n"
    caption_err = "ERROR"
    menu_template = {
        0: (lambda: True, True),
        1: (make_mat, False),
        2: (algoritm, False),
        3: (mat_output, False)}
    flag = 1
    while True:
        ch = valid_value(caption_start,
                         caption_err,
                         list(menu_template))
        f, is_break = menu_template[ch]
        if ch == 1:
            size = input('Введите размер ')
            while is_int(size) != True:
                size = input('Введите целое число ')
            size = int(size)
            mat_1, mat_2 = f(size), f(size)
            flag = 2
        if ch == 2 and valid_comand(ch, flag):
            mat_rezult = f(mat_1, mat_2, size)
            flag = 3
        if ch == 3 and valid_comand(ch, flag):
            f(mat_1, mat_2, mat_rezult)
        if is_break:
            break
    return False
    
    
def menu_second():
    caption_start = "ЗАДАЧА 2\n1. Создать матрицы\n2. Выполнить алгоритм\n3. Вывести результат \n0. Выход\n"
    caption_err = "ERROR"
    menu_template = {
        0: (lambda: True, True),
        1: (make_mat, False),
        2: (proverka_sum, False),
        3: (mat_output, False)}
    flag = 1
    while True:
        ch = valid_value(caption_start,
                         caption_err,
                         list(menu_template))
        f, is_break = menu_template[ch]
        if ch == 1:
            size = input('Введите размер ')
            while is_int(size) != True:
                size = input('Введите целое число ')
            size = int(size)
            mat_1, mat_2, mat_3 = f(size), f(size), f(size)
            flag = 2
        if ch == 2 and valid_comand(ch, flag):
            mat_rezult = []
            for i in range(size):
                rezult = f(mat_1[i], mat_2[i], mat_3[i])
                mat_rezult.append(rezult)
            flag = 3
        if ch == 3 and valid_comand(ch, flag):
            f(mat_1, mat_2, mat_rezult, mat_3)
        if is_break:
            break
    return False

def menu_tree():
    caption_start = "ЗАДАЧА 3\n1. Создать матрицы\n2. Выполнить алгоритм\n3. Вывести результат \n0. Выход\n"
    caption_err = "ERROR"
    menu_template = {
        0: (lambda: True, True),
        1: (make_mat, False),
        2: (proverka_once, False),
        3: (mat_output, False)}
    flag = 1
    while True:
        ch = valid_value(caption_start,
                         caption_err,
                         list(menu_template))
        f, is_break = menu_template[ch]
        if ch == 1:
            size = input('Введите размер ')
            while is_int(size) != True:
                size = input('Введите целое число ')
            size = int(size)
            mat_1, mat_2, mat_3 = f(size), f(size), f(size)
            flag = 2
        if ch == 2 and valid_comand(ch, flag):
            mat_rezult = []
            for i in range(size):
                rezult = f(mat_1[i], mat_2[i], mat_3[i])
                mat_rezult.append(rezult)
            flag = 3
        if ch == 3 and valid_comand(ch, flag):
            f(mat_1, mat_2, mat_rezult, mat_3)
        if is_break:
            break
    return False

def menu_main():
    caption_start = "МЕНЮ\n0. Выход\n1.	Входные данные: 2 массива с числами одинакового размера. Нужно произвести сумму чисел из массивов, первый массив должен быть отсортирован в порядке убывания, второй в порядке возрастания. Если числа в массивах совпадают, их сумма будет равна нулю. Конечный массив нужно отсортировать в порядке возрастания.\n2.	Входные данные: 3 массива с числами одинакового размера. Нужно проверить, могут ли два числа под одним и тем же номером в сумме давать третье число. Если могут, то сумма трех чисел возводится в степень наименьшего числа.\n3.	Входные данные: 3 массива с числами. Требуется проверить, можно ли получить число из 3 массива, арифметическими преобразованиями с числами из двух других массивов. Числа проверяются последовательно (т.е. если проверяется первое число в 3 массиве, в двух других тоже проверяются только первые числа)."
    caption_err = "ERROR"
    menu_template = {
        0: (lambda: True, True),
        1: (menu_first, False),
        2: (menu_second, False),
        3: (menu_tree, False)}
    while True:
        ch = valid_value(caption_start,
                         caption_err,
                         list(menu_template))
        f, is_break = menu_template[ch]
        f()
        if is_break:
            break
        
if __name__ == "__main__":
    menu_main()
    
    
    
    
