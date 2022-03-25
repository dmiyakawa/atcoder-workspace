#!/usr/bin/env python3

import functools
import math


def lcm(a, b):
    return a // math.gcd(a, b) * b


def lcm_all(*args):
    return functools.reduce(lcm, args)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(lcm_all(*A))


if __name__ == "__main__":
    main()
