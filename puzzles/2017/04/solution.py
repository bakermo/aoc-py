
# import sys
# # we need this obnoxiousness to reference the utils package in repo root
# sys.path.append("../../../")
# from aoc_py_utils import utils
from collections.abc import Sequence


def part_one(input: Sequence[str]):
    valid_count = 0
    for line in input:
        tokens = line.split()
        used = set();
        valid = True
        for t in tokens:
            # print(used)
            if t not in used:
                used.add(t)
            else:
                valid = False

        if valid:
            valid_count += 1
            
    return valid_count


def part_two(input: Sequence[str]):
    valid_count = 0
    for line in input:
        tokens = line.split()
        used = set();
        valid = True
        for t in tokens:
            # print(f't: {t}')
            s = ''.join(sorted(t))
            # print(f's: {s}')
            if s not in used:
                used.add(s)
            else:
                valid = False
           

        if valid:
            valid_count += 1
    return valid_count


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
