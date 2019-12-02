import math


def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def solve(program):
    position = 0
    command = {1: add, 2: multiply}
    while program[position] != 99:
        program[program[position + 3]] = command[program[position]](
            program[program[position + 1]], program[program[position + 2]]
        )
        position += 4
    return program[0]


def solve2(program):
    for noun in range(0, 99):
        for verb in range(0, 99):
            attempt = program.copy()
            attempt[1] = noun
            attempt[2] = verb
            res = solve(attempt)
            if res == 19690720:
                return 100 * noun + verb
