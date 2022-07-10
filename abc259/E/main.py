#!/usr/bin/env python3

import sys
from collections import defaultdict

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():
    N = int(input())
    if N == 1:
        print(1)
        return

    # 素数をkey, そのkeyにおいてeが最大となるiの集合をvalue
    p_d = {}

    for i in range(N):
        m = int(input())
        for _ in range(m):
            p, e = map(int, input().split())
            if p not in p_d:
                p_d[p] = (e, {i})
            else:
                if p_d[p][0] < e:
                    p_d[p] = (e, {i})
                elif p_d[p][0] == e:
                    p_d[p][1].add(i)
    uniq = set()
    for p, (e, s_i) in p_d.items():
        if len(s_i) == 1:
            uniq.add(s_i.copy().pop())
    print(1 + len(uniq))


if __name__ == "__main__":
    main()
