filename = '7.txt'
file_rect = open(filename, 'r')
lines = file_rect.readlines()
file_rect.close()
lines = [map(int, line.strip('\r\n').split()) for line in lines]
rect_set = []


class rectangle(object):
    def __init__(self, line):
        self.x = line[0]
        self.y = line[1]
        self.w = line[2]
        self.h = line[3]
        self.clustered = False

    def is_overlayed(self, rectangle):
        if (self.x < rectangle.x < self.x + self.w or \
                rectangle.x < self.x < rectangle.x + rectangle.w) \
                and (self.y < rectangle.y < self.y + self.h \
                     or rectangle.y < self.y < rectangle.y + rectangle.h):
            return True


for line in lines:
    rect_set.append(rectangle(line))



class cluster(object):
    def __init__(self):
        self.element_num = 0
        self.element = []

    def rect_search(self, rect_set):
        for rect in rect_set:
            if rect.clustered == False:
                for el in self.element:
                    if rect.is_overlayed(el) == True:
                        self.element_num += 1
                        self.element.append(rect)
                        rect.clustered = True
                        break


cluster_list = []


# main loop
for rect in rect_set:
    if rect.clustered == False:
        tmp = cluster()
        tmp.element_num = 1
        tmp.element.append(rect)
        tmp.rect_search(rect_set)
        cluster_list.append(tmp)

for cluster in cluster_list:
    print cluster.element
    print cluster.element_num

