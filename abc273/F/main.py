#!/usr/bin/env python3

Inf = float("inf")


def solve_ref(N: int, X: int, Y: "List[int]", Z: "List[int]"):
    """やたら高速
    https://atcoder.jp/contests/abc273/submissions/35939585
    """
    from bisect import bisect_left
    import sys
    sys.setrecursionlimit(10 ** 7)

    INF = 10 ** 18

    if X < 0:
        X *= -1
        Y = [-y for y in Y]
        Z = [-z for z in Z]

    Ys = [0]
    walls = [(0, 0)]
    for y, z in zip(Y, Z):
        if y < X:
            walls.append((y, z))
            Ys.append(y)

    Ys.sort()
    walls.sort()
    num = len(walls)
    mid = -1
    for i, wall in enumerate(walls):
        if wall == (0, 0):
            mid = i
            break
    assert mid >= 0

    dp = [INF] * num
    dp[mid] = 0
    looked = [0] * num
    looked[mid] = 1
    edges = [0] * num
    for i, (_, z) in enumerate(walls):
        edges[i] = z

    for i in range(mid + 1, num):
        edges[i] = min(edges[i], edges[i - 1])

    for i in range(mid - 1, -1, -1):
        edges[i] = max(edges[i], edges[i + 1])

    def calc(idx):
        if looked[idx]:
            return dp[idx]

        looked[idx] = 1
        y, z = walls[idx]
        e = edges[idx]
        if y > 0:
            if z > y or calc(idx - 1) == INF:
                pass
            elif 0 < z < y or e < z:
                pre_y, _ = walls[idx - 1]
                dp[idx] = min(dp[idx], calc(idx - 1) + abs(y - pre_y))
            elif z < 0:
                i = bisect_left(Ys, z)
                yi, zi = walls[i]
                dp[idx] = min(dp[idx], calc(i) + abs(yi - z) + abs(y - z))
        else:  # y < 0
            if z < y or calc(idx + 1) == INF:
                pass
            elif y < z < 0 or z < e:
                pre_y, _ = walls[idx + 1]
                dp[idx] = min(dp[idx], calc(idx + 1) + abs(pre_y - y))
            elif 0 < z:
                i = bisect_left(Ys, z) - 1
                yi, zi = walls[i]
                dp[idx] = min(dp[idx], calc(i) + abs(z - yi) + abs(z - y))

        return dp[idx]

    ans = calc(num - 1) + abs(X - Ys[num - 1])
    print(ans if ans < INF else -1)


def solve(N: int, X: int, Y: "List[int]", Z: "List[int]"):
    """初AC。2900msくらいでギリギリ
    https://atcoder.jp/contests/abc273/submissions/36012497"""
    pos = []
    for i, (y, z) in enumerate(zip(Y, Z)):
        pos.append((y, i))
        pos.append((z, N + i))
    start_i = 2 * N
    goal_i = 2 * N + 1
    pos.append((0, start_i))
    pos.append((X, goal_i))
    pos.sort()
    # 開始点とゴールを含めて 2*N+2 個点がある
    M = 2 * N + 2
    i_to_pi = [-1] * M
    for pi, (p, i) in enumerate(pos):
        i_to_pi[i] = pi
    # 壁と同じ座標には鍵がない状態ではたどり着けない (= -1)
    dp = [[[Inf] * 2 for _ in range(M)] for _ in range(M)]
    ans = Inf
    # print(pos)
    for r_pi in range(M):
        for l_pi in range(r_pi, -1, -1):
            if not (l_pi <= i_to_pi[start_i] <= r_pi):
                continue
            if l_pi == r_pi:
                # 壁ではない場合のみ、その座標にとどまれる（スタート地点も含む)
                if pos[l_pi][1] >= N:
                    dp[l_pi][r_pi][0] = dp[l_pi][r_pi][1] = 0
                    # print(l_pi, r_pi, dp[l_pi][r_pi])
            else:
                # 端がそもそも壁でないか、壁であっても過去にたどった区間にスタートと鍵がある場合は距離が設定できる
                if N <= pos[l_pi][1] or l_pi <= i_to_pi[N + pos[l_pi][1]] <= r_pi:
                    dp[l_pi][r_pi][0] = min(dp[l_pi + 1][r_pi][0] + pos[l_pi + 1][0] - pos[l_pi][0],
                                            dp[l_pi + 1][r_pi][1] + pos[r_pi][0] - pos[l_pi][0])
                    # if dp[l_pi][r_pi][0] != Inf:
                    #     print(l_pi, r_pi, "l", dp[l_pi][r_pi][0])
                if N <= pos[r_pi][1] or l_pi <= i_to_pi[N + pos[r_pi][1]] <= r_pi:
                    dp[l_pi][r_pi][1] = min(dp[l_pi][r_pi - 1][1] + pos[r_pi][0] - pos[r_pi - 1][0],
                                            dp[l_pi][r_pi - 1][0] + pos[r_pi][0] - pos[l_pi][0])
                    # if dp[l_pi][r_pi][1] != Inf:
                    #     print(l_pi, r_pi, "r", dp[l_pi][r_pi][1])
            if l_pi <= i_to_pi[2 * N] <= r_pi and l_pi <= i_to_pi[2 * N + 1] <= r_pi:
                if dp[l_pi][r_pi][0] >= 0:
                    ans = min(ans, dp[l_pi][r_pi][0])
                if dp[l_pi][r_pi][1] >= 0:
                    ans = min(ans, dp[l_pi][r_pi][1])

    if ans == Inf:
        print(-1)
    else:
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
    X = int(next(tokens))  # type: int
    Y = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Z = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve_ref(N, X, Y, Z)
    # solve(N, X, Y, Z)


if __name__ == "__main__":
    main()
