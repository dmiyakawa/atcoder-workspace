#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = [int()] * (N)  # type: "List[int]"
    C = [int()] * (N)  # type: "List[int]"
    S = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        D[i] = int(next(tokens))
        C[i] = int(next(tokens))
        S[i] = int(next(tokens))
    solve(N, D, C, S)


def solve(N: int, D: "List[int]", C: "List[int]", S: "List[int]"):
    return


if __name__ == "__main__":
    main()
