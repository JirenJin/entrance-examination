def g(x):
    if x < 1:
        return 1
    else:
        pre = 1
        for i in range(x):
            present = (1103515245 * pre + 12345) % 2**26
            pre = present
        return present

if __name__ == '__main__':
    print g(2)
    print g(3)
