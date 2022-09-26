#!/usr/bin/env python3

from functools import cmp_to_key
import math
from collections import Counter
from typing import List


def solve_ref(N: int, X: "List[int]", Y: "List[int]"):
    plots = declination_sort(zip(X, Y))
    ans = 0
    for l in range(N):
        r = l
        X = 0
        Y = 0
        for _ in range(N):
            X += plots[r][0]
            Y += plots[r][1]
            ans = max(ans, X ** 2 + Y ** 2)
            r += 1
            r %= N
    print(ans ** 0.5)


def declination_sort(l):
    def convert_arg(p):
        x, y = p
        if x >= 0:
            if y > 0:
                orthant = 1
                a, b = x, y
            elif y < 0:
                orthant = 4
                a, b = -y, x
            else:
                orthant = 0
                a, b = x, y
        else:
            if y >= 0:
                orthant = 2
                a, b = y, -x
            else:
                orthant = 3
                a, b = -x, -y
        d = [3, 2, 1, 5, 4]  # -pi<=theta<pi のとき
        return a, b, d[orthant]

    def arg_sort(p0, p1):
        x0, y0, orthant0 = convert_arg(p0)
        x1, y1, orthant1 = convert_arg(p1)
        if orthant0 < orthant1:
            return 1
        if orthant0 > orthant1:
            return -1
        if x0 * y1 == x1 * y0:
            return 0
        return 1 if x0 * y1 < x1 * y0 else -1

    return sorted(l, key=cmp_to_key(arg_sort))


def solve_wip(N: int, X: "List[int]", Y: "List[int]"):
    # WAのまま。O(N logN) ... にもなってない気がする
    counter = Counter(zip(X, Y))
    cords = sorted(((x, y, math.atan2(y, x) * 180 / math.pi % 360) for (x, y) in counter.keys() if (x, y) != (0, 0)),
                   key=lambda tup: tup[2])
    M = len(cords)
    ans = 0
    for i, c in enumerate(cords):
        x, y, t = c
        p_c = cords[(i - 1) % M]
        p_x, p_y, p_t = p_c

        left, right = 0, M
        while left + 1 < right:
            mid = (left + right) // 2
            if cords[(mid + i) % M][2] < (t + 180) % 360:
                left = mid
            else:
                right = mid

        if p_x * y == x * p_y:
            k0 = left
        else:
            p_l, p_r = 0, M
            while p_l + 1 < p_r:
                mid = (p_l + p_r) // 2
                if cords[(mid + i) % M][2] < (p_t + 180) % 360:
                    p_l = mid
                else:
                    p_r = mid
            k0 = p_l

        # print(i, k0, right)
        for k in range(k0, right + 1):
            a_x, a_y = 0, 0
            for j in range(k + 1):
                if j > 0 and (i + j) % M == i:
                    break
                c1 = cords[(i + j) % M]
                x1, y1 = c1[0], c1[1]
                cn = counter[(x1, y1)]
                a_x += x1 * cn
                a_y += y1 * cn
            a = math.sqrt(a_x * a_x + a_y * a_y)
            ans = max(ans, a)
    print(ans)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve_ref(N, x, y)


if __name__ == "__main__":
    main()
