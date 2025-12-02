
# import sys
# # we need this obnoxiousness to reference the utils package in repo root
# sys.path.append("../../../")
# from aoc_py_utils import utils
from collections.abc import Sequence
import time


def part_one(input: Sequence[str]):
    result = 0

    return result


def part_two(input: Sequence[str]):
    result = 0

    return result


is_test = True

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

print(f"Starting part 1...\n")
start = time.perf_counter()
print(f"Part 1:\n\n{part_one(input)}\n")
elapsed = time.perf_counter() - start
print(f"Finished part 1 in {elapsed:.6f} seconds\n\n")

print(f"Starting part 2...\n")
start = time.perf_counter()
print(f"Part 2:\n\n{part_two(input)}\n")
elapsed = time.perf_counter() - start
print(f"Finished part 2 in {elapsed:.6f} seconds")
