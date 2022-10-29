#!/usr/bin/env python3

def main_ref():
    """https://atcoder.jp/contests/abc208/editorial/2207"""
    import sys
    N, M = map(int, sys.stdin.buffer.readline().split())
    ABC = map(int, sys.stdin.buffer.read().split())
    d = [[1 << 60] * N for i in range(N)]
    for i in range(N):
        d[i][i] = 0
    for a, b, c in zip(ABC, ABC, ABC):
        d[a - 1][b - 1] = c
    answer = 0
    for k in range(N):
        nxt = [[0] * N for i in range(N)]
        for i in range(N):
            for j in range(N):
                nxt[i][j] = min(d[i][j], d[i][k] + d[k][j])
                if nxt[i][j] < 1 << 59:
                    answer += nxt[i][j]
        d = nxt
    print(answer)


def main():
    """初AC。タイトすぎ https://atcoder.jp/contests/abc208/submissions/36022316"""
    import sys
    input = sys.stdin.buffer.readline
    inf = 10**9
    N, M = map(int, input().split())
    costs = [inf] * N**2
    for _ in range(M):
        a, b, c = map(int, input().split())
        costs[(a - 1) * N + b - 1] = c

    cache = [0] * N**3
    ans = 0
    for k in range(N):
        for s in range(N):
            for t in range(N):
                if s == t:
                    continue
                c = min(costs[s * N + t], costs[s * N + k] + costs[k * N + t])
                if k > 0 and cache[s*N**2 + (k-1)*N + t]:
                    c = min(c, cache[s*N**2 + (k-1)*N + t])
                if k > 0 and cache[s*N**2+(k-1)*N+k] and cache[k*N**2+(k-1)*N+t]:
                    c = min(c, cache[s*N**2+(k-1)*N+k] + cache[k*N**2+(k-1)*N+t])
                if c < inf:
                    cache[s*N**2+k*N+t] = c
                    ans += c
    print(ans)


if __name__ == "__main__":
    main_ref()
