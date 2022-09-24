#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(a: int, b: int, c: int):
    l = 4 * a * b
    r = (c - a - b) ** 2
    print(YES if 0 < c - a - b and l < r else NO)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    solve(a, b, c)


if __name__ == "__main__":
    main()
