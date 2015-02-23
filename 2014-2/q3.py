def sum_long(x, y):
    #result = [ (int(x[i])+int(y[i])+(int(x[i+1])+int(y[i+1]))/10)%10 for i in range(len(x)-1) ] + [int(x[-1]) + int(y[-1])%10]
    result = [None] * len(x)
    c = 0
    for i in range(len(x) - 1, -1, -1):
        sums = int(x[i]) + int(y[i]) + c
        result[i] = sums % 10
        c = sums / 10
    return ''.join(str(e) for e in result)

A = '00123456789012345678901234567890'
B = '00987654321098765432109876543210'

#if __name__ == '__main__':
#    print sum_long(A, B)
