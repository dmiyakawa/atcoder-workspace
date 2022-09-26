#!/usr/bin/env python3

from bisect import bisect_left
from math import atan2, degrees


def solve(N: int, X: "List[int]", Y: "List[int]"):
    P = [(x, y) for x, y in zip(X, Y)]
    ans = 0
    for x0, y0 in P:
        args = []
        for x, y in P:
            if (x, y) == (x0, y0):
                continue
            arg = degrees(atan2(y - y0, x - x0)) % 360
            args.append(arg)
        args.sort()
        l = len(args)
        for j, a1 in enumerate(args):
            left, right = 0, l
            while left + 1 < right:
                mid = (left + right) // 2
                am = args[(mid + j) % l]
                if am < (a1 + 180) % 360:
                    left = mid
                else:
                    right = mid
            a2 = args[(left + j) % l]
            a3 = args[(right + j) % l]
            ans = max(ans,
                      min(abs(a1 - a2), 360 - abs(a1 - a2)),
                      min(abs(a1 - a3), 360 - abs(a1 - a3)))
    print(ans)


def solve_ref(N, X, Y):
    """https://atcoder.jp/contests/typical90/submissions/35024939"""
    xy = [(x, y) for x, y in zip(X, Y)]
    ans = 0
    for i, (x, y) in enumerate(xy):
        num = []
        for j, (xx, yy) in enumerate(xy):
            if i == j:
                continue
            num.append(degrees(atan2(yy - y, xx - x)) % 360)
        num.sort()

        for j in range(len(num)):
            want = (num[j] + 180) % 360
            cnt = min(bisect_left(num, want), N - 2)
            a = min(abs(num[j] - num[cnt]), 360 - abs(num[j] - num[cnt]))
            b = min(abs(num[j] - num[cnt - 1]), 360 - abs(num[j] - num[cnt - 1]))
            ans = max(ans, a, b)
    print(ans)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, X, Y)


if __name__ == "__main__":
    main()
