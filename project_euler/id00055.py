"""
project euler #55
"""

def is_palindrome(num: int) -> bool:
    string = str(num)
    word = "".join(string.split())
    if word == word[::-1]:
        return True
    return False


def sum_reverse(num: int):
    num = str(num)
    rev_num = str(num)[::-1]
    return int(num) + int(rev_num)


def is_lychrel(num):
    i = 0
    sum_rev = num
    while i < 50:
        sum_rev = sum_reverse(sum_rev)
        if is_palindrome(sum_rev):
            return False
        i += 1
    return True

lychrel_numbers = []
for i in range(1,10001):
    if is_lychrel(i):
        lychrel_numbers.append(i)

print(f'{len(lychrel_numbers)} lychrel numbers')