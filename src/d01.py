import math
from .utils import get_int_input


def fuel(mass):
    return math.floor(mass / 3) - 2


def fuel2(mass):
    all_fuel = fuel(mass)
    f = fuel(all_fuel)
    while f >= 0:
        all_fuel += f
        f = fuel(f)

    return all_fuel


def solve():
    lines = get_int_input(1)
    res = 0

    res2 = 0

    for line in lines:
        res += fuel(line)
        res2 += fuel2(line)
    return res, res2
