import itertools


def is_permuted_multiple(num):
     nums = [num*2, num*3, num*4, num*5, num*6]
     str_nums = [''.join(set(str(x))) for x in nums]
     if all(x == str_nums[0] for x in str_nums):
         return str_nums

for i in itertools.count():
     if is_permuted_multiple(i):
         print(i)
         break

