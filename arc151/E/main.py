#!/usr/bin/env python3



def solve(N: int, A: "List[int]", P: int, X: "List[int]", Q: int, Y: "List[int]"):
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
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    P = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(P)]  # type: "List[int]"
    Q = int(next(tokens))  # type: int
    Y = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, A, P, X, Q, Y)


if __name__ == "__main__":
    main()
