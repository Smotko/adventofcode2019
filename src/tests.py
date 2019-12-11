from src import d01, d02, d03, d04, d05, d06, d07, d08, d09, d10, d11
from .utils import get_input, get_int_input


def test_11():
    program = [int(i) for i in get_input(11)[0].split(",")]
    assert len(d11.solve(program)) == 1894
    program = [int(i) for i in get_input(11)[0].split(",")]
    assert d11.solve2(program) == "JKZLZJBH"


def test_10():
    assert (
        d10.solve(
            """.#..#
.....
#####
....#
...##"""
        )
        == 8
    )
    assert d10.solve("\n".join(get_input(10))) == 344
    assert (
        d10.solve2(
            """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""",
            (11, 13),
        )
        == 802
    )
    assert d10.solve2("\n".join(get_input(10)), (30, 34)) == 2732


def test_09():
    assert d09.solve([1102, 34915192, 34915192, 7, 4, 7, 99, 0]) == 1219070632396864
    assert (d09.solve([104, 1125899906842624, 99])) == 1125899906842624
    assert (
        d09.solve(
            [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        )
        == 99
    )
    program = [int(i) for i in get_input(9)[0].split(",")]
    assert d09.solve(program) == 4288078517

    program = [int(i) for i in get_input(9)[0].split(",")]
    assert d09.solve2(program) == 69256


def test_08():
    assert d08.solve(["123456789012"], 3, 2) == 1
    assert d08.solve(["122456789202"], 3, 2) == 2
    assert d08.solve(get_input(8)) == 2318
    assert d08.solve2(get_input(8)) == "AHFCB"


def test_07():
    assert (
        d07.solve([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0])
        == 43210
    )
    program = [int(i) for i in get_input(7)[0].split(",")]
    assert d07.solve(program) == 206580
    assert (
        d07.solve2(
            [
                3,
                26,
                1001,
                26,
                -4,
                26,
                3,
                27,
                1002,
                27,
                2,
                27,
                1,
                27,
                26,
                27,
                4,
                27,
                1001,
                28,
                -1,
                28,
                1005,
                28,
                6,
                99,
                0,
                0,
                5,
            ]
        )
        == 139629729
    )
    program = [int(i) for i in get_input(7)[0].split(",")]
    assert d07.solve2(program) == 2299406


def test_06():
    assert (
        d06.solve(
            """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""".splitlines()
        )
        == 42
    )
    assert d06.solve(get_input(6)) == 142497
    assert (
        d06.solve2(
            """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""".splitlines()
        )
        == 4
    )
    assert d06.solve2(get_input(6)) == 301


def test_05():
    # assert d05.solve([1002, 4, 3, 4, 33, 99], 0) == 0
    assert d05.solve([3, 0, 4, 0, 99], 1) == 1
    program = [int(i) for i in get_input(5)[0].split(",")]
    assert d05.solve(program, 1) == 12896948

    assert d05.solve([3, 3, 1108, -1, 8, 3, 4, 3, 99], 8) == 1
    assert d05.solve([3, 3, 1108, -1, 8, 3, 4, 3, 99], 9) == 0

    assert d05.solve([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 0) == 0
    assert d05.solve([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 32) == 1

    # assert d05.solve([3,3,1108,-1,8,3,4,3,99, 8], 8) == 1

    assert d05.solve([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 8) == 1
    assert d05.solve([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 9) == 0
    assert d05.solve([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 4) == 1
    assert d05.solve([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 9) == 0
    assert d05.solve(
        [
            3,
            21,
            1008,
            21,
            8,
            20,
            1005,
            20,
            22,
            107,
            8,
            21,
            20,
            1006,
            20,
            31,
            1106,
            0,
            36,
            98,
            0,
            0,
            1002,
            21,
            125,
            20,
            4,
            20,
            1105,
            1,
            46,
            104,
            999,
            1105,
            1,
            46,
            1101,
            1000,
            1,
            20,
            4,
            20,
            1105,
            1,
            46,
            98,
            99,
        ],
        4,
    ), 999
    assert d05.solve(
        [
            3,
            21,
            1008,
            21,
            8,
            20,
            1005,
            20,
            22,
            107,
            8,
            21,
            20,
            1006,
            20,
            31,
            1106,
            0,
            36,
            98,
            0,
            0,
            1002,
            21,
            125,
            20,
            4,
            20,
            1105,
            1,
            46,
            104,
            999,
            1105,
            1,
            46,
            1101,
            1000,
            1,
            20,
            4,
            20,
            1105,
            1,
            46,
            98,
            99,
        ],
        8,
    ), 1000
    assert d05.solve(
        [
            3,
            21,
            1008,
            21,
            8,
            20,
            1005,
            20,
            22,
            107,
            8,
            21,
            20,
            1006,
            20,
            31,
            1106,
            0,
            36,
            98,
            0,
            0,
            1002,
            21,
            125,
            20,
            4,
            20,
            1105,
            1,
            46,
            104,
            999,
            1105,
            1,
            46,
            1101,
            1000,
            1,
            20,
            4,
            20,
            1105,
            1,
            46,
            98,
            99,
        ],
        9,
    ), 1001
    program = [int(i) for i in get_input(5)[0].split(",")]
    assert d05.solve(program, 5) == 7704130


def test_04():
    assert d04.solve() == (1169, 757)


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
