from pylab import *
file1 = open('data1.txt', 'r')
lines = file1.readlines()
tmp = 0
x = [None] * 30
y = [None] * 30
for i in range(len(lines)):
    lines[i] = lines[i].strip('\r\n()').split(',')
    lines[i] = map(int, lines[i])
    x[i] = lines[i][0]
    y[i] = lines[i][1]

print x, y
plot(x, y, 'o')
show()
