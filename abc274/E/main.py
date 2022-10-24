#!/usr/bin/env python3
import math


def solve(N: int, M: int, X: "List[int]", Y: "List[int]", P: "List[int]", Q: "List[int]"):
    """初回AC時の実装。出発点をdpに含めているために微妙にTLEしてしまう"""
    Inf = float("inf")
    NM = N + M + 1
    dp = [[Inf] * NM for _ in range(1 << NM)]
    dp[(1 << NM) - 1][0] = 0

    PX, PY = [0], [0]
    for x, y in zip(X, Y):
        PX.append(x)
        PY.append(y)
    for p, q in zip(P, Q):
        PX.append(p)
        PY.append(q)

    for S in range((1 << NM) - 2, -1, -1):
        for u in range(NM):
            ux, uy = PX[u], PY[u]
            # これがないとpypy3でTLE。N + M + 1 <= 18 でギリギリのところ
            if (S >> u) & 1 and u != 0:
                continue
            for v in range(NM):
                if (S >> v) & 1:
                    continue
                vx, vy = PX[v], PY[v]
                dist = math.sqrt((ux - vx) ** 2 + (uy - vy) ** 2)
                c = M
                tmp = (S | 1 << v) >> (N + 1)
                while tmp:
                    if tmp & 1:
                        c -= 1
                    tmp >>= 1
                if c:
                    dist /= 2**c
                # if dp[S | 1 << v][u] != Inf:
                #     print(format(S | 1 << v, "b").zfill(NM), format(S, "b").zfill(NM), u, "->", v,
                #           dp[S][v], dp[S | 1 << v][u], "+", dist)
                dp[S][v] = min(dp[S][v], dp[S | 1 << v][u] + dist)

    ans = Inf
    for i in range(1 << M):
        # print(format(i << (N + 1), "b").zfill(NM), dp[i << (N + 1)])
        ans = min(ans, dp[i << (N + 1)][0])
    print(ans)


def solve_ref(N: int, M: int, X: "List[int]", Y: "List[int]", P: "List[int]", Q: "List[int]"):
    """https://atcoder.jp/contests/abc274/submissions/35636696 上の解より速い"""
    popcount = [0] * 32
    for i in range(1, 32):
        popcount[i] = popcount[i // 2] + (i % 2)

    def hypot(p, q):
        return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5

    pos = [(x, y) for x, y in zip(X, Y)] + [(x, y) for x, y in zip(P, Q)]

    dp = [[1e18] * (1 << (N + M)) for _ in range(N + M)]
    for i in range(N + M):
        dp[i][1 << i] = hypot(pos[i], (0, 0))

    for s in range(1, 1 << (N + M)):
        coef = 0.5 ** popcount[s >> N]
        for i in range(N + M):
            if not (s >> i) & 1:
                continue
            for j in range(N + M):
                if (s >> j) & 1:
                    continue
                new_dist = dp[i][s] + hypot(pos[i], pos[j]) * coef
                if dp[j][s ^ (1 << j)] > new_dist:
                    dp[j][s ^ (1 << j)] = new_dist

    ans = 1e18
    for i in range(N + M):
        for s in range((1 << N) - 1, 1 << (N + M), 1 << N):
            ans = min(ans, dp[i][s] + hypot(pos[i], (0, 0)) * 0.5 ** popcount[s >> N])
    print(f"{ans:.10f}")


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    P = [int()] * (M)  # type: "List[int]"
    Q = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        P[i] = int(next(tokens))
        Q[i] = int(next(tokens))
    solve_ref(N, M, X, Y, P, Q)


if __name__ == "__main__":
    main()
