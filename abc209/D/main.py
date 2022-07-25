#!/usr/bin/env python3
from collections import defaultdict, deque

Inf = float("inf")

def main():
    N, Q = map(int, input().split())
    links = defaultdict(set)
    for _ in range(N - 1):
        a, b = [int(e) - 1 for e in input().split()]
        links[a].add(b)
        links[b].add(a)
    lst = []
    for key, value in links.items():
        if len(value) == 1:
            lst.append(key)
    lst.sort()
    costs = [Inf for _ in range(N)]
    to_visit = deque([(0, lst[0])])
    visited = set()
    while to_visit:
        c, n = to_visit.pop()
        if n in visited:
            continue
        visited.add(n)
        costs[n] = c
        for next_n in links[n]:
            if next_n in visited:
                continue
            to_visit.appendleft((c + 1, next_n))
    for _ in range(Q):
        c, d = [int(e) - 1 for e in input().split()]
        print("Town" if abs(costs[c] - costs[d]) % 2 == 0 else "Road")


if __name__ == "__main__":
    main()
