from pylab import *
import random

x = [None] * 30
y = [None] * 30
a = 0.5
b = 10
for i in range(30):
    x[i] = random.randrange(0, 30)
    y[i] = a * x[i] + b


plot(x, y, 'o')
title('3')
xlim(0, 30)
ylim(0, 30)
show()
