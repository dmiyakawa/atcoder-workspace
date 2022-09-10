#!/usr/bin/env python3



def solve(S_x: int, S_y: int, G_x: int, G_y: int):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S_x = int(next(tokens))  # type: int
    S_y = int(next(tokens))  # type: int
    G_x = int(next(tokens))  # type: int
    G_y = int(next(tokens))  # type: int
    solve(S_x, S_y, G_x, G_y)


if __name__ == "__main__":
    main()
