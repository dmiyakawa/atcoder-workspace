#!/usr/bin/env python3



def solve(X: int, Y: int, Z: int):
    if 0 < Y < X or X < Y < 0:
        if 0 < Y < Z or Z < Y < 0:
            print(-1)
        else:
            print(abs(Z) + abs(Z - X))
    else:
        print(abs(X))


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    solve(X, Y, Z)


if __name__ == "__main__":
    main()
