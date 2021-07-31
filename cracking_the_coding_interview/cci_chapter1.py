def is_unique(string):
    char_list = []
    for char in string:
        if char in char_list:
            print("string does not contain all unique chars")
            return False
    return True


def is_unique_with_set(string):
    return len(set(string)) == len(string)

def is_permutation(first, second):
    return sorted(first.replace(" ", "")) == sorted(second.replace(" ", ""))

def urlify(string):
    return (string.strip()).replace(" ", "%20")

def palindrome_permutation(string, second):
    reverse = ""
    string = string.replace(" ", "")
    second = second.replace(" ", "")
    for i in range(0, len(string)):
        reverse += string[~i]
    if string == reverse:
        string = sorted(string)
        second = sorted(second)
        if string == second:
            print("is palindrome permutation")
        else:
            print("not a palindrome permutation")

def is_one_away(first: str, other: str) -> bool:
    """Given two strings, check if they are one edit away. An edit can be any one of the following.
    1) Inserting a character
    2) Removing a character
    3) Replacing a character"""

    skip_difference = {
        -1: lambda i: (i, i + 1),  # Delete
        1: lambda i: (i + 1, i),  # Add
        0: lambda i: (i + 1, i + 1),  # Modify
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

from itertools import groupby


def compress(string):
    compressed = "".join(
        "%s%s" % (char, sum(1 for _ in group)) for char, group in groupby(string)
    )
    if len(compressed) <= len(string):
        print(compressed)
    else:
        print(string)
