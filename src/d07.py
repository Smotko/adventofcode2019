import itertools


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


def solve_program(program, input, position=0):
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
            try:
                program[program[position + 1]] = input.pop()
            except:
                return output, position
        elif opcode == 4:
            output = (
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
    return output, False


def solve(program):
    outputs = []
    seq = {}
    for sequence in list(itertools.permutations([0, 1, 2, 3, 4])):
        input = 0
        for setting in sequence:
            input, _ = solve_program(program, [input, setting])
        outputs.append(input)
        seq[input] = sequence

    return max(outputs)


def solve2(program):
    outputs = []
    seq = {}

    for sequence in list(itertools.permutations([5, 6, 7, 8, 9])):
        programs = {}
        positions = {}
        for prgrm in sequence:
            programs[prgrm] = program.copy()
        input = 0
        for setting in sequence:
            input, position = solve_program(programs[setting], [input, setting])
            positions[setting] = position
        while any(positions.values()):
            for setting in sequence:
                input, positions[setting] = solve_program(
                    programs[setting], [input], positions[setting]
                )
            outputs.append(input)
        seq[input] = sequence

    return max(outputs)
