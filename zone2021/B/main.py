#!/usr/bin/env python3



def solve(N: int, D: int, H: int, d: "List[int]", h: "List[int]"):
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
    D = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    d = [int()] * (N)  # type: "List[int]"
    h = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        d[i] = int(next(tokens))
        h[i] = int(next(tokens))
    solve(N, D, H, d, h)


if __name__ == "__main__":
    main()
