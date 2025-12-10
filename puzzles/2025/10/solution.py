
from collections import deque
import math
import sys
from typing import List, Set, Tuple
# we need this obnoxiousness to reference the utils package in repo root
sys.path.append("../")
sys.path.append("../../../")
from aoc_py_utils import utils
from collections.abc import Sequence


def flip(indicator: str):
    if indicator == '.':
        return '#'
    else:
        return '.'


def start_machine(machine: str, target: str, buttons: List[Tuple]):
    queue = deque()
    states = {}
    states[machine] = 0

    queue.append(machine)

    while queue:
        state = queue.popleft()
        if state == target:
            print(f"result: {states[state]}")
            print(f"all {states}")
            return states[state]

        before = state
        for b in buttons:
            state_list = list(state)
            for i in b:
                state_list[i] = flip(state[i])
            newstate = ''.join(state_list)
            print(f'{before} toggle {b} {newstate}')
            if newstate not in states:
                states[newstate] = states[state] + 1
                queue.append(newstate)


@utils.aoctimer("Part 1")
def part_one(input: Sequence[str]):
    result = 0

    machines = []
    buttons = []

    for line in input:
        parts = line.split()

        machine = parts[0].strip('[]')
        button_parts = parts[1:-1]
        button_list = []
        for b in button_parts:
            button = tuple(map(int, b.strip('()').split(',')))
            button_list.append(button)

        joltage = parts[-1]

        machines.append(machine)
        buttons.append(button_list)

    for i in range(0, len(machines)):
        print(machines[i], buttons[i])

    for j in range(0, len(machines)):
        result += start_machine("".join("." *
                                len(machines[j])), machines[j], buttons[j])

    return result


@utils.aoctimer("Part 2")
def part_two(input: Sequence[str]):
    result = 0

    return result


is_test = True

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

part_one(input)

part_two(input)
