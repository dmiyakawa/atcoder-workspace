#!/usr/bin/env python3

from typing import List


def solve_ref(N: int, A: int, B: int, C: int, L: "List[int]"):
    """DFSの練習"""
    inf = float("inf")

    def _dfs(i, bc, a, b, c):
        if i == N:
            if not (a > 0 and b > 0 and c > 0):
                return inf
            return bc + abs(A - a) + abs(B - b) + abs(C - c)
        return min(_dfs(i + 1, bc, a, b, c),
                   _dfs(i + 1, bc + (10 if a > 0 else 0), a + L[i], b, c),
                   _dfs(i + 1, bc + (10 if b > 0 else 0), a, b + L[i], c),
                   _dfs(i + 1, bc + (10 if c > 0 else 0), a, b, c + L[i]))

    return _dfs(0, 0, 0, 0, 0)


def solve(N: int, A: int, B: int, C: int, L: "List[int]"):
    min_cost = 10**9
    for n in range(4**N):
        bars = [0, 0, 0]
        base_cost = 0
        # dbg = [[], [], []]
        for i in range(N):
            j = (n // 4**i) % 4
            if j == 0:
                continue
            j -= 1
            if bars[j]:
                base_cost += 10
            bars[j] += L[i]
            # dbg[j].append(i)
        if min(bars) == 0:
            continue
        cand = base_cost + abs(A - bars[0]) + abs(B - bars[1]) + abs(C - bars[2])
        if min_cost > cand:
            min_cost = cand

    print(min_cost)



def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    l = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, C, l)


if __name__ == "__main__":
    main()
