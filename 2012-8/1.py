filename = r'prog1.txt'
lines = [line.strip('\r\n') for line in open(filename, 'r').readlines()]
for line in lines:
    line = line.split(' ')
    print line[1]
