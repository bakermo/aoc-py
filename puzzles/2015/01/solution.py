from collections.abc import Sequence


def part_one(input: Sequence[str]):
    count = 0
    for x in input[0]:
        if x == '(':
            count += 1
        else:
            count -= 1
    return count


def part_two(input: Sequence[str]):
    count = 0
    floor = 0

    for x in input[0]:
        if x == '(':
            floor += 1
        else:
            floor -= 1
        count += 1

        if floor == -1:
            break

    return count


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

# print(input)

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
