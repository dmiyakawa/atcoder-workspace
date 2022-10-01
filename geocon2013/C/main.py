#!/usr/bin/env python3



def solve(N: int, S: "List[str]", X: "List[int]", Y: "List[int]"):
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
    S = [str()] * (N)  # type: "List[str]"
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = next(tokens)
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, S, X, Y)


if __name__ == "__main__":
    main()
