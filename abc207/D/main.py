#!/usr/bin/env python3

import math


def rotate(x, y, rad):
    l = math.sqrt(x**2 + y**2)
    cos_a, sin_a = x / l, y / l
    cos_b, sin_b = math.cos(rad), math.sin(rad)
    rot_x, rot_y = l * (cos_a * cos_b - sin_a * sin_b), l * (sin_a * cos_b + cos_a * sin_b)
    return rot_x, rot_y


def all_same_points(S, T):
    # 多分ダメ
    if all(math.isclose(s[0], t[0]) and math.isclose(s[1], t[1]) for s, t in zip(S, T)):
        # print(S)
        # print(T)
        return True


def solve(N, S, T) -> bool:
    # うなー！方針あってるのに！
    scx, scy = sum(s[0] for s in S) / N, sum(s[1] for s in S) / N
    tcx, tcy = sum(t[0] for t in T) / N, sum(t[1] for t in T) / N
    Sc = [(x - scx, y - scy) for x, y in S]
    Tc = [(x - tcx, y - tcy) for x, y in T]
    max_sl = max(math.sqrt(x ** 2 + y ** 2) for x, y in Sc)
    max_tl = max(math.sqrt(x ** 2 + y ** 2) for x, y in Tc)
    if not math.isclose(max_sl, max_tl):
        return False
    Scn = [(x / max_sl, y / max_sl, math.sqrt(x**2 + y**2)) for x, y in Sc]
    Tcn = [(x / max_tl, y / max_tl, math.sqrt(x**2 + y**2)) for x, y in Tc]
    Scn.sort(key=lambda tup: tup[2])
    Tcn.sort(key=lambda tup: tup[2])
    for deg in range(0, 360):
        rad = math.pi * deg / 180
        Tcnr = [(*rotate(x, y, rad), l) for x, y, l in Tcn]
        if all_same_points(Scn, Tcnr):
            return True

    return False


def main():
    N = int(input())
    S = [tuple(int(e) for e in input().split()) for _ in range(N)]
    T = [tuple(int(e) for e in input().split()) for _ in range(N)]
    print("Yes" if solve(N, S, T) else "No")


if __name__ == "__main__":
    main()
