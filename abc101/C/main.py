#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, K: int, A: "List[int]"):
    i = A.index(1)
    rem_left = i
    rem_right = N - 1 - i
    rem_min = min(rem_left, rem_right)
    rem_max = max(rem_left, rem_right)
    rem = rem_max + rem_min % (K - 1)
    ans = rem_min // (K - 1) + rem // (K - 1) + (1 if rem % (K - 1) else 0)
    print(ans)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)


if __name__ == "__main__":
    main()
