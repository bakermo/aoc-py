
from collections import deque
import math
import sys
from typing import List, Set, Tuple
# we need this obnoxiousness to reference the utils package in repo root
sys.path.append("../")
sys.path.append("../../../")
from aoc_py_utils import utils
from collections.abc import Sequence
from z3 import *


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
            # print(f"result: {states[state]}")
            # print(f"all {states}")
            return states[state]

        before = state
        for b in buttons:
            state_list = list(state)
            for i in b:
                state_list[i] = flip(state[i])
            newstate = ''.join(state_list)
            # print(f'{before} toggle {b} {newstate}')
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

    # for i in range(0, len(machines)):
    #     print(machines[i], buttons[i])

    for j in range(0, len(machines)):
        result += start_machine("".join("." *
                                len(machines[j])), machines[j], buttons[j])

    return result


def optimize(buttons, joltage):
    opt = Optimize()
    vars = []
    for i in range(len(buttons)):
        vars.append(z3.Int(f"x{i}"))

    for var in vars:
        opt.add(var >= 0)

    for i, joltage in enumerate(joltage):
        equation = 0
        for b, button in enumerate(buttons):
            if i in button:
                equation += vars[b]
        opt.add(equation == joltage)
    opt.minimize(sum(vars))
    opt.check()
    return opt.model().eval(sum(vars)).as_long()

    '''
        To my future self, and  whoever else on the leaderboard might be creeping my code:

        Apparently this is one of those part 2s where if you haven't spent time studying advanced
        math, you're pretty screwed. 2024 had a similar problem (see Day 13) where you were hosed if 
        you didn't recognize it as a Linear Algebra problem. I had forgotten most of my university
        Linear Algebra by then, and after several hints still had to go back and re-learn some of that 
        to solve that day. But this problem is apparently an order of magnitude above that where 
        a simple Kramer's rule, refreshing on what a determinant is, and solving a system of equations
        with 2 variables isn't going to cut it. This is a class of problem called Integer Linear Programming.

        Apparently everyone including the nerdiest of leet-coders are just slapping this into z3 and calling
        it a day:
        https://www.reddit.com/r/adventofcode/comments/1pj8326/2025_day_10_part_2_how/
        https://www.reddit.com/r/adventofcode/comments/1pjdy1u/2025_day_10_part_2_how_do_i_come_up_with_a/

        As a commenter summed up perfectly in that second reddit link:
        "The solution is always the same, a bit of math with linear algebra, but I don't
         pretend to be a GPU from January to November and I'm certainly not going to start
         pretending to be one in the month of December."
        
        I have never heard of ILP and Z3 until this problem, if everyone else is saying screw it, so am I.
        So while I cheated today, I did spend some time on these resources to understand the general math concept:
        
        Concept:
        https://en.wikipedia.org/wiki/Linear_programming
        Linear Programming (LP) (in 2 minutes)
        https://www.youtube.com/watch?v=C0TTxV0n9OA

        Intro to Linear Programming
        https://www.youtube.com/watch?v=K7TL5NMlKIk&

        Integer Linear Programming - Graphical Method - Optimal Solution, Mixed, Rounding, Relaxation
        https://www.youtube.com/watch?v=RhHhy-8sz-4

        How to solve an Integer Linear Programming Problem Using Branch and Bound
        https://www.youtube.com/watch?v=upcsrgqdeNQ&


        Then I used the following to help figure out how z3 even worked:

        Code help:
        Z3 Explained - Satisfiability Modulo Theories & SMT Solvers
        https://www.youtube.com/watch?v=EacYNe7moSs


        https://stackoverflow.com/questions/37609820/python-optimize-system-of-inequalities

        I got as far as proving out this code snippet which would give the correct answer
        on the first line of input in the sample (10 button presses):

            a = Int('a')
            b = Int('b')
            c = Int('c')
            d = Int('d')
            e = Int('e')
            f = Int('f')
            opt.add(e + f == 3)
            opt.add(b + f == 5)
            opt.add(c + d + e == 4)
            opt.add(a + b + d == 7)

            opt.add(a >= 0, b >= 0, c >= 0, d >= 0, e >= 0, f >= 0)

            opt.minimize(sum([a, b, c, d, e, f]))
            print(opt.check())
            # print(opt.model())
            # model = opt.model()
            result = opt.model().eval(sum([a, b, c, d, e, f])).as_long()
       

        And at that point, I felt I've done enough "learning" and Hyperneutrino helped me get it
        accross the finish line:

        https://youtu.be/OJ4dxrIfDfs?si=DgBqQOepw_YAzP4r&t=652

        This is a bullshit problem
    '''


@utils.aoctimer("Part 2")
def part_two(input: Sequence[str]):
    result = 0
    # machines = []
    buttons = []
    joltages = []

    for line in input:
        parts = line.split()

        button_parts = parts[1:-1]
        button_list = []
        for b in button_parts:
            button = tuple(map(int, b.strip('()').split(',')))
            button_list.append(button)

        joltage = list(map(int, parts[-1].strip('{}').split(',')))
        joltages.append(joltage)

        buttons.append(button_list)

    for i in range(0, len(buttons)):
        # print(f"{buttons[i]} {joltages[i]}")
        result += optimize(buttons[i], joltages[i])

    return result


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

part_one(input)

part_two(input)
