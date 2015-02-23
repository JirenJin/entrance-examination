import random
lines = [None] * 30
for i in range(0, 30):
    lines[i] = (random.randint(0, 30), random.randint(0, 30))
print lines

filename = open('data1.txt', 'w')
for line in lines:
    filename.writelines(str(line) + '\r\n')
