#!/usr/bin/env python3



def solve(N: int, X: int, Y: "List[int]", Z: "List[int]"):
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
    X = int(next(tokens))  # type: int
    Y = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Z = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, Y, Z)


if __name__ == "__main__":
    main()
