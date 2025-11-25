from collections.abc import Sequence
from typing import List


class Cross:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.top_to_bottom = ""
        self.bottom_to_top = ""


def get_grid(input: Sequence[str]):
    return [list(row) for row in input]


def print_grid(grid: Sequence[Sequence[str]]):
    print('\n')
    for row in grid:
        print("".join(row))
    print('\n')


def get_columns(input: Sequence[str]):
    rows = input
    columns = []
    for i in range(0, len(rows[0])):
        col = ''
        for j in range(0, len(rows)):
            col += rows[j][i]
        columns.append(col)
    return columns


def get_diagonals(grid: Sequence[Sequence[str]], diagonal_length):
    diagonals_safety_bound = diagonal_length - 1
    diagonals = []
    rows = len(grid)
    cols = len(grid[0])
    for row in range(0, rows):
        for col in range(0, cols):
            if row + diagonals_safety_bound < rows and col + diagonals_safety_bound < cols:
                diagonal = ''
                for k in range(0, diagonal_length):
                    diagonal += grid[row + k][col + k]
                diagonals.append(diagonal)
            if row + diagonals_safety_bound < rows and col - diagonals_safety_bound >= 0:
                diagonal = ''
                for k in range(0, diagonal_length):
                    diagonal += grid[row + k][col - k]
                diagonals.append(diagonal)
    return diagonals


def get_centered_crosses(grid: Sequence[Sequence[str]], cross_length) -> List[Cross]:
    safety_bound = cross_length // 2  # intentional flooring division here
    crosses = []
    rows = len(grid)
    cols = len(grid[0])

    for row in range(0, rows):
        for col in range(0, cols):
            if row + safety_bound < rows and col + safety_bound < cols and row - safety_bound >= 0 and col-safety_bound >= 0:
                cross = Cross(row, col)
                for k in range(-safety_bound, safety_bound + 1):
                    cross.top_to_bottom += grid[row + k][col + k]
                    cross.bottom_to_top += grid[row - k][col + k]
                crosses.append(cross)
    return crosses
