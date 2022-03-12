#!/usr/bin/env python3


MOD = 1000000007  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    x = [int()] * (Q)  # type: "List[int]"
    y = [int()] * (Q)  # type: "List[int]"
    z = [int()] * (Q)  # type: "List[int]"
    w = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        z[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, Q, x, y, z, w)


def solve(N: int, Q: int, x: "List[int]", y: "List[int]", z: "List[int]", w: "List[int]"):
    return


if __name__ == "__main__":
    main()
