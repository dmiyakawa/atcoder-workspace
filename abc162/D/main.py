#!/usr/bin/env python3

from collections import Counter
from math import factorial


def solve(N: int, S: str):
    counter = Counter(S)
    R, G, B = counter["R"], counter["G"], counter["B"]
    a = R * G * B
    b = 0
    for n in range(1, N // 2 + 1):
        for i in range(N - 2 * n):
            if S[i] == S[i + n] or S[i + n] == S[i + 2 * n] or S[i] == S[i + 2 * n]:
                continue
            b += 1
    print(a - b)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == "__main__":
    main()
