#!/usr/bin/env python3
from collections import defaultdict


def main_2():
    """\
    DFSベースの解法。groupを使い回せるせいかbit全探索ライクの方法 (400msくらい）より高速（100ms）
    https://blog.hamayanhamayan.com/entry/2019/12/31/235645
    """
    import sys
    input = sys.stdin.readline
    N = int(input())

    A = defaultdict(dict)
    for i in range(N):
        for j, v in enumerate(list(map(int, input().split())), start=i + 1):
            A[i][j] = v
            A[j][i] = v

    groups = [[], [], []]


    def dfs(n=0, score=0):
        if n == N:
            return score

        max_score = -10 ** 9
        for group in groups:
            sc = sum(A[n][m] for m in group)
            group.append(n)
            max_score = max(max_score, dfs(n + 1, score + sc))
            group.pop()
        return max_score

    print(dfs())


def main():
    """初AC。bit全探索チック"""
    import sys
    input = sys.stdin.readline
    N = int(input())

    A = defaultdict(dict)
    for i in range(N):
        for j, v in enumerate(list(map(int, input().split())), start=i + 1):
            A[i][j] = v
            A[j][i] = v
    # print(A)
    max_score = -10**9
    for i in range(3**N):
        groups = [[], [], []]
        for n in range(N):
            groups[(i // 3**n) % 3].append(n)
        score = 0
        for group in groups:
            for j in range(len(group)):
                for l in range(j + 1, len(group)):
                    score += A[group[j]][group[l]]
        max_score = max(max_score, score)

    print(max_score)



if __name__ == "__main__":
    main_2()
