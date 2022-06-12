#!/usr/bin/env python3

from typing import Dict, Set


def main():
    N, Q = [int(e) for e in input().split()]
    d: Dict[int, Set[int]] = {n: set() for n in range(1, N + 1)}
    for _ in range(Q):
        op, u, v = [int(e) for e in input().split()]
        if op == 1:
            if v in d[u]:
                d[u].remove(v)
                d[v].remove(u)
            else:
                d[u].add(v)
                d[v].add(u)
        else:
            visited = {u}
            to_visit = d[u].copy()
            visitable = False
            while to_visit:
                i = to_visit.pop()
                if i == v:
                    visitable = True
                    break
                if i not in visited:
                    visited.add(i)
                    to_visit |= d[i]
            print("Yes" if visitable else "No")


if __name__ == "__main__":
    main()
