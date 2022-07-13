#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(s: str, k: int):
    if len(s) < k:
        return 0
    p = set()
    for i in range(len(s) - k + 1):
        p.add(s[i:i + k])
    return len(p)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    k = int(next(tokens))  # type: int
    print(solve(s, k))


if __name__ == "__main__":
    main()
