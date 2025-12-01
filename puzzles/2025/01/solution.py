
# import sys
# # we need this obnoxiousness to reference the utils package in repo root
# sys.path.append("../../../")
# from aoc_py_utils import utils
from collections.abc import Sequence


def part_one(input: Sequence[str]):
    result = 0

    index = 50

    for line in input:
        turn = line[0]
        rest = int(line[1::])

    for line in input:
        turn = line[0]
        rest = line[1::]
        if turn == 'R':
            index = (index + int(rest)) % 100
        elif turn == 'L':
            index = (index - int(rest)) % 100
        # print(index)
        if index == 0:
            result += 1

    # the below is what I should have done...
    # it would have been a 1 tab difference from
    # part 2. instead I tried to be cute and cost
    # myself 35 mins

    # for r in range(0, rest):
    #     if turn == 'R':
    #         index += 1

    #     if turn == 'L':
    #         index -= 1

    #     if index > 99:
    #         index = 0
    #         # result += 1
    #     if index < 0:
    #         index = 99
    #         # result += 1

    # if index == 0:
    #     result += 1

    return result


def part_two(input: Sequence[str]):
    result = 0

    index = 50

    # TODO: figure out if how to do this the math-y way
    # like I was trying before I got stupid
    for line in input:
        turn = line[0]
        rest = int(line[1::])

        for r in range(0, rest):
            if turn == 'R':
                index += 1

            if turn == 'L':
                index -= 1

            if index > 99:
                index = 0
                # result += 1
            if index < 0:
                index = 99
                # result += 1
            if index == 0:
                result += 1

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
