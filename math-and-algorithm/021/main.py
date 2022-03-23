#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    r = int(next(tokens))  # type: int
    solve(n, r)


def solve(n: int, r: int):
    return


if __name__ == "__main__":
    main()
