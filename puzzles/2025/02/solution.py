
# import sys
# # we need this obnoxiousness to reference the utils package in repo root
# sys.path.append("../../../")
# from aoc_py_utils import utils
from collections.abc import Sequence

import time


def part_one(input: Sequence[str]):
    result = 0

    ids = input[0].split(',')
    for i in ids:
        s = i.split('-')
        start = int(s[0])
        end = int(s[1])

        for id in range(int(start), int(end) + 1):
            idstr = str(id)
            left = idstr[0:len(idstr) // 2:]
            right = idstr[len(idstr) // 2::]
            if left == right:
                result += id

    return result


def part_two(input: Sequence[str]):
    result = 0

    ids = input[0].split(',')
    for id in ids:
        s = id.split('-')
        start = int(s[0])
        end = int(s[1])

        for id in range(start, end + 1):
            idstr = str(id)
            max_div = len(idstr)
            invalid = False
            # TODO: think of a way we can prune searches
            # for example, 1231231231234 will never match
            # because of the 4, but with the code below
            # we won't find that until trying every possible
            # divisible chunk
            for counter in range(2, max_div + 1):
                if invalid:
                    break

                if max_div % counter == 0:
                    chunk_len = max_div // counter

                    chunks = [idstr[i:i + chunk_len]
                              for i in range(0, max_div, chunk_len)]
                    first_chunk = chunks[0]
                    match = True
                    for chunk in chunks:
                        if first_chunk != chunk:
                            match = False
                            break

                    if match:
                        result += id
                        invalid = True
                        # print(f'invalid id: {id}')
    return result


is_test = False

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
