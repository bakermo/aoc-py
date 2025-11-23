from collections.abc import Sequence


def parse(input):
    return input


def part_one(input: Sequence[str]):
    return 0


def part_two(input: Sequence[str]):
    return 0


isTest = True

filePath = "sample.txt" if isTest else "input.txt"
print(f"file: {filePath}")

input = []

file = open(f"{filePath}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
