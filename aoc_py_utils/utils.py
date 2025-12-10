from collections.abc import Sequence
from enum import Enum
from functools import wraps
import time
from typing import List, NamedTuple
from datetime import timedelta


def aoctimer(descriptor):
    def decorator(base_fn):
        @wraps(base_fn)
        def timer_fn(*args):
            print(f"Starting {descriptor}...\n{descriptor}:\n")
            start = time.perf_counter()
            base_fn_result = base_fn(*args)
            print(f"{base_fn_result}\n")
            elapsed = time.perf_counter() - start
            print(
                f"Finished {descriptor} in {elapsed:.6f} seconds\n\n {str(timedelta(seconds=elapsed))}")
        return timer_fn
    return decorator


class Position(NamedTuple):
    row: int
    col: int


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Cross:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.top_to_bottom = ""
        self.bottom_to_top = ""


def turn_right(direction: Direction) -> Direction:
    return Direction((direction.value + 1) % 4)


def turn_left(direction: Direction) -> Direction:
    return Direction((direction.value + 3) % 4)


def get_next_pos(row: int, col: int, direction: Direction) -> Position:
    if direction == Direction.UP:
        return Position(row - 1, col)
    elif direction == Direction.RIGHT:
        return Position(row, col + 1)
    elif direction == Direction.DOWN:
        return Position(row + 1, col)
    else:
        return Position(row, col - 1)


def get_test_neighbors(position: Position) -> List[Position]:
    positions = []
    # below
    positions.append(Position(position.row + 1, position.col))
    positions.append(Position(position.row + 1, position.col - 1))
    positions.append(Position(position.row + 1, position.col + 1))

    # left and right
    positions.append(Position(position.row, position.col - 1))
    positions.append(Position(position.row, position.col + 1))

    # above
    positions.append(Position(position.row - 1, position.col))
    positions.append(Position(position.row - 1, position.col - 1))
    positions.append(Position(position.row - 1, position.col + 1))

    return positions


def get_pos_next_pos(position: Position, direction: Direction) -> Position:
    return get_next_pos(position.row, position.col, direction)


def get_grid(input: Sequence[str]):
    return [list(row) for row in input]


def print_grid(grid: Sequence[Sequence[str]]):
    print('\n')
    for row in grid:
        print("".join(row))
    print('\n')


def is_in_bounds(grid: Sequence[Sequence[str]], row, col):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])


def get_columns(input: Sequence[str]):
    rows = input
    columns = []
    for i in range(0, len(rows[0])):
        col = ''
        for j in range(0, len(rows)):
            col += rows[j][i]
        columns.append(col)
    return columns


def get_columns_lists(input: Sequence[str]):
    rows = input
    columns = []
    for i in range(0, len(rows[0])):
        col = []
        for j in range(0, len(rows)):
            col.append(rows[j][i])
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
            if row + safety_bound < rows and col + safety_bound < cols and row - safety_bound >= 0 and col - safety_bound >= 0:
                cross = Cross(row, col)
                for k in range(-safety_bound, safety_bound + 1):
                    cross.top_to_bottom += grid[row + k][col + k]
                    cross.bottom_to_top += grid[row - k][col + k]
                crosses.append(cross)
    return crosses
