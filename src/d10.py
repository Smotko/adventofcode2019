import math
import itertools


class AsteroidDistance:
    def __init__(self, amap):
        self.asteroids = set()
        for j, line in enumerate(amap.splitlines()):
            for i, point in enumerate(line):
                if point == "#":
                    self.asteroids.add((i, j))

    def distances(self):
        for asteroid in self.asteroids:
            yield asteroid, self.line_of_sight(asteroid)

    def line_of_sight(self, asteroid):
        can_see = 0
        for other_asteroid in self.asteroids:
            if asteroid == other_asteroid:
                continue

            dx = other_asteroid[0] - asteroid[0]
            dy = other_asteroid[1] - asteroid[1]
            gcd = math.gcd(dx, dy)
            dx /= gcd
            dy /= gcd
            blocked = False
            while other_asteroid != asteroid:
                other_asteroid = (other_asteroid[0] - dx, other_asteroid[1] - dy)
                if other_asteroid in self.asteroids and other_asteroid != asteroid:
                    blocked = True
                    break
            if not blocked:
                can_see += 1
        return can_see


def solve(amap):
    ad = AsteroidDistance(amap)
    return max([distance for _, distance in ad.distances()])


def solve2(lines, base):
    best = base[1], base[0]
    asteroids = set()
    for i, line in enumerate(lines.splitlines()):
        for j, point in enumerate(line):
            if point == "#":
                asteroids.add((i, j))

    phase = lambda point: math.atan2((point[1] - best[1]), (point[0] - best[0]))
    so = sorted(asteroids, key=phase, reverse=True)
    for i, (_, res) in enumerate(itertools.groupby(so, key=phase)):
        if i == 199:
            l = list(res)[0]
            return l[1] * 100 + l[0]
