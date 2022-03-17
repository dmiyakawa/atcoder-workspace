#!/usr/bin/env python3


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    solve2(a, b, c)


def solve(a: int, b: int, c: int):
    print(YES if a < c ** b else NO, end="")


def solve2(a: int, b: int, c: int):
    import math
    print(YES if math.log2(a) < b * math.log2(c) else NO, end="")


if __name__ == "__main__":
    main()
