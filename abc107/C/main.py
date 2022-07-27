#!/usr/bin/env python3

import bisect
import sys


def solve(N: int, K: int, x: "List[int]"):
    p = bisect.bisect_left(x, 0)
    left = p - K if p - K >= 0 else 0
    right = left + K - 1
    ans = float("inf")
    while right < N:
        lv, rv = x[left], x[right]
        if left == right:
            ans = abs(lv)
        elif lv * rv >= 0:
            ans = min(ans, max(abs(lv), abs(rv)))
        else:
            ans = min(ans, abs(rv - lv) + min(abs(lv), abs(rv)))
        left, right = left + 1, right + 1
    assert ans != float("inf")
    print(ans)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, x)


if __name__ == "__main__":
    main()
