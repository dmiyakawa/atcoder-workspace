#!/usr/bin/env python3

import heapq
import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(S: str, T: str, K: int, C: "List[str]", A: "List[str]"):
    to_visit = [(0, T)]
    visited = set()
    while to_visit:
        (cost, t) = heapq.heappop(to_visit)
        if t in visited:
            continue
        visited.add(t)
        if t == S:
            return cost
        for c, a in zip(C, A):
            i = 0
            while True:
                i = t.find(a, i)
                if i < 0:
                    break
                new_t = t[:i] + c + t[i+len(a):]
                if new_t == S:
                    return cost + 1
                if new_t in visited:
                    continue
                heapq.heappush(to_visit, (cost + 1, new_t))
                i = i + len(a)

    return -1


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    C = [str()] * (K)  # type: "List[str]"
    A = [str()] * (K)  # type: "List[str]"
    for i in range(K):
        C[i] = next(tokens)
        A[i] = next(tokens)
    print(solve(S, T, K, C, A))


if __name__ == "__main__":
    main()
