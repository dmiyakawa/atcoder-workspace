#!/usr/bin/env python3

import sys

def solve_editorial(N: int, L: int, R: int, A: "List[int]"):
    """https://atcoder.jp/contests/abc263/editorial/4549
    Lで置き換える操作とRと置き換える操作を同時に行うindexに意味はない
    よって「LとRの操作は重ならない」と仮定して問題はない。
    Lで「置き換えても良い」範囲とRで「置き換えても良い」範囲を仕切りのように0〜Nで移動させたときどこかの仕切りで最小になる
    Lで「途中まで置き換えても良い」操作による最小値をf(x)、
    Rで「途中まで置き換えても良い」操作による最小値をg(x)としたとき、上記の解説のような定式化となる。
    f(0)...f(N), g(0)...g(N)を求める操作をO(N)で行い、
    それを用いて仕切りを移動させつつ最小値を求める操作をO(N)で行うので、全体でO(N)
    """

    f = [0 for _ in range(N+1)]
    g = [0 for _ in range(N+1)]
    for n in range(1, N+1):
        f[n] = min(f[n - 1] + A[n - 1], L * n)
        g[n] = min(g[n - 1] + A[N - n], R * n)
    print(min(f[n] + g[N - n] for n in range(0, N+1)))


def solve_wa(N: int, L: int, R: int, A: "List[int]"):
    """\
    コンテスト時。LとRの範囲が「食い合う」状態が発生してしまって対応に苦慮した
    - 累積和は負値に対してあまり良い見通しを与えない。定数値で置き換える場合はさらにそう
    - 「LとRの操作が重なる」ケースを考えすぎ。そもそも本質的には重なるわけではない
    """
    Aac = []
    for i, a in enumerate(A):
        Aac.append(a + (Aac[i - 1] if i > 0 else 0))

    # 候補になり得るx, y
    ssx = [(0, 0)]
    ssy = [(0, 0)]
    for x in range(1, N + 1):
        if x * L < Aac[x - 1]:
            ssx.append((x, Aac[x - 1] - x * L))
    for y in range(1, N + 1):
        org = Aac[N - 1] - (Aac[N - y - 1] if y < N else 0)
        if y * R < org:
            ssy.append((y, org - y * R))
    ssx.sort(key=lambda tup: (-tup[1]/tup[0] if tup[0] > 0 else 0))
    ssy.sort(key=lambda tup: (-tup[1]/tup[0] if tup[0] > 0 else 0))
    print(ssx, ssy)
    xi = 0
    yi = 0
    ax: int
    ay: int
    while True:
        x, val_x = ssx[xi]
        y, val_y = ssy[yi]
        if x + y <= N:
            ax, ay = x, y
            break
        else:
            if val_x * y > val_y * x:
                yi += 1
            else:
                xi += 1
    if ax + ay <= N:
        mid = (Aac[N - ay - 1] if ay < N else 0) - (Aac[ax - 1] if ax > 0 else 0)
    else:
        mid = 0
    dprint(ax, ay)
    print(ax * L + ay * R + mid)


def dprint(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve_editorial(N, L, R, A)


if __name__ == "__main__":
    main()
