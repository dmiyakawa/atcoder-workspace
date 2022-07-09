#!/usr/bin/env python3

import sys
from typing import Dict, Set

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")

def reachable(links: Dict[int, Set[int]], a, b):
    to_visit = {a}
    visited = set()
    while to_visit:
        cur_node = to_visit.pop()
        if cur_node == b:
            return True
        if cur_node in visited:
            continue
        visited.add(cur_node)
        for next_node in links[cur_node]:
            to_visit.add(next_node)
    return False


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    links: Dict[int, Set[int]] = {n: set() for n in range(1, N + 1)}
    for a, b in zip(A, B):
        links[a].add(b)
        links[b].add(a)

    num_bridges = 0
    for a, b in zip(A, B):
        links[a].remove(b)
        links[b].remove(a)

        if not reachable(links, a, b):
            num_bridges += 1

        links[a].add(b)
        links[b].add(a)

    print(num_bridges)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)


if __name__ == "__main__":
    main()
