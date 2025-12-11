
from collections import deque
from functools import cache
import sys
from typing import List, Tuple
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
                    print(f"new_path: {new_path}")
                    stack.append((c, new_path))

    return path


# def dfs(root: str, target: str, nodes: dict):
#     seen_paths = set()
#     path = []
#     stack = deque()
#     stack.append((root, [root]))

#     while stack:
#         (node, node_path) = stack.pop()
#         nt = tuple(node_path)
#         if nt not in seen_paths:
#             seen_paths.add(nt)
#             if node == target:
#                 path.append(node_path)
#             for c in nodes[node]:
#                 if c not in node_path:
#                     new_path = node_path + [c]
#                     print(f"new_path: {new_path}")
#                     stack.append((c, new_path))

#     return path

# function DFS(graph, node):
#     if node is visited:
#         return
#     mark node as visited
#     process(node)  // e.g., print or store the node
#     for each neighbor in graph[node]:
#         if neighbor is not visited:
#             DFS(graph, neighbor)


# def dfs_recursive(start: str, target: str, nodes: dict, visited: set, path: Tuple, cache: dict):
#     # if start in visited:
#     # print(f"{start} {cache}")
#     # print(f"{start}")
#     # for c in cache.items():
#     #     print(c)
#     path = path + (start,)
#     if start == target:
#         print(f"hit end: {path}")
#         # print(f"{start} {cache}")
#         # path.append(start)  # this line is really for debugging

#         # if 'fft' in path and 'dac' in path:
#         #     return 1
#         # else:
#         #     return 0
#         return 1

#     # visited.add(start)
#     # print(path)
#     # path = path + (start,)
#     print(path)
#     if start not in cache:
#         # print(path)
#         result = 0
#         for c in nodes[start]:
#             # if c not in path:
#             # result += dfs_recursive(c, target, nodes, visited, path, cache)
#             # cache[c] = result
#             # if c not in path:
#             cache[c] = dfs_recursive(
#                 c, target, nodes, visited, path, cache)

#             result += cache[c]
#         cache[start] = result
#         return result
#     else:
#         return cache[start]

def dfs_recursive(start: str, target: str, nodes: dict, visited: set, path: Tuple, cache: dict):
    # if start in visited:
    # print(f"{start} {cache}")
    # print(f"{start}")
    # for c in cache.items():
    #     print(c)
    path = path + (start,)
    if start == target:
        print(f"hit end: {path}")
        # print(f"{start} {cache}")
        # path.append(start)  # this line is really for debugging

        # if 'fft' in path and 'dac' in path:
        #     return 1
        # else:
        #     return 0
        return 1

    # visited.add(start)
    # print(path)
    # print(path)
    if start not in cache:
        # print(path)
        result = 0
        for c in nodes[start]:
            # if c not in path:
            # result += dfs_recursive(c, target, nodes, visited, path, cache)
            # cache[c] = result
            if c not in path:
                cache[c] = dfs_recursive(
                    c, target, nodes, visited, path, cache)

            result += cache[c]
        cache[start] = result
        return result
    else:
        return cache[start]

    # else:
    #     return cache[tuple(path)]

    # return path
    # if node is visited:
    #     return
    # mark node as visited
    # process(node)  // e.g., print or store the node
    # for each neighbor in graph[node]:
    #     if neighbor is not visited:
    #         DFS(graph, neighbor)

# iterative
# def dfs_v2(graph, startNode):
#     visited = set
    # visited = set()
    # stack = [startNode]
    # while stack is not empty:
    #     node = stack.pop()
    #     if node not in visited:
    #         mark node as visited
    #         process(node)
    #         for each neighbor in graph[node]:
    #             if neighbor not in visited:
    #                 stack.push(neighbor)


def bfs(root: str, target: str, nodes: dict):
    queue = deque()
    path = {}
    path[root] = 0

    queue.append(root)

    while queue:
        node = queue.popleft()
        if node == target:
            # print(f"result: {states[state]}")
            # print(f"all {states}")
            return path[node]

        # before = state
        for c in nodes[node]:
            # queue all of the children
            if c not in path:
                path[c] = path[node] + 1
                queue.append(c)


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

    for n in nodes.items():
        print(n)

    # result += find_shortest_bfs('you', 'out', nodes)
    # result += dfs('you', 'out', nodes)
    paths = dfs('you', 'out', nodes)
    print(paths)
    # print(len(paths))
    result += len(paths)
    return result


@utils.aoctimer("Part 2")
def part_two(input: Sequence[str]):
    result = 0
    # nodes = []
    nodes = dict()
    for line in input:
        parsed = [n.strip(':') for n in line.split()]
        nodes[parsed[0]] = parsed[1:]

    # out is the end so doesn't have any neighbors
    # so this feels like a hack/code smell
    nodes['out'] = []

    for n in nodes.items():
        print(n)

    # result += find_shortest_bfs('you', 'out', nodes)
    # result += dfs('you', 'out', nodes)
    # paths = dfs('svr', 'fft', nodes)
    visited = set()
    cache = dict()
    # paths = dfs_recursive('svr', 'out', nodes, visited, (), cache)
    # dfsyou = dfs('you', 'out', nodes)
    # for d in dfsyou:
    #     print(d)
    # print(len(dfsyou))

    # dfsold = dfs('svr', 'fft', nodes) + dfs('fft',
    #                                         'dac', nodes) + dfs('dac', 'out', nodes)
    # for d in dfsold:
    #     print(d)
    # print(len(dfsold))

    # print(len(dfs('svr', 'fft', nodes)) * len(dfs('fft',
    #                                               'dac', nodes)) * len(dfs('dac', 'out', nodes)))
    result = 1
    paths = dfs_recursive('svr', 'fft', nodes, visited, (), cache)
    print(paths)
    result *= paths

    cache.clear()
    paths = dfs_recursive('fft', 'dac', nodes, visited, (), cache)
    print(paths)
    result *= paths

    cache.clear()
    paths = dfs_recursive('dac', 'out', nodes, visited, (), cache)
    print(paths)
    result *= paths

    # svr_to_dac = dfs_recursive('svr', 'dac', nodes, visited, (), cache)
    # print(f"svr_to_dac {svr_to_dac}")
    # print(cache)

    # cache.clear()
    # svr_to_fft = dfs_recursive('svr', 'fft', nodes, visited, (), cache)
    # print(f"svr_to_fft {svr_to_fft}")
    # print(cache)

    # cache.clear()
    # fft_to_dac = dfs_recursive('fft', 'dac', nodes, visited, (), cache)
    # print(f"fft_to_dac {fft_to_dac}")
    # print(cache)

    # cache.clear()
    # dac_to_fft = dfs_recursive('dac', 'fft', nodes, visited, (), cache)
    # print(f"dac_to_fft {dac_to_fft}")
    # print(cache)

    # cache.clear()
    # dac_to_out = dfs_recursive('dac', 'out', nodes, visited, (), cache)
    # print(f"dac_to_out {dac_to_out}")
    # print(cache)

    # cache.clear()
    # fft_to_out = dfs_recursive('fft', 'out', nodes, visited, (), cache)
    # print(f"fft_to_out {fft_to_out}")
    # print(cache)

    # print(f"fft {cache['fft']} dac {cache['dac']} out {cache['out']}")
    # result = cache['fft'] // cache['dac'] // cache['out']
    # print(f"dfs:  {paths}")

    # shortestbfs = bfs('svr', 'out', nodes)
    # print(f"shortest bfs {shortestbfs}")
    # print(paths)
    # print(len(paths))
    # for p in paths:
    #     print(p)
    print('\n')
    # filtered_paths = list(filter(lambda x: 'dac' in x and 'fft' in x, paths))
    # for f in filtered_paths:
    #     print(f)

    # result += len(filtered_paths)
    # result += len(paths)
    # result = paths
    return result
# there are no paths from dac to fft
# this is false somehow in my DFS approach, but my recursive one finds 153 ???
# fft to out and fft to dac both go on forever it seems
# so does svr to dac and svr to fft
# dac to out is 9755
# but since there are no paths from dac to fft, svr must go to dac first


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

# part_one(input)
# 25 is incorrect
# 455644248 completes in time, but is too low
part_two(input)
