def parse(input):
    return input


def part_one(input):
    print(0)


def part_two(input):
    print(0)


isTest = True

filePath = "sample.txt" if isTest else "input.txt"
print(f"file: {filePath}")

input = []

file = open(f"{filePath}")

for line in file:
    input.append(str(line.strip()))

part_one(input)

part_two(input)
