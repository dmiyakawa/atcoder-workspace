#!/usr/bin/env python3
import math
import sys
from collections import Counter

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, S: "List[str]"):
    counter = Counter("".join(sorted(s)) for s in S)
    ans = 0
    for key, value in counter.items():
        ans += value * (value - 1) // 2
    # print(counter)
    print(ans)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, s)


if __name__ == "__main__":
    main()
