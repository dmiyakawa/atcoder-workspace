#!/usr/bin/env python3

"""\
巡回セールスマン問題 (TSP)をDPで解くケース

"""

from typing import List


def solve_tsp(N, d: "List[List[float]]"):
    """\
    三角不等式の成り立つ非負コストの重み付き有向グラフのNxN距離行列をdとしてTSPを解く
    dにおいて経路がない部分は float("inf") を含めること（そのため、型もfloatになっている）
    適切な経路がある場合はその値を、見つからない場合 -1 を返す

    想定されるNはせいぜい15〜17程度。手法としては(bit)DPを用いる

    この解法だと出発点一つ分点が多くなり、ギリギリのケースでTLEすることがある
    """
    # メモ化版はこちら。 ABC180 Eだと最大3〜4秒程度かかりTLEになる
    # @lru_cache(maxsize=10**9)
    # def rec(S, u):
    #     if S == (1 << N) - 1 and u == 0:
    #         return 0
    #     ret = Inf
    #     for v in range(N):
    #         if not (S >> u & 1):
    #             ret = min(ret, d[u][v] + rec(S | 1 << u, v))
    #     return ret
    # print(rec(0, 0))
    Inf = float("inf")
    # dp[S][u] ... すでに訪れた点の集合を(bit表現で)S、現在uにいるとしたとき、残りの頂点を全てたどって点0に帰るパスの重みの総和
    dp = [[Inf] * N for _ in range(1 << N)]

    # dp[0][0]は点0を開始点としたときに、自分も含む他の点を全て通ったときの重みの総和
    # 0番目の点に戻ってきたときにS == (1 << N) - 1（全ての点を辿った状態）になっていると「全て辿って戻ってきた」という意味になる
    dp[(1 << N) - 1][0] = 0  # 全部の点を辿った後に0にいる

    # 1の立っているbitが減る方向でループを回すと
    # 「巡回の終わりの方」が全て「巡回の最初の方」より先に計算される（蟻本 p174 の「S(i)∈S(j)ならばi<=j」）ので都合が良い
    for S in range((1 << N) - 2, -1, -1):
        for u in range(N):
            for v in range(N):
                if not (S >> v & 1):
                    dp[S][u] = min(dp[S][u], d[u][v] + dp[S | 1 << v][v])
    return -1 if dp[0][0] == Inf else dp[0][0]


def DPL_2_A():
    Inf = float("inf")
    V, E = map(int, input().split())
    S, T, D = [0] * E, [0] * E, [0] * E
    for i in range(E):
        S[i], T[i], D[i] = map(int, input().split())

    d = [[Inf] * V for _ in range(V)]
    for i in range(V):
        d[i][i] = 0
    for s, t, d0 in zip(S, T, D):
        d[s][t] = d0
    print(solve_tsp(V, d))


def abc180_e():
    N = int(input())
    X, Y, Z = [0] * N, [0] * N, [0] * N
    for i in range(N):
        X[i], Y[i], Z[i] = map(int, input().split())

    d = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            a, b, c = X[i], Y[i], Z[i]
            p, q, r = X[j], Y[j], Z[j]
            d[i][j] = abs(p - a) + abs(q - b) + max(0, r - c)
            d[j][i] = abs(p - a) + abs(q - b) + max(0, c - r)

    print(solve_tsp(N, d))


if __name__ == "__main__":
    DPL_2_A()
    # abc180_e()
