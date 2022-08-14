#!/usr/bin/env python3

from collections import defaultdict


def solve(N: int, U: "List[int]", V: "List[int]"):
    """https://atcoder.jp/contests/abc240/submissions/34056803"""
    # メモ
    # BFSの中でも帰りに結果が確定するやつ。「後行順巡回」と呼ぶそう
    # 最初、発想がSortedSetに行きかけた。しかし毎回初期化するとO(N^2)以上は確定なのでダメ
    # 単に局所の min, max をとってきて根であらためてmin, maxを選べば良いので二値で定数。SortedSetの「真ん中が要らない」
    # 実装面では lmin, lmax の取り扱いでだいぶミスって5分はロストした

    links = defaultdict(list)

    for u, v in zip(U, V):
        links[u - 1].append(v - 1)
        links[v - 1].append(u - 1)

    ans = {}
    n = 1
    used = set()

    def _search(i):
        nonlocal n
        used.add(i)

        lmin, lmax = None, None
        for j in links[i]:
            if j in used:
                continue
            tup = _search(j)
            lmin = tup[0] if lmin is None else min(lmin, tup[0])
            lmax = tup[1] if lmax is None else max(lmax, tup[1])
        if lmin is None or lmax is None:
            lmin, lmax = n, n
            n += 1
        assert i not in ans
        ans[i] = (lmin, lmax)
        return lmin, lmax

    _search(0)

    for i in range(N):
        print(ans[i][0], ans[i][1])


def main():
    import sys

    sys.setrecursionlimit(10**9)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, u, v)


if __name__ == "__main__":
    main()
