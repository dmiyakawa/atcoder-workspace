#!/usr/bin/env python3

import sys
from collections import defaultdict, deque

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)

def solve(N: int, a: "List[int]", b: "List[int]"):
    links = defaultdict(set)
    for i, (a0, b0) in enumerate(zip(a, b)):
        a0 -= 1
        b0 -= 1
        links[a0].add((b0, i))
        links[b0].add((a0, i))
    num_colors = max(len(v) for v in links.values())

    colors = [-1] * (N - 1)
    to_visit = deque([0])
    visited = set()
    while to_visit:
        u = to_visit.pop()
        if u in visited:
            continue
        visited.add(u)

        dests = links[u]
        used_colors = set()
        links_to_care = set()
        for v, link_id in dests:
            color = colors[link_id]
            assert color < num_colors
            if color >= 0:
                assert color not in used_colors
                used_colors.add(color)
            else:
                links_to_care.add(link_id)

            if v not in visited:
                to_visit.appendleft(v)

        min_unused = 0
        for link_id in links_to_care:
            while min_unused in used_colors:
                min_unused += 1
            colors[link_id] = min_unused
            used_colors.add(min_unused)
        assert min_unused < num_colors

    print(num_colors)
    for color in colors:
        assert color >= 0
        print(color + 1)


def solve_wa(N: int, a: "List[int]", b: "List[int]"):
    links = defaultdict(set)
    for i, (a0, b0) in enumerate(zip(a, b)):
        a0 -= 1
        b0 -= 1
        links[a0].add((b0, i))
        links[b0].add((a0, i))

    colors = [-1] * (N - 1)
    num_colors = 0
    for n, ls in sorted(links.items(), key=lambda tup: len(tup[1]), reverse=True):
        used_colors = set()
        links_to_care = set()
        for dst, link_id in ls:
            color = colors[link_id]
            assert color < num_colors
            if color >= 0:
                # WA: これを満たさない
                assert color not in used_colors
                used_colors.add(color)
            else:
                links_to_care.add(link_id)

        min_unused = 0
        while min_unused in used_colors:
            min_unused += 1

        for link_id in links_to_care:
            colors[link_id] = min_unused
            used_colors.add(min_unused)
            while min_unused in used_colors:
                min_unused += 1
        num_colors = max(num_colors, min_unused)

    print(num_colors)
    for color in colors:
        assert color >= 0
        print(color + 1)


if __name__ == "__main__":
    main()
