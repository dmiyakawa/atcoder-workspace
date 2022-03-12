#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    V = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(V, A, B, C)


def solve(V: int, A: int, B: int, C: int):
    V = V % (A + B + C)
    if V - A < 0:
        print("F", end="")
    elif V - A - B < 0:
        print("M", end="")
    else:
        print("T", end="")


if __name__ == "__main__":
    main()
