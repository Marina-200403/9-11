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

if __name__ == "__main__":
    print(is_int(23423), is_int("dlfj"), is_int("3452"))