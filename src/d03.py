import math

directions = {"D": (0, -1), "U": (0, 1), "L": (1, 0), "R": (-1, 0)}


def get_points(instructions):
    pos = (0, 0)
    points = set()
    for instr in instructions.split(","):
        distance = int(instr[1:])
        direction = instr[0]
        for i in range(distance):
            pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
            points.add(pos)
    return points


def get_steps(instructions, points):
    pos = (0, 0)
    step = 0
    point_steps = {}
    for instr in instructions.split(","):
        distance = int(instr[1:])
        direction = instr[0]
        for i in range(distance):
            pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
            step += 1
            if pos in points and pos not in point_steps:
                point_steps[pos] = step
    return point_steps


def solve(input):
    first, second = input
    first_points = get_points(first)
    second_points = get_points(second)
    int_points = first_points.intersection(second_points)
    points = [abs(p[0]) + abs(p[1]) for p in int_points]
    point_steps_first = get_steps(first, int_points)
    point_steps_second = get_steps(second, int_points)
    step_points = [
        point_steps_first[point] + point_steps_second[point] for point in int_points
    ]
    print(min(points), min(step_points))
    return min(points), min(step_points)
