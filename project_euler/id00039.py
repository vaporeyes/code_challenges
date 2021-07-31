# If p is the perimeter of a right angle triangle with integral
# length sides, {a,b,c}, there are exactly three solutions for 
# p = 120.
#
#   {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

# perimeter of a right triangle
# P = lambda a,b: a + b + math.sqrt((a**2)+(b**2))
# a = lambda P,b: P * ((P - (2 * b)) / (2 * (P - b)))
# b = lambda P,a: P * ((P - (2 *a)) / (2 * (P - a)))
from collections import defaultdict
import math
import operator

P = lambda a,b: a + b + math.sqrt((a**2)+(b**2))
res = defaultdict(list)
k = []
for a in range(1,1001):
    for b in range(1,1001):
        p = P(a,b)
        if p <= 1000 and p.is_integer():
            k.append([p,a,b])

for p, a, b in k:
    res[p].append(1)

print(sorted(res.items(), key=operator.itemgetter(1)))

