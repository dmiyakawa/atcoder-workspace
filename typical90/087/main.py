#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, P, K, A)


def solve(N: int, P: int, K: int, A: "List[List[int]]"):
    return


if __name__ == "__main__":
    main()
