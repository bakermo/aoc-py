from collections.abc import Sequence


def parse(input):
    return str(input).split('x')


def part_one(input: Sequence[str]):
    measurements = []
    for row in input:
        dimensions = parse(row)
        # print(dimensions)
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])

        sides = [(l * w), (w * h), (h * l)]
        smallest = min(sides)

        measurement = sum(map(lambda num: num * 2, sides), smallest)
        measurements.append(measurement)

    return sum(measurements)


def part_two(input: Sequence[str]):
    measurements = []
    for row in input:
        dimensions = parse(row)
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])

        # calculate all possible perimeters
        perimeters = list(map(lambda num: 2 * int(num), dimensions))

        # then sort them
        perimeters.sort()

        # then take the first 2
        perimeter = sum(perimeters[:2])

        area = l * w * h
        total = perimeter + area
        measurements.append(total)

    return sum(measurements)


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

print(f"Part 1:\n\n{part_one(input)}\n\n")

print(f"Part 2:\n\n{part_two(input)}\n\n")
