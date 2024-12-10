from random import randint

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

def output_arr(mat_1, mat_2, mat_rezult):
    print(mat_1, '\n', mat_2)
    print(mat_rezult)
    
    
if __name__ == "__main__":
    size = 3
    print(is_int(23423), is_int("dlfj"), is_int("3452"))
    mat_1 = input_arr(size)
    print(mat_1)
    mat_2 = generation_arr(size)
    print(mat_2)
    mat_rezult = sum_arr(mat_1, mat_2, size)
    print(mat_rezult)
    print(sort_incr(mat_1, size), sort_incr(mat_2, size))
    print(sort_decr(mat_1, size), sort_decr(mat_2, size))
    output_arr(mat_1, mat_2, mat_rezult)
    
    
    
    
    