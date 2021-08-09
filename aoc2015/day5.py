#!/usr/bin/env python3

import collections
import multiprocessing
import re

# nice string:
# contains any vowel
# one letter twice in a row
# does not contain 'ab', 'cd', 'pq', 'xy'
#


VOWELS = "aeiou"


def _is_nice_string1(input_str: str) -> bool:
    has_vowels = r"(a|e|i|o|u)"
    has_two_consec_letters = r"(.)\1+"
    bad_substrings = r"(ab|cd|pq|xy)"
    vowels_match = re.findall(has_vowels, input_str)
    if len(vowels_match) >= 3:
        if re.search(has_two_consec_letters, input_str):
            if not re.search(bad_substrings, input_str):
                return True
    return False


def _get_string_pairs(input_str: str) -> list:
    data_str = list()
    for i, k in enumerate(input_str):
        try:
            data_str.append(input_str[i] + input_str[i + 1])
        except IndexError:
            pass
    return data_str


def _is_nice_string2(input_str: str) -> bool:
    every_other = r"(.)(.)\1+"
    pairs = _get_string_pairs(input_str)
    if pairs:
        if any([input_str.count(x) for x in pairs if input_str.count(x) > 1]):
            s = re.search(every_other, input_str)
            if s:
                return True
    return False


def day5():
    with open("day5_input") as f:
        data = [x.strip() for x in f.readlines()]
        with multiprocessing.Pool(10) as pool:
            imap_it1 = pool.map(_is_nice_string1, data)
            imap_it2 = pool.map(_is_nice_string2, data)
            day5_1 = len([x for x in imap_it1 if x])
            day5_2 = len([x for x in imap_it2 if x])
            print(f"day5 1: {day5_1}")
            print(f"day5 2: {day5_2}")
    return imap_it2
