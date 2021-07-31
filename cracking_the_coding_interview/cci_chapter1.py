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
