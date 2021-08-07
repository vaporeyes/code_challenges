#!/usr/bin/env python3

FLOORS = {"(": 1, ")": -1}


def day1():
    with open("day1_input") as f:
        running_num = 0
        data = [x.strip() for x in f.readlines()]
        print(sum([FLOORS[x] for x in data[0]]))
        for i, k in enumerate(data[0]):
            running_num += FLOORS[k]
            if running_num == -1:
                return i + 1
