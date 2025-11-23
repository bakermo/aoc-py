from collections.abc import Sequence


def parse(input):
    return input


def part_one(input: Sequence[str]):

    left = []
    right = []

    for row in input:
        split = row.split()
        left.append(int(split[0]))
        right.append(int(split[1]))

    left.sort()
    right.sort()

    distances = []
    for x in range(0, len(left)):
        distance = abs(left[x] - right[x])
        distances.append(distance)

    return sum(distances)


def part_two(input: Sequence[str]):
    left = []
    right = []

    for row in input:
        split = row.split()
        left.append(int(split[0]))
        right.append(int(split[1]))

    similarities = []
    for x in range(0, len(left)):
        similarity = 0
        for y in range(0, len(right)):
            if left[x] == right[y]:
                similarity += left[x]

        similarities.append(similarity)
    return sum(similarities)


isTest = False

filePath = "sample.txt" if isTest else "input.txt"
print(f"file: {filePath}")

input = []

file = open(f"{filePath}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
