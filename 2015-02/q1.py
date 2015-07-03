def f(x):
    if x < 1:
        return 1
    else:
        pre = 1
        for i in range(x):
            present = (161 * pre + 2457) % 2**24
            pre = present
        return present

if __name__ == "__main__":
    print f(100)
