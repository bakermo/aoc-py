
from collections import deque
from functools import cache
import sys
from typing import List
# we need this obnoxiousness to reference the utils package in repo root
sys.path.append("../")
sys.path.append("../../../")
from aoc_py_utils import utils
from collections.abc import Sequence


def dfs(root: str, target: str, nodes: dict):
    seen_paths = set()
    path = []
    stack = deque()
    stack.append((root, [root]))

    while stack:
        (node, node_path) = stack.pop()
        nt = tuple(node_path)
        if nt not in seen_paths:
            seen_paths.add(nt)
            if node == target:
                path.append(node_path)
            for c in nodes[node]:
                if c not in node_path:
                    new_path = node_path + [c]
                    # print(f"new_path: {new_path}")
                    stack.append((c, new_path))

    return path


@utils.aoctimer("Part 1")
def part_one(input: Sequence[str]):
    result = 0

    # nodes = []
    nodes = dict()
    for line in input:
        parsed = [n.strip(':') for n in line.split()]
        nodes[parsed[0]] = parsed[1:]

    # out is the end so doesn't have any neighbors
    # so this feels like a hack/code smell
    nodes['out'] = []

    # for n in nodes.items():
    #     print(n)

    paths = dfs('you', 'out', nodes)
    # print(paths)
    result += len(paths)
    return result


@utils.aoctimer("Part 2")
def part_two(input: Sequence[str]):
    result = 0

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
