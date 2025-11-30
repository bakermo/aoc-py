
# import sys
# # we need this obnoxiousness to reference the utils package in repo root
# sys.path.append("../../../")
# from aoc_py_utils import utils
from collections.abc import Sequence
import re
from typing import List


def part_one(input: Sequence[str]):

    result = 0
    for line in input:
        f = None
        l = None
        for c in line:
            if c.isdigit():
                f = c
                break
        for c in reversed(line):
            if c.isdigit():
                l = c
                break

        result += int(f"{f}{l}")

        # print(f"{f}{l}")

    return result


def map_nums(input):
    mapping = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    return mapping.get(input)


def part_two(input: Sequence[str]):
    result = 0
    for line in input:
        matches: List[re.Match] = []
        matches.extend(re.finditer("[0-9]", line))
        matches.extend(re.finditer('zero', line))
        matches.extend(re.finditer('one', line))
        matches.extend(re.finditer('two', line))
        matches.extend(re.finditer('three', line))
        matches.extend(re.finditer('four', line))
        matches.extend(re.finditer('five', line))
        matches.extend(re.finditer('six', line))
        matches.extend(re.finditer('seven', line))
        matches.extend(re.finditer('eight', line))
        matches.extend(re.finditer('nine', line))

        matches.sort(key=lambda m: m.span())
        result_m = []

        for m in matches:
            g = m.group()
            if not g.isdigit():
                result_m.append(map_nums(m.group()))
            else:
                result_m.append(g)

        f = result_m[0]
        l = result_m[-1]

        result += int(f"{f}{l}")

    return result


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
