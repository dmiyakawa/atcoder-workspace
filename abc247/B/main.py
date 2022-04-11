#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [str()] * (N)  # type: "List[str]"
    t = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        s[i] = next(tokens)
        t[i] = next(tokens)
    solve(N, s, t)


def solve(N: int, s: "List[str]", t: "List[str]"):
    count = {}
    for si in s:
        count[si] = count.get(si, 0) + 1
    for ti in t:
        count[ti] = count.get(ti, 0) + 1

    possibly_unique = True
    for si, ti in zip(s, t):
        if si == ti:
            if count[si] > 2:
                possibly_unique = False
                break
        else:
            if count[si] > 1 and count[ti] > 1:
                possibly_unique = False
                break
    print(YES if possibly_unique else NO)


if __name__ == "__main__":
    main()
