#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = int(next(tokens)) - 1  # type: int
    Y = int(next(tokens)) - 1 # type: int
    A = [int()] * M  # type: "List[int]"
    B = [int()] * M  # type: "List[int]"
    T = [int()] * M  # type: "List[int]"
    K = [int()] * M  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens)) - 1
        B[i] = int(next(tokens)) - 1
        T[i] = int(next(tokens))
        K[i] = int(next(tokens))
    solve(N, M, X, Y, A, B, T, K)


def solve(N: int, M: int, X: int, Y: int, A: "List[int]", B: "List[int]", T: "List[int]", K: "List[int]"):
    import heapq
    from collections import defaultdict

    E = defaultdict(list)
    for a, b, t, k in zip(A, B, T, K):
        E[a].append((b, t, k))
        E[b].append((a, t, k))

    arr_time = [Inf] * N
    arr_time[X] = 0
    h = [(0, X)]
    visited = set()

    while len(h) > 0:
        cur_t, v = heapq.heappop(h)
        if v in visited:
            continue
        visited.add(v)

        for dest, t, k in E[v]:
            next_t = (cur_t // k + (1 if cur_t % k else 0)) * k + t
            if arr_time[dest] > next_t:
                arr_time[dest] = next_t
                heapq.heappush(h, (next_t, dest))  # type: ignore
    print(-1 if arr_time[Y] == Inf else arr_time[Y])


if __name__ == "__main__":
    main()
