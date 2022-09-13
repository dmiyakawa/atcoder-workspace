#!/usr/bin/env python3



def solve(N: int, K: int, C: int, S: str):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, K, C, S)


if __name__ == "__main__":
    main()
