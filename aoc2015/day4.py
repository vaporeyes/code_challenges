#!/usr/bin/env python3
from hashlib import md5


INPUT_KEY = "iwrupvqb"
# INPUT_KEY = "abcdef"

# To do this, he needs to find MD5 hashes which, in hexadecimal,
# start with at least five zeroes. The input to the MD5 hash is
# some secret key (your puzzle input, given below) followed by a
# number in decimal. To mine AdventCoins, you must find Santa the
# lowest positive number (no leading zeroes: 1, 2, 3, ...) that
# produces such a hash.
#
#
def _hash_string(input_str: str):
    return md5(input_str.encode("utf-8")).hexdigest()


def mine_adventcoins():
    n = 0
    while True:
        input_str = f"{INPUT_KEY}{n}"
        md5_hash = _hash_string(input_str)
        if md5_hash.startswith("00000"):
            print(f"5 digit hash num: {n}")
        if md5_hash.startswith("000000"):
            print(f"6 digit hash num: {n}")
            return n
        n += 1
