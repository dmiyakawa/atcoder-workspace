#!/usr/bin/env python3



def solve(A: int, B: int, T: int):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    solve(A, B, T)


if __name__ == "__main__":
    main()
