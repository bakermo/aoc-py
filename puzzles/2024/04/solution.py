from collections.abc import Sequence
# from dataclasses import dataclass, field

import re
from typing import List


# TODO: Convert this to a helper mdodule!
def print_grid(grid: Sequence[Sequence[str]]):
    print('\n')
    for row in grid:
        print("".join(row))
    print('\n')

# TODO: Convert this to a helper mdodule!


def get_grid(input: Sequence[str]):
    return [list(row) for row in input]

# TODO: Convert this to a helper mdodule!


def get_columns(input: Sequence[str]):
    rows = input
    columns = []
    for i in range(0, len(rows[0])):
        col = ''
        for j in range(0, len(rows)):
            col += rows[j][i]
        columns.append(col)
    return columns

# TODO: Convert this to a helper module!


def get_diagonals(grid: Sequence[Sequence[str]], diagonal_length):
    diagonals_safety_bound = diagonal_length - 1
    diagonals = []
    rows = len(grid)
    cols = len(grid[0])
    for row in range(0, rows):
        for col in range(0, cols):
            if row + diagonals_safety_bound < rows and col + diagonals_safety_bound < cols:
                diagonal = ''
                for k in range(0, diagonal_length):
                    diagonal += grid[row + k][col + k]
                diagonals.append(diagonal)
            if row + diagonals_safety_bound < rows and col - diagonals_safety_bound >= 0:
                diagonal = ''
                for k in range(0, diagonal_length):
                    diagonal += grid[row + k][col - k]
                diagonals.append(diagonal)
    return diagonals


class Cross:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.top_to_bottom = ""
        self.bottom_to_top = ""


def get_centered_crosses(grid: Sequence[Sequence[str]], cross_length) -> List[Cross]:
    safety_bound = cross_length // 2  # intentional flooring division here
    crosses = []
    rows = len(grid)
    cols = len(grid[0])

    for row in range(0, rows):
        for col in range(0, cols):
            if row + safety_bound < rows and col + safety_bound < cols and row - safety_bound >= 0 and col-safety_bound >= 0:
                cross = Cross(row, col)
                for k in range(-safety_bound, safety_bound + 1):
                    cross.top_to_bottom += grid[row + k][col + k]
                    cross.bottom_to_top += grid[row - k][col + k]
                crosses.append(cross)
    return crosses


def part_one(input: Sequence[str]):
    match_count = 0
    for row in input:
        match_count += len(re.findall("XMAS", row))
        rev_row = row[::-1]
        match_count += len(re.findall("XMAS", rev_row))

    columns = get_columns(input)
    for col in columns:
        match_count += len(re.findall("XMAS", col))
        rev_col = col[::-1]
        match_count += len(re.findall("XMAS", rev_col))

    grid = get_grid(input)
    fours_diagonal = get_diagonals(grid, 4)
    for d in fours_diagonal:
        if d == "XMAS":
            match_count += 1

        rev = d[::-1]
        if rev == "XMAS":
            match_count += 1

    return match_count


def part_two(input: Sequence[str]):
    grid = get_grid(input)
    crosses = get_centered_crosses(grid, 3)

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
