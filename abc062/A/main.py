#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(x: int, y: int):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(x, y)


if __name__ == "__main__":
    main()
