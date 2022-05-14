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
    S = next(tokens)  # type: str
    N = int(next(tokens))  # type: int
    l = [int()] * (N)  # type: "List[int]"
    r = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(S, N, l, r)


def solve(S: str, N: int, l: "List[int]", r: "List[int]"):
    for left, right in zip(l, r):
        S = S[:left - 1] + "".join(reversed(S[left - 1:right])) + S[right:]
    print(S)


if __name__ == "__main__":
    main()
