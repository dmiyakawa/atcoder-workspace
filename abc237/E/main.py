#!/usr/bin/env python3

import heapq
import sys
from collections import defaultdict
from typing import List


def solve(N: int, M: int, H: "List[int]", U: "List[int]", V: "List[int]"):
    E = defaultdict(list)
    for u, v in zip(U, V):
        u -= 1
        v -= 1
        if H[u] < H[v]:
            E[u].append((2 * (H[u] - H[v]), v))
            E[v].append((H[v] - H[u], u))
        else:
            E[u].append((H[u] - H[v], v))
            E[v].append((2 * (H[v] - H[u]), u))
    H_max = max(H)
    H_diff = H_max - min(H)
    scores = [- 2 * H_max] * N
    scores[0] = 0
    max_score = 0
    hq = [(0, 0)]
    st = [0]
    visited = set()
    while hq:
        _, v = heapq.heappop(hq)
        print(v, scores[v])
        if scores[v] < max_score - H_diff:
            continue
        if v in visited:
            continue
        visited.add(v)


        for score, dest in E[v]:
            next_score = scores[v] + score
            if scores[dest] < next_score:
                scores[dest] = next_score
                max_score = max(max_score, scores[dest])
                # st.append(dest)
                heapq.heappush(hq, (-next_score, dest))
    print(max_score)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    U = [int()] * (M)  # type: "List[int]"
    V = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, M, H, U, V)


def _debug():
    N = 2 * 10**5
    M = 2 * 10**5 - 1
    H = [0 for _ in range(N)]
    U = [i for i in range(1, N)]
    V = [i for i in range(2, N + 1)]
    solve(N, M, H, U, V)


if __name__ == "__main__":
    # _debug()
    main()
