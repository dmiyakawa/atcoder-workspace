#!/usr/bin/env python3

import sys


def solve2(N: int, M: int, L: "List[int]", R: "List[int]", S: "List[int]"):
    # 満点解法
    d = {}
    S_total = sum(S)
    for l, s in zip(L, S):
        d[l] = d.get(l, 0) + s
    for r, s in zip(R, S):
        d[r + 1] = d.get(r + 1, 0) - s
    lst = sorted(d.items())
    if lst[0][0] != 1 or lst[-1][0] != M + 1:
        print(S_total)
        return
    # print(lst, M)
    min_score = S_total
    score = 0
    for tup in lst:
        if tup[0] == M + 1:
            break
        score += tup[1]
        min_score = min(min_score, score)
    print(S_total - min_score)


def solve(N: int, M: int, L: "List[int]", R: "List[int]", S: "List[int]"):
    # 100点 (not 満点 = 101点) 解法を想定
    tups = list(zip(L, R, S))
    max_score = 0
    for m in range(1, M + 1):
        score = 0
        for l, r, s in tups:
            if l <= m <= r:
                continue
            score += s
        max_score = max(max_score, score)
    print(max_score)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    l = [int()] * (N)  # type: "List[int]"
    r = [int()] * (N)  # type: "List[int]"
    s = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
        s[i] = int(next(tokens))
    solve2(N, M, l, r, s)


if __name__ == "__main__":
    main()
