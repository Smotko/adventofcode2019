import itertools
from collections import defaultdict


def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def store(program, loc, input):
    program[loc] = input


def load(program, loc):
    ...


def jump_if_true():
    pass


def jump_if_false():
    pass


def less_than(a, b):
    return 1 if a < b else 0


def equals(a, b):
    return 1 if a == b else 0


def inc(command):
    return


def get_pos_nums(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    return pos_nums


def get_param(program, position, param, mode, relbase):
    loc = 0
    if mode == 0:
        loc = program[position + param]
    if mode == 1:
        loc = position + param
    if mode == 2:
        return program[program[position + param] + relbase]
    return program[loc]


def rel_base(a):
    return


def solve_program(program, input, position=0):
    for _ in range(110):
        program.append(0)
    command = {
        1: add,
        2: multiply,
        3: store,
        4: load,
        5: jump_if_true,
        6: jump_if_false,
        7: less_than,
        8: equals,
        9: rel_base,
    }
    relbase = 0
    increment = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2}
    while program[position] != 99:
        mode_1 = 0
        mode_2 = 0
        mode_3 = 0

        opcode = 0

        instruction = program[position]
        params = get_pos_nums(instruction)
        opcode = params.pop(0)
        try:
            params.pop(0)
            mode_1 = params.pop(0)
            mode_2 = params.pop(0)
            mode_3 = params.pop(0)
        except IndexError:
            pass

        if opcode == 3:
            # try:
            loc = 0
            if mode_1 == 0:
                loc = program[position + 1]
            if mode_1 == 1:
                loc = position + 1
            if mode_1 == 2:
                loc = program[position + 1] + relbase

            program[loc] = input.pop()
            # except:
            #     return output
        elif opcode == 4:
            output = get_param(program, position, 1, mode_1, relbase)
        elif opcode == 5:
            if get_param(program, position, 1, mode_1, relbase) != 0:
                position = get_param(program, position, 2, mode_2, relbase)
                continue

        elif opcode == 6:
            if get_param(program, position, 1, mode_1, relbase) == 0:
                position = get_param(program, position, 2, mode_2, relbase)
                continue
        elif opcode == 9:
            relbase += get_param(program, position, 1, mode_1, relbase)
        else:
            loc = 0
            if mode_3 == 0:
                loc = program[position + 3]
            if mode_3 == 1:
                loc = position + 3
            if mode_3 == 2:
                loc = program[position + 3] + relbase

            program[loc] = command[opcode](
                get_param(program, position, 1, mode_1, relbase),
                get_param(program, position, 2, mode_2, relbase),
            )
        position += increment[opcode]
    return output


def solve(program):
    return solve_program(program, [1])


def solve2(program):
    return solve_program(program, [2])
