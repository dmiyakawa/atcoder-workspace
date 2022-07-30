#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, A: "List[int]", C: "List[str]"):
    Rs, Gs, Bs = [], [], []
    for a, c in zip(A, C):
        if c == "R":
            Rs.append(a)
        elif c == "G":
            Gs.append(a)
        else:
            Bs.append(a)

    if len(Rs) % 2 == 0 and len(Gs) % 2 == 0:
        assert len(Bs) % 2 == 0
        return 0
    if len(Rs) % 2 == 0:
        x, y, z = Rs, Gs, Bs
    elif len(Gs) % 2 == 0:
        x, y, z = Gs, Rs, Bs
    else:
        assert len(Bs) % 2 == 0
        x, y, z = Bs, Rs, Gs
    Merged_xy = sorted([(_a, "x") for _a in x] + [(_a, "y") for _a in y])
    Merged_xz = sorted([(_a, "x") for _a in x] + [(_a, "z") for _a in z])
    Merged_yz = sorted([(_a, "y") for _a in y] + [(_a, "z") for _a in z])
    return min(calc_min_score(Merged_yz, "y"),
               calc_min_score(Merged_xy, "x") + calc_min_score(Merged_xz, "x"))


def calc_min_score(Merged, c1):
    min_score = Inf
    prev_ax = None
    prev_ay = None
    # print(Merged)
    for a, c in Merged:
        if c == c1:
            if prev_ay is not None:
                min_score = min(min_score, abs(a - prev_ay))
            prev_ax = a
        else:
            if prev_ax is not None:
                min_score = min(min_score, abs(a - prev_ax))
            prev_ay = a
    return min_score


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (2 * N)  # type: "List[int]"
    c = [str()] * (2 * N)  # type: "List[str]"
    for i in range(2 * N):
        a[i] = int(next(tokens))
        c[i] = next(tokens)
    print(solve(N, a, c))


if __name__ == "__main__":
    main()
