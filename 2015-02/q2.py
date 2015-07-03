import q1
def count_even(i_list):
    count = 0
    for i in i_list:
        if q1.f(i) % 2 == 0:
            count += 1
    return count

if __name__ == "__main__":
    i_list = [x for x in range(100)]
    print count_even(i_list)
