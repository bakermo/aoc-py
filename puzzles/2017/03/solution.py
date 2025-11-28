
import math
import sys
# we need this obnoxiousness to reference the utils package in repo root
sys.path.append("../../../")
from aoc_py_utils import utils
from collections.abc import Sequence


def part_one(input: Sequence[str]):
    target = int(input[0])
    filled: set[utils.Position] = {()}
    center_x, center_y = 0, 0

    counter = 1
    filled.add(utils.Position(center_x, center_y))

    current_pos = utils.Position(center_x, center_y + 1)
    counter += 1;
    filled.add(current_pos)
    pointing_dir = utils.Direction.UP

    while counter < target:
        counter += 1
        next_pos = utils.get_pos_next_pos(current_pos, pointing_dir)

        current_pos = next_pos
        filled.add(current_pos)

        left_pos = utils.get_pos_next_pos(current_pos, utils.turn_left(pointing_dir))
        if left_pos not in filled:
            pointing_dir = utils.turn_left(pointing_dir)

    print(current_pos)
    rise = abs(current_pos.row - center_x)
    run = abs(current_pos.col - center_y)
    steps = rise + run
    return steps


def part_two(input: Sequence[str]):
    target = int(input[0])
    #band2 = dict(vocals="Plant", guitar="Page")
    filled = dict()

    # filled: set[utils.Position] = {()}
    center_x, center_y = 0, 0

    counter = 1
    filled[utils.Position(center_x, center_y)] = 1

    current_pos = utils.Position(center_x, center_y + 1)
    counter += 1;
    filled[current_pos] = 1
    pointing_dir = utils.Direction.UP

    while counter < target:
        counter += 1
        next_pos = utils.get_pos_next_pos(current_pos, pointing_dir)

        current_pos = next_pos
        neighbors = utils.get_test_neighbors(current_pos)
        acc = 0
        for n in neighbors:
            if n in filled:
                acc += filled[n]

        filled[current_pos] = acc
        if acc > target:
            return acc

        left_pos = utils.get_pos_next_pos(current_pos, utils.turn_left(pointing_dir))
        if left_pos not in filled:
            pointing_dir = utils.turn_left(pointing_dir)

    return 0

is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
