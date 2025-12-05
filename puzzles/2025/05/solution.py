
import sys
# we need this obnoxiousness to reference the utils package in repo root
sys.path.append("../")
sys.path.append("../../../")
from aoc_py_utils import utils
from collections.abc import Sequence


@utils.aoctimer("Part 1")
def part_one(input: Sequence[str]):
    ranges = []
    ingredients = []
    result = 0

    found_split = False
    for line in input:
        if not found_split:
            if line.strip() == '':
                found_split = True
            else:
                ranges.append(line)
        else:
            ingredients.append(int(line))

    rlist = []
    for r in ranges:
        x, y = map(int, r.split('-'))
        rlist.append((x, y))

    for i in ingredients:
        for j in rlist:
            if i >= j[0] and i <= j[1]:
                # print(i, j)
                result += 1
                break

    # print(ranges)
    # print(ingredients)
    # print(rlist)
    return result


@utils.aoctimer("Part 2")
def part_two(input: Sequence[str]):
    ranges = []
    result = 0
    found_split = False
    for line in input:
        if not found_split:
            if line.strip() == '':
                found_split = True
                break
            else:
                x, y = map(int, line.split('-'))
                ranges.append((x, y))
    while True:
        to_remove = set()
        to_add = []
        print(f"\nranges: {ranges}")
        ranges.sort()
        for i, r in enumerate(ranges):
            if i > 0:
                last = ranges[i - 1]
                if last[1] >= r[0]:
                    print(f"last 1 r 0: {last[1]}, {r[0]}")
                    # print(f"length of range {i} {r}: {r[1] - r[0]}")
                    to_remove.add(last)
                    print(f"removing last: {last}")
                    to_remove.add(r)
                    print(f"removing r: {r}")
                    n = (last[0], max(last[1], r[1]))
                    to_add.append(n)
                    print(f"adding: {n}")
            # rset.append((int(x), int(y)))
            # for i in range(int(x), int(y) + 1):
        ranges = list(filter(lambda r: r not in to_remove, ranges)) + to_add
        print(f'new ranges:{ranges}')
        # print(to_remove)
        # print(to_add)

        if len(to_remove) == 0:
            break
        # rset.add(i)
    print(f"\nranges at end: {ranges}\n")
    for r in ranges:
        result += ((r[1] + 1) - r[0])

    return result


is_test = False
# 24709063398958 wrong
# 336790092076639 too high
# 336790092076620 please be it
file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

part_one(input)

part_two(input)
