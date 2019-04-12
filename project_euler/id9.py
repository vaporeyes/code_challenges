#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#   a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math


def sum_py(a,b):
    a = a**2
    b = b**2
    c = math.sqrt(a + b)
    if (c).is_integer():
        return c

def find_triplet(n):
    for i in range(1, n):
        for j in range(1, n - 1):
            c = n - (i + j)
            if sum_py(i,j) == c:
                return i * j * c