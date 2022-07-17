#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(s: str):
    l, r = 0, len(s) - 1
    count = 0
    while l < r:
        if s[l] == s[r]:
            l, r = l + 1, r - 1
        elif s[l] == "x":
            count += 1
            l += 1
        elif s[r] == "x":
            count += 1
            r -= 1
        else:
            return -1

    return count


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    print(solve(s))


if __name__ == "__main__":
    main()
