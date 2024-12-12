from random import randint

def valid_value(message_input: str, message_err: str, template: list):
    while True:
        ch = input(message_input, )
        if is_int(ch):
            ch = int(ch)
            if ch in template:
                return ch
        print(message_err)

def valid_comand(ch, flag):
    if flag >= ch:
        return True
    print ('ERROR')
    return False

def is_int(s):
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
    mat = []
    for i in range(size):
        mat.append(randint(-10, 10))
    return mat

def sum_arr(mat_1, mat_2, size):
    mat_rezult = []
    for i in range(size):
        if mat_1[i] == mat_2[i]:
            mat_rezult.append(0)
        else:
            mat_rezult.append(mat_1[i] + mat_2[i])
    return mat_rezult

def sort_incr(mat, size):
    for i in range (size):
        for j in range(size-i-1):
            if mat[j]<mat[j+1]:
                mat[j], mat[j+1] = mat[j+1], mat[j]
    return mat

def sort_decr(mat, size):
    for i in range (size):
        for j in range(size-i-1):
            if mat[j]>mat[j+1]:
                mat[j], mat[j+1] = mat[j+1], mat[j]
    return mat

def mat_output(mat_1, mat_2, mat_rezult, mat_3 = []):
    print(mat_1, '\n', mat_2, '\n', mat_3)
    print(mat_rezult)
    
def proverka_sum(m_1, m_2, m_3):
    if m_1+m_2 == m_3:
        degree = sort_decr([m_1, m_2, m_3], 3)[0]
        return (m_1+m_2+m_3)**degree

def proverka_once(m_1, m_2, m_3):
    if (m_1+m_2 == m_3) or (m_1*m_2 == m_3):
        return True
    else:
        return proverka_twice(m_1, m_2, m_3)

def proverka_twice(m_1, m_2, m_3):
    for i in range(2):
        if m_2 != 0:
            if (m_1/m_2 == m_3) or (m_1**(1/m_2) == m_3):
                return True
        if (m_1-m_2 == m_3) or (m_1**m_2 == m_3):
            return True
        m_1, m_2 = m_2, m_1
    return False
        
def make_mat(size):
    i = input('Нажмите Enter, если хотите ввести матрицу ')
    if i == '':
        mat_1 = input_arr(size)
    else:
        mat_1 = generation_arr(size)
    return mat_1

def algoritm(mat_1, mat_2, size):
    mat_1 = sort_incr(mat_1, size)
    mat_2 = sort_decr(mat_2, size)
    mat_rezult = sum_arr(mat_1, mat_2, size)
    return sort_decr(mat_rezult, size)



if __name__ == "__main__":
    print(proverka_sum(1,2,3), proverka_sum(1, 2, 4))
    print(proverka_once(1, 2, 3), proverka_once(1, 2, 1), proverka_once(16, 2, 4))
    print(make_mat())
    
    
    