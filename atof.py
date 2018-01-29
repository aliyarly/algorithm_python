#!encoding=utf-8
ini = 0


def my_atof(item):
    global ini
    flag = True
    tmp = []
    item = item.strip()
    print item
    for s in item:
        print s, "char"
        if s == "-":
            flag = False
            item = item[1:]
            continue
        # check the frist char is integer    
        if not (s >= '0' and s <= '9'):
            break
        else:
            # split it to different process
            tmp = item.split(".")
            print tmp
            break
    print tmp
    integer_process(tmp[0])
    decimal_process(tmp[-1])
    ini = ini * (1 if flag else -1)
    return ini


def integer_process(data):
    global ini
    m = 10
    for si in data:
        ini = ini * m + ord(si) - ord('0')


def decimal_process(data):
    d = 10.0
    global ini
    for sd in data:
        # no e or E
        ini = ini + (ord(sd) - ord('0')) / d
        d *= d


def index_process():
    pass


if __name__ == '__main__':
    s = "  -123.45"
    print my_atof(s)
