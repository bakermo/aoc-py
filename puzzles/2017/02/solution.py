
# import sys
# # we need this obnoxiousness to reference the utils package in repo root
# sys.path.append("../../../")
# from aoc_py_utils import utils
from collections.abc import Sequence


def part_one(input: Sequence[str]):
    diffs = []
    for line in input:
        nums = list(map(int, line.split()))
        diff = max(nums) - min(nums)
        diffs.append(diff)

    return sum(diffs)


def part_two(input: Sequence[str]):
    diffs = []
    for line in input:
        split = line.split()
        nums = list(map(int, split))
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i == j:
                    continue
                if nums[i] % nums[j] == 0:
                    diffs.append(nums[i] // nums[j])

    return sum(diffs)


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
