#!/usr/bin/env python3
import math
from functools import lru_cache


@lru_cache(None)
def solve(N: int):
    if N == 0:
        return 1
    a = solve(math.floor(N//2))
    b = solve(math.floor(N//3))
    return a + b


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    print(solve(N))


if __name__ == "__main__":
    main()
