from collections.abc import Sequence
import re


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
    return 0


is_test = True

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
