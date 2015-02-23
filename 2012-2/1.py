file1 = open('data1.txt', 'r')
lines = file1.readlines()
tmp = 0
for i in range(len(lines)):
    lines[i] = lines[i].strip('\r\n()').split(',')
    lines[i] = map(int, lines[i])
    if lines[i][1] > tmp:
        tmp = lines[i][1]
for line in lines:
    if line[1] == tmp:
        print tuple(line)
