
# import sys
# # we need this obnoxiousness to reference the utils package in repo root
# sys.path.append("../../../")
# from aoc_py_utils import utils
from collections import deque
from collections.abc import Sequence


class FileBlock:
    def __init__(self, id, blocksize, freespace):
        self.id = id
        self.blocksize = blocksize
        self.freespace = freespace


def is_complete(values, start_index):
    for i in range(start_index, len(values)):
        if values[i] != -1:
            return False
    return True


def part_one(input: Sequence[str]):
    file_stream = input[0]
    print(file_stream)
    file_blocks = []
    for f in range(0, len(file_stream), 2):
        i = int(f)
        blocksize = int(file_stream[i])
        freespace = int(file_stream[i + 1]) if i + 1 < len(file_stream) else 0
        # print(freespace)
        file_block = FileBlock(i // 2, blocksize, freespace)
        file_blocks.append(file_block)

    stack = deque()
    values = []
    counter = 0
    # print(len(file_blocks))
    for fb in file_blocks:
        for j in range(0, fb.blocksize):
            stack.append((counter, fb.id))
            values.append(fb.id)
            counter += 1

        for i in range(0, fb.freespace):
            values.append(-1)
            counter += 1

    index_spaces = []
    for i in range(0, len(values)):
        if values[i] == -1:
            index_spaces.append(i)

    value_arr = values.copy()
    for si in index_spaces:
        if is_complete(value_arr, si):
            break
        if len(stack) > 0:
            popped = stack.pop()
            value_arr[si] = popped[1]
            value_arr[popped[0]] = -1
            # print(value_arr)

    result = 0
    for i in range(0, len(value_arr)):
        value = value_arr[i]
        if value >= 0:
            result += value * i

    return result


def part_two(input: Sequence[str]):
    return 0


is_test = True

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
