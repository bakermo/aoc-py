
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
    utils.print_grid(grid)
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            # print(f"{row}{col}")
            if grid[row][col] == "@":
                neighbors = utils.get_test_neighbors(utils.Position(row, col))
                count = 0
                for n in neighbors:
                    # print(n)
                    if utils.is_in_bounds(grid, n.row, n.col) and grid[n.row][n.col] == "@":
                        count += 1
                if count < 4:
                    result += 1

    return result


@utils.aoctimer("Part 2")
def part_two(input: Sequence[str]):
    result = 0

    grid = utils.get_grid(input)
    utils.print_grid(grid)

    run = True
    while run:
        positions_removed = set()
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                # print(f"{row}{col}")
                if grid[row][col] == "@":
                    neighbors = utils.get_test_neighbors(
                        utils.Position(row, col))
                    count = 0
                    for n in neighbors:
                        # print(n)
                        if utils.is_in_bounds(grid, n.row, n.col) and grid[n.row][n.col] == "@":
                            count += 1
                    if count < 4:
                        positions_removed.add(utils.Position(row, col))
        result += len(positions_removed)
        for pos in positions_removed:
            grid[pos.row][pos.col] = "."

        if len(positions_removed) == 0:
            run = False

    utils.print_grid(grid)
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
