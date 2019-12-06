from src import d01, d02
from .utils import get_input


def test_03():
    assert d03.solve(["R8,U5,L5,D3", "U7,R6,D4,L4"]) == (6, 30)
    assert d03.solve(
        ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
    ) == (159, 610)
    assert d03.solve(
        [
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
        ]
    ) == (135, 410)
    assert d03.solve(get_input(3)) == (245, 48262)


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
