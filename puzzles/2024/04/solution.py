import sys
sys.path.append("../../../")
from aoc_py_utils import utils
from collections.abc import Sequence
import re


def part_one(input: Sequence[str]):
    match_count = 0
    for row in input:
        match_count += len(re.findall("XMAS", row))
        rev_row = row[::-1]
        match_count += len(re.findall("XMAS", rev_row))

    columns = utils.get_columns(input)
    for col in columns:
        match_count += len(re.findall("XMAS", col))
        rev_col = col[::-1]
        match_count += len(re.findall("XMAS", rev_col))

    grid = utils.get_grid(input)
    fours_diagonal = utils.get_diagonals(grid, 4)
    for d in fours_diagonal:
        if d == "XMAS":
            match_count += 1

        rev = d[::-1]
        if rev == "XMAS":
            match_count += 1

    return match_count


def part_two(input: Sequence[str]):
    grid = utils.get_grid(input)
    crosses = utils.get_centered_crosses(grid, 3)

    xmas_count = 0
    for cross in crosses:
        if (
            (cross.top_to_bottom == "MAS" or cross.top_to_bottom[::-1] == "MAS") and
            (cross.bottom_to_top ==
             "MAS" or cross.bottom_to_top[::-1] == "MAS")
        ):
            xmas_count += 1
    return xmas_count


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
