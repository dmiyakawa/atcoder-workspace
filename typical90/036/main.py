#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    q = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, x, y, q)


def solve(N: int, Q: int, x: "List[int]", y: "List[int]", q: "List[int]"):
    return


if __name__ == "__main__":
    main()
