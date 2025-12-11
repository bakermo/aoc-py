
from collections import deque
from functools import cache
import sys
from typing import Dict, List, Tuple
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


def dfs_recursive(start: str, target: str, nodes: dict, path: Tuple, cache: dict):
    path = path + (start,)
    if start == target:
        # print(f"hit end: {path}")
        return 1

    if start not in cache:
        # print(path)
        result = 0
        for c in nodes[start]:
            # I found after cleaning this up that we don't
            # really have to check the cache for c here.
            # It is still blazingly fast checking just cache[start].
            # However, it does shave a few milliseconds on average,
            # so figure it was interesting enough to keep in. Before,
            # I was resetting the cache each time, which was useless,
            # as it was essentially going down the path each time
            if c not in path and c not in cache:
                cache[c] = dfs_recursive(
                    c, target, nodes, path, cache)

            result += cache[c]
        cache[start] = result
        return result
    else:
        return cache[start]


def parse_input(input: Sequence[str]) -> Dict:
    nodes = dict()
    for line in input:
        parsed = [n.strip(':') for n in line.split()]
        nodes[parsed[0]] = parsed[1:]
        for c in parsed[1:]:
            if c not in nodes:
                nodes[c] = []

    # for n in nodes.items():
    #     print(n)

    return nodes


@utils.aoctimer("Part 1")
def part_one(input: Sequence[str]):
    result = 0

    nodes = parse_input(input)
    paths = dfs('you', 'out', nodes)
    # print(paths)
    # print(len(paths))
    result += len(paths)
    return result


def process_choke_points(start: str, target: str, nodes: dict):
    paths = dfs_recursive(start, target, nodes, tuple(), dict())
    # print(paths)
    return paths


@utils.aoctimer("Part 2")
def part_two(input: Sequence[str]):
    result = 0

    nodes = parse_input(input)

    result = process_choke_points('svr', 'fft', nodes)
    result *= process_choke_points('fft', 'dac', nodes)
    result *= process_choke_points('dac', 'out', nodes)

    return result


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

# have to do this song and dance because the
# sample input has incompatible graphs
# between part one and two
if is_test:
    input1 = input[0:10]
    input2 = input[11:]
    input = input1

part_one(input)

if is_test:
    input = input2

part_two(input)
