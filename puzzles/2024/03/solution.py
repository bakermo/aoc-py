from collections.abc import Sequence

import re


def parse(input):
    return input


def part_one(input: Sequence[str]):
    products = []
    for line in input:
        matches = re.findall(f"mul\((\d+),(\d+)\)", line)
        for match in matches:
            x, y = map(int, match)
            products.append(x * y)

    return sum(products)


def part_two(input: Sequence[str]):
    products = []
    instructions = []

    fullInput = "".join(str(s) for s in input)

    domatches = re.finditer(f"do\(\)", fullInput)
    for d in domatches:
        instructions.append(d)
    dontmatches = re.finditer(f"don\'t\(\)", fullInput)
    for d in dontmatches:
        instructions.append(d)

    mulmatches = re.finditer(f"mul\((\d+),(\d+)\)", fullInput)
    for m in mulmatches:
        instructions.append(m)

    # span(0) is equivalent
    instructions.sort(key=lambda i: i.span())

    isDoing = True
    for i in instructions:
        if i.group(0) == 'do()':
            isDoing = True
        elif i.group(0) == 'don\'t()':
            isDoing = False
        elif isDoing:
            x, y = map(int, i.groups())
            products.append(x * y)

    return sum(products)


isTest = False

filePath = "sample.txt" if isTest else "input.txt"
print(f"file: {filePath}")

input = []

file = open(f"{filePath}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
