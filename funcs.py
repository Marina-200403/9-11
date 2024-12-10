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

if __name__ == "__main__":
    print(is_int(23423), is_int("dlfj"), is_int("3452"))
    print(input_arr(3))
    print(generation_arr(3))