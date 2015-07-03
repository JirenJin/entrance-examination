def small_int(x):
    # dictionary for already existing h(n)
    d = {}
    if x < 1:
        d[1] = 0
        return None
    else:
        pre = 1
        for i in range(x):
            # compute h(n)
            present = (1103515245 * pre + 12345) % 2**26 % 2**10
            # if h(n) not exists, add (h(n), n) to the dictionary
            if present not in d:
                d[present] = i
            # if h(n) already exists, then we found the n0+k and n0
            else:
                return i - d[present]
            pre = present
        return None
print small_int(2**10+1)

