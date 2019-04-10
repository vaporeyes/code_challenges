from itertools import izip
with open("day2_inputs.txt") as f:
    inputfile = [line.split()[0] for line in f.readlines()]

for i in range(len(inputfile)):
    for j in range(1, len(inputfile)):
        index = [x for x, (a1, a2) in enumerate(izip(inputfile[i], inputfile[j])) if a1 != a2]
        if len(index) == 1:
            index = index[0]
            string = inputfile[i][:index] + inputfile[i][(index + 1):]

print string