#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(A, B, C, D)


def solve(A: int, B: int, C: int, D: int):
    if A < C:
        print("Takahashi")
    elif A > C:
        print("Aoki")
    else:
        if B <= D:
            print("Takahashi")
        else:
            print("Aoki")


if __name__ == "__main__":
    main()
