from random import randint

def valid_value(message_input: str, message_err: str, template: list):
    """
    Ввод допустимого целого числа
    :param message_input: Сообщение перед вводом
    :param message_err:   Сообщение при вводе символа, не из шаблона
    :param template:      Список допустимых значений
    :return: целое число
    """
    
    while True:
        ch = input(message_input, )
        if is_int(ch):
            ch = int(ch)
            if ch in template:
                return ch
        print(message_err)

def valid_comand(ch, flag):
    """
    Ввод допустимой команды
    """
    
    if flag >= ch:
        return True
    print ('ERROR')
    return False

def is_int(s):
    """
    Проверка, является ли число s целым
    """
    
    try:
        if type(s) is int:
            return True
        if s is None:
            return False
        if not s.isdecimal():
            return False
        int(s)
        return True
    except (Exception, ValueError, TypeError):
        return False
    
def input_arr(size):
    """
    Ввод матрицы
    :param size: размер создаваемой матрицы
    """
    
    mat = []
    i = 0
    print ("Введите числа")
    while i != size:
        count = input()
        if is_int(count):
            mat.append(int(count))
            i += 1
        else:
            print ('try again')
    return mat

def generation_arr(size):
    """
    Генерация матрицы
    :param size: размер создаваемой матрицы
    """
    
    mat = []
    for i in range(size):
        mat.append(randint(-10, 10))
    return mat

def sum_arr(mat_1, mat_2, size):
    """
    Суммирование матриц
    :param mat_1: первое слагаемое
    :param mat_2: второе слагаемое
    :param size:  размер матриц
    """
    
    mat_rezult = []
    for i in range(size):
        if mat_1[i] == mat_2[i]:
            mat_rezult.append(0)
        else:
            mat_rezult.append(mat_1[i] + mat_2[i])
    return mat_rezult

def sort_incr(mat, size):
    """
    Сортировка матрицы в возрастающем порядке
    :param mat:  сортируемая матрица   
    :param size: размер матриц
    """
    
    for i in range (size):
        for j in range(size-i-1):
            if mat[j]<mat[j+1]:
                mat[j], mat[j+1] = mat[j+1], mat[j]
    return mat

def sort_decr(mat, size):
    """
    Сортировка матрицы в убывающем порядке
    :param mat:  сортируемая матрица   
    :param size: размер матриц
    """
    
    for i in range (size):
        for j in range(size-i-1):
            if mat[j]>mat[j+1]:
                mat[j], mat[j+1] = mat[j+1], mat[j]
    return mat

def mat_output(mat_1, mat_2, mat_rezult, mat_3 = []):
    """
    Вывод матриц
    :param mat_1:      первая введенная матрица 
    :param mat_2:      вторая введенная матрица 
    :param mat_rezult: результат выполнения алгоритма
    :param mat_3:      третья введенная матрица, если таковая есть
    :param size:       размер матриц
    """
    
    print(mat_1, '\n', mat_2, '\n', mat_3)
    print(mat_rezult)
    
def proverka_sum(m_1, m_2, m_3):
    """
    Проверка, является ли число m_3 суммой m_2 и m_1. Если является, возвращает 
    сумму этих трех чисел, возведенную в степень наименьшего
    :param mat_1: первое слагаемое
    :param mat_2: второе слагаемое
    :param mat_3: сумма 
    """
    
    if m_1+m_2 == m_3:
        degree = sort_decr([m_1, m_2, m_3], 3)[0]
        return (m_1+m_2+m_3)**degree

def proverka_once(m_1, m_2, m_3):
    """
    Первичная проверка для симметричных вычислений (от перемены мест 1 и 2 
    элемента ничего не меняется). Сумма и произведение. Возвращает True, если 
    mat_1 и mat_2 дают mat_3
    :param mat_1: первое число
    :param mat_2: второе число
    :param mat_3: результат математических операций над mat_1 и mat_2
    """
    
    if (m_1+m_2 == m_3) or (m_1*m_2 == m_3):
        return True
    else:
        return proverka_twice(m_1, m_2, m_3)

def proverka_twice(m_1, m_2, m_3):
    """
    Вторичная проверка для несимметричных вычислений (деление, корень, разница, 
    возведение в степень). Возвращает True, если mat_1 и mat_2 дают mat_3
    :param mat_1: первое число
    :param mat_2: второе число
    :param mat_3: результат математических операций над mat_1 и mat_2
    """
    
    for i in range(2):
        if m_2 != 0:
            if (m_1/m_2 == m_3) or (m_1**(1/m_2) == m_3):
                return True
        if (m_1-m_2 == m_3) or (m_1**m_2 == m_3):
            return True
        m_1, m_2 = m_2, m_1
    return False
        
def make_mat(size):
    """
    Выбор способа создания матрицы - самостоятельный ввод или генерация
    :param size: размер матрицы
    """
    
    i = input('Нажмите Enter, если хотите ввести матрицу ')
    if i == '':
        mat_1 = input_arr(size)
    else:
        mat_1 = generation_arr(size)
    return mat_1

def algoritm(mat_1, mat_2, size):
    """
    Выполнение алгоритма задачи 1: сортировка первой матрицы в возрастающем 
    порядке, второй в убывающей, суммирование этих матриц и сортировка этой 
    суммы в убывающем порядке
    :param mat_1: первая матрица
    :param mat_2: вторая матрица
    :param size:  размер матрицы
    """
    
    mat_1 = sort_incr(mat_1, size)
    mat_2 = sort_decr(mat_2, size)
    mat_rezult = sum_arr(mat_1, mat_2, size)
    return sort_decr(mat_rezult, size)



if __name__ == "__main__":
    """
    Тесты
    """
    
    print(proverka_sum(2, 3, 5), proverka_sum(1, 2, 4))
    print(proverka_once(1, 2, 3), proverka_once(1, 2, 1), proverka_once(16, 2, 4))
    print(make_mat(2))
    
    
    