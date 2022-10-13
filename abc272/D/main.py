#!/usr/bin/env python3
from collections import deque


def solve(N: int, M: int):
    grid = [-1] * (N * N)
    grid[0] = 0
    to_visit = deque([0])
    visited = set()
    movables = set()
    for i in range(N):
        for j in range(N):
            if (i, j) != (0, 0) and i**2 + j**2 == M:
                movables.add((i, j))
                movables.add((-i, j))
                movables.add((i, -j))
                movables.add((-i, -j))

    while to_visit:
        u = to_visit.pop()

        if u in visited:
            continue
        visited.add(u)

        c = grid[u]
        i, j = divmod(u, N)
        for k, l in movables:
            ni = i + k
            nj = j + l
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            v = ni * N + nj
            if v in visited:
                continue
            next_c = c + 1
            if 0 <= grid[v] <= next_c:
                continue
            grid[v] = next_c
            to_visit.appendleft(v)

    for i in range(N):
        print(*[grid[i * N + j] for j in range(N)])


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)


if __name__ == "__main__":
    main()
