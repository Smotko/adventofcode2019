from collections import defaultdict
import heapq


def get_orbits(inpts):
    orbits = {}
    reverse_orbits = defaultdict(set)
    objects = set()
    for inpt in inpts:
        obj1, obj2 = inpt.split(")")
        orbits[obj2] = obj1
        reverse_orbits[obj1].add(obj2)
        reverse_orbits
        objects.add(obj1)
        objects.add(obj2)
    return orbits, objects, reverse_orbits


def solve2(inpts):
    orbits, objects, reverse_orbits = get_orbits(inpts)
    finish = "SAN"
    visited = set()
    h = []
    heapq.heappush(h, (0, "YOU"))

    while finish not in visited:
        priority, obj = heapq.heappop(h)
        if obj in visited:
            continue
        if obj == finish:
            return priority - 2

        visited.add(obj)
        if obj in orbits:
            heapq.heappush(h, (priority + 1, orbits[obj]))
        for to_add in reverse_orbits[obj]:
            heapq.heappush(h, (priority + 1, to_add))


def solve(inpts):
    orbits, objects, reverse_orbits = get_orbits(inpts)
    checksum = 0
    for obj in objects:
        orbiter = orbits.get(obj)
        while orbiter:
            checksum += 1
            orbiter = orbits.get(orbiter)

    return checksum
