def iter_fibo(x):
    if x <= 2:
        return 1
    else:
        pre1, pre2 = 1, 1
        for i in range(3,x+1):
            present = pre1 + pre2
            pre2 = pre1
            pre1 = present

        return present

print iter_fibo(10)
