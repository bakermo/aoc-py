import os


def scaffold_file(file_path, content=None):
    if not os.path.exists(file_path):
        print(f"Creating {file_path}")
        f = open(file_path, "w")
        if content is not None:
            f.write(content)
        f.close()


with open("template/solution.py") as f:
    content = f.read()

for year in range(2015, 2026):
    days = 25 if year < 2025 else 12
    for day in range(1, days + 1):
        directory = f"puzzles/{year}/{day:02d}"
        if not os.path.exists(directory):
            print(f"Creating {directory}")
            os.makedirs(directory, exist_ok=True)

        scaffold_file(f"{directory}/solution.py", content)
        scaffold_file(f"{directory}/input.txt")
        scaffold_file(f"{directory}/sample.txt")
