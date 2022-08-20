#!/usr/bin/env python3

from collections import defaultdict
import math


def solve(N: int, K: int, X: "List[int]", Y: "List[int]"):
    """公式解説と違う方法。嘘解法かも……

    直線はそれを通る点と傾きをうまくとれば一意になる -> 辞書のkeyにする
    「うまくとる」について
    - 点は「x座標に一番近い, x, y が両方とも整数の座標」（これを雑にやるとダブルカウントする）
    - 傾きは、gcd取ったベクトルのx, yの組
    例外がy軸と平行の直線（傾きが無限大）。これはx座標が同じ点の集合を別途用意する
    """
    if K == 1:
        return "Infinity"
    ans = 0

    xs = defaultdict(set)
    ss = {}
    cs = sorted(zip(X, Y))
    for x, y in cs:
        xs[x].add(y)
        for x1, y1 in cs:
            if x == x1:
                continue
            # x, y を直接使うとループが壊れるようぇーい
            if x > x1:
                x0, y0 = x1, y1
                x1, y1 = x, y
            else:
                x0, y0 = x, y
                x1, y1 = x1, y1

            xg, yg = x1 - x0, y1 - y0
            g = math.gcd(xg, yg)
            xg //= g
            yg //= g

            # xが0以上で最初にx, yともに整数の座標になるものを(xb, yb)としてkeyとする
            xb = x0
            yb = y0
            if xb > 0:
                t = (xb // xg)
                xb -= t * xg
                yb -= t * yg
            else:
                d, m = divmod(abs(xb), xg)
                t = (d + (1 if m else 0))
                xb += t * xg
                yb += t * yg

            # 上の条件で作成した座標(xb, yb)と直線の傾きで直線は一意になる
            key = (xb, yb, xg, yg)
            if key not in ss:
                ss[key] = {(x0, y0)}
            ss[key].add((x1, y1))

    for key, tups in ss.items():
        if len(tups) >= K:
            # print(key, tups)
            ans += 1

    for x, ys in xs.items():
        if len(ys) >= K:
            # print(ys)
            ans += 1

    return ans



def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    print(solve(N, K, X, Y))


if __name__ == "__main__":
    main()
