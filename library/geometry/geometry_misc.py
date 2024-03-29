
from typing import List


def declination_sort(l: "List[int, int]"):
    """\
    偏角ソート
    c.f. https://atcoder.jp/contests/abc139/submissions/34882045"""
    from functools import cmp_to_key

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
        # 象限と優先度の変換
        d = [3, 2, 1, 5, 4]  # -pi<=theta<pi のとき
        # d = [0, 1, 2, 3, 4]  # 0<=theta<2pi のときはこっち
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
