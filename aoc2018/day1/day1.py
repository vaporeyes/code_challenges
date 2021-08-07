with open('day1_input.txt') as f:
    print(sum([int(line.strip()) for line in f.readlines()]))