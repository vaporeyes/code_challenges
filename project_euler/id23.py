# A perfect number is a number for which the sum of its proper
# divisors is exactly equal to the number. For example, the sum
# of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors 
# is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two 
# abundant numbers is 24. By mathematical analysis, it can be shown 
# that all integers greater than 28123 can be written as the sum of 
# two abundant numbers. However, this upper limit cannot be reduced 
# any further by analysis even though it is known that the greatest 
# number that cannot be expressed as the sum of two abundant numbers 
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written
# as the sum of two abundant numbers.
import math


def divisors(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and n != i:
            divs.extend([i, n // i])
    return list(set(divs))

def is_perfect(n):
    if sum(divisors(n)) == n:
        return True

def is_abundant(n):
    if sum(divisors(n)) > n:
        return True

def solve(j):
    n = []
    sums = [0] * j
    total = 0
    for x in range(1, j):
        if is_abundant(x):
            n.append(x)
    
    for x in range(0, len(n)):
        for y in range(x, len(n)):
            s = n[x] + n[y]
            if s < j:
                if sums[s] == 0:
                    sums[s] = s
    
    for x in range(1, len(sums)):
        if sums[x] == 0:
            total += x
