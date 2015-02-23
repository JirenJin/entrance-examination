

def fibo_long(x):
    import q3
    if x <= 2:
        return '0'*31+'1'
    else:
        pre1, pre2 = '0'*31+'1', '0'*31+'1'
        for i in range(x - 2):
            present = q3.sum_long(pre1, pre2)
            pre2 = pre1
            pre1 = present
        return present

if __name__ == '__main__':
    print fibo_long(140)
