def delete_duplicates(A):
	if not A:
		return 0
	write-index = 1
	for i in range(l, len(A)):
		if A[write-index - 1] != A[i]:
		A[write-index] = A[i]
		write-index += 1
	return write-index

# 1.1
def is_unique(string):
	char_list = []
	for char in string:
		if char in char_list:
			print("string does not contain all unique chars")
			return False
		else:
			char_list.append(char)
	return True
	
def is_unique_with_set(string):
	if len(set(string)) == len(string):
		return True
	else:
		return False

# 1.2
def is_permutation(first, second):
	first = sorted(first.replace(' ',''))
	second = sorted(second.replace(' ',''))
	if first == second:
		return True
	else:
		return False

# 1.3
def urlify(string):
	return (string.strip()).replace(' ', '%20')

# 1.4
def palindrome_permutation(string, second):
	reverse = ''
	string = string.replace(' ','')
	second = second.replace(' ','')
	for i in range(0, len(string)):
		reverse += string[~i]
	if string == reverse:
		string = sorted(string)
		second = sorted(second)
		if string == second:
			print("is palindrome permutation")
		else:
			print("not a palindrom permutation")
			
# 1.5
# did not solve this one on my own
def is_one_away(first: str, other: str) -> bool:
    """Given two strings, check if they are one edit away. An edit can be any one of the following.
    1) Inserting a character
    2) Removing a character
    3) Replacing a character"""

    skip_difference = {
        -1: lambda i: (i, i+1),  # Delete
        1: lambda i: (i+1, i),  # Add
        0: lambda i: (i+1, i+1),  # Modify
    }
    try:
        skip = skip_difference[len(first) - len(other)]
    except KeyError:
        return False  # More than 2 letters of difference

    for i, (l1, l2) in enumerate(zip(first, other)):
        if l1 != l2:
            i -= 1  # Go back to the previous couple of identical letters
            break

    # At this point, either there was no differences and we exhausted one word
    # and `i` indicates the last common letter or we found a difference and
    # got back to the last common letter. Skip that common letter and handle
    # the difference properly.
    remain_first, remain_other = skip(i + 1)
    return first[remain_first:] == other[remain_other:]

# 1.6
from itertools import groupby
def compress(string):
    compressed = ''.join('%s%s' % (char, sum(1 for _ in group)) for char, group in groupby(string))
	if len(compressed) <= len(string):
		print(compressed)
	else:
		print(string)
		
# palindromic number
def reverse(x):
	result, x_remaining = 0, abs(x)
	while x_remaining:
		result = result * 10 + x_remaining % 10
		x_remaining //= 10
	return -result if x < 0 else result
# alternate
# def is_palindromic_number(x):
# 	if x == int(str(x)[::-1]):
#		return True
def is_palindromic_number(x):
	return True if x == reverse(x)