import math


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


def solve(program, input):
    position = 0
    command = {
        1: add,
        2: multiply,
        3: store,
        4: load,
        5: jump_if_true,
        6: jump_if_false,
        7: less_than,
        8: equals,
    }
    increment = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}
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
            program[program[position + 1]] = input
        elif opcode == 4:
            input = (
                program[program[position + 1]] if mode_1 == 0 else program[position + 1]
            )
        elif opcode == 5:
            if (
                program[program[position + 1]] if mode_1 == 0 else program[position + 1]
            ) != 0:
                position = (
                    program[program[position + 2]]
                    if mode_2 == 0
                    else program[position + 2]
                )
                continue

        elif opcode == 6:
            if (
                program[program[position + 1]] if mode_1 == 0 else program[position + 1]
            ) == 0:
                position = (
                    program[program[position + 2]]
                    if mode_2 == 0
                    else program[position + 2]
                )
                continue
        else:
            program[program[position + 3]] = command[opcode](
                program[program[position + 1]]
                if mode_1 == 0
                else program[position + 1],
                program[program[position + 2]]
                if mode_2 == 0
                else program[position + 2],
            )
        position += increment[opcode]
    return input
