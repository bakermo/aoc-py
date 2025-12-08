
from collections import deque
import math
import sys
from typing import List, Tuple
# we need this obnoxiousness to reference the utils package in repo root
sys.path.append("../")
sys.path.append("../../../")
from aoc_py_utils import utils
from collections.abc import Sequence


class Node():
    def __init__(self, current: Tuple, neighbors: List = []):
        self.current = current
        self.neighbors = neighbors

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __str__(self):
        return f"{self.current} => {[n.current for n in self.neighbors]}"

    def __repr__(self):
        return f"{self.current} => {[n.current for n in self.neighbors]}"


def get_distance(n, q):
    return math.sqrt(((n[0] - q[0])**2) + ((n[1] - q[1])**2) + ((n[2] - q[2])**2))


def is_in_circuit(x, y, cache):
    if (x.current, y.current) in cache or (y.current, x.current) in cache:
        return True

    seen = set()
    queue = deque()
    # print(f"detecting for x, y: {x.current}, {y.current}")
    for xn in x.neighbors:
        queue.append(xn)

    while queue:
        n = queue.popleft()
        if n.current == y.current:
            cache[(x.current, y.current)] = True
            cache[(y.current, x.current)] = True
            return True

        seen.add(n)

        for nn in n.neighbors:
            if nn not in seen:
                queue.append(nn)

    return False


def get_circuit(root):
    circuit = set()
    queue = deque()

    circuit.add(root.current)

    for rn in root.neighbors:
        queue.append(rn)

    while queue:
        n = queue.popleft()
        circuit.add(n.current)

        for nn in n.neighbors:
            if nn.current not in circuit:
                queue.append(nn)

    return circuit


# def is_full_circuit(nodes, cache):
#     for x in nodes.values():
#         for y in nodes.values():
#             if x.current != y.current:
#                 if (x.current, y.current) not in cache and (y.current, x.current) not in cache:
#                     return False
#     return True


@utils.aoctimer("Part 1")
def part_one(input: Sequence[str]):
    result = 0

    nodes = dict()
    distances = dict()
    for line in input:
        x, y, z = map(int, line.split(','))
        nodes[(x, y, z)] = Node((x, y, z), [])

    for n in nodes.keys():
        for q in nodes.keys():
            if n != q and (n, q) not in distances and (q, n) not in distances:
                d = get_distance(n, q)
                distances[(n, q)] = d

    counter = 0
    # pairs = set()
    is_circuit_cache = dict()
    while counter < 29:
        lowest = min(distances, key=distances.get)
        distances.pop(lowest)
        # print(f"lowest: {lowest}")
        p, q = lowest
        # print(f"pq {(p, q)}")
        # @if ((p, q)) not in pairs and ((q, p)) not in pairs:
        np = nodes[p]
        nq = nodes[q]
        counter += 1
        if not is_in_circuit(np, nq, is_circuit_cache):
            nq.add_neighbor(np)
            nodes[q] = nq
            np.add_neighbor(nq)
            nodes[p] = np
            is_circuit_cache[(p, q)] = True
            is_circuit_cache[(q, p)] = True
            # is_circuit_cache[(np.current, nq.current)] = True
            # is_circuit_cache[(nq.current, np.current)] = True
        # print(f"P AND Q {p} {q}")
        test_circuit = get_circuit(nodes[p])
        print(f"test circuit: {test_circuit}")
        print(len(test_circuit))
        if (len(test_circuit) == len(input)):
            print("FOUND IT!")
        # if is_full_circuit(nodes, is_circuit_cache):
        #     print("FOUND IT!")

    circuit_lengths = []
    visited = set()
    for n in nodes.values():
        if n.current not in visited:
            circuit = get_circuit(n)
            for c in circuit:
                visited.add(c)
            print(f"circuit: {circuit}")
            circuit_lengths.append(len(circuit))

    circuit_lengths.sort(reverse=True)
    print(circuit_lengths)
    print(len(circuit_lengths))
    result += math.prod(circuit_lengths[0:3])
    return result


@utils.aoctimer("Part 2")
def part_two(input: Sequence[str]):
    result = 0
    nodes = dict()
    distances = dict()
    for line in input:
        x, y, z = map(int, line.split(','))
        nodes[(x, y, z)] = Node((x, y, z), [])

    for n in nodes.keys():
        for q in nodes.keys():
            if n != q and (n, q) not in distances and (q, n) not in distances:
                d = get_distance(n, q)
                distances[(n, q)] = d

    counter = 0
    # pairs = set()
    is_circuit_cache = dict()
    while counter < len(distances):  # len(distances) > 0:
        lowest = min(distances, key=distances.get)
        distances.pop(lowest)
        print(f"lowest: {lowest}")
        p, q = lowest
        # print(f"pq {(p, q)}")
        # @if ((p, q)) not in pairs and ((q, p)) not in pairs:
        np = nodes[p]
        nq = nodes[q]
        counter += 1
        if not is_in_circuit(np, nq, is_circuit_cache):
            nq.add_neighbor(np)
            nodes[q] = nq
            np.add_neighbor(nq)
            nodes[p] = np

            is_circuit_cache[(p, q)] = True
            is_circuit_cache[(q, p)] = True

        test_circuit = get_circuit(nodes[p])
        print(f"test circuit: {test_circuit}")
        print(len(test_circuit))
        if (len(test_circuit) == len(input)):
            result += p[0] * q[0]
            print("FOUND IT!")
            break

        # if is_full_circuit(nodes, is_circuit_cache):
        #     result += p[0] * q[0]
        #     break
    return result
    # circuit_lengths = []
    # visited = set()
    # for n in nodes.values():
    #     if n.current not in visited:
    #         circuit = get_circuit(n)
    #         for c in circuit:
    #             visited.add(c)
    #         print(f"circuit: {circuit}")
    #         circuit_lengths.append(len(circuit))

    # circuit_lengths.sort(reverse=True)
    # print(circuit_lengths)
    # print(len(circuit_lengths))
    # result += math.prod(circuit_lengths[0:3])
    # return result


is_test = False

file_path = "sample.txt" if is_test else "input.txt"
print(f"file: {file_path}")

input = []

file = open(f"{file_path}")

for line in file:
    input.append(str(line.strip()))

part_one(input)

part_two(input)
