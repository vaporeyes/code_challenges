with open('day1_inputs') as f:
    my_arr = []
    for line in f.readlines():
        my_arr.append(int(line.strip()))
    print reduce(lambda a, b: a + b, my_arr)
