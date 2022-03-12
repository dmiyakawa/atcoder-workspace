#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    lx = [int()] * (N)  # type: "List[int]"
    ly = [int()] * (N)  # type: "List[int]"
    rx = [int()] * (N)  # type: "List[int]"
    ry = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        lx[i] = int(next(tokens))
        ly[i] = int(next(tokens))
        rx[i] = int(next(tokens))
        ry[i] = int(next(tokens))
    solve(N, lx, ly, rx, ry)


def solve(N: int, lx: "List[int]", ly: "List[int]", rx: "List[int]", ry: "List[int]"):
    return


if __name__ == "__main__":
    main()
