#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, S: "List[str]"):
    d = {}
    for name in S:
        d[name] = d.get(name, 0) + 1
    max_value = 0
    ans = None
    for name, value in d.items():
        if value > max_value:
            max_value = value
            ans = name
    print(ans)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)


if __name__ == "__main__":
    main()
