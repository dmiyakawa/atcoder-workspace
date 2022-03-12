#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    E = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(T, L, X, Y, Q, E)


def solve(T: int, L: int, X: int, Y: int, Q: int, E: "List[int]"):
    return


if __name__ == "__main__":
    main()
