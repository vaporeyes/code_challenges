# i[1:][0:3], i[1:][1:4], i[1:][2:5], i[1:][3:6], i[1:][4:7], i[1:][5:8], i[1:][6:9]

# is_sub_div(k[0],k[1],k[2],k[3],k[4],k[5],k[6])
from itertools import permutations


c = []
perms = list(permutations([1,2,3,4,5,6,7,8,9,0]))
for s in perms:
    i = list(s)
    i = ''.join([str(x) for x in i])
    k = int(i[1:][0:3]), int(i[1:][1:4]), int(i[1:][2:5]), int(i[1:][3:6]), int(i[1:][4:7]), int(i[1:][5:8]), int(i[1:][6:9])
    if is_sub_div(k[0],k[1],k[2],k[3],k[4],k[5],k[6]):
        c.append(int(i))

print(sum(c))