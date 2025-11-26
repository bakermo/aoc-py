
import sys
from typing import List, Set, Tuple
# # we need this obnoxiousness to reference the utils package in repo root
sys.path.append("../../../")
from aoc_py_utils import utils
from collections.abc import Sequence
import re


class Antennae:
    def __init__(self, row, col, freq):
        self.position = utils.Position(row, col)
        self.freq = freq

    def __str__(self):
        return f"{self.freq} {self.position}"

    def __repr__(self):
        return self.__str__()


def valid_pair(a1: Antennae, a2: Antennae):

    return (
        a1.freq == a2.freq and
        a1.position.row != a2.position.row and
        a1.position.col != a2.position.col
    )


def part_one(input: Sequence[str]):
    grid = utils.get_grid(input)
    utils.print_grid(grid)

    antennaes = []
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if re.match("^[a-zA-Z0-9]", grid[row][col]):
                antennaes.append(Antennae(row, col, grid[row][col]))

    unique_pairs: Set[Tuple[Antennae, Antennae]] = set()
    for a in antennaes:
        for o in antennaes:
            if valid_pair(a, o):
                pair = (a, o)
                alt_pair = (o, a)
                # don't double count the pair's counterpart
                if alt_pair not in unique_pairs:
                    unique_pairs.add(pair)

    unique_pos = set()
    for pair in unique_pairs:
        print(pair)
        a1 = pair[0]
        a2 = pair[1]

        run = a1.position.col - a2.position.col
        rise = a1.position.row - a2.position.row

        antinode1row = a1.position.row + rise
        antinode1col = a1.position.col + run

        if utils.is_in_bounds(grid, antinode1row, antinode1col):
            unique_pos.add(utils.Position(antinode1row, antinode1col))
            if grid[antinode1row][antinode1col] == '.':
                grid[antinode1row][antinode1col] = '#'

        antinode2row = a2.position.row - rise
        antinode2col = a2.position.col - run

        if utils.is_in_bounds(grid, antinode2row, antinode2col):
            unique_pos.add(utils.Position(antinode2row, antinode2col))
            if grid[antinode2row][antinode2col] == '.':
                grid[antinode2row][antinode2col] = '#'

    utils.print_grid(grid)
    # print(*unique_pairs, sep='\n')
    # print('\n'.join(map(str, unique_pairs)))
    # print(f"{a.position.row} {a.position.col} {a.freq}")
    # print('\n'.join(map(str, unique_pos)))
    return len(unique_pos)


def part_two(input: Sequence[str]):
    grid = utils.get_grid(input)
    utils.print_grid(grid)

    antennaes = []
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if re.match("^[a-zA-Z0-9]", grid[row][col]):
                antennaes.append(Antennae(row, col, grid[row][col]))

    unique_pairs: Set[Tuple[Antennae, Antennae]] = set()
    for a in antennaes:
        for o in antennaes:
            if valid_pair(a, o):
                pair = (a, o)
                alt_pair = (o, a)
                # don't double count the pair's counterpart
                if alt_pair not in unique_pairs:
                    unique_pairs.add(pair)

    unique_pos = set()
    for pair in unique_pairs:
        print(pair)
        a1 = pair[0]
        a2 = pair[1]

        # we count the antennae's themselves now too as anti-nodes
        unique_pos.add(a1.position)
        unique_pos.add(a2.position)

        run = a1.position.col - a2.position.col
        rise = a1.position.row - a2.position.row

        antinode1row = a1.position.row + rise
        antinode1col = a1.position.col + run

        while utils.is_in_bounds(grid, antinode1row, antinode1col):
            unique_pos.add(utils.Position(antinode1row, antinode1col))
            if grid[antinode1row][antinode1col] == '.':
                grid[antinode1row][antinode1col] = '#'

            antinode1row += rise
            antinode1col += run

        antinode2row = a2.position.row - rise
        antinode2col = a2.position.col - run

        while utils.is_in_bounds(grid, antinode2row, antinode2col):
            unique_pos.add(utils.Position(antinode2row, antinode2col))
            if grid[antinode2row][antinode2col] == '.':
                grid[antinode2row][antinode2col] = '#'

            antinode2row -= rise
            antinode2col -= run

    utils.print_grid(grid)
    # print(*unique_pairs, sep='\n')
    # print('\n'.join(map(str, unique_pairs)))
    # print(f"{a.position.row} {a.position.col} {a.freq}")
    # print('\n'.join(map(str, unique_pos)))
    return len(unique_pos)


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
