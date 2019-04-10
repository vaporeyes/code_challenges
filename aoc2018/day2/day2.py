# aoc 2018 day 2
with open("day2_inputs.txt") as f:
    input = f.read()

j = 0
k = 0
for x in input.split():
    if [i for i in x if x.count(i) == 2]:
        j += 1
    if [i for i in x if x.count(i) == 3]:
        k += 1

print "total: {0}".format(j * k)