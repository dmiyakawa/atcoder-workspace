#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(K: int, X: int):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(K, X)


if __name__ == "__main__":
    main()
