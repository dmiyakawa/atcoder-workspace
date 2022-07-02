#!/usr/bin/env python3

from collections import defaultdict, deque
from typing import Tuple


def solve(M, links, first_tup: Tuple) -> int:
    visited = {first_tup}

    to_check = deque()
    to_check.appendleft((first_tup, 0))
    all_pos = {i for i in range(9)}
    min_count = 10**9

    while to_check:
        tup, count = to_check.popleft()
        if tup == tuple(i for i in range(8)):
            min_count = min(min_count, count)
            continue
        cur_ep_s = all_pos - set(tup)
        assert len(cur_ep_s) == 1
        cur_ep = cur_ep_s.pop()
        for next_ep in links[cur_ep]:
            next_tup = tuple(cur_ep if p == next_ep else p for p in tup)
            if next_tup not in visited and count + 1 < min_count:
                visited.add(next_tup)
                to_check.append((next_tup, count + 1))
    return min_count if min_count < 10**8 else -1


def main():
    M = int(input())
    links = defaultdict(set)
    for _ in range(M):
        u, v = [int(e) - 1 for e in input().split()]
        links[u].add(v)
        links[v].add(u)
    first_pos = tuple(int(e) - 1 for e in input().split())
    print(solve(M, links, first_pos))


if __name__ == "__main__":
    main()
