#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 1000000007  # type: int


def solve(N: int, C: "List[int]"):
    C.sort()
    ans = 1
    for i, v in enumerate(C):
        if v < i:
            return 0
        ans = (ans * (v - i)) % MOD

    return ans


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, C))


if __name__ == "__main__":
    main()
