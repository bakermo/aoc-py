
import math
import sys
# we need this obnoxiousness to reference the utils package in repo root
sys.path.append("../")
sys.path.append("../../../")
from aoc_py_utils import utils
from collections.abc import Sequence


@utils.aoctimer("Part 1")
def part_one(input: Sequence[str]):
    result = 0

    col_count = len(input[0].split())
    columns = []
    for col in range(0, col_count):
        columns.append([])
    for row in input:
        tokens = row.split()
        for c, t in enumerate(tokens):
            if (t.isdigit()):
                t = int(t)
            columns[c].append(t)
        # print(tokens)

    for col in columns:
        terms = col[0:len(col) - 1]
        if col[-1] == '*':
            result += math.prod(terms)
        else:
            result += sum(terms)

    return result


@utils.aoctimer("Part 2")
def part_two(input: Sequence[str]):
    result = 0

    grid = utils.get_grid(input)
    max_length = max(len(row) for row in grid)
    for row in grid:
        if len(row) < max_length:
            row.extend([' '] * (max_length - len(row)))

    columns = reversed(utils.get_columns_lists(grid))
    terms = []
    for col in columns:
        # print(col)
        op = col[-1]
        if all(t == ' ' for t in col):
            terms.clear()
            continue

        term = int("".join(col[0:len(col) - 1]))
        # print(term)
        terms.append(term)

        if op == '*':
            r = math.prod(terms)
            # print(f"result: {r}")
            result += r
        elif op == '+':
            r = sum(terms)
            # print(f"result: {r}")
            result += r

    return result


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    # For this one and only problem, we only want to strip
    # new lines! We want to keep the spaces!!!
    input.append(str(line).strip('\n'))

part_one(input)

part_two(input)
