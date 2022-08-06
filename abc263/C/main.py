#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def construct(prev, rem, M):
    if rem == 1:
        for n in range(prev + 1, M + 1):
            yield [n]
    else:
        for n in range(prev + 1, M - rem + 2):
            for con in construct(n, rem - 1, M):
                yield [n, *con]


def solve(N: int, M: int):
    answers = []
    for ans in construct(0, N, M):
        answers.append(ans)
    for ans in sorted(answers):
        print(*ans)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)


if __name__ == "__main__":
    main()
