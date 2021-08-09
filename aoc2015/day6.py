#!/usr/bin/env python3

import multiprocessing
import re
import turtle
from itertools import combinations


PARSE_REGEX = r"(turn\s(on|off)|toggle)\s(?P<start>\d+,\d+)\sthrough\s(?P<end>\d+,\d+)"


def _build_grid(x_size, y_size):
    grid_dict = dict()
    points = list()
    for i in range(x_size):
        for k in range(y_size):
            points.append((i, k))
    for p in points:
        sp, ep = p
        p_key = f"{sp}-{ep}"
        grid_dict[p_key] = 0
    return grid_dict


def _parse_line(input_str):
    state = 0
    p_keys = list()
    o_state, s_state, start_point, end_point = re.match(PARSE_REGEX, input_str).groups()
    if s_state == "on":
        state = 1
    elif s_state is None:
        state = None
    else:
        state = 0
    start_p1, start_p2 = start_point.split(",")
    end_p1, end_p2 = end_point.split(",")
    for i in range(int(start_p1), int(end_p1) + 1):
        for k in range(int(start_p2), int(end_p2) + 1):
            p_keys.append(f"{i}-{k}")
    return p_keys, state


def _parse_line2(input_str):
    state = 0
    p_keys = list()
    o_state, s_state, start_point, end_point = re.match(PARSE_REGEX, input_str).groups()
    if s_state == "on":
        state = 1
    # None is 'toggle'
    elif s_state is None:
        state = 2
    else:
        state = -1
    start_p1, start_p2 = start_point.split(",")
    end_p1, end_p2 = end_point.split(",")
    for i in range(int(start_p1), int(end_p1) + 1):
        for k in range(int(start_p2), int(end_p2) + 1):
            p_keys.append(f"{i}-{k}")
    return p_keys, state


def day6():
    grid = _build_grid(1000, 1000)
    with open("day6_input") as f:
        data = [x.strip() for x in f.readlines()]
        for item in data:
            p_keys, state = _parse_line(item)
            for k in p_keys:
                if state is None:
                    if grid[k] == 1:
                        grid.update({k: 0})
                    else:
                        grid.update({k: 1})
                else:
                    grid.update({k: state})
    turned_on = list()
    for item in grid:
        if grid[item] == 1:
            turned_on.append(item)
    return grid, turned_on


def day6_2():
    grid = _build_grid(1000, 1000)
    with open("day6_input") as f:
        data = [x.strip() for x in f.readlines()]
        for item in data:
            p_keys, state_change = _parse_line2(item)
            for k in p_keys:
                grid[k] += state_change
                if grid[k] < 0:
                    grid[k] = 0
    return grid


def draw_with_turtle():
    g, _ = day6()
    t = turtle.Turtle()
    for p in g:
        x, y = p.split("-")
        state = g[p]
        ptx = int(x)
        pty = int(y)
        t.goto(float(ptx), float(pty))
        if state == 1:
            t.dot(2, "blue")
        else:
            t.dot(2, "white")
