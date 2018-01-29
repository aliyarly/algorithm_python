#!encoding=utf-8

def my_atoi(item):
    ini = 0
    flag = True
    m = 10
    for s in item:
        # step the space
        if s == " ":
            continue
        elif s == "-":
            flag = False
        else:
            ini = ini * m + ord(s) - ord('0')
    # handle the +/-
    ini = ini * (1 if flag else -1)
    return ini


if __name__ == '__main__':
    s = "123"
    s2 = " 0123"
    s3 = "-123"
    print my_atoi(s)
    print my_atoi(s2)
    print my_atoi(s3)
