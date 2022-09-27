#!/usr/bin/env python3

import sys
from collections import deque

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, A: "List[int]"):
    A.sort()
    ans = 0
    rest = deque()
    first = A.pop()
    second = A.pop()
    ans += first
    rest.appendleft(second)
    rest.appendleft(second)
    while A:
        a = A.pop()
        ans += rest.pop()
        rest.appendleft(a)
        rest.appendleft(a)
    print(ans)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == "__main__":
    main()
