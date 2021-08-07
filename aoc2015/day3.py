#!/usr/bin/env python3

DIRS = {
    "^": (1, 0),
    ">": (0, 1),
    "v": (-1, 0),
    "<": (0, -1),
}


def day3_1():
    points = list()
    point_longi = 0
    point_lati = 0
    with open("day3_input") as f:
        data = [dir for dir in [x.strip() for x in f.readlines()][0]]
        for direction in data:
            longi, lati = DIRS[direction]
            point_longi += longi
            point_lati += lati
            points.append([point_longi, point_lati])
            unique_points = list()
            for i in points:
                unique_points.append(str(i))
        print(len(set(unique_points)))
    return points


def day3_2(points):
    odds = list()
    evens = list()
    even_longi = 0
    even_lati = 0
    odd_longi = 0
    odd_lati = 0
    with open("day3_input") as f:
        data = [dir for dir in [x.strip() for x in f.readlines()][0]]
        for i, direction in enumerate(data):
            if i == 0:
                evens.append(direction)
            elif i % 2 == 0:
                evens.append(direction)
            else:
                odds.append(direction)
        points_even = list()
        for e in evens:
            longi, lati = DIRS[e]
            even_longi += longi
            even_lati += lati
            points_even.append([even_longi, even_lati])
            unique_points_even = list()
            for ie in points_even:
                unique_points_even.append(str(ie))
        ule = len(set(unique_points_even))
        points_odd = list()
        for o in odds:
            longi, lati = DIRS[o]
            odd_longi += longi
            odd_lati += lati
            points_odd.append([odd_longi, odd_lati])
            unique_points_odd = list()
            for io in points_odd:
                unique_points_odd.append(str(io))
        alls = unique_points_even + unique_points_odd
        print(f"total: {len(set(alls)) + 1}")
        ulo = len(set(unique_points_odd))
