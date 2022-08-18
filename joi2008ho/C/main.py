#!/usr/bin/env python3
#
# https://atcoder.jp/contests/joi2008ho/submissions/34087659
# 注意: メモリ制限64MBのためPyPyだとMLEを起こす
#

import bisect


def main():
    N, M = map(int, input().split())
    P = [int(input()) for _ in range(N)]
    cand = set()
    for p1 in P:
        if p1 <= M:
            cand.add(p1)
        for p2 in P:
            if p1 + p2 <= M:
                cand.add(p1 + p2)
    ans = max(cand)
    s = sorted(cand)
    for c in s:
        v = M - c
        if v < 0:
            break
        i = bisect.bisect(s, M - c)
        if i > 0 and c + s[i - 1] <= M:
            ans = max(ans, c + s[i - 1])
        if i < N and c + s[i] <= M:
            print(ans, v, s[i])
            ans = max(ans, c + s[i])
    print(ans)


if __name__ == "__main__":
    main()
