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

    full_input = "".join(str(s) for s in input)

    do_matches = re.finditer(f"do\(\)", full_input)
    for d in do_matches:
        instructions.append(d)
    dont_matches = re.finditer(f"don\'t\(\)", full_input)
    for d in dont_matches:
        instructions.append(d)

    mulmatches = re.finditer(f"mul\((\d+),(\d+)\)", full_input)
    for m in mulmatches:
        instructions.append(m)

    # span(0) is equivalent
    instructions.sort(key=lambda i: i.span())

    is_doing = True
    for i in instructions:
        if i.group(0) == 'do()':
            is_doing = True
        elif i.group(0) == 'don\'t()':
            is_doing = False
        elif is_doing:
            x, y = map(int, i.groups())
            products.append(x * y)

    return sum(products)


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
