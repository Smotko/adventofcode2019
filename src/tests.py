from src import d01, d02
from .utils import get_input


def test_02():
    assert d02.solve([1, 0, 0, 0, 99]) == 2
    assert d02.solve([2, 3, 0, 3, 99]) == 2
    assert d02.solve([1, 1, 1, 4, 99, 5, 6, 0, 99]) == 30
    input = [int(i) for i in get_input(2)[0].split(",")]
    input[1] = 12
    input[2] = 2
    assert d02.solve(input.copy()) == 3085697
    assert d02.solve2(input.copy()) == 9425


def test_01():
    assert d01.fuel(12) == 2
    assert d01.fuel(100756) == 33583
    assert d01.fuel2(14) == 2
    assert d01.fuel2(1969) == 966
    assert d01.fuel2(100756) == 50346
    assert d01.solve() == (3154112, 4728317)
