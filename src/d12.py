def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


def simulate(positions, velocities):
    for frst in range(len(positions)):
        for scnd in range(frst + 1, len(positions)):
            pos1 = positions[frst]
            vel1 = velocities[frst]

            pos2 = positions[scnd]
            vel2 = velocities[scnd]

            for i in range(3):
                if pos1[i] > pos2[i]:
                    vel1[i] -= 1
                    vel2[i] += 1
                elif pos1[i] < pos2[i]:
                    vel1[i] += 1
                    vel2[i] -= 1

    for indx in range(len(positions)):
        for i in range(3):
            positions[indx][i] += velocities[indx][i]


def to_tuples(lst):
    return tuple([tuple(i) for i in lst])


def parse_input(input):
    positions = []
    velocities = []
    for position in input:
        position = position.split(",")
        positions.append([int(val.split("=")[1].replace(">", "")) for val in position])
        velocities.append([0, 0, 0])
    return positions, velocities


def solve(input, steps):
    positions, velocities = parse_input(input)
    for _ in range(steps):
        simulate(positions, velocities)

        # print("step", _)
        # print(velocities, positions)
    energy = 0
    for indx in range(len(positions)):
        energy += sum(map(abs, positions[indx])) * sum(map(abs, velocities[indx]))
    return energy


def solve2(input):
    positions, velocities = parse_input(input)
    intervals = [0, 0, 0]
    for axis in range(3):
        states = set()

        axis_positions = tuple(pos[axis] for pos in positions)
        axis_speeds = [0, 0, 0, 0]

        for i in range(1000000):
            key = (axis_positions, tuple(axis_speeds))
            if key in states:
                intervals[axis] = i
                break

            states.add(key)

            new_axis_speeds = []
            for i in range(len(axis_positions)):
                for j in range(i, len(axis_positions)):
                    if axis_positions[i] < axis_positions[j]:
                        axis_speeds[i] += 1
                    elif axis_positions[i] > axis_positions[j]:
                        axis_speeds[i] -= 1
                # new_axis_speeds.append(vel_a)

            # axis_speeds = new_axis_speeds

            axis_positions = tuple(
                val + speed for val, speed in zip(axis_positions, axis_speeds)
            )

    return lcm(intervals[0], lcm(intervals[1], intervals[2]))
