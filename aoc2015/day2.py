#!/usr/bin/env python3

# 2*l*w + 2*w*h + 2*h*l
# 2x3x4
from functools import reduce


def surface_area_plus_extra(length: int, width: int, height: int):
    SURF_KEYS = {
        "length": length * width,
        "width": width * height,
        "height": height * length,
    }
    sorted_nums = sorted([length, width, height])[0:2]
    ribbon_len = sum([x for x in map(lambda x: x + x, sorted_nums)])
    surface_area = sum([x for x in map(lambda x: 2 * x, SURF_KEYS.values())])
    cubic_ft = reduce(lambda x, y: x * y, [length, width, height])
    smallest_area = min(SURF_KEYS.values())
    day2_1_total = surface_area + smallest_area
    day2_2_total = ribbon_len + cubic_ft
    print(day2_1_total)
    print(day2_2_total)
    return day2_1_total, day2_2_total


def day2():
    all_dims = list()
    with open("day2_input") as f:
        data = [x.strip() for x in f.readlines()]
        total_area = list()
        total_ribbon = list()
        for line in data:
            item = [int(x.strip()) for x in line.split("x")]
            area, ribbon = surface_area_plus_extra(*item)
            print(area, ribbon)
            total_area.append(area)
            total_ribbon.append(ribbon)
    print(f"total_area: {sum(total_area)}")
    print(f"total_ribbon: {sum(total_ribbon)}")
