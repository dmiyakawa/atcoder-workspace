#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a_x = int(next(tokens))  # type: int
    a_y = int(next(tokens))  # type: int
    b_x = int(next(tokens))  # type: int
    b_y = int(next(tokens))  # type: int
    c_x = int(next(tokens))  # type: int
    c_y = int(next(tokens))  # type: int
    solve(a_x, a_y, b_x, b_y, c_x, c_y)


def solve(a_x: int, a_y: int, b_x: int, b_y: int, c_x: int, c_y: int):
    return


if __name__ == "__main__":
    main()
