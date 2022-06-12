#!/usr/bin/env python3
#
# https://atcoder.jp/contests/past202112-open/submissions/32359776
#
from collections import defaultdict
from bisect import bisect_left
from heapq import heappush, heappop


def main():
    N, M = map(int, input().split())

    xs = []
    d = defaultdict(list)
    for _ in range(M):
        A, B, C = map(int, input().split())
        xs.append(A)
        xs.append(B)
        d[A].append((B, C))
        d[B].append((A, C))

    xs = sorted(set(xs))
    q = [(0, 1)]  # (経過時間、今いるフロア)
    used = set()
    while q:
        t, cur = heappop(q)
        if cur == N:
            print(t)
            break
        if cur in used:
            continue
        used.add(cur)

        # エレベータに乗る(もしあれば)
        for to, c in d[cur]:
            if to in used:
                continue
            heappush(q, (t + c, to))

        # 近くのエレベータへ移動
        p = bisect_left(xs, cur)
        for k in [p - 1, p, p + 1]:
            if not (0 <= k < len(xs)):
                continue
            if xs[k] in used:
                continue
            heappush(q, (t + abs(xs[k] - cur), xs[k]))

        # N 階へ向かう
        heappush(q, (t + (N - cur), N))


if __name__ == "__main__":
    main()
