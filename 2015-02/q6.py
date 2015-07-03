def small_int(x):
    d = {}
    if x < 1:
        d[1] = 0
        return None
    else:
        pre = 1
        for i in range(x):
            present = (1103515245 * pre + 12345) % 2**26
            if present not in d:
                d[present] = i
            else:
                return i - d[present]
            pre = present
        return None
print small_int(2**26+1)
