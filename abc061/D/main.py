#!/usr/bin/env python3
#
# 解答閲覧済。ベルマンフォードっぽい部分はわかったが後半が……
#
# https://img.atcoder.jp/abc061/editorial.pdf
# https://drken1215.hatenablog.com/entry/2019/02/16/075900
#

Inf = float("inf")

def main():
    N, M = map(int, input().split())
    links = {}
    for _ in range(M):
        a, b, d = [int(e) for e in input().split()]
        a -= 1
        b -= 1
        links[(a, b)] = d

    points = [-Inf for _ in range(N)]
    points[0] = 0
    for i in range(N):
        for (s, t), d in links.items():
            if points[t] < points[s] + d:
                points[t] = points[s] + d

    # 本家解説より
    # - スコアの無限上昇を検出するため、長さNの配列を用意してfalseで初期化する
    # - スコア更新をN回繰り返す
    #
    # けんちょんブログの説明に基づく
    # 純粋なベルマンフォード法だとゴールに辿り着くかと関係なく「負の閉路」を検出する（今回はスコアが無限に増え続ける閉路）
    # 一方、今回の解答においてはノードNに閉路が影響を与えなければ解に関係がない
    # よって、閉路検出方法も「ゴールに辿り着くか」を見る必要がある
    looped = [False for _ in range(N)]
    for _ in range(N + 1):
        for (s, t), d in links.items():
            if points[t] < points[s] + d:
                points[t] = points[s] + d
                looped[t] = True
            if looped[s]:
                looped[t] = True

    if looped[N - 1]:
        print("inf")
    else:
        print(points[N - 1])


def main_wa():
    # 単純なベルマンフォード法でWA
    # 反例
    # 6 6
    # 1 2 1
    # 2 6 1
    # 2 3 1
    # 3 4 1
    # 4 5 1
    # 5 3 1
    N, M = map(int, input().split())
    links = {}
    for _ in range(M):
        a, b, d = [int(e) for e in input().split()]
        a -= 1
        b -= 1
        links[(a, b)] = d

    costs = [-Inf for _ in range(N)]
    costs[0] = 0
    cycle_detected = False
    for i in range(N):
        updated = False
        for (s, t), d in links.items():
            if costs[t] < costs[s] + d:
                costs[t] = costs[s] + d
                updated = True
        if updated:
            if i == N - 1:
                cycle_detected = True
        else:
            break
    if cycle_detected:
        print("inf")
    else:
        print(costs[N - 1])


if __name__ == "__main__":
    main()
