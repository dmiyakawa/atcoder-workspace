#!/usr/bin/env python3


def solve(N: int, A: int, W: "List[int]", X: "List[int]", V: "List[int]"):
    """
    AC版 https://atcoder.jp/contests/abc274/submissions/35916487
    参考 https://atcoder.jp/contests/abc274/submissions/35914487
    - 距離を10**9倍して演算を整数のみにした (大体2倍弱になる。これが一番効く
    - 更新のかかる時刻をkeysという集合に別途管理してincl_d.keys()とdecl_d.keys()をマージするオーバーヘッドを削減した。
    - defaultdictをやめた。これで数百ms早くなる (これでは不足)
    """
    ans = 0
    for i in range(N):
        incl_d = {}
        decl_d = {}
        incl_d[0] = W[i]
        keys = {0}
        for j in range(N):
            if i == j:
                continue
            if V[i] == V[j] and X[i] <= X[j] <= X[i] + A:
                incl_d[0] = incl_d.get(0, 0) + W[j]
            elif V[i] > V[j] and X[i] <= X[j]:
                s = max(0, (X[j] - X[i] - A) * 10**9 // (V[i] - V[j]))
                t = (X[j] - X[i]) * 10**9 // (V[i] - V[j])
                incl_d[s] = incl_d.get(s, 0) + W[j]
                decl_d[t] = decl_d.get(t, 0) - W[j]
                keys.add(s)
                keys.add(t)
            elif V[i] < V[j] and X[i] + A >= X[j]:
                s = max(0, (X[i] - X[j]) * 10**9 // (V[j] - V[i]))
                t = (X[i] + A - X[j]) * 10**9 // (V[j] - V[i])
                incl_d[s] = incl_d.get(s, 0) + W[j]
                decl_d[t] = decl_d.get(t, 0) - W[j]
                keys.add(s)
                keys.add(t)
        local_max = 0
        cur = 0
        for t in sorted(keys):
            cur += incl_d.get(t, 0)
            if cur > local_max:
                local_max = cur
            cur += decl_d.get(t, 0)
        ans = max(ans, local_max)
    print(ans)


def solve_tle(N: int, A: int, W: "List[int]", X: "List[int]", V: "List[int]"):
    """https://atcoder.jp/contests/abc274/submissions/35916097"""
    from collections import defaultdict
    ans = 0
    for i in range(N):
        incl_d = defaultdict(int)
        decl_d = defaultdict(int)
        incl_d[0] = W[i]
        for j in range(N):
            if i == j:
                continue
            if V[i] == V[j] and X[i] <= X[j] <= X[i] + A:
                incl_d[0] += W[j]
            elif V[i] > V[j] and X[i] <= X[j]:
                s = max(0, (X[j] - X[i] - A) / (V[i] - V[j]))
                t = (X[j] - X[i]) / (V[i] - V[j])
                incl_d[s] += W[j]
                decl_d[t] -= W[j]
            elif V[i] < V[j] and X[i] + A >= X[j]:
                s = max(0, (X[i] - X[j]) / (V[j] - V[i]))
                t = (X[i] + A - X[j]) / (V[j] - V[i])
                incl_d[s] += W[j]
                decl_d[t] -= W[j]
        local_max = 0
        cur = 0
        sorted_keys = sorted(set(incl_d.keys()) | set(decl_d.keys()))
        for t in sorted_keys:
            cur += incl_d[t]
            if cur > local_max:
                local_max = cur
                # print("", t, "x=", X[i] + V[i] * t, local_max)
            cur += decl_d[t]
        ans = max(ans, local_max)
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
    A = int(next(tokens))  # type: int
    W = [int()] * (N)  # type: "List[int]"
    X = [int()] * (N)  # type: "List[int]"
    V = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        W[i] = int(next(tokens))
        X[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, A, W, X, V)


if __name__ == "__main__":
    main()
