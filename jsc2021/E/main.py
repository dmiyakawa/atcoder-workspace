#!/usr/bin/env python3

NO = "impossible"  # type: str


def solve(K: int, S: str):
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
    S = next(tokens)  # type: str
    solve(K, S)


if __name__ == "__main__":
    main()
