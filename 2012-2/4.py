from pylab import *
import random
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


x_times_y= 0
x_sum = 0
y_sum = 0
x_square_sum = 0
y_square_sum = 0

N = 30

for i in range(N):
    x_times_y += x[i] * y[i]
    x_sum += x[i]
    y_sum += y[i]
    x_square_sum += x[i] * x[i]
    y_square_sum += y[i] * y[i]

a = float(N * x_times_y - x_sum * y_sum) / (N * x_square_sum - x_sum * x_sum)
b = float(x_sum * x_sum * y_sum - x_times_y * x_sum) / \
    (N * x_square_sum - x_sum * x_sum)

print a, b


