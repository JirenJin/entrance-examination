import open_file
filename = r'prog2.txt'
lines = open_file.open_file(filename)
lines = [line.split() for line in lines]
dict_xy = {}.fromkeys(['x', 'y'])

for line in lines:
    try:
        operand1 = int(line[1])
    except ValueError:
        operand1 = dict_xy[line[1]]
    try:
        operand2 = int(line[2])
    except ValueError:
        operand2 = dict_xy[line[2]]
    if line[0] == 'SET':
        dict_xy[line[1]] = operand2 
    elif line[0] == 'ADD':
        dict_xy[line[2]] = operand1 + operand2
    elif line[0] == 'PRN':
        print operand1, operand2
    else:
        pass
