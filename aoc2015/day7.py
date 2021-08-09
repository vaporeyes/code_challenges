#!/usr/bin/env python3

import re

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i

# NOT dq -> dr

OPS = {
    "LSHIFT": lambda x, y: x << y,
    "RSHIFT": lambda x, y: x >> y,
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "NOT": lambda x: ~x,
    "XOR": lambda x, y: x ^ y,
}

def day7_first_start():
    with open("day7_input_test") as f:
        data = [x.strip() for x in f.readlines()]
        for i in data:
            ... # derp
