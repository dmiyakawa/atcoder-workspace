#!/usr/bin/env python3
#
# 座標圧縮版
#
from typing import List, Dict


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    P = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        P[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, M, P, Y)


def solve(N: int, M: int, P: "List[int]", Y: "List[int]"):
    import bisect
    p_to_ys: Dict[int, List[int]] = {}
    for p, y in zip(P, Y):
        p_to_ys.setdefault(p, []).append(y)

    for lst in p_to_ys.values():
        lst.sort()

    for p, y in zip(P, Y):
        print("{:06d}{:06d}".format(p, bisect.bisect_left(p_to_ys[p], y) + 1))


if __name__ == "__main__":
    main()
