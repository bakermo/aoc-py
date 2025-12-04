
import sys
# we need this obnoxiousness to reference the utils package in repo root
sys.path.append("../")
sys.path.append("../../../")
from aoc_py_utils import utils
from collections.abc import Sequence


@utils.aoctimer("Part 1")
def part_one(input: Sequence[str]):
    result = 0
    for line in input:
        val = 0
        for i in range(0, len(line)):
            for j in range(i + 1, len(line)):
                newval = int(f"{line[i]}{line[j]}")
                if newval > val:
                    val = newval

        result += val

    return result


@utils.aoctimer("Part 1")
def part_two(input: Sequence[str]):
    result = 0

    for line in input:
        val = 0
        index = 0
        used_indexes = set()
        while len(used_indexes) < 12:
            for i in range(0, len(line)):

                if i not in used_indexes:
                    test_indices = []
                    test_indices.append(i)
                    for j in used_indexes:
                        test_indices.append(j)

                    newval = int("".join([line[x]
                                 for x in sorted(test_indices)]))
                    if newval > val:
                        index = i
                        val = newval

            used_indexes.add(index)
        # print(val)
        result += val

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
