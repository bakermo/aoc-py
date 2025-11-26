
# import sys
# # we need this obnoxiousness to reference the utils package in repo root
# sys.path.append("../../../")
# from aoc_py_utils import utils
from collections.abc import Sequence


def part_one(input: Sequence[str]):
    line = input[0]
    counter = 0

    for i in range(0, len(line)):
        if line[i] == line[i - 1]:
            counter += int(line[i])
    return counter


def part_two(input: Sequence[str]):
    line = input[0]
    counter = 0

    for i in range(0, len(line)):
        if line[i] == line[i - len(line) // 2]:
            counter += int(line[i])
    return counter


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
