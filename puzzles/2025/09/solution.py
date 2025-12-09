
import sys
from typing import List
# we need this obnoxiousness to reference the utils package in repo root
sys.path.append("../")
sys.path.append("../../../")
from aoc_py_utils import utils
from collections.abc import Sequence


@utils.aoctimer("Part 1")
def part_one(input: Sequence[str]):
    result = 0

    positions: List[utils.Position] = []
    for line in input:
        # print(line)
        col, row = map(int, line.split(','))
        # print(f"row {row} col {col}")
        positions.append(utils.Position(row, col))

    # print(points)
    largest = ()
    largest_area = 0
    for p1 in positions:
        for p2 in positions:
            # we would end up checking this same pair twice accidentally though
            # so doing double the work
            if p1 != p2:  # and p1.row <= p2.row and p1.col <= p2.col:
                # 5, 2 and 7, 9
                # or 5, 2 and 1, 11
                area = (abs(p2.row - p1.row) + 1) * (abs(p2.col - p1.col) + 1)
                if area > largest_area:
                    largest_area = area
                    largest = (p1, p2)
    print(largest)
    return largest_area


def connect_points(pos, last, borders):
    # print(f"last: {last}")
    if pos.row == last.row:
        mincol = min(pos.col, last.col)
        maxcol = max(pos.col, last.col)
        for c in range(mincol, maxcol + 1):
            b = utils.Position(pos.row, c)
            # print(f"adding: {b}")
            borders.add(b)
    elif pos.col == last.col:
        minrow = min(pos.row, last.row)
        maxrow = max(pos.row, last.row)
        for r in range(minrow, maxrow + 1):
            b = utils.Position(r, pos.col)
            # print(f"adding: {b}")
            borders.add(b)


def is_valid_bounds(p1, p2, p3, p4, borders):
    rows = p1.row, p2.row, p3.row, p4.row
    cols = p1.col, p2.col, p3.col, p4.col
    # test the new polgon, but ignore its borders
    # because its fine for the new polygon borders
    # to overlap with global map borders, but if the interior
    # crosses at all, then its invalid
    minrow = min(rows) + 1
    maxrow = max(rows) - 1
    mincol = min(cols) + 1
    maxcol = max(cols) - 1

    start_pos = utils.Position(minrow, mincol)
    pos = start_pos

    for c in range(mincol, maxcol + 1):
        # go right
        pos = utils.Position(pos.row, c)
        if pos in borders:
            return False

    for r in range(minrow, maxrow + 1):
        # go down
        pos = utils.Position(r, pos.col)
        if pos in borders:
            return False

    for c in range(maxcol, mincol - 1, -1):
        # go left
        pos = utils.Position(pos.row, c)
        if pos in borders:
            return False

    for r in range(maxrow, minrow - 1, -1):
        # go up
        pos = utils.Position(r, pos.col)
        if pos in borders:
            return False

    return True


@utils.aoctimer("Part 2")
def part_two(input: Sequence[str]):
    result = 0

    positions: List[utils.Position] = []

    borders = set()
    first = None
    last = None
    for line in input:
        col, row = map(int, line.split(','))
        pos = utils.Position(row, col)
        borders.add(pos)

        if first == None:
            first = pos

        if last != None:
            connect_points(pos, last, borders)

        last = pos
        positions.append(pos)

    connect_points(first, last, borders)

    largest = ()
    largest_area = 0
    iteration = 0
    checked = set()
    for p1 in positions:
        for p2 in positions:
            if (p1, p2) in checked or (p2, p1) in checked:
                continue
            checked.add((p1, p2))
            iteration += 1
            # print(iteration)

            if p1 != p2:
                area = (abs(p2.row - p1.row) + 1) * (abs(p2.col - p1.col) + 1)

                # TOMORROW TRY RAYCASTING!

                if area > largest_area:
                    # we can save some time here by only checking validity
                    # of new ones that we know are larger

                    p3 = utils.Position(p2.row, p1.col)
                    p4 = utils.Position(p1.row, p2.col)
                    if is_valid_bounds(p1, p2, p3, p4, borders):
                        # print(f"p1 {p1} p2 {p2} t1 {p3} t2 {p4}")

                        largest_area = area
                        largest = (p1, p2)

    print(largest)
    return largest_area


is_test = True

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

part_one(input)

part_two(input)
