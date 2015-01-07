def open_file(filename):
    lines = [line.strip('\r\n') for line in open(filename, 'r').readlines()]
    return lines
