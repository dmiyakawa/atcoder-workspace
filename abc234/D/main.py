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
    K = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, P)


def solve(N: int, K: int, P: "List[int]"):
    from bisect import bisect
    lst = sorted(P[:K])
    print(lst[-1])
    for i in range(K, N):
        lst.insert(bisect(lst, P[i]), P[i])
        print(lst[i])




if __name__ == "__main__":
    main()
