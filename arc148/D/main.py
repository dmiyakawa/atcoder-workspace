#!/usr/bin/env python3



def solve(N: int, M: int, A: "List[int]"):
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
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(2 * N)]  # type: "List[int]"
    solve(N, M, A)


if __name__ == "__main__":
    main()
