
import sys
# we need this obnoxiousness to reference the utils package in repo root
sys.path.append("../")
sys.path.append("../../../")
from aoc_py_utils import utils
from collections.abc import Sequence


@utils.aoctimer("Part 1")
def part_one(input: Sequence[str]):
    result = 0
    grid = utils.get_grid(input)
    first_row = grid[0]
    for i, c in enumerate(first_row):
        if c == 'S':
            grid[1][i] = "|"
            break
            # print(grid[1][i])
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row - 1][col] == "|":
                if grid[row][col] == "^":
                    result += 1
                    if utils.is_in_bounds(grid, row, col - 1):
                        grid[row][col - 1] = "|"
                    if utils.is_in_bounds(grid, row, col + 1):
                        grid[row][col + 1] = "|"
                else:
                    grid[row][col] = "|"
    # utils.print_grid(grid)

    return result


def timeline(grid, row, col, cache):
    if not utils.is_in_bounds(grid, row + 1, col):
        return 1

    grid[row][col] = "|"
    if (row, col) not in cache:
        if grid[row + 1][col] == "^":
            result = timeline(grid, row + 1, col + 1, cache) + \
                timeline(grid, row + 1, col - 1, cache)
        else:
            result = timeline(grid, row + 1, col, cache)
    else:
        return cache[(row, col)]

    cache[(row, col)] = result

    return result


@utils.aoctimer("Part 2")
def part_two(input: Sequence[str]):
    result = 0
    grid = utils.get_grid(input)
    first_row = grid[0]
    col = 0
    for i, c in enumerate(first_row):
        if c == 'S':
            grid[1][i] = "|"
            col = i
            break

    cache = dict()
    result = timeline(grid, 1, col, cache)
    # utils.print_grid(grid)

    return result


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

part_one(input)

part_two(input)
