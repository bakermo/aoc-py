import os


def scaffold_file(file_path, sim, content=None):
    if not os.path.exists(file_path):
        print(f"Creating {file_path}")
        if not sim:
            f = open(file_path, "w")
            if content is not None:
                f.write(content)
            f.close()


with open("template/solution.py") as f:
    content = f.read()


def scaffold_day(year, day, sim):
    directory = f"puzzles/{year}/{day:02d}"
    if not os.path.exists(directory):
        print(f"Creating {directory}")
        if not sim:
            os.makedirs(directory, exist_ok=True)

    scaffold_file(f"{directory}/solution.py", sim, content)
    scaffold_file(f"{directory}/input.txt", sim)
    scaffold_file(f"{directory}/sample.txt", sim)


def scaffold_all(sim):
    for year in range(2015, 2026):
        days = 25 if year < 2025 else 12
        for day in range(1, days + 1):
            scaffold_day(year, day, sim)


def scaffold(all=False, arg_day=None, arg_year=None, sim=False):
    if all:
        scaffold_all(sim)
    else:
        if arg_year is None:
            print("Year is required")
            return
        if arg_day is not None:
            scaffold_day(int(arg_year), int(arg_day), sim)
        else:
            days = 25 if int(arg_year) < 2025 else 12
            for day in range(1, days + 1):
                scaffold_day(int(arg_year), day, sim)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Scaffolds one or more puzzle directories for a given day and/or year"
    )

    parser.add_argument(
        "-d", "--day", metavar="day",
        required=False, help="The day of the puzzle to create. Must be used with year."
    )

    parser.add_argument(
        "-y", "--year", metavar="year",
        required=False, help="The year of the puzzle to create. If day is not specified, all valid days will be created for that year."
    )

    parser.add_argument(
        "-s", "--sim", action="store_true",
        required=False, help="Simulates a run and prints to the console the files and directories that would be created without actually writing to file."
    )

    parser.add_argument(
        "-a", "--all", action="store_true",
        required=False, help="Creates all valid days and years from 2015 to 2025 (inclusive)."
    )

    args = parser.parse_args()
    # print(args)

    scaffold(args.all, args.day, args.year, args.sim)
