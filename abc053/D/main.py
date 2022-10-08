#!/usr/bin/env python3
from collections import Counter


def solve(N: int, A: "List[int]"):
    rem = 0
    for v, n in Counter(A).items():
        rem += n - 1
    print(N - (rem // 2 + rem % 2) * 2)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

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
