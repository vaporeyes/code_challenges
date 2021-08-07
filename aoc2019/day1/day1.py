import math
from functools import reduce


def get_fuel(mass: int) -> float:
    return math.floor((float(mass) / 3.0)) - 2

def expand_fuel(mass: int) -> float:
    def get_fuel(mass: int) -> float:
        return math.floor((float(mass) / 3.0)) - 2
    mass_sum = 0
    while True:
        mass = get_fuel(mass)
        if mass <= 0:
            break
        mass_sum += mass
    return mass_sum

def recurse_fuel(mass: int):
    def get_fuel(mass: int) -> float:
        return math.floor((float(mass) / 3.0)) - 2
    mass = get_fuel(mass)
    if mass <= 0:
        return 0
    mass_sum += mass
    return recurse_fuel(mass)
#