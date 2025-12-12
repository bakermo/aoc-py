
import sys
# we need this obnoxiousness to reference the utils package in repo root
sys.path.append("../")
sys.path.append("../../../")
from aoc_py_utils import utils
from collections.abc import Sequence


@utils.aoctimer("Part 1")
def part_one(input: Sequence[str]):
    result = 0

    shapes = []
    i = 0
    while i < len(input) and len(shapes) < 5:
        if input[i].endswith(":"):
            shape = utils.get_grid(input[i + 1: i + 4])
            shapes.append(shape)
        i += 1

    for s in shapes:
        utils.print_grid(s)

    regions = []
    for i in range(30, len(input)):
        line = input[i]
        parts = line.split(":")
        l, w = parts[0].split("x")
        regions.append(list(map(int, parts[1].split() + [l, w])))

    for r in regions:
        region_area = r[-1] * r[-2]
        count = sum(r[0:6])
        area_presents = count * 7
        max_present_area = count * 9

        # this was a total troll. you don't have
        # to consider the shapes at all
        if max_present_area <= region_area:
            result += 1

        print(r, region_area, count, area_presents, max_present_area)
    return result


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

part_one(input)
